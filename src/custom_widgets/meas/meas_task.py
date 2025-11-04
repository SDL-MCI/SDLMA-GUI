from PySide6 import QtGui
from PySide6.QtCore import Slot
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QDialog, QFileDialog, QLineEdit
from sdlma_hardware.sdlma_hardware import SDLMAHardware, SDLMANiTask

from models.hardware_model import ChannelModel, PyMAGuiChannel
from ui import sdlma_channel_gui, sdlma_task_gui
from util.line_edits import check_line_edits_valid, set_line_edit_change_func


class TaskWindow(QDialog):
    def __init__(self, task_data=None):
        super().__init__()
        self.ui = sdlma_task_gui.Ui_Dialog()
        self.ui.setupUi(self)
        self.available_channels_model = ChannelModel()
        self.ui.meas_list_available_channels.setModel(
            self.available_channels_model
        )
        set_line_edit_change_func(
            self.ui.centralwidget, self.line_edit_changed
        )
        set_line_edit_change_func(
            self.ui.centralwidget, self.meas_is_task_valid
        )
        self.init_line_edits()
        self.meas_button_refresh_channels_pressed()
        self.init_task(task_data)
        self.meas_is_task_valid()

    def init_task(self, task_data):
        if task_data:
            self.ui.meas_line_edit_task_name.setText(task_data["name"])
            self.ui.meas_line_edit_num_impacts.setText(
                task_data["num_impacts"]
            )
            self.ui.meas_line_edit_impact_time.setText(
                task_data["impact_time"]
            )
            self.ui.meas_line_edit_sampling_freq.setText(
                task_data["sampling_freq"]
            )
            self.ui.meas_line_edit_overflow_samples.setText(
                task_data["overflow_samples"]
            )
            self.ui.meas_line_edit_double_impact_limit.setText(
                task_data["double_impact_limit"]
            )
            self.available_channels_model.channels = task_data["channels"]
            self.ui.meas_button_refresh_channels.setEnabled(False)

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

    @Slot()
    def meas_is_task_valid(self):
        line_edits = self.ui.centralwidget.findChildren(QLineEdit)
        if check_line_edits_valid(line_edits) and self.is_valid_selection():
            self.ui.meas_button_create_task.setEnabled(True)
        else:
            self.ui.meas_button_create_task.setEnabled(False)

    def is_valid_selection(self):
        exc = 0
        resp = 0
        for channel in self.available_channels_model.channels:
            if channel.selected:
                if channel.channel.is_resp:
                    resp += 1
                else:
                    exc += 1
        return exc == 1 and resp >= 1  # 1 exc sig and at least 1 resp sig

    def init_line_edits(self):
        len_validator = QtGui.QRegularExpressionValidator(r"^.{1,}$")
        i_validator = QtGui.QIntValidator(bottom=1, top=100)
        freq_validator = QtGui.QIntValidator(bottom=1, top=500000)
        d_validator = QtGui.QDoubleValidator(bottom=1, top=100000, decimals=1)

        self.ui.meas_line_edit_task_name.setValidator(len_validator)
        self.ui.meas_line_edit_sampling_freq.setValidator(freq_validator)
        self.ui.meas_line_edit_num_impacts.setValidator(i_validator)
        self.ui.meas_line_edit_impact_time.setValidator(d_validator)

    def meas_button_refresh_channels_pressed(self):
        hw = SDLMAHardware()
        hw.get_available_ni_channels()
        gui_channels = []
        for channel in hw.sdlma_channels:
            gui_channels.append(PyMAGuiChannel(channel=channel))
        self.available_channels_model.channels = gui_channels
        self.available_channels_model.layoutChanged.emit()

    def meas_list_item_double_clicked(self, index):
        gui_channel = self.available_channels_model.channels[index.row()]
        sdlma_channel = gui_channel.channel
        channel_window = ChannelWindow(sdlma_channel)
        if channel_window.exec() == QDialog.Accepted:
            channel_data = channel_window.get_form_data()
            gui_channel.selected = channel_data["add"]
            sdlma_channel.is_resp = channel_data["is_resp"]
            sdlma_channel.direction = channel_data["direction"]
            sdlma_channel.comment = channel_data["comment"]
            sdlma_channel.serial_number = channel_data["serial_number"]
            if not sdlma_channel.hw_teds:
                sdlma_channel.set_channel_info(
                    teds_info={"sens_ref": channel_data["sens_ref"]}
                )
            sdlma_channel.disp_name = channel_data["disp_name"]
            self.meas_is_task_valid()

    def meas_button_reset_hardware_pressed(self):
        SDLMAHardware.reset_devices()

    def meas_button_create_pressed(self):
        self.window().accept()

    def get_task_data(self):
        name = self.ui.meas_line_edit_task_name.text()
        sampling_freq = int(self.ui.meas_line_edit_sampling_freq.text())
        num_impacts = int(self.ui.meas_line_edit_num_impacts.text())
        impact_time = float(self.ui.meas_line_edit_impact_time.text())
        overflow_samples = int(self.ui.meas_line_edit_overflow_samples.text())
        double_impact_limit = float(
            self.ui.meas_line_edit_double_impact_limit.text()
        )
        channels = self.available_channels_model.get_selected_channels()
        return {
            "name": name,
            "sampling_freq": sampling_freq,
            "num_impacts": num_impacts,
            "impact_time": impact_time,
            "channels": channels,
            "overflow_samples": overflow_samples,
            "double_impact_limit": double_impact_limit,
        }


