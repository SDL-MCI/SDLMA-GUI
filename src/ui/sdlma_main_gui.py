# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sdlma_main_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QButtonGroup,
    QComboBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListView, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

from custom_widgets.ema.ema_main_widget import EmaMainWidget
from custom_widgets.ema.ema_plot_widget import EmaPlotWidget
from custom_widgets.meas.meas_main_widget import MeasMainWidget
from custom_widgets.meas.meas_plot_widget import MeasPlotWidget
from custom_widgets.post_proc.post_proc_geometry_widget import GeometryWidget
from custom_widgets.post_proc.post_proc_main_widget import PostProcMainWidget
from pyqtgraph import GraphicsLayoutWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1754, 1068)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(6)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.setup_tab = QWidget()
        self.setup_tab.setObjectName(u"setup_tab")
        sizePolicy.setHeightForWidth(self.setup_tab.sizePolicy().hasHeightForWidth())
        self.setup_tab.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.setup_tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabWidget.addTab(self.setup_tab, "")
        self.meas_tab = QWidget()
        self.meas_tab.setObjectName(u"meas_tab")
        sizePolicy.setHeightForWidth(self.meas_tab.sizePolicy().hasHeightForWidth())
        self.meas_tab.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.meas_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.meas_widget_main = MeasMainWidget(self.meas_tab)
        self.meas_widget_main.setObjectName(u"meas_widget_main")
        sizePolicy.setHeightForWidth(self.meas_widget_main.sizePolicy().hasHeightForWidth())
        self.meas_widget_main.setSizePolicy(sizePolicy)
        self.meas_widget_main.setProperty(u"sampling_freq", 0)
        self.meas_widget_main.setProperty(u"meas_time", 0.000000000000000)
        self.horizontalLayout_6 = QHBoxLayout(self.meas_widget_main)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.meas_layout_task = QVBoxLayout()
        self.meas_layout_task.setObjectName(u"meas_layout_task")
        self.meas_layout_task.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.meas_label_start_stop = QLabel(self.meas_widget_main)
        self.meas_label_start_stop.setObjectName(u"meas_label_start_stop")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.meas_label_start_stop.sizePolicy().hasHeightForWidth())
        self.meas_label_start_stop.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(15)
        font.setBold(True)
        self.meas_label_start_stop.setFont(font)
        self.meas_label_start_stop.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.meas_label_start_stop.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.meas_layout_task.addWidget(self.meas_label_start_stop)

        self.meas_label_load_task = QLabel(self.meas_widget_main)
        self.meas_label_load_task.setObjectName(u"meas_label_load_task")
        self.meas_label_load_task.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.meas_label_load_task.sizePolicy().hasHeightForWidth())
        self.meas_label_load_task.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.meas_label_load_task.setFont(font1)
        self.meas_label_load_task.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.meas_label_load_task.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.meas_layout_task.addWidget(self.meas_label_load_task)

        self.meas_list_tasks = QListView(self.meas_widget_main)
        self.meas_list_tasks.setObjectName(u"meas_list_tasks")

        self.meas_layout_task.addWidget(self.meas_list_tasks)

        self.meas_layout_create_load = QHBoxLayout()
        self.meas_layout_create_load.setObjectName(u"meas_layout_create_load")
        self.meas_button_create_task = QPushButton(self.meas_widget_main)
        self.meas_button_create_task.setObjectName(u"meas_button_create_task")

        self.meas_layout_create_load.addWidget(self.meas_button_create_task)

        self.meas_button_edit_task = QPushButton(self.meas_widget_main)
        self.meas_button_edit_task.setObjectName(u"meas_button_edit_task")
        self.meas_button_edit_task.setEnabled(False)

        self.meas_layout_create_load.addWidget(self.meas_button_edit_task)


        self.meas_layout_task.addLayout(self.meas_layout_create_load)

        self.meas_layout_task_edit = QHBoxLayout()
        self.meas_layout_task_edit.setObjectName(u"meas_layout_task_edit")
        self.meas_label_task_name = QLabel(self.meas_widget_main)
        self.meas_label_task_name.setObjectName(u"meas_label_task_name")
        self.meas_label_task_name.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.meas_label_task_name.sizePolicy().hasHeightForWidth())
        self.meas_label_task_name.setSizePolicy(sizePolicy2)
        self.meas_label_task_name.setFont(font1)
        self.meas_label_task_name.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.meas_label_task_name.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.meas_layout_task_edit.addWidget(self.meas_label_task_name)

        self.meas_button_init = QPushButton(self.meas_widget_main)
        self.meas_button_init.setObjectName(u"meas_button_init")
        self.meas_button_init.setEnabled(False)

        self.meas_layout_task_edit.addWidget(self.meas_button_init)


        self.meas_layout_task.addLayout(self.meas_layout_task_edit)

        self.meas_line_edit_task_name = QLineEdit(self.meas_widget_main)
        self.meas_line_edit_task_name.setObjectName(u"meas_line_edit_task_name")
        self.meas_line_edit_task_name.setEnabled(False)

        self.meas_layout_task.addWidget(self.meas_line_edit_task_name)

        self.meas_label_num_impacts = QLabel(self.meas_widget_main)
        self.meas_label_num_impacts.setObjectName(u"meas_label_num_impacts")
        self.meas_label_num_impacts.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.meas_label_num_impacts.sizePolicy().hasHeightForWidth())
        self.meas_label_num_impacts.setSizePolicy(sizePolicy1)
        self.meas_label_num_impacts.setFont(font1)
        self.meas_label_num_impacts.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.meas_label_num_impacts.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.meas_layout_task.addWidget(self.meas_label_num_impacts)

        self.meas_line_edit_task_num_impacts = QLineEdit(self.meas_widget_main)
        self.meas_line_edit_task_num_impacts.setObjectName(u"meas_line_edit_task_num_impacts")
        self.meas_line_edit_task_num_impacts.setEnabled(False)
        self.meas_line_edit_task_num_impacts.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)

        self.meas_layout_task.addWidget(self.meas_line_edit_task_num_impacts)

        self.meas_label_impact_time = QLabel(self.meas_widget_main)
        self.meas_label_impact_time.setObjectName(u"meas_label_impact_time")
        self.meas_label_impact_time.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.meas_label_impact_time.sizePolicy().hasHeightForWidth())
        self.meas_label_impact_time.setSizePolicy(sizePolicy1)
        self.meas_label_impact_time.setFont(font1)
        self.meas_label_impact_time.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.meas_label_impact_time.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.meas_layout_task.addWidget(self.meas_label_impact_time)

        self.meas_line_edit_task_impact_time = QLineEdit(self.meas_widget_main)
        self.meas_line_edit_task_impact_time.setObjectName(u"meas_line_edit_task_impact_time")
        self.meas_line_edit_task_impact_time.setEnabled(False)

        self.meas_layout_task.addWidget(self.meas_line_edit_task_impact_time)

        self.meas_label_freq_sampling_freq = QLabel(self.meas_widget_main)
        self.meas_label_freq_sampling_freq.setObjectName(u"meas_label_freq_sampling_freq")
        self.meas_label_freq_sampling_freq.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.meas_label_freq_sampling_freq.sizePolicy().hasHeightForWidth())
        self.meas_label_freq_sampling_freq.setSizePolicy(sizePolicy1)
        self.meas_label_freq_sampling_freq.setFont(font1)
        self.meas_label_freq_sampling_freq.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.meas_label_freq_sampling_freq.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.meas_layout_task.addWidget(self.meas_label_freq_sampling_freq)

        self.meas_line_edit_task_sampling_freq = QLineEdit(self.meas_widget_main)
        self.meas_line_edit_task_sampling_freq.setObjectName(u"meas_line_edit_task_sampling_freq")
        self.meas_line_edit_task_sampling_freq.setEnabled(False)

        self.meas_layout_task.addWidget(self.meas_line_edit_task_sampling_freq)

        self.meas_label_freq_double_overflow_samples = QLabel(self.meas_widget_main)
        self.meas_label_freq_double_overflow_samples.setObjectName(u"meas_label_freq_double_overflow_samples")
        self.meas_label_freq_double_overflow_samples.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.meas_label_freq_double_overflow_samples.sizePolicy().hasHeightForWidth())
        self.meas_label_freq_double_overflow_samples.setSizePolicy(sizePolicy1)
        self.meas_label_freq_double_overflow_samples.setFont(font1)
        self.meas_label_freq_double_overflow_samples.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.meas_label_freq_double_overflow_samples.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.meas_layout_task.addWidget(self.meas_label_freq_double_overflow_samples)

        self.meas_line_edit_task_overflow_samples = QLineEdit(self.meas_widget_main)
        self.meas_line_edit_task_overflow_samples.setObjectName(u"meas_line_edit_task_overflow_samples")
        self.meas_line_edit_task_overflow_samples.setEnabled(False)

        self.meas_layout_task.addWidget(self.meas_line_edit_task_overflow_samples)

        self.meas_label_freq_double_impact_limit = QLabel(self.meas_widget_main)
        self.meas_label_freq_double_impact_limit.setObjectName(u"meas_label_freq_double_impact_limit")
        self.meas_label_freq_double_impact_limit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.meas_label_freq_double_impact_limit.sizePolicy().hasHeightForWidth())
        self.meas_label_freq_double_impact_limit.setSizePolicy(sizePolicy1)
        self.meas_label_freq_double_impact_limit.setFont(font1)
        self.meas_label_freq_double_impact_limit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.meas_label_freq_double_impact_limit.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.meas_layout_task.addWidget(self.meas_label_freq_double_impact_limit)

        self.meas_line_edit_task_double_impact_limit = QLineEdit(self.meas_widget_main)
        self.meas_line_edit_task_double_impact_limit.setObjectName(u"meas_line_edit_task_double_impact_limit")
        self.meas_line_edit_task_double_impact_limit.setEnabled(False)

        self.meas_layout_task.addWidget(self.meas_line_edit_task_double_impact_limit)

        self.meas_label_channels = QLabel(self.meas_widget_main)
        self.meas_label_channels.setObjectName(u"meas_label_channels")
        self.meas_label_channels.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.meas_label_channels.sizePolicy().hasHeightForWidth())
        self.meas_label_channels.setSizePolicy(sizePolicy1)
        self.meas_label_channels.setFont(font1)
        self.meas_label_channels.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.meas_label_channels.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.meas_layout_task.addWidget(self.meas_label_channels)

        self.meas_list_chosen_channels = QListView(self.meas_widget_main)
        self.meas_list_chosen_channels.setObjectName(u"meas_list_chosen_channels")
        self.meas_list_chosen_channels.setEnabled(False)

        self.meas_layout_task.addWidget(self.meas_list_chosen_channels)

        self.meas_layout_start_stop = QHBoxLayout()
        self.meas_layout_start_stop.setObjectName(u"meas_layout_start_stop")
        self.meas_button_start_meas = QPushButton(self.meas_widget_main)
        self.meas_button_start_meas.setObjectName(u"meas_button_start_meas")
        self.meas_button_start_meas.setEnabled(False)
        self.meas_button_start_meas.setMinimumSize(QSize(0, 50))

        self.meas_layout_start_stop.addWidget(self.meas_button_start_meas)

        self.meas_button_stop_meas = QPushButton(self.meas_widget_main)
        self.meas_button_stop_meas.setObjectName(u"meas_button_stop_meas")
        self.meas_button_stop_meas.setEnabled(False)
        self.meas_button_stop_meas.setMinimumSize(QSize(50, 50))

        self.meas_layout_start_stop.addWidget(self.meas_button_stop_meas)


        self.meas_layout_task.addLayout(self.meas_layout_start_stop)

        self.meas_layout_save_detect = QHBoxLayout()
        self.meas_layout_save_detect.setObjectName(u"meas_layout_save_detect")
        self.meas_button_detect_double_impact = QPushButton(self.meas_widget_main)
        self.meas_button_detect_double_impact.setObjectName(u"meas_button_detect_double_impact")
        self.meas_button_detect_double_impact.setEnabled(False)
        self.meas_button_detect_double_impact.setMinimumSize(QSize(0, 0))

        self.meas_layout_save_detect.addWidget(self.meas_button_detect_double_impact)

        self.meas_button_clear = QPushButton(self.meas_widget_main)
        self.meas_button_clear.setObjectName(u"meas_button_clear")
        self.meas_button_clear.setEnabled(False)

        self.meas_layout_save_detect.addWidget(self.meas_button_clear)


        self.meas_layout_task.addLayout(self.meas_layout_save_detect)

        self.meas_button_save_result = QPushButton(self.meas_widget_main)
        self.meas_button_save_result.setObjectName(u"meas_button_save_result")
        self.meas_button_save_result.setEnabled(False)

        self.meas_layout_task.addWidget(self.meas_button_save_result)


        self.horizontalLayout_6.addLayout(self.meas_layout_task)

        self.meas_widget_plot = MeasPlotWidget(self.meas_widget_main)
        self.meas_widget_plot.setObjectName(u"meas_widget_plot")
        sizePolicy.setHeightForWidth(self.meas_widget_plot.sizePolicy().hasHeightForWidth())
        self.meas_widget_plot.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.meas_widget_plot)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 1)
        self.meas_tab_plot = QTabWidget(self.meas_widget_plot)
        self.meas_tab_plot.setObjectName(u"meas_tab_plot")

        self.verticalLayout_4.addWidget(self.meas_tab_plot)

        self.meas_progress_meas = QProgressBar(self.meas_widget_plot)
        self.meas_progress_meas.setObjectName(u"meas_progress_meas")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.meas_progress_meas.sizePolicy().hasHeightForWidth())
        self.meas_progress_meas.setSizePolicy(sizePolicy3)
        self.meas_progress_meas.setValue(0)
        self.meas_progress_meas.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.meas_progress_meas.setTextVisible(True)
        self.meas_progress_meas.setOrientation(Qt.Orientation.Horizontal)
        self.meas_progress_meas.setInvertedAppearance(False)
        self.meas_progress_meas.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout_4.addWidget(self.meas_progress_meas)


        self.horizontalLayout_6.addWidget(self.meas_widget_plot)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 3)

        self.gridLayout_2.addWidget(self.meas_widget_main, 0, 0, 1, 1)

        self.tabWidget.addTab(self.meas_tab, "")
        self.ema_tab = QWidget()
        self.ema_tab.setObjectName(u"ema_tab")
        sizePolicy.setHeightForWidth(self.ema_tab.sizePolicy().hasHeightForWidth())
        self.ema_tab.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.ema_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ema_widget_main = EmaMainWidget(self.ema_tab)
        self.ema_widget_main.setObjectName(u"ema_widget_main")
        sizePolicy.setHeightForWidth(self.ema_widget_main.sizePolicy().hasHeightForWidth())
        self.ema_widget_main.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.ema_widget_main)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ema_layout_setup = QVBoxLayout()
        self.ema_layout_setup.setObjectName(u"ema_layout_setup")
        self.ema_layout_setup.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.ema_label_main = QLabel(self.ema_widget_main)
        self.ema_label_main.setObjectName(u"ema_label_main")
        sizePolicy1.setHeightForWidth(self.ema_label_main.sizePolicy().hasHeightForWidth())
        self.ema_label_main.setSizePolicy(sizePolicy1)
        self.ema_label_main.setFont(font)
        self.ema_label_main.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.ema_label_main.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ema_layout_setup.addWidget(self.ema_label_main)

        self.ema_button_load = QPushButton(self.ema_widget_main)
        self.ema_button_load.setObjectName(u"ema_button_load")

        self.ema_layout_setup.addWidget(self.ema_button_load)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.ema_layout_setup.addLayout(self.horizontalLayout)

        self.ema_label_freq_boundary_lower = QLabel(self.ema_widget_main)
        self.ema_label_freq_boundary_lower.setObjectName(u"ema_label_freq_boundary_lower")
        self.ema_label_freq_boundary_lower.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.ema_label_freq_boundary_lower.sizePolicy().hasHeightForWidth())
        self.ema_label_freq_boundary_lower.setSizePolicy(sizePolicy1)
        self.ema_label_freq_boundary_lower.setFont(font1)
        self.ema_label_freq_boundary_lower.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ema_label_freq_boundary_lower.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.ema_layout_setup.addWidget(self.ema_label_freq_boundary_lower)

        self.ema_line_edit_freq_boundary_lower = QLineEdit(self.ema_widget_main)
        self.ema_line_edit_freq_boundary_lower.setObjectName(u"ema_line_edit_freq_boundary_lower")

        self.ema_layout_setup.addWidget(self.ema_line_edit_freq_boundary_lower)

        self.ema_label_freq_boundary_upper = QLabel(self.ema_widget_main)
        self.ema_label_freq_boundary_upper.setObjectName(u"ema_label_freq_boundary_upper")
        self.ema_label_freq_boundary_upper.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.ema_label_freq_boundary_upper.sizePolicy().hasHeightForWidth())
        self.ema_label_freq_boundary_upper.setSizePolicy(sizePolicy1)
        self.ema_label_freq_boundary_upper.setFont(font1)
        self.ema_label_freq_boundary_upper.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ema_label_freq_boundary_upper.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.ema_layout_setup.addWidget(self.ema_label_freq_boundary_upper)

        self.ema_line_edit_freq_boundary_upper = QLineEdit(self.ema_widget_main)
        self.ema_line_edit_freq_boundary_upper.setObjectName(u"ema_line_edit_freq_boundary_upper")

        self.ema_layout_setup.addWidget(self.ema_line_edit_freq_boundary_upper)

        self.ema_label_pol_order = QLabel(self.ema_widget_main)
        self.ema_label_pol_order.setObjectName(u"ema_label_pol_order")
        self.ema_label_pol_order.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.ema_label_pol_order.sizePolicy().hasHeightForWidth())
        self.ema_label_pol_order.setSizePolicy(sizePolicy1)
        self.ema_label_pol_order.setFont(font1)
        self.ema_label_pol_order.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ema_label_pol_order.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.ema_layout_setup.addWidget(self.ema_label_pol_order)

        self.ema_line_edit_pol_order = QLineEdit(self.ema_widget_main)
        self.ema_line_edit_pol_order.setObjectName(u"ema_line_edit_pol_order")

        self.ema_layout_setup.addWidget(self.ema_line_edit_pol_order)

        self.ema_label_nat_freq = QLabel(self.ema_widget_main)
        self.ema_label_nat_freq.setObjectName(u"ema_label_nat_freq")
        self.ema_label_nat_freq.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.ema_label_nat_freq.sizePolicy().hasHeightForWidth())
        self.ema_label_nat_freq.setSizePolicy(sizePolicy1)
        self.ema_label_nat_freq.setFont(font1)
        self.ema_label_nat_freq.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ema_label_nat_freq.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.ema_layout_setup.addWidget(self.ema_label_nat_freq)

        self.ema_line_edit_nat_freq = QLineEdit(self.ema_widget_main)
        self.ema_line_edit_nat_freq.setObjectName(u"ema_line_edit_nat_freq")
        self.ema_line_edit_nat_freq.setEnabled(True)

        self.ema_layout_setup.addWidget(self.ema_line_edit_nat_freq)

        self.ema_label_solver = QLabel(self.ema_widget_main)
        self.ema_label_solver.setObjectName(u"ema_label_solver")
        self.ema_label_solver.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.ema_label_solver.sizePolicy().hasHeightForWidth())
        self.ema_label_solver.setSizePolicy(sizePolicy1)
        self.ema_label_solver.setFont(font1)
        self.ema_label_solver.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ema_label_solver.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.ema_layout_setup.addWidget(self.ema_label_solver)

        self.ema_combo_box_pole_calc = QComboBox(self.ema_widget_main)
        self.ema_combo_box_pole_calc.addItem("")
        self.ema_combo_box_pole_calc.addItem("")
        self.ema_combo_box_pole_calc.addItem("")
        self.ema_combo_box_pole_calc.addItem("")
        self.ema_combo_box_pole_calc.setObjectName(u"ema_combo_box_pole_calc")

        self.ema_layout_setup.addWidget(self.ema_combo_box_pole_calc)

        self.ema_label_frf = QLabel(self.ema_widget_main)
        self.ema_label_frf.setObjectName(u"ema_label_frf")
        self.ema_label_frf.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.ema_label_frf.sizePolicy().hasHeightForWidth())
        self.ema_label_frf.setSizePolicy(sizePolicy1)
        self.ema_label_frf.setFont(font1)
        self.ema_label_frf.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ema_label_frf.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.ema_layout_setup.addWidget(self.ema_label_frf)

        self.ema_list_frfs = QListView(self.ema_widget_main)
        self.ema_list_frfs.setObjectName(u"ema_list_frfs")
        self.ema_list_frfs.setEnabled(True)
        self.ema_list_frfs.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.ema_layout_setup.addWidget(self.ema_list_frfs)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ema_button_calc = QPushButton(self.ema_widget_main)
        self.ema_button_calc.setObjectName(u"ema_button_calc")
        self.ema_button_calc.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.ema_button_calc)

        self.ema_button_select_poles = QPushButton(self.ema_widget_main)
        self.ema_button_select_poles.setObjectName(u"ema_button_select_poles")
        self.ema_button_select_poles.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.ema_button_select_poles)


        self.ema_layout_setup.addLayout(self.horizontalLayout_2)

        self.ema_label_nat_freq_sel = QLabel(self.ema_widget_main)
        self.ema_label_nat_freq_sel.setObjectName(u"ema_label_nat_freq_sel")
        self.ema_label_nat_freq_sel.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.ema_label_nat_freq_sel.sizePolicy().hasHeightForWidth())
        self.ema_label_nat_freq_sel.setSizePolicy(sizePolicy1)
        self.ema_label_nat_freq_sel.setFont(font1)
        self.ema_label_nat_freq_sel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ema_label_nat_freq_sel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.ema_layout_setup.addWidget(self.ema_label_nat_freq_sel)

        self.ema_line_edit_nat_freq_sel = QLineEdit(self.ema_widget_main)
        self.ema_line_edit_nat_freq_sel.setObjectName(u"ema_line_edit_nat_freq_sel")
        self.ema_line_edit_nat_freq_sel.setEnabled(False)

        self.ema_layout_setup.addWidget(self.ema_line_edit_nat_freq_sel)

        self.ema_label_damping_coeff_sel = QLabel(self.ema_widget_main)
        self.ema_label_damping_coeff_sel.setObjectName(u"ema_label_damping_coeff_sel")
        self.ema_label_damping_coeff_sel.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.ema_label_damping_coeff_sel.sizePolicy().hasHeightForWidth())
        self.ema_label_damping_coeff_sel.setSizePolicy(sizePolicy1)
        self.ema_label_damping_coeff_sel.setFont(font1)
        self.ema_label_damping_coeff_sel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ema_label_damping_coeff_sel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.ema_layout_setup.addWidget(self.ema_label_damping_coeff_sel)

        self.ema_line_edit_damping_coeff_sel = QLineEdit(self.ema_widget_main)
        self.ema_line_edit_damping_coeff_sel.setObjectName(u"ema_line_edit_damping_coeff_sel")
        self.ema_line_edit_damping_coeff_sel.setEnabled(False)

        self.ema_layout_setup.addWidget(self.ema_line_edit_damping_coeff_sel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ema_button_save = QPushButton(self.ema_widget_main)
        self.ema_button_save.setObjectName(u"ema_button_save")
        self.ema_button_save.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.ema_button_save)

        self.ema_button_clear = QPushButton(self.ema_widget_main)
        self.ema_button_clear.setObjectName(u"ema_button_clear")
        self.ema_button_clear.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.ema_button_clear)


        self.ema_layout_setup.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addLayout(self.ema_layout_setup)

        self.ema_widget_plot = EmaPlotWidget(self.ema_widget_main)
        self.ema_widget_plot.setObjectName(u"ema_widget_plot")
        sizePolicy.setHeightForWidth(self.ema_widget_plot.sizePolicy().hasHeightForWidth())
        self.ema_widget_plot.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.ema_widget_plot)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ema_tab_widget = QTabWidget(self.ema_widget_plot)
        self.ema_tab_widget.setObjectName(u"ema_tab_widget")
        self.ema_tab_widget.setDocumentMode(False)
        self.ema_tab_frf_coh = QWidget()
        self.ema_tab_frf_coh.setObjectName(u"ema_tab_frf_coh")
        self.gridLayout_7 = QGridLayout(self.ema_tab_frf_coh)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.ema_plot_frf_phase_coh = GraphicsLayoutWidget(self.ema_tab_frf_coh)
        self.ema_plot_frf_phase_coh.setObjectName(u"ema_plot_frf_phase_coh")
        sizePolicy.setHeightForWidth(self.ema_plot_frf_phase_coh.sizePolicy().hasHeightForWidth())
        self.ema_plot_frf_phase_coh.setSizePolicy(sizePolicy)
        self.ema_plot_frf_phase_coh.setMinimumSize(QSize(687, 250))
        self.ema_plot_frf_phase_coh.setBaseSize(QSize(500, 250))

        self.gridLayout_7.addWidget(self.ema_plot_frf_phase_coh, 0, 0, 1, 1)

        self.ema_tab_widget.addTab(self.ema_tab_frf_coh, "")
        self.ema_tab_frf_coh_comb = QWidget()
        self.ema_tab_frf_coh_comb.setObjectName(u"ema_tab_frf_coh_comb")
        self.gridLayout_8 = QGridLayout(self.ema_tab_frf_coh_comb)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.ema_plot_frf_plus_coh = GraphicsLayoutWidget(self.ema_tab_frf_coh_comb)
        self.ema_plot_frf_plus_coh.setObjectName(u"ema_plot_frf_plus_coh")
        sizePolicy.setHeightForWidth(self.ema_plot_frf_plus_coh.sizePolicy().hasHeightForWidth())
        self.ema_plot_frf_plus_coh.setSizePolicy(sizePolicy)
        self.ema_plot_frf_plus_coh.setMinimumSize(QSize(687, 250))
        self.ema_plot_frf_plus_coh.setBaseSize(QSize(500, 250))

        self.gridLayout_8.addWidget(self.ema_plot_frf_plus_coh, 0, 0, 1, 1)

        self.ema_tab_widget.addTab(self.ema_tab_frf_coh_comb, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.ema_tab_widget.addTab(self.tab, "")

        self.verticalLayout_5.addWidget(self.ema_tab_widget)


        self.horizontalLayout_5.addWidget(self.ema_widget_plot)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 3)

        self.gridLayout_3.addWidget(self.ema_widget_main, 0, 0, 1, 1)

        self.tabWidget.addTab(self.ema_tab, "")
        self.oma_tab = QWidget()
        self.oma_tab.setObjectName(u"oma_tab")
        sizePolicy.setHeightForWidth(self.oma_tab.sizePolicy().hasHeightForWidth())
        self.oma_tab.setSizePolicy(sizePolicy)
        self.gridLayout_6 = QGridLayout(self.oma_tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget.addTab(self.oma_tab, "")
        self.post_processing_tab = QWidget()
        self.post_processing_tab.setObjectName(u"post_processing_tab")
        sizePolicy.setHeightForWidth(self.post_processing_tab.sizePolicy().hasHeightForWidth())
        self.post_processing_tab.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.post_processing_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.post_proc_widget_main = PostProcMainWidget(self.post_processing_tab)
        self.post_proc_widget_main.setObjectName(u"post_proc_widget_main")
        sizePolicy.setHeightForWidth(self.post_proc_widget_main.sizePolicy().hasHeightForWidth())
        self.post_proc_widget_main.setSizePolicy(sizePolicy)
        self.horizontalLayout_7 = QHBoxLayout(self.post_proc_widget_main)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.post_proc_layout_setup = QVBoxLayout()
        self.post_proc_layout_setup.setObjectName(u"post_proc_layout_setup")
        self.post_proc_layout_setup.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.post_proc_layout_setup.setContentsMargins(-1, -1, 0, -1)
        self.groupBox = QGroupBox(self.post_proc_widget_main)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.post_proc_label_main = QLabel(self.groupBox)
        self.post_proc_label_main.setObjectName(u"post_proc_label_main")
        sizePolicy1.setHeightForWidth(self.post_proc_label_main.sizePolicy().hasHeightForWidth())
        self.post_proc_label_main.setSizePolicy(sizePolicy1)
        self.post_proc_label_main.setFont(font)
        self.post_proc_label_main.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.post_proc_label_main.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.post_proc_label_main)

        self.post_proc_label_main_2 = QLabel(self.groupBox)
        self.post_proc_label_main_2.setObjectName(u"post_proc_label_main_2")
        sizePolicy1.setHeightForWidth(self.post_proc_label_main_2.sizePolicy().hasHeightForWidth())
        self.post_proc_label_main_2.setSizePolicy(sizePolicy1)
        self.post_proc_label_main_2.setFont(font1)
        self.post_proc_label_main_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.post_proc_label_main_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.post_proc_label_main_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.post_proc_button_load_geometry = QPushButton(self.groupBox)
        self.post_proc_button_load_geometry.setObjectName(u"post_proc_button_load_geometry")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.post_proc_button_load_geometry.sizePolicy().hasHeightForWidth())
        self.post_proc_button_load_geometry.setSizePolicy(sizePolicy4)
        self.post_proc_button_load_geometry.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.post_proc_button_load_geometry)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.post_proc_label_main_3 = QLabel(self.groupBox)
        self.post_proc_label_main_3.setObjectName(u"post_proc_label_main_3")
        sizePolicy1.setHeightForWidth(self.post_proc_label_main_3.sizePolicy().hasHeightForWidth())
        self.post_proc_label_main_3.setSizePolicy(sizePolicy1)
        self.post_proc_label_main_3.setFont(font1)
        self.post_proc_label_main_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.post_proc_label_main_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.post_proc_label_main_3)

        self.post_proc_button_load_ema = QPushButton(self.groupBox)
        self.post_proc_button_load_ema.setObjectName(u"post_proc_button_load_ema")
        self.post_proc_button_load_ema.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.post_proc_button_load_ema.sizePolicy().hasHeightForWidth())
        self.post_proc_button_load_ema.setSizePolicy(sizePolicy4)

        self.verticalLayout_3.addWidget(self.post_proc_button_load_ema)

        self.post_proc_label_main_4 = QLabel(self.groupBox)
        self.post_proc_label_main_4.setObjectName(u"post_proc_label_main_4")
        sizePolicy1.setHeightForWidth(self.post_proc_label_main_4.sizePolicy().hasHeightForWidth())
        self.post_proc_label_main_4.setSizePolicy(sizePolicy1)
        self.post_proc_label_main_4.setFont(font1)
        self.post_proc_label_main_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.post_proc_label_main_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.post_proc_label_main_4)

        self.post_proc_ema_list = QListView(self.groupBox)
        self.post_proc_ema_list.setObjectName(u"post_proc_ema_list")
        self.post_proc_ema_list.setEnabled(False)
        self.post_proc_ema_list.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.verticalLayout_3.addWidget(self.post_proc_ema_list)

        self.post_proc_label_mode = QLabel(self.groupBox)
        self.post_proc_label_mode.setObjectName(u"post_proc_label_mode")

        self.verticalLayout_3.addWidget(self.post_proc_label_mode)

        self.post_proc_combo_box_mode = QComboBox(self.groupBox)
        self.post_proc_combo_box_mode.setObjectName(u"post_proc_combo_box_mode")

        self.verticalLayout_3.addWidget(self.post_proc_combo_box_mode)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.post_proc_button_show_deformation = QPushButton(self.groupBox)
        self.post_proc_button_show_deformation.setObjectName(u"post_proc_button_show_deformation")

        self.horizontalLayout_11.addWidget(self.post_proc_button_show_deformation)

        self.post_proc_line_edit_deformation_scale = QLineEdit(self.groupBox)
        self.post_proc_line_edit_deformation_scale.setObjectName(u"post_proc_line_edit_deformation_scale")

        self.horizontalLayout_11.addWidget(self.post_proc_line_edit_deformation_scale)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.post_proc_label_nat_freq = QLabel(self.groupBox)
        self.post_proc_label_nat_freq.setObjectName(u"post_proc_label_nat_freq")
        self.post_proc_label_nat_freq.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.post_proc_label_nat_freq.sizePolicy().hasHeightForWidth())
        self.post_proc_label_nat_freq.setSizePolicy(sizePolicy1)
        self.post_proc_label_nat_freq.setFont(font1)
        self.post_proc_label_nat_freq.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.post_proc_label_nat_freq.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.post_proc_label_nat_freq)

        self.post_proc_line_edit_nat_freq = QLineEdit(self.groupBox)
        self.post_proc_line_edit_nat_freq.setObjectName(u"post_proc_line_edit_nat_freq")
        self.post_proc_line_edit_nat_freq.setEnabled(False)

        self.verticalLayout_3.addWidget(self.post_proc_line_edit_nat_freq)

        self.post_proc_label_damping_coeff = QLabel(self.groupBox)
        self.post_proc_label_damping_coeff.setObjectName(u"post_proc_label_damping_coeff")
        self.post_proc_label_damping_coeff.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.post_proc_label_damping_coeff.sizePolicy().hasHeightForWidth())
        self.post_proc_label_damping_coeff.setSizePolicy(sizePolicy1)
        self.post_proc_label_damping_coeff.setFont(font1)
        self.post_proc_label_damping_coeff.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.post_proc_label_damping_coeff.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.post_proc_label_damping_coeff)

        self.post_proc_line_edit_daming_coeff = QLineEdit(self.groupBox)
        self.post_proc_line_edit_daming_coeff.setObjectName(u"post_proc_line_edit_daming_coeff")
        self.post_proc_line_edit_daming_coeff.setEnabled(False)

        self.verticalLayout_3.addWidget(self.post_proc_line_edit_daming_coeff)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.post_proc_button_save_geometry = QPushButton(self.groupBox)
        self.post_proc_button_save_geometry.setObjectName(u"post_proc_button_save_geometry")
        self.post_proc_button_save_geometry.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.post_proc_button_save_geometry.sizePolicy().hasHeightForWidth())
        self.post_proc_button_save_geometry.setSizePolicy(sizePolicy4)

        self.horizontalLayout_9.addWidget(self.post_proc_button_save_geometry)

        self.post_proc_button_save_ema = QPushButton(self.groupBox)
        self.post_proc_button_save_ema.setObjectName(u"post_proc_button_save_ema")
        self.post_proc_button_save_ema.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.post_proc_button_save_ema.sizePolicy().hasHeightForWidth())
        self.post_proc_button_save_ema.setSizePolicy(sizePolicy4)

        self.horizontalLayout_9.addWidget(self.post_proc_button_save_ema)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.post_proc_button_save_all = QPushButton(self.groupBox)
        self.post_proc_button_save_all.setObjectName(u"post_proc_button_save_all")
        self.post_proc_button_save_all.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.post_proc_button_save_all.sizePolicy().hasHeightForWidth())
        self.post_proc_button_save_all.setSizePolicy(sizePolicy4)

        self.horizontalLayout_8.addWidget(self.post_proc_button_save_all)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.post_proc_button_clear = QPushButton(self.groupBox)
        self.post_proc_button_clear.setObjectName(u"post_proc_button_clear")

        self.verticalLayout_3.addWidget(self.post_proc_button_clear)


        self.post_proc_layout_setup.addWidget(self.groupBox)


        self.horizontalLayout_7.addLayout(self.post_proc_layout_setup)

        self.post_proc_geometry = QFrame(self.post_proc_widget_main)
        self.post_proc_geometry.setObjectName(u"post_proc_geometry")
        sizePolicy.setHeightForWidth(self.post_proc_geometry.sizePolicy().hasHeightForWidth())
        self.post_proc_geometry.setSizePolicy(sizePolicy)
        self.gridLayout_9 = QGridLayout(self.post_proc_geometry)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.post_proc_vispy = GeometryWidget(self.post_proc_geometry)
        self.post_proc_vispy.setObjectName(u"post_proc_vispy")
        sizePolicy.setHeightForWidth(self.post_proc_vispy.sizePolicy().hasHeightForWidth())
        self.post_proc_vispy.setSizePolicy(sizePolicy)
        self.post_proc_vispy_settings = QWidget(self.post_proc_vispy)
        self.post_proc_vispy_settings.setObjectName(u"post_proc_vispy_settings")
        self.post_proc_vispy_settings.setEnabled(True)
        self.post_proc_vispy_settings.setGeometry(QRect(30, 120, 181, 181))
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.post_proc_vispy_settings.sizePolicy().hasHeightForWidth())
        self.post_proc_vispy_settings.setSizePolicy(sizePolicy5)
        self.post_proc_vispy_settings.setMinimumSize(QSize(100, 10))
        self.post_proc_vispy_settings.setAutoFillBackground(False)
        self.post_proc_vispy_settings.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.post_proc_vispy_settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_2 = QRadioButton(self.post_proc_vispy_settings)
        self.post_proc_connector = QButtonGroup(MainWindow)
        self.post_proc_connector.setObjectName(u"post_proc_connector")
        self.post_proc_connector.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.radioButton_2.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.post_proc_vispy_settings)
        self.post_proc_connector.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_3 = QRadioButton(self.post_proc_vispy_settings)
        self.post_proc_connector.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.post_proc_vispy_settings)
        self.post_proc_connector.addButton(self.radioButton_4)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setEnabled(True)
        self.radioButton_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.radioButton_4)

        self.radioButton_3.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.radioButton_4.raise_()

        self.gridLayout_9.addWidget(self.post_proc_vispy, 0, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.post_proc_geometry)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 3)

        self.gridLayout_4.addWidget(self.post_proc_widget_main, 0, 0, 1, 1)

        self.tabWidget.addTab(self.post_processing_tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.exception_scroll_area = QScrollArea(self.centralwidget)
        self.exception_scroll_area.setObjectName(u"exception_scroll_area")
        self.exception_scroll_area.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.exception_scroll_area.setWidgetResizable(True)
        self.exception_scroll_area_widget = QWidget()
        self.exception_scroll_area_widget.setObjectName(u"exception_scroll_area_widget")
        self.exception_scroll_area_widget.setGeometry(QRect(0, 0, 1734, 214))
        sizePolicy.setHeightForWidth(self.exception_scroll_area_widget.sizePolicy().hasHeightForWidth())
        self.exception_scroll_area_widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_10 = QHBoxLayout(self.exception_scroll_area_widget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.exception_scroll_area_layout = QVBoxLayout()
        self.exception_scroll_area_layout.setObjectName(u"exception_scroll_area_layout")
        self.exception_scroll_area_layout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.label = QLabel(self.exception_scroll_area_widget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label.setFont(font2)

        self.exception_scroll_area_layout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.exception_scroll_area_list_view = QListView(self.exception_scroll_area_widget)
        self.exception_scroll_area_list_view.setObjectName(u"exception_scroll_area_list_view")
        sizePolicy.setHeightForWidth(self.exception_scroll_area_list_view.sizePolicy().hasHeightForWidth())
        self.exception_scroll_area_list_view.setSizePolicy(sizePolicy)

        self.exception_scroll_area_layout.addWidget(self.exception_scroll_area_list_view)


        self.horizontalLayout_10.addLayout(self.exception_scroll_area_layout)

        self.exception_scroll_area.setWidget(self.exception_scroll_area_widget)

        self.gridLayout.addWidget(self.exception_scroll_area, 1, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 11)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1754, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.ema_line_edit_nat_freq.editingFinished.connect(self.ema_widget_main.ema_nat_freq_edited)
        self.ema_line_edit_freq_boundary_upper.editingFinished.connect(self.ema_widget_main.ema_setting_changed)
        self.ema_line_edit_pol_order.editingFinished.connect(self.ema_widget_main.ema_setting_changed)
        self.ema_button_save.clicked.connect(self.ema_widget_main.ema_button_save_pressed)
        self.ema_list_frfs.doubleClicked.connect(self.ema_widget_main.ema_list_frf_double_clicked)
        self.ema_button_select_poles.clicked.connect(self.ema_widget_main.ema_button_select_poles_pressed)
        self.ema_button_load.clicked.connect(self.ema_widget_main.ema_button_load_pressed)
        self.ema_line_edit_freq_boundary_lower.editingFinished.connect(self.ema_widget_main.ema_setting_changed)
        self.ema_button_calc.clicked.connect(self.ema_widget_main.ema_button_calc_pressed)
        self.ema_button_clear.clicked.connect(self.ema_widget_main.ema_button_clear_pressed)
        self.ema_combo_box_pole_calc.currentIndexChanged.connect(self.ema_widget_main.ema_solver_changed)
        self.meas_button_save_result.clicked.connect(self.meas_widget_main.meas_button_save_meas_pressed)
        self.meas_list_tasks.doubleClicked.connect(self.meas_widget_main.meas_list_task_double_clicked)
        self.meas_button_edit_task.clicked.connect(self.meas_widget_main.meas_button_edit_task_pressed)
        self.meas_button_clear.clicked.connect(self.meas_widget_main.meas_button_clear_pressed)
        self.meas_button_stop_meas.clicked.connect(self.meas_widget_main.meas_button_stop_meas_pressed)
        self.meas_button_create_task.clicked.connect(self.meas_widget_main.meas_button_create_pressed)
        self.meas_button_start_meas.clicked.connect(self.meas_widget_main.meas_button_start_meas_pressed)
        self.meas_button_detect_double_impact.clicked.connect(self.meas_widget_main.meas_button_check_double_impact_pressed)
        self.post_proc_button_load_geometry.clicked.connect(self.post_proc_widget_main.post_proc_button_load_geometry_pressed)
        self.post_proc_connector.idToggled.connect(self.post_proc_widget_main.post_proc_connector_changed)
        self.post_proc_button_load_ema.clicked.connect(self.post_proc_widget_main.post_proc_button_load_ema_pressed)
        self.post_proc_button_clear.clicked.connect(self.post_proc_widget_main.post_proc_button_clear_pressed)
        self.post_proc_button_save_all.clicked.connect(self.post_proc_widget_main.post_proc_button_save_all_pressed)
        self.post_proc_button_save_geometry.clicked.connect(self.post_proc_widget_main.post_proc_button_save_geometry_pressed)
        self.post_proc_button_save_ema.clicked.connect(self.post_proc_widget_main.post_proc_button_save_ema_pressed)
        self.meas_tab_plot.tabBarDoubleClicked.connect(self.meas_widget_main.meas_tab_bar_double_clicked)
        self.meas_button_init.clicked.connect(self.meas_widget_main.meas_button_init_pressed)
        self.post_proc_combo_box_mode.currentIndexChanged.connect(self.post_proc_widget_main.post_proc_combo_button_mode_changed)
        self.post_proc_button_show_deformation.clicked.connect(self.post_proc_widget_main.post_proc_button_show_deformation_pressed)

        self.tabWidget.setCurrentIndex(1)
        self.meas_tab_plot.setCurrentIndex(-1)
        self.ema_tab_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyMA", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setup_tab), QCoreApplication.translate("MainWindow", u"Setup", None))
        self.meas_label_start_stop.setText(QCoreApplication.translate("MainWindow", u"Measurement", None))
        self.meas_label_load_task.setText(QCoreApplication.translate("MainWindow", u"Load Task", None))
        self.meas_button_create_task.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.meas_button_edit_task.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.meas_label_task_name.setText(QCoreApplication.translate("MainWindow", u"Task Name", None))
        self.meas_button_init.setText(QCoreApplication.translate("MainWindow", u"Init", None))
        self.meas_line_edit_task_name.setText("")
        self.meas_label_num_impacts.setText(QCoreApplication.translate("MainWindow", u"Number of Impacts / 1", None))
        self.meas_line_edit_task_num_impacts.setText("")
        self.meas_label_impact_time.setText(QCoreApplication.translate("MainWindow", u"Impact Time / s", None))
        self.meas_label_freq_sampling_freq.setText(QCoreApplication.translate("MainWindow", u"Sampling Frequency / Hz", None))
#if QT_CONFIG(tooltip)
        self.meas_label_freq_double_overflow_samples.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'Lato','proxima-nova','Helvetica Neue','Arial','sans-serif'; font-size:16px; font-weight:400; color:#404040; background-color:#fcfcfc;\">number of samples that need to be equal to max for overflow identification (source: pyFRF docs)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.meas_label_freq_double_overflow_samples.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.meas_label_freq_double_overflow_samples.setText(QCoreApplication.translate("MainWindow", u"Overflow Samples (i)", None))
        self.meas_line_edit_task_overflow_samples.setText("")
#if QT_CONFIG(tooltip)
        self.meas_label_freq_double_impact_limit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'Lato','proxima-nova','Helvetica Neue','Arial','sans-serif'; font-size:16px; font-weight:400; color:#404040; background-color:#fcfcfc;\">ratio of freqency content of the double vs single hit (source: pyFRF docs)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.meas_label_freq_double_impact_limit.setText(QCoreApplication.translate("MainWindow", u"Double Impact Limit (i)", None))
        self.meas_line_edit_task_double_impact_limit.setText("")
        self.meas_label_channels.setText(QCoreApplication.translate("MainWindow", u"Chosen Channels", None))
        self.meas_button_start_meas.setText(QCoreApplication.translate("MainWindow", u"Start Measurement", None))
#if QT_CONFIG(shortcut)
        self.meas_button_start_meas.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.meas_button_stop_meas.setText(QCoreApplication.translate("MainWindow", u"Stop Measurement", None))
#if QT_CONFIG(shortcut)
        self.meas_button_stop_meas.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.meas_button_detect_double_impact.setText(QCoreApplication.translate("MainWindow", u"Check Double Impact", None))
        self.meas_button_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.meas_button_save_result.setText(QCoreApplication.translate("MainWindow", u"Save Result", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.meas_tab), QCoreApplication.translate("MainWindow", u"Measurement", None))
        self.ema_label_main.setText(QCoreApplication.translate("MainWindow", u"EMA", None))
        self.ema_button_load.setText(QCoreApplication.translate("MainWindow", u"Add Measurement", None))
        self.ema_label_freq_boundary_lower.setText(QCoreApplication.translate("MainWindow", u"Frequency Boundary (lower) / Hz", None))
        self.ema_line_edit_freq_boundary_lower.setInputMask("")
        self.ema_line_edit_freq_boundary_lower.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.ema_label_freq_boundary_upper.setText(QCoreApplication.translate("MainWindow", u"Frequency Boundary (upper) / Hz", None))
        self.ema_line_edit_freq_boundary_upper.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.ema_label_pol_order.setText(QCoreApplication.translate("MainWindow", u"Pol Order / 1", None))
        self.ema_line_edit_pol_order.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.ema_label_nat_freq.setText(QCoreApplication.translate("MainWindow", u"Nat frequencies / list[Hz]", None))
        self.ema_line_edit_nat_freq.setText("")
        self.ema_line_edit_nat_freq.setPlaceholderText(QCoreApplication.translate("MainWindow", u"15, 20, 30", None))
        self.ema_label_solver.setText(QCoreApplication.translate("MainWindow", u"Fit Method", None))
        self.ema_combo_box_pole_calc.setItemText(0, QCoreApplication.translate("MainWindow", u"lscf", None))
        self.ema_combo_box_pole_calc.setItemText(1, QCoreApplication.translate("MainWindow", u"lsce", None))
        self.ema_combo_box_pole_calc.setItemText(2, QCoreApplication.translate("MainWindow", u"rfp", None))
        self.ema_combo_box_pole_calc.setItemText(3, QCoreApplication.translate("MainWindow", u"rfp segment", None))

        self.ema_label_frf.setText(QCoreApplication.translate("MainWindow", u"FRFs", None))
        self.ema_button_calc.setText(QCoreApplication.translate("MainWindow", u"Calc", None))
        self.ema_button_select_poles.setText(QCoreApplication.translate("MainWindow", u"Select Poles", None))
        self.ema_label_nat_freq_sel.setText(QCoreApplication.translate("MainWindow", u"Selected Nat frequencies / list[Hz]", None))
        self.ema_line_edit_nat_freq_sel.setText("")
        self.ema_line_edit_nat_freq_sel.setPlaceholderText("")
        self.ema_label_damping_coeff_sel.setText(QCoreApplication.translate("MainWindow", u"Selected Damping / list[1]", None))
        self.ema_line_edit_damping_coeff_sel.setText("")
        self.ema_line_edit_damping_coeff_sel.setPlaceholderText("")
        self.ema_button_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.ema_button_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.ema_tab_widget.setTabText(self.ema_tab_widget.indexOf(self.ema_tab_frf_coh), QCoreApplication.translate("MainWindow", u"FRF / Coherence", None))
        self.ema_tab_widget.setTabText(self.ema_tab_widget.indexOf(self.ema_tab_frf_coh_comb), QCoreApplication.translate("MainWindow", u"FRF + Coherence", None))
        self.ema_tab_widget.setTabText(self.ema_tab_widget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Stab Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ema_tab), QCoreApplication.translate("MainWindow", u"EMA", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.oma_tab), QCoreApplication.translate("MainWindow", u"OMA", None))
        self.post_proc_label_main.setText(QCoreApplication.translate("MainWindow", u"Post Processing", None))
        self.post_proc_label_main_2.setText(QCoreApplication.translate("MainWindow", u"Setup", None))
        self.post_proc_button_load_geometry.setText(QCoreApplication.translate("MainWindow", u"Load Geometry", None))
        self.post_proc_label_main_3.setText(QCoreApplication.translate("MainWindow", u"Add EMA Files", None))
        self.post_proc_button_load_ema.setText(QCoreApplication.translate("MainWindow", u"Load EMA", None))
        self.post_proc_label_main_4.setText(QCoreApplication.translate("MainWindow", u"FRF's in EMA File", None))
        self.post_proc_label_mode.setText(QCoreApplication.translate("MainWindow", u"Display Mode", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Start and Scale", None))
        self.post_proc_button_show_deformation.setText(QCoreApplication.translate("MainWindow", u"Start/Stop", None))
        self.post_proc_line_edit_deformation_scale.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.post_proc_line_edit_deformation_scale.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Scale [1,100]", None))
        self.post_proc_label_nat_freq.setText(QCoreApplication.translate("MainWindow", u"Natural Frequencies", None))
        self.post_proc_line_edit_nat_freq.setText("")
        self.post_proc_line_edit_nat_freq.setPlaceholderText("")
        self.post_proc_label_damping_coeff.setText(QCoreApplication.translate("MainWindow", u"Damping Coefficients", None))
        self.post_proc_line_edit_daming_coeff.setText("")
        self.post_proc_line_edit_daming_coeff.setPlaceholderText("")
        self.post_proc_button_save_geometry.setText(QCoreApplication.translate("MainWindow", u"Save Geometry", None))
        self.post_proc_button_save_ema.setText(QCoreApplication.translate("MainWindow", u"Save EMA", None))
        self.post_proc_button_save_all.setText(QCoreApplication.translate("MainWindow", u"Save All", None))
        self.post_proc_button_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Tri", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Quad", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.post_processing_tab), QCoreApplication.translate("MainWindow", u"Post Processing", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Errors", None))
    # retranslateUi

