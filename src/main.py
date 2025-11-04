# This Python file uses the following encoding: utf-8
import os.path
import sys
import traceback
from datetime import datetime, timezone

from PySide6 import QtGui
from PySide6.QtCore import QStringListModel, QUrl, Slot
from PySide6.QtGui import QColor, QPalette
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow

from ui import sdlma_gui, sdlma_teds_gui
from util.line_edits import set_line_edit_change_func


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = sdlma_gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_media_player()
        self.ui.meas_widget_main.init(self.ui)
        self.ui.ema_widget_main.init(self.ui)
        self.ui.post_proc_widget_main.init(self.ui)
        self.default_palette = QtGui.QGuiApplication.palette()
        set_line_edit_change_func(
            self.ui.centralwidget, self.line_edit_changed
        )
        self.exc_model = QStringListModel()
        self.ui.exception_scroll_area_list_view.setModel(self.exc_model)
        # Hook global exceptions
        sys.excepthook = self.handle_exception

    # https://stackoverflow.com/questions/76148904/in-pyqt6-how-to-play-audio
    def setup_media_player(self):
        self.ui.media_player = QMediaPlayer()
        self.ui.audio = QAudioOutput()
        self.ui.media_player.setAudioOutput(self.ui.audio)
        self.ui.media_player.setSource(
            QUrl.fromLocalFile(
                "../assets/mixkit-positive-interface-beep-221.wav"
            )
        )
        # print(os.path.exists("../assets/mixkit-positive-interface-beep-221"
        #                      ".wav"))

    def handle_exception(self, exception_type, exception_value, exc_traceback):

        now_utc = datetime.now(timezone.utc)
        formatted = now_utc.strftime("%d.%m.%Y %H:%M:%S")
        sys.__excepthook__(exception_type, exception_value, exc_traceback)
        msg = f"{formatted} - {exception_type.__name__}: {exception_value}"
        items = self.exc_model.stringList()
        items.insert(0, msg)  # prepend to the start
        self.exc_model.setStringList(items)  # update

    @Slot(str)
    def line_edit_changed(self, arg):
        line_edit = self.sender()
        if arg and line_edit.hasAcceptableInput():
            palette = QPalette()
            palette.setColor(QPalette.Base, QColor(255, 255, 255))  # light red
            line_edit.setPalette(palette)  # Reset to default
        else:
            palette = QPalette()
            palette.setColor(QPalette.Base, QColor(255, 220, 220))  # light red
            line_edit.setPalette(palette)

    def teds_test(self):
        channel_window = TedsWindow()
        if channel_window.exec() == QDialog.Accepted:
            pass


# https://www.pythonguis.com/tutorials/pyside6-creating-multiple-windows/
class TedsWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = sdlma_teds_gui.Ui_Dialog()
        self.ui.setupUi(self)
        self.init_form_data()

    def init_form_data(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
