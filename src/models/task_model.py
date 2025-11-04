from datetime import date

import numpy as np
from PySide6 import QtGui
from PySide6.QtCore import QAbstractListModel, Qt
from PySide6.QtWidgets import QFileDialog
from sdlma_hardware.sdlma_hardware import SDLMANiTask, SDLMATask
from sdlma_modal_analysis.sdlma_measurement import (
    SDLMAMeasurement,
    SDLMATimeSeriesSEP005,
)

from util.models import data_proto, row_count_proto


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
        enable_buttons,
        start_timer,
        stop_timer,
    ):

        self.overflow_samples = overflow_samples
        self.double_impact_limit = double_impact_limit
        self.double_impact_indices = []
        self.selected = False

        self.name = name
        self.num_impacts = num_impacts
        self.impacts_to_perform = num_impacts
        self.impact_time = impact_time
        self.sampling_freq = sampling_freq
        self.channels = channels
        self.exc_dim, self.resp_dim = self.get_dimensions()
        self.window_len = int(self.impact_time * self.sampling_freq)
        self.num_samples = int(self.window_len * self.num_impacts)

        self.done_impacts = 0
        self.current_index = 0
        self.time_data, self.exc_data, self.resp_data = (None, None, None)
        self.sdlma_measurement = None
        self.reset()
        self.media_player = media_player
        self.enable_buttons = enable_buttons
        self.stop_timer = stop_timer
        self.start_timer = start_timer
        self.task = SDLMANiTask(
            name,
            impact_time,
            sampling_freq,
            self.channels,
            self.update,
            self.done,
        )

    def init(self):
        pass

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
            self.stop_timer()
            exc_comments, resp_comments = self.get_comments()
            exc_serial_numbers, resp_serial_numbers = self.get_serial_numbers()
            exc_names, resp_names = self.get_names()
            exc_directions, resp_directions = self.get_directions()
            exc = SDLMATimeSeriesSEP005.from_array(
                self.get_clean_impacts(self.exc_data),
                "N",
                self.sampling_freq,
                "f",
                exc_names,
                exc_directions,
                exc_comments,
                exc_serial_numbers,
            )
            resp = SDLMATimeSeriesSEP005.from_array(
                self.get_clean_impacts(self.resp_data),
                "m/s^2",
                self.sampling_freq,
                "a",
                resp_names,
                resp_directions,
                resp_comments,
                resp_serial_numbers,
            )
            self.sdlma_measurement = SDLMAMeasurement(
                self.name,
                window_len=int(self.impact_time * self.sampling_freq),
                sampling_freq=self.sampling_freq,
                exc=exc,
                resp=resp,
                comment="",
            )
        return 0

    def start(self):
        self.enable_buttons(False)
        self.media_player.play()
        self.task.start()

    def stop(self):
        self.task.stop()
        self.enable_buttons(True)

    def get_clean_impacts(self, arr):
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
        filename, _ = QFileDialog.getSaveFileName(
            dir=self.get_file_name(), filter="*h5"
        )
        if filename:
            self.sdlma_measurement.export_to_hd5f_file(filename)

    def get_file_name(self):
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
        self.time_data = np.zeros(self.num_samples, dtype=np.float64)
        self.exc_data = np.zeros(
            (self.exc_dim, self.num_samples), dtype=np.float64
        )
        self.resp_data = np.zeros(
            (self.resp_dim, self.num_samples), dtype=np.float64
        )
        self.done_impacts = 0
        self.impacts_to_perform = self.num_impacts
        self.current_index = 0
        self.double_impact_indices.clear()
        self.sdlma_measurement = None

    def get_dimensions(self):
        exc_dim, resp_dim = (0, 0)
        for i, gui_channel in enumerate(self.channels):
            if gui_channel.channel.is_resp:
                resp_dim += 1
            else:
                exc_dim += 1
        return exc_dim, resp_dim

    def get_comments(self):
        exc_comments = []
        resp_comments = []
        for i, gui_channel in enumerate(self.channels):
            if gui_channel.channel.is_resp:
                resp_comments.append(gui_channel.channel.comment)
            else:
                exc_comments.append(gui_channel.channel.comment)
        return exc_comments, resp_comments

    def get_serial_numbers(self):
        exc_serial_numbers = []
        resp_serial_numbers = []
        for i, gui_channel in enumerate(self.channels):
            if gui_channel.channel.is_resp:
                resp_serial_numbers.append(gui_channel.channel.comment)
            else:
                exc_serial_numbers.append(gui_channel.channel.comment)
        return exc_serial_numbers, resp_serial_numbers

    def get_names(self):
        exc_names = []
        resp_names = []
        for i, gui_channel in enumerate(self.channels):
            if gui_channel.channel.is_resp:
                resp_names.append(gui_channel.channel.disp_name)
            else:
                exc_names.append(gui_channel.channel.disp_name)
        return exc_names, resp_names

    def get_directions(self):
        exc_directions = []
        resp_directions = []
        for i, gui_channel in enumerate(self.channels):
            if gui_channel.channel.is_resp:
                resp_directions.append(gui_channel.channel.direction)
            else:
                exc_directions.append(gui_channel.channel.direction)
        return exc_directions, resp_directions

    def check_double_impact(self):
        double_impacts = self.sdlma_measurement.check_double_impact(
            self.overflow_samples,
            self.double_impact_limit,
        )
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
            (self.exc_dim, self.exc_data.shape[1] + self.num_samples),
            dtype=np.float64,
        )
        new_exc_data[:, : self.exc_data.shape[1]] = self.exc_data
        self.exc_data = new_exc_data

        # Extend resp_data
        new_resp_data = np.zeros(
            (self.resp_dim, self.resp_data.shape[1] + self.num_samples),
            dtype=np.float64,
        )
        new_resp_data[:, : self.resp_data.shape[1]] = self.resp_data

        self.resp_data = new_resp_data


class PyMATaskModel(QAbstractListModel):

    def __init__(self, *args, tasks: list[SDLMAGuiTask] = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.tasks = tasks or []

    def data(self, index, role):
        return data_proto(self.tasks, index, role)

    def rowCount(self, index):
        return row_count_proto(self.tasks)
