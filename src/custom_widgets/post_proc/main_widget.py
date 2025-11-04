import re
import shutil

import numpy as np
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QWidget,
)
from sdlma_modal_analysis.sdlma_ema import SDLMAEMA
from sdlma_modal_analysis.sdlma_uff import SDLMAUFF

from ui import sdlma_mp_to_nodes_gui
from util.models import data_proto, row_count_proto


# https://github.com/pyqtgraph/pyqtgraph/blob/4951bd743ef7e2a5198615573167301c9603b72f/examples/linkedViews.py
class PostProcMainWidget(QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.deformed_nodes = None
        self.ui = None
        self.sdlma_ema = None
        self.sdlma_uff = None
        self.nodes = None
        self.show_deformation = False
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_deformation)
        self.step = 0
        self.max_step = 50

    def init(self, ui):
        self.ui = ui

    def init_line_edits(self):
        i_validator = QtGui.QDoubleValidator(bottom=1, top=100, decimals=3)
        self.ui.post_proc_line_edit_deformation_scale.setValidator(i_validator)

    def post_proc_button_load_geometry_pressed(self):
        filename, _ = QFileDialog.getOpenFileName(filter="*.txt")
        if filename:
            self.ui.post_proc_vispy.setup()
            nodes = []
            with open(filename, "r") as f:
                for line in f.readlines():
                    # https://stackoverflow.com/questions/4703390/how-to
                    # -extract-a-floating-number-from-a-string
                    nodes.append(
                        tuple(re.findall(r"[-+]?(" r"?:\d*\.*\d+)", line))
                    )
            self.ui.post_proc_vispy.lower()
            self.ui.post_proc_vispy_settings.raise_()
            self.nodes = np.array(nodes, dtype=float)
            # self.ui.post_proc_vispy.connector = "line"
            self.select_connector(self.ui.post_proc_connector.checkedId())
            self.ui.post_proc_vispy.create_nodes(self.nodes)
            self.ui.post_proc_button_load_geometry.setEnabled(False)
            self.ui.post_proc_vispy_settings.setEnabled(True)
            self.ui.post_proc_button_load_ema.setEnabled(True)
            self.ui.post_proc_button_save_geometry.setEnabled(True)

    def post_proc_button_load_uff_pressed(self):
        filename, _ = QFileDialog.getOpenFileName(filter="*.unv *.uff")
        if filename:
            shutil.copyfile(filename, filename + "_old")
            self.sdlma_uff = SDLMAUFF(name="", filename=filename)
            self.sdlma_uff.get_points()

    def post_proc_button_load_ema_pressed(self):
        filename, _ = QFileDialog.getOpenFileName(filter="*.h5")
        if filename:
            self.sdlma_ema = SDLMAEMA.import_from_hd5f_file(filename)
            # self.ui.post_proc_line_edit_nat_freq.setText(
            #     str(self.sdlma_ema.nat_freq)
            # )
            # self.ui.post_proc_line_edit_daming_coeff.setText(
            #     str(self.sdlma_ema.nat_xi)
            # )

            ema_window = EmaWindow(
                self.nodes, self.sdlma_ema.get_unique_names()
            )
            if ema_window.exec() == QDialog.Accepted:
                self.mp_to_node = ema_window.mp_to_node
                self.ui.post_proc_button_load_ema.setEnabled(False)
                self.ui.post_proc_button_save_ema.setEnabled(True)
                self.ui.post_proc_button_save_all.setEnabled(True)
            self.init_mode_combo_box(self.sdlma_ema.nat_freq)
            self.post_proc_combo_button_mode_changed(0)

    def init_mode_combo_box(self, nat_freqs):
        self.ui.post_proc_combo_box_mode.clear()
        if self.sdlma_ema:
            for nat_freq in nat_freqs:
                self.ui.post_proc_combo_box_mode.addItem(
                    str("%.2f Hz" % nat_freq)
                )

    def post_proc_combo_button_mode_changed(self, idx):
        if self.sdlma_ema:
            scale = float(self.ui.post_proc_line_edit_deformation_scale.text())
            self.deformed_nodes = SDLMAUFF.calculate_displacement_period(
                self.sdlma_ema,
                self.mp_to_node,
                idx,
                self.ui.post_proc_vispy.points,
                steps=self.max_step,
                scale=scale,
            )

    def post_proc_button_show_deformation_pressed(self):
        self.show_deformation = not self.show_deformation
        if self.show_deformation:
            self.timer.start(2000)
        else:
            self.timer.stop()
            self.ui.post_proc_vispy.update_points(self.nodes)

    def update_deformation(self):
        if self.step == self.max_step:
            self.step = 0
        self.ui.post_proc_vispy.update_points(self.deformed_nodes[self.step])
        self.step += 1

    def post_proc_connector_changed(self, id, is_toggled):
        if is_toggled:
            self.select_connector(id)

    def select_connector(self, id):
        match id:
            case -2:
                connector = "line"
            case -3:
                connector = "tri"
            case -4:
                connector = "quad"
            case -5:
                connector = "delete"
            case _:
                connector = "line"
        self.ui.post_proc_vispy.change_connector(connector)

    def check_sdlma_uff(self):
        if not self.sdlma_uff:
            filename, _ = QFileDialog.getSaveFileName(filter="*.unv *.uff")
            if filename:
                self.sdlma_uff = SDLMAUFF(name="", filename=filename)

    def post_proc_button_save_geometry_pressed(self):
        self.check_sdlma_uff()
        self.sdlma_uff.write_coord_system()
        self.sdlma_uff.write_units()
        self.sdlma_uff.write_nodes(self.nodes)
        self.sdlma_uff.write_mesh(
            self.ui.post_proc_vispy.line_nodes,
            self.ui.post_proc_vispy.face_nodes,
        )

    def post_proc_button_save_ema_pressed(self):
        self.check_sdlma_uff()
        self.sdlma_uff.write_modes(self.sdlma_ema, self.mp_to_node)
        self.sdlma_uff.write_frfs(self.sdlma_ema, self.mp_to_node)

    def post_proc_button_save_all_pressed(self):
        self.post_proc_button_save_geometry_pressed()
        self.post_proc_button_save_ema_pressed()

    def post_proc_button_clear_pressed(self):
        self.sdlma_uff = None
        self.sdlma_ema = None
        self.nodes = None
        self.ui.post_proc_vispy.clear()
        self.timer.stop()
        self.select_connector(self.ui.post_proc_connector.checkedId())
        self.ui.post_proc_button_load_ema.setEnabled(False)
        self.ui.post_proc_button_save_ema.setEnabled(False)
        self.ui.post_proc_button_save_all.setEnabled(False)
        self.ui.post_proc_button_save_geometry.setEnabled(False)
        self.ui.post_proc_button_load_geometry.setEnabled(True)


