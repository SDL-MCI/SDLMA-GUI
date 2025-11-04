from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QFileDialog,
    QLabel,
    QLayout,
    QLineEdit,
    QScrollArea,
    QWidget,
)
from sdlma_teds.teds import StandardTeds

from util.layouts import clear_layout


class PyMATedsWidget(QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

    @Slot()
    def teds_button_new_pressed(self):
        pass

    @Slot()
    def teds_button_load_pressed(self):
        path, ext = QFileDialog.getOpenFileName(filter="*.ted")
        if path != "":
            bitstream = StandardTeds.read_bitstream_from_file(path)
            teds_data = StandardTeds(bitstream, has_preamble=True)
            layout = self.findChild(QLayout, name="teds_layout_data")
            clear_layout(layout)
            self.create_teds_form(layout, teds_data.teds)

    def create_teds_form(self, layout, teds: dict):
        for name, value in teds.items():
            label = QLabel(name)
            line_edit = QLineEdit(str(value.val))

            layout.addWidget(label)
            layout.addWidget(line_edit)
            label.setMinimumHeight(50)
            line_edit.setMinimumHeight(50)
            label.show()
            line_edit.show()

        # https://stackoverflow.com/questions/78922304/qt-pyside6-add-widget-to-qscrollarea-during-runtime-not-showing-up
        scroll_area = self.findChild(QScrollArea, name="teds_scroll_area")
        scroll_area.widget().adjustSize()
        scroll_area.widget().updateGeometry()

    @Slot()
    def teds_button_save_pressed(self):
        # self.window().accept = True
        self.window().accept()
