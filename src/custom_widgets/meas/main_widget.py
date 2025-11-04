import logging
import time

import numpy as np
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QUrl, Slot
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QDial, QDialog, QFileDialog, QLineEdit, QWidget
from sdlma_hardware.sdlma_hardware import SDLMAHardware, SDLMANiTask
from sdlma_modal_analysis.sdlma_measurement import SDLMAMeasurement

from custom_widgets.meas.meas_task import TaskWindow
from models.hardware_model import ChannelModel
from models.task_model import PyMATaskModel, SDLMAGuiTask
from ui import sdlma_channel_gui, sdlma_task_gui


# https://doc.qt.io/qtforpython-6/PySide6/QtCore/Property.html
# https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/
# https://pythonpyqt.com/qtimer/
# https://www.pythonguis.com/tutorials/pyside6-creating-multiple-windows/
# https://doc.qt.io/qtforpython-5/PySide2/QtCore/SignalEvent.html
# https://www.pythonguis.com/tutorials/pyside6-creating-multiple-windows/
class MeasMainWidget(QWidget):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.ui = None
        self.plot_widget = None
        self.meas_tree_hardware_model = None
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.init_timer = QtCore.QTimer(singleShot=True)
        self.init_timer.timeout.connect(self.meas_button_stop_meas_pressed)
        self.tasks_model = PyMATaskModel()
        self.chosen_channels_model = ChannelModel()
        self.chosen_task = None
        self.progress = 0

    def init(self, ui):
        self.ui = ui
        self.ui.meas_list_tasks.setModel(self.tasks_model)
        self.ui.meas_list_chosen_channels.setModel(self.chosen_channels_model)
        self.plot_widget = self.ui.meas_widget_plot
        self.plot_widget.init(self.ui)

    def meas_button_init_pressed(self):
        # self.ui.meas_button_start_meas.setEnabled(False)
        self.ui.meas_button_init.setEnabled(False)
        self.chosen_task.task.init()

    def meas_button_start_meas_pressed(self):
        self.progress = 0
        self.ui.meas_button_start_meas.setEnabled(False)
        self.ui.meas_button_init.setEnabled(False)
        self.start_timer(100)
        self.chosen_task.start()

    def meas_button_clear_pressed(self):
        self.chosen_task.reset()
        self.plot_widget.clear()
        self.meas_buttons_enable(False)
        self.ui.meas_button_start_meas.setEnabled(True)
        self.ui.meas_button_init.setEnabled(True)
        self.ui.meas_button_stop_meas.setEnabled(False)
        self.init_task(self.chosen_task)

    def meas_button_stop_meas_pressed(self):
        # self.init_task.stop()
        self.chosen_task.stop()
        self.meas_button_clear_pressed()

    def meas_buttons_enable(self, enable):
        self.ui.meas_button_clear.setEnabled(enable)
        self.ui.meas_button_save_result.setEnabled(enable)
        self.ui.meas_button_detect_double_impact.setEnabled(enable)
        self.ui.meas_button_edit_task.setEnabled(enable)
        self.ui.meas_button_stop_meas.setEnabled(not enable)

    def meas_button_save_meas_pressed(self):
        self.chosen_task.save()

    def meas_button_check_double_impact_pressed(self):
        self.ui.meas_button_detect_double_impact.setEnabled(False)
        self.plot_widget.mark_double_impacts(
            self.chosen_task.check_double_impact()
        )
        self.plot_widget.create_tabs(
            self.chosen_task.done_impacts,
            self.chosen_task.impacts_to_perform,
            self.chosen_task.channels,
        )
        self.plot_widget.setup_plot_lines(
            self.chosen_task.channels,
            self.chosen_task.done_impacts + 1,
            self.chosen_task.impacts_to_perform + 1,
        )
        if (
            self.chosen_task.done_impacts
            != self.chosen_task.impacts_to_perform
        ):
            self.ui.meas_button_start_meas.setEnabled(True)
            self.ui.meas_button_init.setEnabled(True)
            self.ui.meas_button_save_result.setEnabled(False)

    def meas_button_edit_task_pressed(self):
        task_data = {
            "name": self.chosen_task.name,
            "num_impacts": str(self.chosen_task.num_impacts),
            "impact_time": str(self.chosen_task.impact_time),
            "sampling_freq": str(self.chosen_task.sampling_freq),
            "overflow_samples": str(
                self.ui.meas_line_edit_task_overflow_samples.text()
            ),
            "double_impact_limit": str(
                self.ui.meas_line_edit_task_double_impact_limit.text()
            ),
            "channels": self.chosen_task.channels,
        }
        self.chosen_task.task.close()

        task_window = TaskWindow(task_data)
        if task_window.exec() == QDialog.Accepted:
            task_index = self.get_task_index_from_name(self.chosen_task.name)
            if task_index != -1:
                del self.tasks_model.tasks[task_index]
            task_data = task_window.get_task_data()
            sdlma_gui_task = SDLMAGuiTask(
                media_player=self.ui.media_player,
                enable_buttons=self.meas_buttons_enable,
                start_timer=self.start_timer,
                stop_timer=self.stop_timer,
                **task_data
            )
            self.init_task(sdlma_gui_task)

            self.tasks_model.tasks.append(sdlma_gui_task)
            self.tasks_model.layoutChanged.emit()

    def get_task_index_from_name(self, name):
        for i, task in enumerate(self.tasks_model.tasks):
            if task.name == name:
                return i
        return -1

    def meas_list_task_double_clicked(self, index):
        task = self.tasks_model.tasks[index.row()]
        self.init_task(task)

    def init_task(self, task):
        self.chosen_channels_model.channels = []
        self.ui.meas_line_edit_task_name.setText(task.name)
        self.ui.meas_line_edit_task_num_impacts.setText(str(task.num_impacts))
        self.ui.meas_line_edit_task_impact_time.setText(str(task.impact_time))
        self.ui.meas_line_edit_task_sampling_freq.setText(
            str(task.sampling_freq)
        )
        self.ui.meas_line_edit_task_overflow_samples.setText(
            str(task.overflow_samples)
        )
        self.ui.meas_line_edit_task_double_impact_limit.setText(
            str(task.double_impact_limit)
        )
        for channel in task.channels:

            self.chosen_channels_model.channels.append(channel)
        task.reset()
        self.plot_widget.reset()

        self.ui.meas_button_start_meas.setEnabled(True)
        self.ui.meas_button_init.setEnabled(True)
        self.ui.meas_button_edit_task.setEnabled(True)

        self.plot_widget.setup(task.num_impacts, task.channels)

        self.chosen_channels_model.layoutChanged.emit()
        self.chosen_task = task

    def meas_button_create_pressed(self):
        task_window = TaskWindow()
        if task_window.exec() == QDialog.Accepted:
            task_data = task_window.get_task_data()
            task_index = self.get_task_index_from_name(task_data["name"])
            if task_index == -1:
                sdlma_gui_task = SDLMAGuiTask(
                    media_player=self.ui.media_player,
                    enable_buttons=self.meas_buttons_enable,
                    start_timer=self.start_timer,
                    stop_timer=self.stop_timer,
                    **task_data
                )
                self.tasks_model.tasks.append(sdlma_gui_task)
                self.tasks_model.layoutChanged.emit()
                self.init_task(sdlma_gui_task)
            else:
                raise ValueError("Invalid task chosen!")

    def update_progress(self):
        self.update_plot(
            self.chosen_task.time_data[: self.chosen_task.current_index],
            self.chosen_task.exc_data[:, : self.chosen_task.current_index],
            self.chosen_task.resp_data[:, : self.chosen_task.current_index],
            self.chosen_task.done_impacts,
        )
        self.ui.meas_progress_meas.setValue(self.progress)

    def stop_timer(self):
        self.timer.stop()
        self.update_plot(
            self.chosen_task.time_data[: self.chosen_task.current_index],
            self.chosen_task.exc_data[:, : self.chosen_task.current_index],
            self.chosen_task.resp_data[:, : self.chosen_task.current_index],
            self.chosen_task.done_impacts - 1,
        )

    def start_timer(self, interval):
        self.ui.meas_progress_meas.setValue(0)
        self.timer.start(interval)

    def update_plot(self, time, exc_data, resp_data, done_impacts):
        self.progress = int(
            (resp_data.shape[1] / self.chosen_task.sampling_freq)
            / (self.chosen_task.impact_time * self.chosen_task.num_impacts)
            * 100
        )
        start = int(
            self.chosen_task.sampling_freq
            * done_impacts
            * self.chosen_task.impact_time
        )
        self.plot_widget.update_plots(
            time, exc_data, resp_data, done_impacts + 1, start
        )

    def meas_tab_bar_double_clicked(self, index):
        mark = False
        if index in self.chosen_task.double_impact_indices:
            self.chosen_task.double_impact_indices.remove(index)
        else:
            mark = True
            self.chosen_task.double_impact_indices.append(index)
        self.plot_widget.mark_unmark_double_impacts(
            self.chosen_task.index, mark
        )
