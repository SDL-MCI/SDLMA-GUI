# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sdlma_task_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListView,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(707, 810)
        self.centralwidget = QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGeometry(QRect(0, 0, 351, 751))
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 10, 331, 731))
        self.meas_layout_task = QVBoxLayout(self.verticalLayoutWidget_3)
        self.meas_layout_task.setObjectName("meas_layout_task")
        self.meas_layout_task.setContentsMargins(0, 0, 0, 0)
        self.meas_label_settings = QLabel(self.verticalLayoutWidget_3)
        self.meas_label_settings.setObjectName("meas_label_settings")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.meas_label_settings.sizePolicy().hasHeightForWidth()
        )
        self.meas_label_settings.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies(["Calibri"])
        font.setPointSize(15)
        font.setBold(True)
        self.meas_label_settings.setFont(font)
        self.meas_label_settings.setLayoutDirection(
            Qt.LayoutDirection.RightToLeft
        )
        self.meas_label_settings.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.meas_layout_task.addWidget(self.meas_label_settings)

        self.meas_label_task_name = QLabel(self.verticalLayoutWidget_3)
        self.meas_label_task_name.setObjectName("meas_label_task_name")
        self.meas_label_task_name.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.meas_label_task_name.sizePolicy().hasHeightForWidth()
        )
        self.meas_label_task_name.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies(["Calibri"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.meas_label_task_name.setFont(font1)
        self.meas_label_task_name.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight
        )
        self.meas_label_task_name.setAlignment(
            Qt.AlignmentFlag.AlignBottom
            | Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
        )

        self.meas_layout_task.addWidget(self.meas_label_task_name)

        self.meas_line_edit_task_name = QLineEdit(self.verticalLayoutWidget_3)
        self.meas_line_edit_task_name.setObjectName("meas_line_edit_task_name")
        self.meas_line_edit_task_name.setInputMethodHints(
            Qt.InputMethodHint.ImhNone
        )

        self.meas_layout_task.addWidget(self.meas_line_edit_task_name)

        self.meas_label_num_impacts = QLabel(self.verticalLayoutWidget_3)
        self.meas_label_num_impacts.setObjectName("meas_label_num_impacts")
        self.meas_label_num_impacts.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.meas_label_num_impacts.sizePolicy().hasHeightForWidth()
        )
        self.meas_label_num_impacts.setSizePolicy(sizePolicy)
        self.meas_label_num_impacts.setFont(font1)
        self.meas_label_num_impacts.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight
        )
        self.meas_label_num_impacts.setAlignment(
            Qt.AlignmentFlag.AlignBottom
            | Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
        )

        self.meas_layout_task.addWidget(self.meas_label_num_impacts)

        self.meas_line_edit_num_impacts = QLineEdit(
            self.verticalLayoutWidget_3
        )
        self.meas_line_edit_num_impacts.setObjectName(
            "meas_line_edit_num_impacts"
        )
        self.meas_line_edit_num_impacts.setInputMethodHints(
            Qt.InputMethodHint.ImhDigitsOnly
        )

        self.meas_layout_task.addWidget(self.meas_line_edit_num_impacts)

        self.meas_label_impact_time = QLabel(self.verticalLayoutWidget_3)
        self.meas_label_impact_time.setObjectName("meas_label_impact_time")
        self.meas_label_impact_time.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.meas_label_impact_time.sizePolicy().hasHeightForWidth()
        )
        self.meas_label_impact_time.setSizePolicy(sizePolicy)
        self.meas_label_impact_time.setFont(font1)
        self.meas_label_impact_time.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight
        )
        self.meas_label_impact_time.setAlignment(
            Qt.AlignmentFlag.AlignBottom
            | Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
        )

        self.meas_layout_task.addWidget(self.meas_label_impact_time)

        self.meas_line_edit_impact_time = QLineEdit(
            self.verticalLayoutWidget_3
        )
        self.meas_line_edit_impact_time.setObjectName(
            "meas_line_edit_impact_time"
        )
        self.meas_line_edit_impact_time.setInputMethodHints(
            Qt.InputMethodHint.ImhDigitsOnly
        )

        self.meas_layout_task.addWidget(self.meas_line_edit_impact_time)

        self.meas_label_freq = QLabel(self.verticalLayoutWidget_3)
        self.meas_label_freq.setObjectName("meas_label_freq")
        self.meas_label_freq.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.meas_label_freq.sizePolicy().hasHeightForWidth()
        )
        self.meas_label_freq.setSizePolicy(sizePolicy)
        self.meas_label_freq.setFont(font1)
        self.meas_label_freq.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.meas_label_freq.setAlignment(
            Qt.AlignmentFlag.AlignBottom
            | Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
        )

        self.meas_layout_task.addWidget(self.meas_label_freq)

        self.meas_line_edit_sampling_freq = QLineEdit(
            self.verticalLayoutWidget_3
        )
        self.meas_line_edit_sampling_freq.setObjectName(
            "meas_line_edit_sampling_freq"
        )
        self.meas_line_edit_sampling_freq.setInputMethodHints(
            Qt.InputMethodHint.ImhDigitsOnly
        )

        self.meas_layout_task.addWidget(self.meas_line_edit_sampling_freq)

        self.meas_label_double_overflow_samples = QLabel(
            self.verticalLayoutWidget_3
        )
        self.meas_label_double_overflow_samples.setObjectName(
            "meas_label_double_overflow_samples"
        )
        self.meas_label_double_overflow_samples.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.meas_label_double_overflow_samples.sizePolicy().hasHeightForWidth()
        )
        self.meas_label_double_overflow_samples.setSizePolicy(sizePolicy)
        self.meas_label_double_overflow_samples.setFont(font1)
        self.meas_label_double_overflow_samples.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight
        )
        self.meas_label_double_overflow_samples.setAlignment(
            Qt.AlignmentFlag.AlignBottom
            | Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
        )

        self.meas_layout_task.addWidget(
            self.meas_label_double_overflow_samples
        )

        self.meas_line_edit_overflow_samples = QLineEdit(
            self.verticalLayoutWidget_3
        )
        self.meas_line_edit_overflow_samples.setObjectName(
            "meas_line_edit_overflow_samples"
        )
        self.meas_line_edit_overflow_samples.setEnabled(True)

        self.meas_layout_task.addWidget(self.meas_line_edit_overflow_samples)

        self.meas_label_double_impact_limit = QLabel(
            self.verticalLayoutWidget_3
        )
        self.meas_label_double_impact_limit.setObjectName(
            "meas_label_double_impact_limit"
        )
        self.meas_label_double_impact_limit.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.meas_label_double_impact_limit.sizePolicy().hasHeightForWidth()
        )
        self.meas_label_double_impact_limit.setSizePolicy(sizePolicy)
        self.meas_label_double_impact_limit.setFont(font1)
        self.meas_label_double_impact_limit.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight
        )
        self.meas_label_double_impact_limit.setAlignment(
            Qt.AlignmentFlag.AlignBottom
            | Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
        )

        self.meas_layout_task.addWidget(self.meas_label_double_impact_limit)

        self.meas_line_edit_double_impact_limit = QLineEdit(
            self.verticalLayoutWidget_3
        )
        self.meas_line_edit_double_impact_limit.setObjectName(
            "meas_line_edit_double_impact_limit"
        )
        self.meas_line_edit_double_impact_limit.setEnabled(True)

        self.meas_layout_task.addWidget(
            self.meas_line_edit_double_impact_limit
        )

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.meas_button_refresh_channels = QPushButton(
            self.verticalLayoutWidget_3
        )
        self.meas_button_refresh_channels.setObjectName(
            "meas_button_refresh_channels"
        )

        self.horizontalLayout.addWidget(self.meas_button_refresh_channels)

        self.meas_button_reset_hardware = QPushButton(
            self.verticalLayoutWidget_3
        )
        self.meas_button_reset_hardware.setObjectName(
            "meas_button_reset_hardware"
        )

        self.horizontalLayout.addWidget(self.meas_button_reset_hardware)

        self.meas_layout_task.addLayout(self.horizontalLayout)

        self.meas_label_channels = QLabel(self.verticalLayoutWidget_3)
        self.meas_label_channels.setObjectName("meas_label_channels")
        self.meas_label_channels.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.meas_label_channels.sizePolicy().hasHeightForWidth()
        )
        self.meas_label_channels.setSizePolicy(sizePolicy)
        self.meas_label_channels.setFont(font1)
        self.meas_label_channels.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight
        )
        self.meas_label_channels.setAlignment(
            Qt.AlignmentFlag.AlignBottom
            | Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
        )

        self.meas_layout_task.addWidget(self.meas_label_channels)

        self.meas_list_available_channels = QListView(
            self.verticalLayoutWidget_3
        )
        self.meas_list_available_channels.setObjectName(
            "meas_list_available_channels"
        )
        self.meas_list_available_channels.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        self.meas_layout_task.addWidget(self.meas_list_available_channels)

        self.meas_button_create_task = QPushButton(self.verticalLayoutWidget_3)
        self.meas_button_create_task.setObjectName("meas_button_create_task")

        self.meas_layout_task.addWidget(self.meas_button_create_task)

        self.retranslateUi(Dialog)
        self.meas_button_refresh_channels.clicked.connect(
            Dialog.meas_button_refresh_channels_pressed
        )
        self.meas_list_available_channels.doubleClicked.connect(
            Dialog.meas_list_item_double_clicked
        )
        self.meas_button_create_task.clicked.connect(
            Dialog.meas_button_create_pressed
        )
        self.meas_button_reset_hardware.clicked.connect(
            Dialog.meas_button_reset_hardware_pressed
        )

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", "Dialog", None)
        )
        self.meas_label_settings.setText(
            QCoreApplication.translate("Dialog", "Task Editor", None)
        )
        self.meas_label_task_name.setText(
            QCoreApplication.translate("Dialog", "Task Name", None)
        )
        # if QT_CONFIG(tooltip)
        self.meas_line_edit_task_name.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.meas_line_edit_task_name.setText(
            QCoreApplication.translate("Dialog", "test", None)
        )
        self.meas_line_edit_task_name.setPlaceholderText(
            QCoreApplication.translate("Dialog", "name", None)
        )
        self.meas_label_num_impacts.setText(
            QCoreApplication.translate("Dialog", "Number of Impacts / 1", None)
        )
        self.meas_line_edit_num_impacts.setText(
            QCoreApplication.translate("Dialog", "2", None)
        )
        self.meas_label_impact_time.setText(
            QCoreApplication.translate("Dialog", "Impact time / s", None)
        )
        self.meas_line_edit_impact_time.setText(
            QCoreApplication.translate("Dialog", "2", None)
        )
        self.meas_label_freq.setText(
            QCoreApplication.translate(
                "Dialog", "Sampling Frequency / Hz", None
            )
        )
        self.meas_line_edit_sampling_freq.setText(
            QCoreApplication.translate("Dialog", "12800", None)
        )
        self.meas_label_double_overflow_samples.setText(
            QCoreApplication.translate("Dialog", "Overflow Samples", None)
        )
        self.meas_line_edit_overflow_samples.setText(
            QCoreApplication.translate("Dialog", "3", None)
        )
        self.meas_label_double_impact_limit.setText(
            QCoreApplication.translate("Dialog", "Double Impact Limit", None)
        )
        self.meas_line_edit_double_impact_limit.setText(
            QCoreApplication.translate("Dialog", "1e-3", None)
        )
        self.meas_button_refresh_channels.setText(
            QCoreApplication.translate("Dialog", "Refresh Channels", None)
        )
        self.meas_button_reset_hardware.setText(
            QCoreApplication.translate("Dialog", "Reset Hardware", None)
        )
        self.meas_label_channels.setText(
            QCoreApplication.translate("Dialog", "Available Channels", None)
        )
        self.meas_button_create_task.setText(
            QCoreApplication.translate("Dialog", "Create", None)
        )

    # retranslateUi
