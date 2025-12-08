import random

import numpy as np
import pyqtgraph as pg
from PySide6.QtWidgets import QWidget


class EmaPlotWidget(QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        """
         Custom Widget Class connected to the plot sub section
        of the EMA Tab. Plots are created using pyqtgraph
        """
        super().__init__(parent, *args, **kwargs)
        self.stab_widget = None
        self.frf_plus_coh_graph_widget = None
        self.frf_phase_coh_graph = None
        self.frf_plot = None
        self.coherence_plot = None
        self.phase_plot = None
        self.frf_coherence_plot = None

    def init(
        self,
        frf_phase_coh_graph_widget,
        frf_plus_coh_graph_widget,
        x_range,
    ):
        """
        Method to connect the gui containers for the pyqtgraph plots
        with the correct member variables.
        :param frf_phase_coh_graph_widget: The placeholder widget utilized
        for the frf, phase and coherence plot.
        :param frf_plus_coh_graph_widget: Placeholder widget utilized for the
        combined frf and phase plot.
        :param x_range: The frequency range for the current view
        """
        styles = {"color": "b", "font-size": "18px"}
        self.frf_phase_coh_graph = frf_phase_coh_graph_widget
        self.frf_plus_coh_graph_widget = frf_plus_coh_graph_widget
        self.frf_phase_coh_graph.setBackground("w")
        self.frf_plus_coh_graph_widget.setBackground("w")

        self.frf_plot = self.create_plot(
            self.frf_phase_coh_graph,
            0,
            0,
            "FRF",
            "f / Hz",
            "m/s²·N⁻¹",
            False,
            True,
            styles,
            x_range,
        )
        self.phase_plot = self.create_plot(
            self.frf_phase_coh_graph,
            1,
            0,
            "Phase",
            "f / Hz",
            "phi / deg",
            False,
            False,
            styles,
            x_range,
            y_ticks=[-180, -90, 0, 90, 180],
        )
        self.coherence_plot = self.create_plot(
            self.frf_phase_coh_graph,
            2,
            0,
            "Coherence",
            "f / Hz",
            "1",
            False,
            False,
            styles,
            x_range,
        )

        self.frf_coherence_plot = self.create_plot(
            self.frf_plus_coh_graph_widget,
            0,
            0,
            "FRF and Coherence",
            "f / Hz",
            "m/s²·N⁻¹",
            False,
            True,
            styles,
            x_range,
            y_label2="1",
        )

    def create_plot(
        self,
        graph_widget: object,
        row: int,
        col: int,
        name: str,
        x_label: str,
        y_label: str,
        x_log: bool,
        y_log: bool,
        styles: dict,
        x_range: list,
        y_range: list = None,
        x_ticks: list = None,
        y_ticks: list = None,
        y_label2: list = None,
    ):
        """
        Method to create and initialize a created plot.

        :param graph_widget: The widget that shall contain plot/
        :param row: The row of the plot in the widget
        :param col: The col of the plot in the widget
        :param name: The display name for the plot
        :param x_label: The x label for the plot
        :param y_label: The y label for the plot
        :param x_log: Bool to indicate a logarithmic scale
        :param y_log: Bool to indicate a logarithmic scale
        :param styles: Dictionary of style parameters
        :param x_range: The x range for the current view
        :param y_range: The y range for the current view
        :param x_ticks: The x ticks for the axis labeling
        :param y_ticks: The y ticks for the axis labeling
        :param y_label2: A second y axis label if a second axis is present
        :return:
        """
        # Set name to make axis linking possible
        plot = graph_widget.addPlot(row, col, name=name)
        plot.setLogMode(x_log, y_log)
        plot.setTitle(name)
        plot.setLabel("left", y_label, **styles)
        plot.setLabel("bottom", x_label, **styles)

        plot.showGrid(x=True, y=True)

        view_box_left = plot.getViewBox()
        plot.getViewBox().setBackgroundColor("w")
        plot.setXRange(x_range[0], x_range[1], padding=0)

        if y_ticks:
            plot.getAxis("left").setTicks(
                [[(y_tick, str(y_tick)) for y_tick in y_ticks]]
            )

        plot.addLegend()

        return {
            "plot": plot,
            "view_box_left": view_box_left,
            "view_box_right": None,
        }

    def init_frf_coherence_plot(self):
        """
        Method to initialize the frf and coherence plot
        :return:
        """
        self.frf_coherence_plot["plot"].showAxis("right")
        styles = {"color": "b", "font-size": "18px"}
        y_label = "1"
        self.frf_coherence_plot["plot"].setLabel("right", y_label, **styles)
        view_box_right = pg.ViewBox()
        self.frf_coherence_plot["plot"].scene().addItem(view_box_right)
        self.frf_coherence_plot["plot"].getAxis("right").linkToView(
            view_box_right
        )
        view_box_right.setXLink(self.frf_coherence_plot["plot"])
        self.frf_coherence_plot["plot"].vb.sigResized.connect(
            self.update_view_frf_coh
        )
        self.frf_coherence_plot["view_box_right"] = view_box_right

        self.frf_coherence_plot["view_box_right"].enableAutoRange(
            axis=pg.ViewBox.YAxis
        )

    def update_view_frf_coh(self):
        """
        Method to update the views of the frf and coherence plot to the
        current scene.
        :return:
        """
        vb = self.frf_coherence_plot["plot"].vb
        self.frf_coherence_plot["plot"].vb.setBackgroundColor(None)
        vb_right = self.frf_coherence_plot["view_box_right"]
        rect = vb.mapRectToScene(vb.boundingRect())
        vb_right.setGeometry(rect)
        vb_right.linkedViewChanged(vb, vb_right.XAxis)

    def create_frf_plots(
        self,
        name: str,
        frf_matrix: np.array,
        f_axis: np.array,
        coherence: np.array,
        exc_names: list,
        resp_names: list,
        estimator="H1",
    ):
        """
        Method to create the frf plots.
        :param name: The display name of the plot
        :param frf_matrix: The frf_matrix that shall be plotted
        :param f_axis: The frequency values that shall be plotted and us
        :param coherence: The coherence matrix
        :param exc_names: The exc signal names
        :param resp_names: The resp signal names
        :param estimator: The utilized estimator for frf reconstruction.
        :return:
        """
        for i in range(frf_matrix.shape[0]):  # Resp
            pen = pg.mkPen(
                color=(
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )
            )
            self.create_plot_line(
                pen,
                self.frf_plot,
                f_axis,
                np.abs(frf_matrix)[i, :],
                f"{name}_{exc_names[0]}_{resp_names[i]}_{estimator}",
            )
            self.create_plot_line(
                pen,
                self.phase_plot,
                f_axis,
                np.angle(frf_matrix, deg=True)[i, :],
                f"{name}_{exc_names[0]}_{resp_names[i]}_{estimator}",
            )
            self.create_plot_line(
                pen,
                self.coherence_plot,
                f_axis,
                np.abs(coherence[i, :]),
                f"{name}_{exc_names[0]}_{resp_names[i]}_{estimator}",
            )
            self.create_plot_line(
                pen,
                self.frf_coherence_plot,
                f_axis,
                np.abs(frf_matrix)[i, :],
                f"{name}_{exc_names[0]}_{resp_names[i]}_{estimator}_FRF",
                "left",
            )
            self.create_plot_line(
                pen,
                self.frf_coherence_plot,
                f_axis,
                np.abs(coherence[i, :]),
                f"{name}_{exc_names[0]}_{resp_names[i]}_{estimator}_Coh",
                "right",
            )
            self.update_view_frf_coh()

    def create_plot_line(
        self,
        pen: object,
        plot: object,
        x_data: np.array,
        y_data: np.array,
        name: str,
        ax: str = None,
    ):
        """
        Method to create a line in the given plot.

        :param pen: The pen (style) that is used to draw the line
        :param plot: The plot object where the line shall be added
        :param x_data: The x data shall be plotted
        :param y_data: The y data shall be plotted
        :param name: The name of the plotted line
        :param ax: Which ax should be used (case for two y axis for example)
        :return:
        """
        if ax == "right":
            item = pg.PlotDataItem(
                x_data, np.log10(y_data), pen=pen, name=name
            )
            plot["view_box_right"].addItem(item)
            plot["plot"].legend.addItem(item, name)
        else:
            plot["plot"].plot(x_data, y_data, pen=pen, name=name)

    def create_plot_lines(self, plot, number_of_lines):
        for i in range(0, number_of_lines):
            pen = pg.mkPen(
                color=(
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )
            )
            plot.plot(pen=pen)

    def reset(self):
        """
        Method to reset the plot widget to default settings
        """
        self.coherence_plot["plot"].clear()
        self.phase_plot["plot"].clear()
        self.frf_plot["plot"].clear()
        self.frf_coherence_plot["plot"].legend.clear()
        self.frf_coherence_plot["plot"].clear()
        self.frf_coherence_plot["view_box_right"].clear()
