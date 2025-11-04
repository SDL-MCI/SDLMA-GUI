import random

import numpy as np
import pyqtgraph as pg
from numpy import linspace
from pyqtgraph import GraphicsLayoutWidget
from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QSizePolicy,
    QStackedLayout,
    QStyle,
    QVBoxLayout,
    QWidget,
)


# https://github.com/pyqtgraph/pyqtgraph/blob/4951bd743ef7e2a5198615573167301c9603b72f/examples/linkedViews.py
class MeasPlotWidget(QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.exc_plot = None
        self.resp_plot = None
        self.qt_graph = None
        self.ui = None
        self.exc_plots = []
        self.resp_plots = []
        self.qt_graphs = []
        self.tabs = []

    def init_old(self, pyqtgraph_widget):
        styles = {"color": "b", "font-size": "18px"}
        self.qt_graph = pyqtgraph_widget
        self.qt_graph.setBackground("w")
        self.exc_plot = self.create_plot(
            0, 0, "Excitation", "Time / s", "f / N", styles
        )
        self.resp_plot = self.create_plot(
            1,
            0,
            "Response",
            "Time / s",
            "a / ms<sup>-2</sup>",
            styles,
        )

    def init(self, ui):
        self.ui = ui
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def setup(self, num_impacts, channels):
        self.create_tab("meas_tab_combined", "Combined")
        self.create_qt_graph(self.tabs[0], "meas_plot_combined")
        self.create_plot_view(self.qt_graphs[0], "exc_comb", "resp_comb")
        self.create_tabs(0, num_impacts, channels)
        self.setup_plot_lines(channels, 0, num_impacts + 1)

    def create_tabs(self, start_idx, end_idx, channels):

        for i in range(start_idx, end_idx):
            tab_name = f"meas_tab_impact_{i}"
            self.create_tab(tab_name, f"Impact {i}")
            self.create_qt_graph(self.tabs[i + 1], f"meas_plot_impact_{i}")
            self.create_plot_view(
                self.qt_graphs[i + 1], f"exc_imp_{i}", f"resp_imp_{i}"
            )

    def mark_double_impacts(self, double_impact_indices):
        for i in double_impact_indices:
            icon = self.style().standardIcon(
                QStyle.StandardPixmap.SP_DialogCancelButton
            )
            tab_idx = self.ui.meas_tab_plot.indexOf(
                self.ui.meas_tab_plot.findChild(
                    QWidget, f"meas_tab_impact_{i}"
                )
            )
            self.ui.meas_tab_plot.setTabIcon(tab_idx, icon)
        self.ui.meas_tab_plot.tabBar().update()

    def mark_unmark_double_impacts(self, index, mark):
        if mark:
            icon = self.style().standardIcon(
                QStyle.StandardPixmap.SP_DialogCancelButton
            )
        else:
            icon = QIcon()
        tab_idx = self.ui.meas_tab_plot.indexOf(
            self.ui.meas_tab_plot.findChild(
                QWidget, f"meas_tab_impact_{index}"
            )
        )
        self.ui.meas_tab_plot.setTabIcon(tab_idx, icon)

    def setup_plot_lines(self, channels, start_idx, end_idx):
        for i in range(start_idx, end_idx):
            for gui_channel in channels:
                disp_name = gui_channel.channel.disp_name
                if gui_channel.channel.is_resp:
                    self.create_plot_line(self.resp_plots[i], disp_name)
                else:
                    self.create_plot_line(self.exc_plots[i], disp_name)

    def create_plot_line(self, plot, disp_name):
        pen = pg.mkPen(
            color=(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
        )
        plot.plot(pen=pen, name=disp_name)
        plot.addLegend()

    def create_tab(self, tab_name, heading):
        new_tab = QWidget()
        self.layout.addWidget(new_tab)
        new_tab.setObjectName(tab_name)
        idx = self.ui.meas_tab_plot.addTab(new_tab, heading)
        self.tabs.append(new_tab)

    def create_qt_graph(self, parent, name):
        new_plot = GraphicsLayoutWidget(parent)
        layout = QVBoxLayout(parent)
        layout.addWidget(new_plot)
        new_plot.setObjectName(name)
        new_plot.setBackground("w")
        new_plot.show()

        self.qt_graphs.append(new_plot)

    def create_plot_view(self, qt_graph, exc_name, resp_name):
        styles = {"color": "b", "font-size": "18px"}
        exc_desc = {
            "row": 0,
            "col": 0,
            "name": exc_name,
            "x_label": "t / s",
            "y_label": "f / N",
            "styles": styles,
        }
        resp_desc = {
            "row": 1,
            "col": 0,
            "name": resp_name,
            "x_label": "t / s",
            "y_label": "a / ms<sup>-2</sup>",
            "styles": styles,
        }
        self.exc_plots.append(self.create_plot(qt_graph, **exc_desc))
        self.resp_plots.append(self.create_plot(qt_graph, **resp_desc))

    def create_plot(self, qt_graph, row, col, name, x_label, y_label, styles):
        # Set name to make axis linking possible
        plot = qt_graph.addPlot(row, col, name=name)
        view_box = plot.getViewBox()
        view_box.setBackgroundColor("w")
        plot.setTitle(name)
        plot.setLabel("left", y_label, **styles)
        plot.setLabel("bottom", x_label, **styles)
        plot.addLegend()
        plot.showGrid(x=True, y=True)
        return plot

    def update_plots(self, time, exc, resp, idx, start):
        for i, row in enumerate(exc):
            if idx <= len(self.exc_plots):
                self.exc_plots[0].items[i].setData(time, row.tolist())
                self.exc_plots[idx].items[i].setData(
                    time[start:], row[start:].tolist()
                )
        for i, row in enumerate(resp):
            if idx <= len(self.resp_plots):
                self.resp_plots[0].items[i].setData(time, row.tolist())
                self.resp_plots[idx].items[i].setData(
                    time[start:], row[start:].tolist()
                )

    # def check_plots(self, exc_ndim, resp_ndim):
    #     if len(self.exc_plot.items) != exc_ndim:
    #         self.create_plot_lines(self.exc_plot, exc_ndim)
    #     if len(self.resp_plot.items) != resp_ndim:
    #         self.create_plot_lines(self.resp_plot, resp_ndim)

    def create_plot_lines(self, plot, number_of_lines):
        for i in range(0, number_of_lines):
            pen = pg.mkPen(
                color=(
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )
            )
            plot.plot(pen=pen, name="")

    def clear(self):
        for i in range(0, len(self.resp_plots)):
            pass

    def reset(self):
        self.exc_plots = []
        self.resp_plots = []
        self.qt_graphs = []
        for i in reversed(range(self.ui.meas_tab_plot.count())):
            self.ui.meas_tab_plot.removeTab(i)
        self.tabs.clear()
        self.ui.meas_tab_plot.clear()

