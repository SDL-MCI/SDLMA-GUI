from datetime import datetime

from PySide6 import QtCore
from PySide6.QtWidgets import QDialog, QWidget

from custom_widgets.meas.meas_task_widget import TaskWindow
from models.meas_models import SDLMAGuiTask, SDLMATaskModel, SDLMAChannel
from sdlma_hardware.sdlma_hardware import SDLMANiTask


class MeasMainWidget(QWidget):
    meas_done = QtCore.Signal(bool)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.ui = None
        self.none = None
        self.meas_tree_hardware_model = None
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.meas_update_progress)
        self.tasks_model = SDLMATaskModel()
        self.chosen_channels_model = SDLMAChannel()
        self.chosen_task = None
        self.init_task = None
        self.progress = 0
        self.meas_done.connect(self.meas_update_bar)

    def init(self, ui):
        self.ui = ui
        self.ui.meas_list_tasks.setModel(self.tasks_model)
        self.ui.meas_list_chosen_channels.setModel(self.chosen_channels_model)
        self.plot_widget = self.ui.meas_widget_plot
        self.plot_widget.init(self.ui)

    def meas_button_init_pressed(self):
        self.ui.meas_button_init.setEnabled(False)
        self.ui.media_player.play()

        self.init_task = SDLMANiTask(
            "INIT_TASK",
            9.0,
            12800,
            self.chosen_task.channels,
            lambda task_handle, evt_type, n_samples, cb_data: 0,
            lambda task_handle, status, cb_data: 0,
        )

        self.init_task.start()
        self.meas_buttons_enable(False)
        self.ui.meas_button_start_meas.setEnabled(False)
        self.ui.meas_button_stop_meas.setEnabled(False)
        QtCore.QTimer().singleShot(10000, self.meas_init_done)

    def meas_init_done(self):
        self.ui.meas_button_start_meas.setEnabled(True)
        self.meas_buttons_enable(True)
        self.ui.media_player.play()
        self.init_task.stop()

    def meas_button_start_meas_pressed(self):
        self.progress = 0
        self.ui.meas_button_start_meas.setEnabled(False)
        self.ui.meas_button_init.setEnabled(False)
        self.meas_start_timer(100)
        self.chosen_task.start()

    def meas_button_clear_pressed(self):
        self.chosen_task.reset()
        self.plot_widget.clear()
        self.meas_buttons_enable(False)
        self.ui.meas_button_start_meas.setEnabled(True)
        self.ui.meas_button_init.setEnabled(True)
        self.ui.meas_button_stop_meas.setEnabled(False)
        self.meas_init_task(self.chosen_task)

    def meas_button_stop_meas_pressed(self):
        self.chosen_task.stop()
        self.meas_stop_timer()
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
        self.meas_update_plots(False, -1, True)

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
            task_index = self.meas_get_task_index_from_name(
                self.chosen_task.name
            )
            if task_index != -1:
                del self.tasks_model.tasks[task_index]
            task_data = task_window.get_task_data()
            sdlma_gui_task = self.create_task(**task_data)
            self.meas_init_task(sdlma_gui_task)

            self.tasks_model.tasks.append(sdlma_gui_task)
            self.tasks_model.layoutChanged.emit()

    def meas_button_create_pressed(self):
        task_window = TaskWindow()
        if task_window.exec() == QDialog.Accepted:
            task_data = task_window.get_task_data()
            task_index = self.meas_get_task_index_from_name(task_data["name"])
            if task_index == -1:
                sdlma_gui_task = self.create_task(**task_data)
                self.tasks_model.tasks.append(sdlma_gui_task)
                self.tasks_model.layoutChanged.emit()
                self.meas_init_task(sdlma_gui_task)
            else:
                raise ValueError("Invalid task chosen!")

    def meas_tab_bar_double_clicked(self, idx):
        mark = False
        impact = idx - 1
        if impact >= 0:
            if impact in self.chosen_task.double_impact_indices:
                self.chosen_task.double_impact_indices.remove(impact)
                self.chosen_task.impacts_to_perform -= 1
                self.meas_update_plots(False, idx)
            else:
                mark = True
                self.chosen_task.double_impact_indices.append(impact)
                self.chosen_task.impacts_to_perform += 1
                self.meas_update_plots(True, idx)
            self.plot_widget.mark_unmark_double_impacts(idx, mark)
            self.chosen_task.resize_arrays()

    def meas_update_plots(self, add, idx, force=False):
        print(self.chosen_task.double_impact_indices)
        if add or (
            self.chosen_task.impacts_to_perform != len(
            self.plot_widget.tabs)
            and force
        ):
            curr_tabs = len(self.plot_widget.tabs) - 1
            if curr_tabs != self.chosen_task.impacts_to_perform:
                self.plot_widget.create_tabs(
                    curr_tabs,
                    self.chosen_task.impacts_to_perform,
                    self.chosen_task.channels,
                )
                self.plot_widget.setup_plot_lines(
                    self.chosen_task.channels,
                    curr_tabs + 1,
                    self.chosen_task.impacts_to_perform + 1,
                )
        else:
            self.plot_widget.remove_tab()
        if (
            self.chosen_task.done_impacts
            != self.chosen_task.impacts_to_perform
        ):
            self.ui.meas_button_start_meas.setEnabled(True)
            self.ui.meas_button_save_result.setEnabled(False)

    def meas_list_task_double_clicked(self, index):
        task = self.tasks_model.tasks[index.row()]
        self.meas_init_task(task)

    def meas_init_task(self, task):
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

    def meas_get_task_index_from_name(self, name):
        for i, task in enumerate(self.tasks_model.tasks):
            if task.name == name:
                return i
        return -1

    def create_task(
        self,
        name,
        num_impacts,
        impact_time,
        sampling_freq,
        overflow_samples,
        double_impact_limit,
        channels,
    ):
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
        self.meas_update_plot(
            self.chosen_task.time_data[: self.chosen_task.current_index],
            self.chosen_task.exc_data[:, : self.chosen_task.current_index],
            self.chosen_task.resp_data[:, : self.chosen_task.current_index],
            self.chosen_task.done_impacts,
        )
        self.meas_update_bar()

    def meas_start_timer(self, interval):
        self.ui.meas_progress_meas.setValue(0)
        self.timer.start(interval)

    def meas_stop_timer(self):
        self.timer.stop()
        self.meas_update_plot(
            self.chosen_task.time_data[: self.chosen_task.current_index],
            self.chosen_task.exc_data[:, : self.chosen_task.current_index],
            self.chosen_task.resp_data[:, : self.chosen_task.current_index],
            self.chosen_task.done_impacts - 1,
        )

    def meas_update_bar(self):
        self.ui.meas_progress_meas.setValue(self.progress)

    def meas_update_plot(self, time, exc_data, resp_data, done_impacts):
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

    def meas_task_done(self, done):
        self.meas_done.emit(True)
        self.meas_buttons_enable(done)
