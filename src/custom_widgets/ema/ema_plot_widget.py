import random

import numpy as np
import pyqtgraph as pg
from PySide6.QtWidgets import QWidget


class EmaPlotWidget(QWidget):
    def __init__(self, parent=None, *args, **kwargs):
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

    # https://stackoverflow.com/questions/23679159/two-y-scales-in-pyqtgraph-twinx-like
    # https://github.com/pyqtgraph/pyqtgraph/discussions/3015
    def create_plot(
        self,
        graph_widget,
        row,
        col,
        name,
        x_label,
        y_label,
        x_log,
        y_log,
        styles,
        x_range,
        y_range=None,
        x_ticks=None,
        y_ticks=None,
        y_label2=None,
    ):
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

        # self.frf_coherence_plot["plot"].getAxis("bottom").get()
        # plot.getViewBox().setMinimumSize(400, 300)
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
        # view_box_right.setBackgroundColor("yellow")
        self.frf_coherence_plot["plot"].vb.sigResized.connect(
            self.update_view_frf_coh
        )
        self.frf_coherence_plot["view_box_right"] = view_box_right

        self.frf_coherence_plot["view_box_right"].enableAutoRange(
            axis=pg.ViewBox.YAxis
        )

    def update_view_frf_coh(self):
        vb = self.frf_coherence_plot["plot"].vb
        self.frf_coherence_plot["plot"].vb.setBackgroundColor(None)
        vb_right = self.frf_coherence_plot["view_box_right"]
        rect = vb.mapRectToScene(vb.boundingRect())
        vb_right.setGeometry(rect)
        vb_right.linkedViewChanged(vb, vb_right.XAxis)

    def create_frf_plots(
        self,
        name,
        frf_matrix,
        f_axis,
        coherence,
        exc_names,
        resp_names,
        estimator="H1",
    ):
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

    def create_plot_line(self, pen, plot, x_data, y_data, name, ax=None):
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
        self.coherence_plot["plot"].clear()
        self.phase_plot["plot"].clear()
        self.frf_plot["plot"].clear()
        self.frf_coherence_plot["plot"].legend.clear()
        self.frf_coherence_plot["plot"].clear()
        self.frf_coherence_plot["view_box_right"].clear()
