from datetime import datetime

import numpy as np
from PySide6 import QtCore
from PySide6.QtCore import QModelIndex, Slot
from PySide6.QtWidgets import QDialog, QWidget
from sdlma_hardware.sdlma_hardware import SDLMANiTask

from custom_widgets.meas.meas_task_window import TaskWindow
from models.meas_models import SDLMAChannel, SDLMAGuiTask, SDLMATaskModel


class MeasMainWidget(QWidget):
    # Signal used to notify on a finished measurement.
    meas_done = QtCore.Signal(bool)

    def __init__(self, parent=None, *args, **kwargs):
        """
        Custom Widget Class connected to the Measurement tab of the PySide6
        GUI.
        """
        super().__init__(parent, *args, **kwargs)

        self.parent = parent
        self.ui = None
        self.meas_plot_widget = None
        self.meas_tree_hardware_model = None
        self.meas_timer = QtCore.QTimer()
        self.meas_timer.timeout.connect(self.meas_update_progress)
        self.meas_tasks_model = SDLMATaskModel()
        self.meas_chosen_channels_model = SDLMAChannel()
        self.meas_chosen_task = None
        self.meas_helper_task = None
        self.meas_progress = 0
        self.meas_done.connect(self.meas_update_bar)

    def init(self, ui):
        """
        Init function of the EMA Class.
        Assigns models, creates plots and adds
        line edit constraints.

        :param ui: The main ui object created by PySide6.
        """
        self.ui = ui
        self.ui.meas_list_tasks.setModel(self.meas_tasks_model)
        self.ui.meas_list_chosen_channels.setModel(
            self.meas_chosen_channels_model
        )
        self.meas_plot_widget = self.ui.meas_widget_plot
        self.meas_plot_widget.init(self.ui)

    @Slot()
    def meas_button_init_pressed(self):
        """
        Slot method used to start the initialization of the selected channels.
        The init takes roughly 10 seconds where the rest of the meas gui is
        disabled.
        """
        self.ui.meas_button_init.setEnabled(False)
        self.ui.media_player.play()
        self.meas_helper_task = SDLMANiTask(
            "INIT_TASK",
            9.0,
            12800,
            self.meas_chosen_task.channels,
            lambda task_handle, evt_type, n_samples, cb_data: 0,
            lambda task_handle, status, cb_data: 0,
        )
        self.meas_helper_task.start()
        self.meas_buttons_enable(False)
        self.ui.meas_button_start_meas.setEnabled(False)
        self.ui.meas_button_stop_meas.setEnabled(False)
        QtCore.QTimer().singleShot(10000, self.meas_init_done)

    def meas_init_done(self):
        """
        Helper method that is called after the initialization of the
        selected channels is done.
        :return:
        """
        self.ui.meas_button_start_meas.setEnabled(True)
        self.meas_buttons_enable(True)
        self.ui.media_player.play()
        self.meas_helper_task.stop()

    @Slot()
    def meas_button_start_meas_pressed(self):
        """
        Slot method that starts the selected measurement task.
        """
        self.meas_progress = 0
        self.ui.meas_button_start_meas.setEnabled(False)
        self.ui.meas_button_init.setEnabled(False)
        self.meas_start_timer(100)
        self.meas_chosen_task.start()

    @Slot()
    def meas_button_clear_pressed(self):
        """
        Slot method that clears/resets the gui and objects for a new
        measurement process.
        """
        self.meas_chosen_task.reset()
        self.meas_plot_widget.clear()
        self.meas_buttons_enable(False)
        self.ui.meas_button_start_meas.setEnabled(True)
        self.ui.meas_button_init.setEnabled(True)
        self.ui.meas_button_stop_meas.setEnabled(False)
        self.meas_init_task(self.meas_chosen_task)

    @Slot()
    def meas_button_stop_meas_pressed(self):
        """
        Slot method to stop measurements
        """
        self.meas_chosen_task.stop()
        self.meas_stop_timer()
        self.meas_button_clear_pressed()

    def meas_buttons_enable(self, enable: bool):
        """
        Method that enables or disables selected buttons
        :param enable: A bool indicating if buttons for starting or stopping
        should be enabled or disabled.
        """
        self.ui.meas_button_clear.setEnabled(enable)
        self.ui.meas_button_save_result.setEnabled(enable)
        # self.ui.meas_button_detect_double_impact.setEnabled(enable)
        self.ui.meas_button_edit_task.setEnabled(enable)
        self.ui.meas_button_stop_meas.setEnabled(not enable)

    @Slot()
    def meas_button_save_meas_pressed(self):
        """
        Slot Method that is utilized to save a measurement result
        """
        self.meas_chosen_task.save()

    @Slot()
    def meas_button_check_double_impact_pressed(self):
        """
        Slot method that checks if a double impact is present in the performed
        measurement
        """
        self.ui.meas_button_detect_double_impact.setEnabled(False)
        self.meas_plot_widget.mark_double_impacts(
            self.meas_chosen_task.check_double_impact()
        )
        self.meas_update_plots(False, True)

    @Slot()
    def meas_button_edit_task_pressed(self):
        """
        Method that is utilized to edit a measurement task
        :return:
        """
        task_data = {
            "name": self.meas_chosen_task.name,
            "num_impacts": str(self.meas_chosen_task.num_impacts),
            "impact_time": str(self.meas_chosen_task.impact_time),
            "sampling_freq": str(self.meas_chosen_task.sampling_freq),
            "overflow_samples": str(
                self.ui.meas_line_edit_task_overflow_samples.text()
            ),
            "double_impact_limit": str(
                self.ui.meas_line_edit_task_double_impact_limit.text()
            ),
            "channels": self.meas_chosen_task.channels,
        }
        self.meas_chosen_task.task.close()

        task_window = TaskWindow(task_data)
        if task_window.exec() == QDialog.Accepted:
            task_index = self.meas_get_task_index_from_name(
                self.meas_chosen_task.name
            )
            if task_index != -1:
                del self.meas_tasks_model.tasks[task_index]
            task_data = task_window.get_task_data()
            sdlma_gui_task = self.create_task(**task_data)
            self.meas_init_task(sdlma_gui_task)

            self.meas_tasks_model.tasks.append(sdlma_gui_task)
            self.meas_tasks_model.layoutChanged.emit()

    @Slot()
    def meas_button_create_pressed(self):
        """
        Method that is utilized to create a Task
        """
        task_window = TaskWindow()
        if task_window.exec() == QDialog.Accepted:
            task_data = task_window.get_task_data()
            task_index = self.meas_get_task_index_from_name(task_data["name"])
            if task_index == -1:
                sdlma_gui_task = self.create_task(**task_data)
                self.meas_tasks_model.tasks.append(sdlma_gui_task)
                self.meas_tasks_model.layoutChanged.emit()
                self.meas_init_task(sdlma_gui_task)
            else:
                raise ValueError("Invalid task chosen!")

    @Slot()
    def meas_tab_bar_double_clicked(self, index: QModelIndex):
        """
        Slot method for double clicking an impact tab in the gui.
        Adds or removes the selected impact from the double impact list
        depending on its current state.
        :param index: The index that has been clicked.
        """
        mark = False
        impact = index - 1
        if impact >= 0:
            if impact in self.meas_chosen_task.double_impact_indices:
                self.meas_chosen_task.double_impact_indices.remove(impact)
                self.meas_chosen_task.impacts_to_perform -= 1
                self.meas_update_plots(False)
            else:
                mark = True
                self.meas_chosen_task.double_impact_indices.append(impact)
                self.meas_chosen_task.impacts_to_perform += 1
                self.meas_update_plots(True)
            self.meas_plot_widget.mark_unmark_double_impacts(index, mark)
            self.meas_chosen_task.resize_arrays()

    def meas_update_plots(self, add: bool, force: bool = False):
        """
        Method to update the plot widget and add/remove tab.

        REALLY UGLY!!!!
        :param add: Bool to indicate removal or addition of tabs
        :param force: Force bool (needed for automatic recognition)
        """
        if add or (
            self.meas_chosen_task.impacts_to_perform
            != len(self.meas_plot_widget.tabs)
            and force
        ):
            curr_tabs = len(self.meas_plot_widget.tabs) - 1
            if curr_tabs != self.meas_chosen_task.impacts_to_perform:
                self.meas_plot_widget.create_tabs(
                    curr_tabs,
                    self.meas_chosen_task.impacts_to_perform,
                )
                self.meas_plot_widget.setup_plot_lines(
                    self.meas_chosen_task.channels,
                    curr_tabs + 1,
                    self.meas_chosen_task.impacts_to_perform + 1,
                )
        else:
            self.meas_plot_widget.remove_last_tab()
        if (
            self.meas_chosen_task.done_impacts
            != self.meas_chosen_task.impacts_to_perform
        ):
            self.ui.meas_button_start_meas.setEnabled(True)
            self.ui.meas_button_save_result.setEnabled(False)
        else:
            self.ui.meas_button_start_meas.setEnabled(False)
            self.meas_buttons_enable(True)

    @Slot()
    def meas_list_task_double_clicked(self, index: QtCore.QModelIndex):
        """
        Slot method that is utilized to load a created task
        :param index: The index of the task that shall be loaded
        """
        task = self.meas_tasks_model.tasks[index.row()]
        self.meas_init_task(task)

    def meas_init_task(self, task: SDLMAGuiTask):
        """
        Method to setup the gui with the chosen task information.

        :param task: The task that has been loaded
        """
        self.meas_chosen_channels_model.channels = []
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
            self.meas_chosen_channels_model.channels.append(channel)
        task.reset()
        self.meas_plot_widget.reset()

        self.ui.meas_button_start_meas.setEnabled(True)
        self.ui.meas_button_init.setEnabled(True)
        self.ui.meas_button_edit_task.setEnabled(True)

        self.meas_plot_widget.setup(task.num_impacts, task.channels)

        self.meas_chosen_channels_model.layoutChanged.emit()
        self.meas_chosen_task = task

    def meas_get_task_index_from_name(self, name: str) -> int:
        """
        Method to get the task index of the model from the task name
        """
        for i, task in enumerate(self.meas_tasks_model.tasks):
            if task.name == name:
                return i
        return -1

    def create_task(
        self,
        name: str,
        num_impacts: int,
        impact_time: float,
        sampling_freq: float,
        overflow_samples: float,
        double_impact_limit: float,
        channels: list,
    ):
        """
        Helper Method to create SDLMAGuiTasks
        :param name: The name of the task
        :param num_impacts: The number of impacts
        :param impact_time: The time for each impact
        :param sampling_freq: The sampling frequency of the measurement
        :param overflow_samples: The number of samples for double impact det.
        :param double_impact_limit: The limit for double impact det.
        :param channels: The channels that shall be used for the sampling
        :return:
        """
        return SDLMAGuiTask(
            name,
            num_impacts,
            impact_time,
            sampling_freq,
            overflow_samples,
            double_impact_limit,
            channels,
            media_player=self.ui.media_player,
            meas_task_done=self.meas_task_done,
            meas_start_timer=self.meas_start_timer,
            meas_stop_timer=self.meas_stop_timer,
        )

    def meas_update_progress(self):
        """
        Method to update the plots with the live measurement data
        """
        self.meas_update_plot(
            self.meas_chosen_task.time_data[
                : self.meas_chosen_task.current_index
            ],
            self.meas_chosen_task.exc_data[
                :, : self.meas_chosen_task.current_index
            ],
            self.meas_chosen_task.resp_data[
                :, : self.meas_chosen_task.current_index
            ],
            self.meas_chosen_task.done_impacts,
        )
        self.meas_update_bar()

    def meas_start_timer(self, interval: int):
        """
        Method that starts the interval timer for updating the live view
        :param interval: The refresh interval
        """
        self.ui.meas_progress_meas.setValue(0)
        self.meas_timer.start(interval)

    def meas_stop_timer(self):
        """
        Method to stop the timer for refreshing the live view
        """
        self.meas_timer.stop()
        self.meas_update_plot(
            self.meas_chosen_task.time_data[
                : self.meas_chosen_task.current_index
            ],
            self.meas_chosen_task.exc_data[
                :, : self.meas_chosen_task.current_index
            ],
            self.meas_chosen_task.resp_data[
                :, : self.meas_chosen_task.current_index
            ],
            self.meas_chosen_task.done_impacts - 1,
        )

    def meas_update_bar(self):
        """
        Method to update the progress bar
        """
        self.ui.meas_progress_meas.setValue(self.meas_progress)

    def meas_update_plot(
        self,
        time: np.array,
        exc_data: np.array,
        resp_data: np.array,
        done_impacts: int,
    ):
        """
        Method to update the plot widget and progress of the ongoing \
        measurement process.

        :param time: The time array (x axis)
        :param exc_data: The exc signals (y axis)
        :param resp_data: The resp signals (y axis)
        :param done_impacts: The number of performed impacts
        """
        self.meas_progress = int(
            (resp_data.shape[1] / self.meas_chosen_task.sampling_freq)
            / (
                self.meas_chosen_task.impact_time
                * self.meas_chosen_task.num_impacts
            )
            * 100
        )
        start = int(
            self.meas_chosen_task.sampling_freq
            * done_impacts
            * self.meas_chosen_task.impact_time
        )
        self.meas_plot_widget.update_plots(
            time, exc_data, resp_data, done_impacts + 1, start
        )

    def meas_task_done(self, done: bool):
        """
        Method used to update the done signal and enable
        the buttons after the measurement is done.
        :param done: Bool indicating if a measurement is done or not.
        """
        self.meas_done.emit(True)
        self.meas_buttons_enable(done)
