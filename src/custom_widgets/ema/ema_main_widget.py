from datetime import date
from idlelib.rpc import response_queue

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog, QFileDialog, QWidget
from sdlma_modal_analysis.sdlma_ema import SDLMAEMA
from sdlma_modal_analysis.sdlma_measurement import SDLMAMeasurement

from custom_widgets.ema.ema_measurement_window import SDLMAGuiMeasurement, SDLMAMeasurementWindow
from models.ema_models import EMAModel, SignalModel
from ui import sdlma_meas_gui


class EmaMainWidget(QWidget):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        """
        Custom Widget Class connected to the EMA TAB of the PySide6 
        GUI.
        """
        self.ui = None
        self.ema_plot_widget = None
        self.ema_model = EMAModel()
        self.ema_data = None

    def init(self, ui):
        """
        Init function of the EMA Class.
        Assigns models, creates plots and adds
        line edit constraints.

        :param ui: The main ui object created by PySide6.
        """
        self.ui = ui
        self.ui.ema_list_frfs.setModel(self.ema_model)
        self.ema_plot_widget = self.ui.ema_widget_plot
        self.ema_plot_widget.init(
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
        """
        Method to assign input constraints to the line edits
        of the ema tab.
        """
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
        """
        Method that initializes the SDLMA-Core SDLMAEMA Object that is
        utilized in the backend to perform curve fitting, pole selection,
        etc...
        """
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
        self.ema_plot_widget.init_frf_coherence_plot()

    @Slot(int)
    def ema_list_frf_double_clicked(self, index: QtCore.QModelIndex):
        """
        Double click callback to select or unselect measurements that
        shall be utilized by the SDLMAEMA Object for calculations.
        :param index: The index of the pressed measurement in the
        measurement list.
        """
        measurement = self.ema_model.measurements[index.row()]
        measurement.selected = not measurement.selected
        self.check_ema_button_select_poles()

    def check_ema_button_select_poles(self):
        """
        Method that checks if at least one measurement is selected
        to perform the EMA using the SDLMA-Core SDLMAEMA Object.
        """
        for measurement in self.ema_model.measurements:
            if measurement.selected:
                self.ui.ema_button_calc.setEnabled(True)
                return
        self.ui.ema_button_select_poles.setEnabled(False)

    @Slot()
    def ema_button_load_pressed(self):
        """
        Method that instantiates the measurement selection window.
        Allows the user to utilize the integrated file browser, selec
        a measurement file and select signals in this file for usage
        in the EMA calculations.
        """
        meas_window = SDLMAMeasurementWindow()
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
            self.ema_plot_widget.create_frf_plots(
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

    @Slot(int)
    def ema_solver_changed(self, index: QtCore.QModelIndex):
        """
        Slot Method that is triggered when the curve fitting algorithm
        has been changed. Currently resets complete EMA Tab.
        :param index: The index of items in the dropdown.
        """
        self.ema_setting_changed()

    @Slot()
    def ema_button_calc_pressed(self):
        """
        Slot method that is triggered when the user click on the calc button.
        Starts EMA modal parameter reconstruction.
        """ ""
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
        self.ema_data.get_poles()
        self.ui.ema_button_calc.setEnabled(False)
        self.ui.ema_button_load.setEnabled(False)
        self.ui.ema_button_select_poles.setEnabled(True)

    @Slot()
    def ema_button_select_poles_pressed(self):
        """
        Slot method that is triggered when the user click on the select
        poles button. Either opens the gui of sdypy to select poles or
        utilizes the passed list of natural frequencies for selection.
        """
        self.ema_data.select_poles()
        self.ui.ema_line_edit_nat_freq_sel.setText(str(self.ema_data.nat_freq))
        self.ui.ema_line_edit_damping_coeff_sel.setText(
            str(self.ema_data.nat_xi)
        )
        self.ui.ema_button_save.setEnabled(True)

    def ema_setting_changed(self):
        """
        Method that is triggered if the ema settings have been changed.
        Currently not really needed and just calls clear. Left for future use.
        """
        self.ema_button_clear_pressed()

    @Slot()
    def ema_button_clear_pressed(self):
        """
        Slot method that is triggered when the clear button is pressed.
        Resets everything for the ema tab to standard settings.
        """
        self.ema_model.measurements = []
        self.ema_model.layoutChanged.emit()
        self.init_ema()
        self.ema_plot_widget.reset()
        self.ui.ema_button_load.setEnabled(True)
        self.ui.ema_button_select_poles.setEnabled(False)
        self.ui.ema_button_save.setEnabled(False)
        self.ui.ema_button_calc.setEnabled(False)

    @Slot()
    def ema_button_save_pressed(self):
        """
        Slot method that is triggered when the save button is pressed.
        Allows the user to save the EMA process results to the disk.
        Suggests a default file name using the current date.
        """
        cur_date = date.today()
        cur_date = cur_date.strftime("%Y-%m-%d")
        filename, _ = QFileDialog.getSaveFileName(
            dir=f"{cur_date}_ema.h5", filter="*h5"
        )
        self.ema_data.export_to_hd5f_file(filename)

    @Slot()
    def ema_nat_freq_edited(self):
        """
        Slot method that is triggered when the natural frequency list has been
        edited. Updates the list of natural frequencies used for pole selction.
        """
        freq_str = self.ui.ema_line_edit_nat_freq.text()
        nat_frequencies = (
            list(map(float, freq_str.split(","))) if freq_str else []
        )
        self.ema_data.freq_estimates = nat_frequencies