class EmaWindow(QDialog):
    def __init__(self, node_list, mp_list, parent=None, *args, **kwargs):
        super().__init__(parent)
        self.ui = sdlma_mp_to_nodes_gui.Ui_Dialog()
        self.ui.setupUi(self)
        self.resp_signals_model = FRFModel()
        self.node_list = node_list
        self.mp_list = mp_list
        self.mp_to_node = {}
        self.init()

    def init(self):
        nodes = []

        for i, node in enumerate(self.node_list):
            nodes.append(str(i + 1))

        for i, mp in enumerate(self.mp_list):
            mp_label = QLabel("Name")
            mp_line_edit = QLineEdit(mp, readOnly=True)
            node_label = QLabel("Node")
            qwidget = QWidget(parent=self.ui.mp_to_nodes_widget)
            layout = QHBoxLayout()
            qwidget.setLayout(layout)
            node_combo_box = QComboBox(parent=qwidget)
            node_combo_box.addItems(nodes)
            layout.addWidget(mp_label)
            layout.addWidget(mp_line_edit)
            layout.addWidget(node_label)
            layout.addWidget(node_combo_box)
            self.ui.mp_to_nodes_layout.addWidget(qwidget)

    def mp_to_nodes_button_done_pressed(self):
        for i, combo_box in enumerate(
            self.ui.mp_to_nodes_widget.findChildren(QComboBox)
        ):
            self.mp_to_node[self.mp_list[i]] = int(combo_box.currentText())
        self.window().accept()


class FRFModel(QtCore.QAbstractListModel):
    def __init__(self, *args, frfs=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.frfs = frfs or []

    def data(self, index, role):
        return data_proto(self.frfs, index, role)

    def rowCount(self, index):
        return row_count_proto(self.frfs)
