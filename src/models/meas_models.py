from datetime import date

import numpy as np
from PySide6 import QtCore
from PySide6.QtCore import QAbstractListModel
from PySide6.QtWidgets import QFileDialog
from sdlma_hardware.sdlma_hardware import SDLMANiTask
from sdlma_modal_analysis.sdlma_measurement import (
    SDLMAMeasurement,
    SDLMATimeSeriesSEP005,
)

from util.models import data_proto, row_count_proto


class SDLMAGuiChannel:
    """
    Helper model for channels utilized for display/picking reasons in the GUI
    """

    def __init__(self, channel):
        self.channel = channel
        self.name = self.channel.name
        self.selected = False


class SDLMAChannel(QtCore.QAbstractListModel):
    """
    Model utilized to display channels in the SDLMA Gui.
    """

    def __init__(self, *args, channels: SDLMAGuiChannel = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.channels = channels or []

    def data(self, index, role):
        return data_proto(self.channels, index, role)

    def rowCount(self, index):
        return row_count_proto(self.channels)

    def get_selected_channels(self):
        sel_channels = []
        for gui_channel in self.channels:
            if gui_channel.selected:
                sel_channels.append(gui_channel)
        return sel_channels


class SDLMAGuiTask:

    def __init__(
        self,
        name,
        num_impacts,
        impact_time,
        sampling_freq,
        overflow_samples,
        double_impact_limit,
        channels,
        media_player,
        meas_task_done,
        meas_start_timer,
        meas_stop_timer,
    ):
        self.name = name
        self.num_impacts = num_impacts
        self.impact_time = impact_time
        self.sampling_freq = sampling_freq
        self.overflow_samples = overflow_samples
        self.double_impact_limit = double_impact_limit
        self.channels = channels
        self.double_impact_indices = []
        self.media_player = media_player
        self.meas_task_done = meas_task_done
        self.meas_task_done = meas_task_done
        self.meas_stop_timer = meas_stop_timer
        self.meas_start_timer = meas_start_timer

        self.selected = False
        self.impacts_to_perform = num_impacts
        self.exc_info, self.resp_info = self.get_info()
        self.window_len = int(self.impact_time * self.sampling_freq)
        self.num_samples = int(self.window_len * self.num_impacts)
        self.done_impacts = 0
        self.current_index = 0
        self.time_data, self.exc_data, self.resp_data = (None, None, None)
        self.sdlma_measurement = None
        self.reset()

        self.task = SDLMANiTask(
            name,
            impact_time,
            sampling_freq,
            self.channels,
            self.update,
            self.done,
        )

    def update(
        self,
        task_handle,
        every_n_samples_event_type,
        number_of_samples,
        callback_data,
    ):

        data = np.array(self.task.read(number_of_samples))
        exc, resp = ([], [])

        for i, gui_channel in enumerate(self.channels):
            append = data[i] if data.ndim > 1 else data
            if gui_channel.channel.is_resp:
                resp.append(append)
            else:
                exc.append(append)

        resp = np.array(resp)
        exc = np.array(exc)
        if len(exc) > 0:
            self.exc_data[
                :, self.current_index : self.current_index + number_of_samples
            ] = exc
        if len(resp) > 0:
            self.resp_data[
                :, self.current_index : self.current_index + number_of_samples
            ] = resp

        self.update_time_array(number_of_samples)
        self.current_index += number_of_samples
        return 0

    def update_time_array(self, number_of_samples):
        """
        Method to update the time array with the appropriate spacing
        from the sampling frequency and number of samples
        """
        start_time = 0
        if self.current_index != 0:
            start_time = self.time_data[self.current_index - 1]
        time = np.linspace(
            start_time,
            start_time + number_of_samples / self.sampling_freq,
            number_of_samples,
        )

        self.time_data[
            self.current_index : self.current_index + number_of_samples
        ] = time

    def done(self, task_handle, status, callback_data):
        self.stop()
        self.done_impacts += 1
        if self.done_impacts < self.impacts_to_perform:
            self.start()
        else:
            self.meas_stop_timer()
            exc = SDLMATimeSeriesSEP005.from_array(
                self.get_clean_impacts(self.exc_data),
                "N",
                self.sampling_freq,
                "f",
                self.exc_info["names"],
                self.exc_info["directions"],
                self.exc_info["comments"],
                self.exc_info["serial_numbers"],
            )
            resp = SDLMATimeSeriesSEP005.from_array(
                self.get_clean_impacts(self.resp_data),
                "m/s^2",
                self.sampling_freq,
                "a",
                self.resp_info["names"],
                self.resp_info["directions"],
                self.resp_info["comments"],
                self.resp_info["serial_numbers"],
            )
            self.sdlma_measurement = SDLMAMeasurement(
                self.name,
                window_len=int(self.impact_time * self.sampling_freq),
                sampling_freq=self.sampling_freq,
                exc=exc,
                resp=resp,
                comment="",
            )
            self.meas_task_done(True)

        return 0

    def start(self):
        """ """
        self.meas_task_done(False)
        self.media_player.play()
        self.task.start()

    def stop(self):
        """ """
        self.task.stop()

    def get_clean_impacts(self, arr):
        """
        Method to get the impacts without double impacts from the given array
        """
        keep_impacts = [
            i
            for i in range(self.done_impacts)
            if i not in self.double_impact_indices
        ]

        clean_impacts = [
            arr[:, i * self.window_len : (i + 1) * self.window_len]
            for i in keep_impacts
        ]
        return np.concatenate(clean_impacts, axis=1)

    def save(self):
        """
        Method to save the measurement to the disk
        """
        filename, _ = QFileDialog.getSaveFileName(
            dir=self.get_file_name(), filter="*h5"
        )
        if filename:
            self.sdlma_measurement.export_to_hd5f_file(filename)

    def get_file_name(self):
        """
        Method to get a sample file name
        """
        cur_date = date.today()
        cur_date = cur_date.strftime("%Y-%m-%d")
        temp_name = f"{cur_date}_EXC_"
        for signal in self.sdlma_measurement.exc:
            temp_name += f"{signal["name"]}_"
        temp_name += "RESP"
        for signal in self.sdlma_measurement.resp:
            temp_name += f"_{signal["name"]}"
        temp_name += ".h5"
        return temp_name

    def reset(self):
        """
        Method to reset the currently selected task
        """
        self.time_data = np.zeros(self.num_samples, dtype=np.float64)
        self.exc_data = np.zeros(
            (self.exc_info["dim"], self.num_samples), dtype=np.float64
        )
        self.resp_data = np.zeros(
            (self.resp_info["dim"], self.num_samples), dtype=np.float64
        )
        self.done_impacts = 0
        self.impacts_to_perform = self.num_impacts
        self.current_index = 0
        self.double_impact_indices.clear()
        self.sdlma_measurement = None

    def get_info(self):
        """
        Method to get info of the excitation and response channels
        """
        exc_info, resp_info = (
            {
                "dim": 0,
                "comments": [],
                "serial_numbers": [],
                "names": [],
                "directions": [],
            },
            {
                "dim": 0,
                "comments": [],
                "serial_numbers": [],
                "names": [],
                "directions": [],
            },
        )
        for i, gui_channel in enumerate(self.channels):
            info = resp_info if gui_channel.channel.is_resp else exc_info
            info["dim"] += 1
            info["comments"].append(gui_channel.channel.comment)
            info["serial_numbers"].append(gui_channel.channel.serial_number)
            info["names"].append(gui_channel.channel.disp_name)
            info["directions"].append(gui_channel.channel.direction)
        return exc_info, resp_info

    def check_double_impact(self):
        double_impacts = self.sdlma_measurement.check_double_impact(
            self.overflow_samples,
            self.double_impact_limit,
        )
        return self.add_new_impacts(double_impacts)

    def add_new_impacts(self, double_impacts):
        new_impacts = len(double_impacts) - len(self.double_impact_indices)
        if new_impacts > 0:
            self.impacts_to_perform += new_impacts
            self.double_impact_indices = double_impacts
            self.resize_arrays()
        return double_impacts

    def resize_arrays(self):

        # Extend time_data
        new_time_data = np.zeros(
            self.time_data.shape[0] + self.num_samples, dtype=np.float64
        )
        new_time_data[: self.time_data.shape[0]] = self.time_data
        self.time_data = new_time_data

        # Extend exc_data
        new_exc_data = np.zeros(
            (self.exc_info["dim"], self.exc_data.shape[1] + self.num_samples),
            dtype=np.float64,
        )
        new_exc_data[:, : self.exc_data.shape[1]] = self.exc_data
        self.exc_data = new_exc_data

        # Extend resp_data
        new_resp_data = np.zeros(
            (
                self.resp_info["dim"],
                self.resp_data.shape[1] + self.num_samples,
            ),
            dtype=np.float64,
        )
        new_resp_data[:, : self.resp_data.shape[1]] = self.resp_data

        self.resp_data = new_resp_data


class SDLMATaskModel(QAbstractListModel):

    def __init__(self, *args, tasks: list[SDLMAGuiTask] = None, **kwargs):
        """
        Model used for storing gui tasks.
        """
        super().__init__(*args, **kwargs)
        self.tasks = tasks or []

    def data(self, index, role):
        return data_proto(self.tasks, index, role)

    def rowCount(self, index):
        return row_count_proto(self.tasks)
