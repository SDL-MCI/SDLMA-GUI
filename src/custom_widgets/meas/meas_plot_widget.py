import random

import numpy as np
import pyqtgraph as pg
from pyqtgraph import GraphicsLayoutWidget
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QStyle, QVBoxLayout, QWidget


class MeasPlotWidget(QWidget):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        """
        Custom Widget Class connected to the plot sub section
        of the Meas Tab. Plots are created using pyqtgraph
        """
        self.exc_plot = None
        self.resp_plot = None
        self.qt_graph = None
        self.ui = None
        self.exc_plots = []
        self.resp_plots = []
        self.qt_graphs = []
        self.tabs = []

    def init(self, ui):
        """
        Method to connect the gui containers for the pyqtgraph plots
        with the correct member variables.
        
        :param ui: The main ui object of PySide6
        """
        self.ui = ui
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def setup(self, num_impacts: int, channels: list):
        """
        Method to setup the plot widgets depending on the amount of channels
        and impacts
        :param num_impacts: The number of impacts
        :param channels: The utilized channels
        :return: 
        """
        self.create_tab("meas_tab_combined", "Combined")
        self.create_qt_graph(self.tabs[0], "meas_plot_combined")
        self.create_plot_view(self.qt_graphs[0], "exc_comb", "resp_comb")
        self.create_tabs(0, num_impacts)
        self.setup_plot_lines(channels, 0, num_impacts + 1)

    def create_tabs(self, start_idx: int, end_idx: int):
        """
        Method to create tabs and number them according to the start and
        end index
        :param start_idx: Start index for the tab creation
        :param end_idx: End index for the tab creation
        """
        for i in range(start_idx, end_idx):
            tab_name = f"meas_tab_impact_{i}"
            self.create_tab(tab_name, f"Impact {i}")
            self.create_qt_graph(self.tabs[i + 1], f"meas_plot_impact_{i}")
            self.create_plot_view(
                self.qt_graphs[i + 1], f"exc_imp_{i}", f"resp_imp_{i}"
            )

    def remove_last_tab(self):
        """
        Method to remove the last tab created
        :return: 
        """
        self.resp_plots.pop()
        self.exc_plots.pop()
        self.qt_graphs.pop()
        self.tabs.pop()
        self.ui.meas_tab_plot.removeTab(self.ui.meas_tab_plot.count() - 1)

    def mark_double_impacts(self, double_impact_indices: list):
        """
        Method to mark double impacts in the tab view
        :param double_impact_indices: List of indices to mark
        """
        for idx in double_impact_indices:
            self.mark_unmark_double_impacts(idx + 1, mark=True)
        self.ui.meas_tab_plot.tabBar().update()

    def mark_unmark_double_impacts(self, index: int, mark: bool):
        """
        Method to mark or unmark double impacts in the tab view
        :param index: The index of the tab that shall be edited
        :param mark: Bool to indicate if mark should be set or removed
        """
        widget = self.tabs[index]
        if not widget:
            return

        tab_idx = self.ui.meas_tab_plot.indexOf(widget)
        if tab_idx == -1:
            return

        icon = (
            self.style().standardIcon(
                QStyle.StandardPixmap.SP_DialogCancelButton
            )
            if mark
            else QIcon()
        )
        self.ui.meas_tab_plot.setTabIcon(tab_idx, icon)

    def setup_plot_lines(self, channels, start_idx, end_idx):
        """
        Method to create the plot lines for the channels and
        also labeling them according to their corresponding impact indices.
        :param channels: The channels that should be plotted
        :param start_idx: The start index for the tab creation
        :param end_idx: The end index for the tab creation
        :return:
        """
        for i in range(start_idx, end_idx):
            for gui_channel in channels:
                disp_name = gui_channel.channel.disp_name
                if gui_channel.channel.is_resp:
                    self.create_plot_line(self.resp_plots[i], disp_name)
                else:
                    self.create_plot_line(self.exc_plots[i], disp_name)

    def create_plot_line(self, plot, disp_name: str):
        """
        Method to create a plot line for measurement signals

        :param plot: The plot object where the plot line should be plotted
        :param disp_name: The display name of the plot line
        :return:
        """
        pen = pg.mkPen(
            color=(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
        )
        plot.plot(pen=pen, name=disp_name)
        plot.addLegend()

    def create_tab(self, tab_name: str, heading: str):
        """
        Method to create a qt widget tab for the measurement tab widget.
        :param tab_name: The internal tab name
        :param heading: The heading of the tab
        :return:
        """
        new_tab = QWidget()
        self.layout.addWidget(new_tab)
        new_tab.setObjectName(tab_name)
        idx = self.ui.meas_tab_plot.addTab(new_tab, heading)
        self.tabs.append(new_tab)

    def create_qt_graph(self, parent , name: str):
        """
        Method to create a qt graph widget

        :param parent: The tab widget where the graph should be located
        :param name: The name of the graph
        :return:
        """
        new_plot = GraphicsLayoutWidget(parent)
        layout = QVBoxLayout(parent)
        layout.addWidget(new_plot)
        new_plot.setObjectName(name)
        new_plot.setBackground("w")
        new_plot.show()
        self.qt_graphs.append(new_plot)

    def create_plot_view(self, qt_graph, exc_name: str, resp_name: str):
        """
        Method to create a plot view in a qt graph widget

        :param qt_graph: The graph widget object
        :param exc_name: The name of the excitation signal
        :param resp_name: The name of the response signal
        :return:
        """
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

    def create_plot(self, qt_graph, row: int, col: int, name: str, x_label:
    str, y_label: str, styles: dict):
        """
        Method to add a plot to a qt graph object
        
        :param qt_graph: The qt graph object
        :param row: The row of the plot
        :param col: The col of the plot
        :param name: The name of the plot
        :param x_label: The x label of the plot
        :param y_label: The y label of the plot
        :param styles: Dictionary containing style parameters
        :return: 
        """
        plot = qt_graph.addPlot(row, col, name=name)
        view_box = plot.getViewBox()
        view_box.setBackgroundColor("w")
        plot.setTitle(name)
        plot.setLabel("left", y_label, **styles)
        plot.setLabel("bottom", x_label, **styles)
        plot.addLegend()
        plot.showGrid(x=True, y=True)
        return plot

    def update_plots(self, time: np.array, exc: np.array, resp: np.array,
                     idx: int, start: int):
        """
        Method to update the plots with data from the measurement
        process
        :param time: The time array
        :param exc: The excitation signal
        :param resp: The response signal
        :param idx: The idx of the plot that shall be updated
        :param start: The start index for the plotting
        :return:
        """
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

    def create_plot_lines(self, plot, number_of_lines: int):
        """
        Method to create plot lines in a qt plot
        :param plot: The plot object
        :param number_of_lines: The number of lines that shall be added
        :return:
        """
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
        """
        Currently unused function to clear
        """

    def reset(self):
        """
        Method to reset the plot widget to initial conditions.
        """
        self.exc_plots = []
        self.resp_plots = []
        self.qt_graphs = []
        for i in reversed(range(self.ui.meas_tab_plot.count())):
            self.ui.meas_tab_plot.removeTab(i)
        self.tabs.clear()
        self.ui.meas_tab_plot.clear()
