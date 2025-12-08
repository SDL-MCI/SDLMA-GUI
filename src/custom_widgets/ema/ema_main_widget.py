from datetime import date
from idlelib.rpc import response_queue

from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QDialog, QFileDialog, QWidget
from sdlma_modal_analysis.sdlma_ema import SDLMAEMA
from sdlma_modal_analysis.sdlma_measurement import SDLMAMeasurement

from models.ema_models import EMAModel, SignalModel
from ui import sdlma_meas_gui


class EmaMainWidget(QWidget):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = None
        self.plot_widget = None
        self.meas_tree_hardware_model = None
        self.progress = 0
        self.ema_model = EMAModel()
        self.ema_data = None

    def init(self, ui):
        self.ui = ui
        self.ui.ema_list_frfs.setModel(self.ema_model)
        self.plot_widget = self.ui.ema_widget_plot
        self.plot_widget.init(
            self.ui.ema_plot_frf_phase_coh,
            self.ui.ema_plot_frf_plus_coh,
            [
                float(self.ui.ema_line_edit_freq_boundary_lower.text()),
                float(self.ui.ema_line_edit_freq_boundary_upper.text()),
            ],
        )
        self.init_line_edits()
        self.init_ema()

    def init_line_edits(self):
        list_validator = QtGui.QRegularExpressionValidator(
            r"^\s*\d+(\.\d+)?(\s*,\s*\d+(\.\d+)?)*\s*$"
        )
        i_validator = QtGui.QIntValidator(bottom=1, top=100000)
        d_validator = QtGui.QDoubleValidator(
            bottom=0.1, top=100000, decimals=1
        )

        self.ui.ema_line_edit_freq_boundary_lower.setValidator(d_validator)
        self.ui.ema_line_edit_freq_boundary_upper.setValidator(d_validator)
        self.ui.ema_line_edit_pol_order.setValidator(i_validator)
        self.ui.ema_line_edit_nat_freq.setValidator(list_validator)

    def init_ema(self):
        freq_str = self.ui.ema_line_edit_nat_freq.text()
        nat_frequencies = (
            list(map(float, freq_str.split(","))) if freq_str else []
        )
        self.ema_data = SDLMAEMA(
            float(self.ui.ema_line_edit_freq_boundary_lower.text()),
            float(self.ui.ema_line_edit_freq_boundary_upper.text()),
            int(self.ui.ema_line_edit_pol_order.text()),
            self.ui.ema_combo_box_pole_calc.currentText(),
            nat_frequencies,
        )
        # self.ui.ema_tab_widget.setCurrentIndex(1)
        self.plot_widget.init_frf_coherence_plot()

    def ema_list_frf_double_clicked(self, index):
        measurement = self.ema_model.measurements[index.row()]
        measurement.selected = not measurement.selected
        # self.ema_data.init_ema()
        self.check_ema_button_select_poles()

    def check_ema_button_select_poles(self):
        for measurement in self.ema_model.measurements:
            if measurement.selected:
                self.ui.ema_button_calc.setEnabled(True)
                return
        self.ui.ema_button_select_poles.setEnabled(False)

    def ema_button_load_pressed(self):
        meas_window = MeasurementWindow()
        if meas_window.exec() == QDialog.Accepted:
            exc_signals, resp_signals = meas_window.get_chosen_signals()

            sdlma_measurement = SDLMAMeasurement(
                meas_window.name,
                meas_window.window_len,
                meas_window.sampling_freq,
                exc_signals,
                resp_signals,
                "",
            )
            self.ema_model.measurements.append(
                SDLMAGuiMeasurement(sdlma_measurement)
            )
            self.ema_model.layoutChanged.emit()
            exc_names, resp_names = sdlma_measurement.get_names()
            self.plot_widget.create_frf_plots(
                "MEAS",
                sdlma_measurement.frf_object.get_FRF("H1", form="accelerance")[
                    :, 0, 1:
                ],
                sdlma_measurement.frf_object.get_f_axis()[1:],
                sdlma_measurement.frf_object.get_coherence()[:, 1:],
                exc_names,
                resp_names,
            )
            self.check_ema_button_select_poles()

    def ema_solver_changed(self, index):
        self.ema_setting_changed()

    def ema_button_calc_pressed(self):
        exc_names_list, resp_names_list = [], []
        for measurement in self.ema_model.measurements:
            if measurement.selected:
                self.ema_data.add_measurement(measurement.sdlma_measurement)
                exc_names, resp_names = (
                    measurement.sdlma_measurement.get_names()
                )
                exc_names_list.extend(exc_names)
                resp_names_list.extend(resp_names)

        self.ema_data.calc()
        # print(self.ema_data.exc_names)
        # self.plot_widget.create_frf_plots(
        #     "EMA",
        #     self.ema_data.frf_matrix,
        #     self.ema_data.f_axis,
        #     self.ema_data.coherence,
        #     exc_names_list,
        #     resp_names_list,
        # )
        self.ema_data.get_poles()
        self.ui.ema_button_calc.setEnabled(False)
        self.ui.ema_button_load.setEnabled(False)
        self.ui.ema_button_select_poles.setEnabled(True)

    def ema_button_select_poles_pressed(self):
        self.ema_data.select_poles()
        # self.ui.ema_button_add.setEnabled(False)
        self.ui.ema_line_edit_nat_freq_sel.setText(str(self.ema_data.nat_freq))
        self.ui.ema_line_edit_damping_coeff_sel.setText(
            str(self.ema_data.nat_xi)
        )
        self.ui.ema_button_save.setEnabled(True)

    def ema_setting_changed(self):
        self.ema_button_clear_pressed()

    def ema_button_clear_pressed(self):
        self.ema_model.measurements = []
        self.ema_model.layoutChanged.emit()
        self.init_ema()
        self.plot_widget.reset()
        self.ui.ema_button_load.setEnabled(True)
        self.ui.ema_button_select_poles.setEnabled(False)
        self.ui.ema_button_save.setEnabled(False)
        self.ui.ema_button_calc.setEnabled(False)

    def ema_button_save_pressed(self):
        cur_date = date.today()
        cur_date = cur_date.strftime("%Y-%m-%d")
        filename, _ = QFileDialog.getSaveFileName(
            dir=f"{cur_date}_ema.h5", filter="*h5"
        )
        self.ema_data.export_to_hd5f_file(filename)
        # test = SDLMAEMA.import_from_hd5f_file(filename)

    def ema_nat_freq_edited(self):
        freq_str = self.ui.ema_line_edit_nat_freq.text()
        nat_frequencies = (
            list(map(float, freq_str.split(","))) if freq_str else []
        )
        self.ema_data.freq_estimates = nat_frequencies