class ChannelWindow(QDialog):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self, sdlma_channel):
        super().__init__()

        self.ui = sdlma_channel_gui.Ui_Dialog()
        self.ui.setupUi(self)
        self.sdlma_channel = sdlma_channel
        self.init_form_data()

    def init_form_data(self):
        self.ui.channel_line_edit_name.setText(self.sdlma_channel.name)

        self.ui.channel_check_box_hw_teds.setChecked(
            self.sdlma_channel.hw_teds
        )
        if self.sdlma_channel.disp_name == "":
            self.ui.channel_line_edit_disp_name.setText(
                self.sdlma_channel.name.rsplit("/", 1)[-1]
            )
        else:
            self.ui.channel_line_edit_disp_name.setText(
                self.sdlma_channel.disp_name
            )
        self.ui.channel_line_edit_serial_number.setText(
            self.sdlma_channel.serial_number
        )
        self.ui.channel_line_edit_comment.setText(self.sdlma_channel.comment)
        if self.sdlma_channel.hw_teds:
            self.ui.channel_combo_box_sensor_type.setCurrentIndex(
                not self.sdlma_channel.is_resp
            )
            self.ui.channel_combo_box_sensor_type.setEnabled(False)
            self.ui.channel_line_edit_sensitivity.setEnabled(False)
            if self.sdlma_channel.is_resp:
                sens_unit = "Sensitivity / Vs<sup>2</sup>·m<sup>-1</sup>"
            else:
                sens_unit = "Sensitivity / V·N<sup>-1</sup>"
            self.ui.channel_label_sensitivity.setText(sens_unit)
            self.ui.channel_line_edit_sensitivity.setText(
                str(self.sdlma_channel.channel_info["sens_ref"].val)
            )
            self.ui.channel_combo_box_sensor_direction.setCurrentText(
                self.sdlma_channel.direction
            )
        elif self.sdlma_channel.channel_info:
            self.ui.channel_line_edit_sensitivity.setText(
                str(self.sdlma_channel.channel_info["sens_ref"])
            )
            self.ui.channel_combo_box_sensor_type.setCurrentIndex(
                not self.sdlma_channel.is_resp
            )

            self.ui.channel_combo_box_sensor_direction.setCurrentText(
                self.sdlma_channel.direction
            )

    def get_form_data(self) -> dict:
        return {
            "add": self.ui.channel_check_box_add.isChecked(),
            "sens_ref": float(self.ui.channel_line_edit_sensitivity.text()),
            "is_resp": (
                True
                if self.ui.channel_combo_box_sensor_type.currentIndex() == 0
                else False
            ),
            "disp_name": self.ui.channel_line_edit_disp_name.text(),
            "direction": self.ui.channel_combo_box_sensor_direction.currentText(),
            "comment": self.ui.channel_line_edit_comment.text(),
            "serial_number": self.ui.channel_line_edit_serial_number.text(),
        }

    def combo_box_choice_change(self, idx):
        if idx == 0:  # Accel Form
            self.ui.channel_label_sensitivity.setText(
                "Sensitivity / " "mVs<sup>2</sup>·m<sup>-1</sup>"
            )
        elif idx == 1:
            self.ui.channel_label_sensitivity.setText(
                "Sensitivity / mV·N<sup>-1</sup>"
            )
        else:
            raise ValueError("")

    def channel_button_select_file_pressed(self):
        path, ext = QFileDialog.getOpenFileName(filter="*.ted")
        self.sdlma_channel.set_channel_info(teds_file_path=path)
        self.init_form_data()

    def channel_button_submit_pressed(self):
        self.window().accept()
