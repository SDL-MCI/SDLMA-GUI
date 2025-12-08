import re
import shutil

import numpy as np
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (QComboBox, QDialog, QFileDialog, QHBoxLayout,
                               QLabel, QLineEdit, QWidget)
from sdlma_modal_analysis.sdlma_ema import SDLMAEMA
from sdlma_modal_analysis.sdlma_uff import SDLMAUFF
from PySide6.QtCore import Slot

from ui import sdlma_mp_to_nodes_gui
from util.models import data_proto, row_count_proto
from custom_widgets.post_proc.post_proc_ema_window import EmaWindow


class PostProcMainWidget(QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        """
        Custom Widget Class connected to the Post Process tab of the PySide6
        GUI.
        """
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
        """
        Method to initialize the post proc widget.
        :param ui: The main ui object created by PySide6.
        """
        self.ui = ui

    def init_line_edits(self):
        """
        Method to assign input constraints to the line edits
        of the post processing tab.
        """
        i_validator = QtGui.QDoubleValidator(bottom=1, top=100, decimals=3)
        self.ui.post_proc_line_edit_deformation_scale.setValidator(i_validator)

    @Slot()
    def post_proc_button_load_geometry_pressed(self):
        """
        Slot method that allows the user to load a geometry file.
        Format:
        x1 y1 z1
        x2 y2 z2
        x3 y3 z3
        xn yn zn
        """
        filename, _ = QFileDialog.getOpenFileName(filter="*.txt")
        if filename:
            self.ui.post_proc_vispy.init()
            nodes = []
            with open(filename, "r") as f:
                for line in f.readlines():
                    nodes.append(
                        tuple(re.findall(r"[-+]?(" r"?:\d*\.*\d+)", line))
                    )
            self.ui.post_proc_vispy.lower()
            self.ui.post_proc_vispy_settings.raise_()
            self.nodes = np.array(nodes, dtype=float)
            self.select_connector(self.ui.post_proc_connector.checkedId())
            self.ui.post_proc_vispy.create_nodes(self.nodes)
            self.ui.post_proc_button_load_geometry.setEnabled(False)
            self.ui.post_proc_vispy_settings.setEnabled(True)
            self.ui.post_proc_button_load_ema.setEnabled(True)
            self.ui.post_proc_button_save_geometry.setEnabled(True)

    @Slot()
    def post_proc_button_load_uff_pressed(self):
        """
        Slot method to load a uff file
        """
        filename, _ = QFileDialog.getOpenFileName(filter="*.unv *.uff")
        if filename:
            shutil.copyfile(filename, filename + "_old")
            self.sdlma_uff = SDLMAUFF(name="", filename=filename)
            self.sdlma_uff.get_points()

    @Slot()
    def post_proc_button_load_ema_pressed(self):
        """
         Slot method that allows the user to load a ema file.
        """
        filename, _ = QFileDialog.getOpenFileName(filter="*.h5")
        if filename:
            self.sdlma_ema = SDLMAEMA.import_from_hd5f_file(filename)
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

    def init_mode_combo_box(self, nat_freqs: list):
        """
        Helper method to initialize the combo box with the given natural frequencies.
        :param nat_freqs: list of nat frequencies.
        """
        self.ui.post_proc_combo_box_mode.clear()
        if self.sdlma_ema:
            for nat_freq in nat_freqs:
                self.ui.post_proc_combo_box_mode.addItem(
                    str("%.2f Hz" % nat_freq)
                )

    @Slot()
    def post_proc_combo_button_mode_changed(self, idx: QtCore.QModelIndex):
        """
        Slot Method to calculate the deformed nodes
        for the given natural frequency according to its index.
        :param idx: The index of the nat frequency in the combo box.
        """
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

    @Slot()
    def post_proc_button_show_deformation_pressed(self):
        """
        Slot Method to showcase the deformation for the selected nat
        frequencies.
        """
        self.show_deformation = not self.show_deformation
        if self.show_deformation:
            self.timer.start(2000)
        else:
            self.timer.stop()
            self.ui.post_proc_vispy.update_points(self.nodes)

    def update_deformation(self):
        """
        Method to update the current view of the deformation
        """
        if self.step == self.max_step:
            self.step = 0
        self.ui.post_proc_vispy.update_points(self.deformed_nodes[self.step])
        self.step += 1

    @Slot()
    def post_proc_connector_changed(self, id: int, is_toggled: bool):
        """
        Slot method to update the connector used for meshing
        :param id: The id of the connector from the selector
        :param is_toggled: Bool indicating if it has been toggled or untoggled
        :return:
        """
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
        """
        Helper Method to check if the sdlmauff object exists and otherwise
        creates it.
        """
        if not self.sdlma_uff:
            filename, _ = QFileDialog.getSaveFileName(filter="*.unv *.uff")
            if filename:
                self.sdlma_uff = SDLMAUFF(name="", filename=filename)

    @Slot()
    def post_proc_button_save_geometry_pressed(self):
        """
        Slot method to save the geometry in the uff file
        """
        self.check_sdlma_uff()
        self.sdlma_uff.write_coord_system()
        self.sdlma_uff.write_units()
        self.sdlma_uff.write_nodes(self.nodes)
        self.sdlma_uff.write_mesh(
            self.ui.post_proc_vispy.line_nodes,
            self.ui.post_proc_vispy.face_nodes,
        )

    @Slot()
    def post_proc_button_save_ema_pressed(self):
        """
        Slot Method to save the ema result in the uff file
        """
        self.check_sdlma_uff()
        self.sdlma_uff.write_modes(self.sdlma_ema, self.mp_to_node)
        self.sdlma_uff.write_frfs(self.sdlma_ema, self.mp_to_node)

    @Slot()
    def post_proc_button_save_all_pressed(self):
        """
        Slot Method to save all in the uff file
        """
        self.post_proc_button_save_geometry_pressed()
        self.post_proc_button_save_ema_pressed()

    @Slot()
    def post_proc_button_clear_pressed(self):
        """
        Slot method to clear the complete widget
        """
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