class SDLMAGuiSignal:

    def __init__(self, data: dict):
        self.data = data
        self.name = data["name"]  # Needed for proto functions
        self.selected = True


class SDLMAGuiMeasurement:

    def __init__(self, sdlma_measurement: SDLMAMeasurement):
        self.sdlma_measurement = sdlma_measurement
        self.name = sdlma_measurement.name  # Needed for proto functions
        self.selected = True


class MeasurementWindow(QDialog):
    def __init__(self):
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

    def ema_button_add_pressed(self):
        self.window().accept()

    def ema_list_exc_signals_double_clicked(self, index):
        clicked_signal = self.exc_signals_model.signals[index.row()]
        for signal in self.exc_signals_model.signals:
            if clicked_signal.name == signal.name:
                signal.selected = not signal.selected
        self.check_add_button()

    def ema_list_resp_signals_double_clicked(self, index):
        clicked_signal = self.resp_signals_model.signals[index.row()]
        for signal in self.resp_signals_model.signals:
            if clicked_signal.name == signal.name:
                signal.selected = not signal.selected
        self.check_add_button()

    def check_add_button(self):
        enable = any(
            signal.selected for signal in self.resp_signals_model.signals
        ) and any(signal.selected for signal in self.exc_signals_model.signals)
        self.ui.ema_button_add.setEnabled(enable)

    def add_signal(self, sig_model, sig_list):

        for signal in sig_list:
            sdlma_signal = SDLMAGuiSignal(
                signal,
            )
            sig_model.signals.append(sdlma_signal)
        sig_model.layoutChanged.emit()

    def get_chosen_signals(self):
        exc_signals = self.get_selected_signals(self.exc_signals_model.signals)
        resp_signals = self.get_selected_signals(
            self.resp_signals_model.signals
        )

        return [item.data for item in exc_signals], [
            item.data for item in resp_signals
        ]

    def get_selected_signals(self, signals):
        sel_signals = []
        for signal in signals:
            if signal.selected:
                sel_signals.append(signal)
        return sel_signals
