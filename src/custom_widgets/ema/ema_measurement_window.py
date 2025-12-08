from PySide6 import QtCore
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog, QFileDialog
from sdlma_modal_analysis.sdlma_measurement import SDLMAMeasurement

from models.ema_models import SignalModel
from ui import sdlma_meas_gui


class SDLMAGuiSignal:

    def __init__(self, data: dict):
        """
        GUI Wrapper for the SDLMA-Core Signals
        """
        self.data = data
        self.name = data["name"]  # Needed for proto functions
        self.selected = True


class SDLMAGuiMeasurement:

    def __init__(self, sdlma_measurement: SDLMAMeasurement):
        """
        GUI Wrapper for the SDLMA-Core Measurements
        """
        self.sdlma_measurement = sdlma_measurement
        self.name = sdlma_measurement.name  # Needed for proto functions
        self.selected = True


class SDLMAMeasurementWindow(QDialog):
    def __init__(self):
        """
        Pyside6 Dialog Window utilized to select signals from measurements
        for EMA
        """
        super().__init__()
        self.ui = sdlma_meas_gui.Ui_Dialog()
        self.ui.setupUi(self)
        self.resp_signals_model = SignalModel()
        self.exc_signals_model = SignalModel()
        self.sampling_freq = None
        self.window_len = None
        self.name = None
        self.init()

    def init(self):
        """
        Init function of the Measurement Window.
        """
        path, ext = QFileDialog.getOpenFileName(filter="*.h5")
        sdlma_data = SDLMAMeasurement.import_from_hd5f_file(path)
        self.ui.ema_line_edit_name.setText(sdlma_data.name)
        self.ui.ema_line_edit_sampling_freq.setText(
            str(sdlma_data.sampling_freq)
        )
        self.name = sdlma_data.name
        self.sampling_freq = sdlma_data.sampling_freq
        self.window_len = sdlma_data.window_len
        self.add_signal(self.exc_signals_model, sdlma_data.exc)
        self.add_signal(self.resp_signals_model, sdlma_data.resp)
        self.ui.ema_list_exc_signals.setModel(self.exc_signals_model)
        self.ui.ema_list_resp_signals.setModel(self.resp_signals_model)
        self.check_add_button()

    @Slot()
    def ema_button_add_pressed(self):
        """
        Slot Method that is triggered when the user is done with selecting
        signals from the measurements to close the dialog in a handled way.
        """
        self.window().accept()

    @Slot()
    def ema_list_exc_signals_double_clicked(self, index: QtCore.QModelIndex):
        """
        Slot method that is triggered when the user double clicks an exc
        signal. Selects or unselects the pressed signal
        :param index: The index of the measurement in the list.
        """
        self.ema_list_signal_double_clicked(
            index, self.exc_signals_model.signals
        )

    @Slot()
    def ema_list_resp_signals_double_clicked(self, index: QtCore.QModelIndex):
        """
        Slot method that is triggered when the user double clicks an resp
        signal. Selects or unselects the pressed signal
        :param index: The index of the measurement in the list.
        """
        self.ema_list_signal_double_clicked(
            index, self.resp_signals_model.signals
        )

    def ema_list_signal_double_clicked(
        self, index: QtCore.QModelIndex, model: SignalModel
    ):
        """
        Helper method utilized for exc, resp signal selection/unselection
        :param index: The index of the selected signal
        :param model: The model (list) of signals
        """
        clicked_signal = model.signals[index.row()]
        for signal in model.signals:
            if clicked_signal.name == signal.name:
                signal.selected = not signal.selected
        self.check_add_button()

    def check_add_button(self):
        """
        Method that checks if at least one exc and one resp signal
        have been selected from the measurement. This is a needed condition
        for the EMA process.
        """
        enable = any(
            signal.selected for signal in self.resp_signals_model.signals
        ) and any(signal.selected for signal in self.exc_signals_model.signals)
        self.ui.ema_button_add.setEnabled(enable)

    def add_signal(self, sig_model: SignalModel, sig_list: list):
        """
        Method that wraps SDLMA-Core Signals in the GUI Wrapper classes
        and adds them to the correct models.
        :param sig_model: The PySide6 Model where the signals shall be added
        :param sig_list: The list of signals that shall be added.
        :return:
        """
        for signal in sig_list:
            sdlma_signal = SDLMAGuiSignal(
                signal,
            )
            sig_model.signals.append(sdlma_signal)
        sig_model.layoutChanged.emit()

    def get_chosen_signals(self):
        """
        Helper method that returns the selected signals from the gui models.
        """
        exc_signals = self.get_selected_signals(self.exc_signals_model.signals)
        resp_signals = self.get_selected_signals(
            self.resp_signals_model.signals
        )

        return [item.data for item in exc_signals], [
            item.data for item in resp_signals
        ]

    def get_selected_signals(self, signals: list):
        """
        Helper method that loops through a list of signals and returns all
        the selected signals.
        :param signals: The list of signals that shall be looped.
        :return: A list of selected signals.
        """
        sel_signals = []
        for signal in signals:
            if signal.selected:
                sel_signals.append(signal)
        return sel_signals
