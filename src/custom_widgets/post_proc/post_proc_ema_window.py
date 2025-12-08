from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QWidget, QHBoxLayout, \
    QComboBox
from PySide6.QtCore import Slot
from models.post_proc_models import FRFModel
from ui import sdlma_mp_to_nodes_gui


class EmaWindow(QDialog):
    def __init__(self, node_list, mp_list, parent=None, *args, **kwargs):
        """
        Pyside6 Dialog Window utilized assign nodes to ema signals
        """
        super().__init__(parent)
        self.ui = sdlma_mp_to_nodes_gui.Ui_Dialog()
        self.ui.setupUi(self)
        self.resp_signals_model = FRFModel()
        self.node_list = node_list
        self.mp_list = mp_list
        self.mp_to_node = {}
        self.init()

    def init(self):
        """
        Method to initialize the window
        """
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

    @Slot()
    def mp_to_nodes_button_done_pressed(self):
        """
        Method to handle the close event
        :return:
        """
        for i, combo_box in enumerate(
            self.ui.mp_to_nodes_widget.findChildren(QComboBox)
        ):
            self.mp_to_node[self.mp_list[i]] = int(combo_box.currentText())
        self.window().accept()