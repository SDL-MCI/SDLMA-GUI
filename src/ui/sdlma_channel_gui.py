# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sdlma_channel_gui.ui'
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
    QApplication,
    QCheckBox,
    QComboBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(418, 503)
        Dialog.setModal(False)
        self.channel_widget = QWidget(Dialog)
        self.channel_widget.setObjectName("channel_widget")
        self.channel_widget.setGeometry(QRect(0, 0, 411, 491))
        self.verticalLayoutWidget = QWidget(self.channel_widget)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 391, 461))
        self.channel_layout_main = QVBoxLayout(self.verticalLayoutWidget)
        self.channel_layout_main.setObjectName("channel_layout_main")
        self.channel_layout_main.setContentsMargins(0, 0, 0, 0)
        self.channel_label_heading = QLabel(self.verticalLayoutWidget)
        self.channel_label_heading.setObjectName("channel_label_heading")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.channel_label_heading.sizePolicy().hasHeightForWidth()
        )
        self.channel_label_heading.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.channel_label_heading.setFont(font)

        self.channel_layout_main.addWidget(self.channel_label_heading)

        self.channel_label_name = QLabel(self.verticalLayoutWidget)
        self.channel_label_name.setObjectName("channel_label_name")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.channel_label_name.sizePolicy().hasHeightForWidth()
        )
        self.channel_label_name.setSizePolicy(sizePolicy1)

        self.channel_layout_main.addWidget(self.channel_label_name)

        self.channel_line_edit_name = QLineEdit(self.verticalLayoutWidget)
        self.channel_line_edit_name.setObjectName("channel_line_edit_name")
        self.channel_line_edit_name.setEnabled(False)

        self.channel_layout_main.addWidget(self.channel_line_edit_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.channel_button_select_file = QPushButton(
            self.verticalLayoutWidget
        )
        self.channel_button_select_file.setObjectName(
            "channel_button_select_file"
        )

        self.horizontalLayout.addWidget(self.channel_button_select_file)

        self.channel_combo_box_sensor_type = QComboBox(
            self.verticalLayoutWidget
        )
        self.channel_combo_box_sensor_type.addItem("")
        self.channel_combo_box_sensor_type.addItem("")
        self.channel_combo_box_sensor_type.setObjectName(
            "channel_combo_box_sensor_type"
        )

        self.horizontalLayout.addWidget(self.channel_combo_box_sensor_type)

        self.channel_check_box_hw_teds = QCheckBox(self.verticalLayoutWidget)
        self.channel_check_box_hw_teds.setObjectName(
            "channel_check_box_hw_teds"
        )
        self.channel_check_box_hw_teds.setEnabled(False)
        sizePolicy.setHeightForWidth(
            self.channel_check_box_hw_teds.sizePolicy().hasHeightForWidth()
        )
        self.channel_check_box_hw_teds.setSizePolicy(sizePolicy)
        self.channel_check_box_hw_teds.setCheckable(True)

        self.horizontalLayout.addWidget(self.channel_check_box_hw_teds)

        self.channel_layout_main.addLayout(self.horizontalLayout)

        self.channel_label_comment = QLabel(self.verticalLayoutWidget)
        self.channel_label_comment.setObjectName("channel_label_comment")
        self.channel_label_comment.setEnabled(True)
        sizePolicy1.setHeightForWidth(
            self.channel_label_comment.sizePolicy().hasHeightForWidth()
        )
        self.channel_label_comment.setSizePolicy(sizePolicy1)

        self.channel_layout_main.addWidget(self.channel_label_comment)

        self.channel_line_edit_comment = QLineEdit(self.verticalLayoutWidget)
        self.channel_line_edit_comment.setObjectName(
            "channel_line_edit_comment"
        )
        self.channel_line_edit_comment.setEnabled(True)

        self.channel_layout_main.addWidget(self.channel_line_edit_comment)

        self.channel_label_serial_number = QLabel(self.verticalLayoutWidget)
        self.channel_label_serial_number.setObjectName(
            "channel_label_serial_number"
        )
        self.channel_label_serial_number.setEnabled(True)
        sizePolicy1.setHeightForWidth(
            self.channel_label_serial_number.sizePolicy().hasHeightForWidth()
        )
        self.channel_label_serial_number.setSizePolicy(sizePolicy1)

        self.channel_layout_main.addWidget(self.channel_label_serial_number)

        self.channel_line_edit_serial_number = QLineEdit(
            self.verticalLayoutWidget
        )
        self.channel_line_edit_serial_number.setObjectName(
            "channel_line_edit_serial_number"
        )
        self.channel_line_edit_serial_number.setEnabled(True)

        self.channel_layout_main.addWidget(
            self.channel_line_edit_serial_number
        )

        self.channel_label_disp_name = QLabel(self.verticalLayoutWidget)
        self.channel_label_disp_name.setObjectName("channel_label_disp_name")
        sizePolicy1.setHeightForWidth(
            self.channel_label_disp_name.sizePolicy().hasHeightForWidth()
        )
        self.channel_label_disp_name.setSizePolicy(sizePolicy1)

        self.channel_layout_main.addWidget(self.channel_label_disp_name)

        self.channel_line_edit_disp_name = QLineEdit(self.verticalLayoutWidget)
        self.channel_line_edit_disp_name.setObjectName(
            "channel_line_edit_disp_name"
        )
        self.channel_line_edit_disp_name.setEnabled(True)

        self.channel_layout_main.addWidget(self.channel_line_edit_disp_name)

        self.channel_label_sensitivity = QLabel(self.verticalLayoutWidget)
        self.channel_label_sensitivity.setObjectName(
            "channel_label_sensitivity"
        )
        sizePolicy1.setHeightForWidth(
            self.channel_label_sensitivity.sizePolicy().hasHeightForWidth()
        )
        self.channel_label_sensitivity.setSizePolicy(sizePolicy1)

        self.channel_layout_main.addWidget(self.channel_label_sensitivity)

        self.channel_line_edit_sensitivity = QLineEdit(
            self.verticalLayoutWidget
        )
        self.channel_line_edit_sensitivity.setObjectName(
            "channel_line_edit_sensitivity"
        )

        self.channel_layout_main.addWidget(self.channel_line_edit_sensitivity)

        self.channel_label_serial_number_2 = QLabel(self.verticalLayoutWidget)
        self.channel_label_serial_number_2.setObjectName(
            "channel_label_serial_number_2"
        )
        self.channel_label_serial_number_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(
            self.channel_label_serial_number_2.sizePolicy().hasHeightForWidth()
        )
        self.channel_label_serial_number_2.setSizePolicy(sizePolicy1)

        self.channel_layout_main.addWidget(self.channel_label_serial_number_2)

        self.channel_combo_box_sensor_direction = QComboBox(
            self.verticalLayoutWidget
        )
        self.channel_combo_box_sensor_direction.addItem("")
        self.channel_combo_box_sensor_direction.addItem("")
        self.channel_combo_box_sensor_direction.addItem("")
        self.channel_combo_box_sensor_direction.addItem("")
        self.channel_combo_box_sensor_direction.addItem("")
        self.channel_combo_box_sensor_direction.addItem("")
        self.channel_combo_box_sensor_direction.setObjectName(
            "channel_combo_box_sensor_direction"
        )

        self.channel_layout_main.addWidget(
            self.channel_combo_box_sensor_direction
        )

        self.channel_check_box_add = QCheckBox(self.verticalLayoutWidget)
        self.channel_check_box_add.setObjectName("channel_check_box_add")
        sizePolicy1.setHeightForWidth(
            self.channel_check_box_add.sizePolicy().hasHeightForWidth()
        )
        self.channel_check_box_add.setSizePolicy(sizePolicy1)
        self.channel_check_box_add.setChecked(True)

        self.channel_layout_main.addWidget(self.channel_check_box_add)

        self.channel_button_submit = QPushButton(self.verticalLayoutWidget)
        self.channel_button_submit.setObjectName("channel_button_submit")

        self.channel_layout_main.addWidget(self.channel_button_submit)

        self.retranslateUi(Dialog)
        self.channel_button_submit.clicked.connect(Dialog.accept)
        self.channel_combo_box_sensor_type.currentIndexChanged.connect(
            Dialog.combo_box_choice_change
        )
        self.channel_button_select_file.clicked.connect(
            Dialog.channel_button_select_file_pressed
        )

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", "Dialog", None)
        )
        self.channel_label_heading.setText(
            QCoreApplication.translate("Dialog", "Channel Information", None)
        )
        self.channel_label_name.setText(
            QCoreApplication.translate("Dialog", "Channel Name", None)
        )
        self.channel_button_select_file.setText(
            QCoreApplication.translate("Dialog", "Select File", None)
        )
        self.channel_combo_box_sensor_type.setItemText(
            0, QCoreApplication.translate("Dialog", "Accelerometer", None)
        )
        self.channel_combo_box_sensor_type.setItemText(
            1, QCoreApplication.translate("Dialog", "Force", None)
        )

        self.channel_check_box_hw_teds.setText(
            QCoreApplication.translate("Dialog", "Hardware TEDS", None)
        )
        self.channel_label_comment.setText(
            QCoreApplication.translate("Dialog", "Comment", None)
        )
        self.channel_label_serial_number.setText(
            QCoreApplication.translate("Dialog", "Serial Number", None)
        )
        self.channel_label_disp_name.setText(
            QCoreApplication.translate("Dialog", "Display Name", None)
        )
        self.channel_label_sensitivity.setText(
            QCoreApplication.translate(
                "Dialog",
                "Sensitivity / mV\u00b7s<sup>2</sup>\u00b7m<sup>-1</sup>",
                None,
            )
        )
        self.channel_label_serial_number_2.setText(
            QCoreApplication.translate("Dialog", "Direction", None)
        )
        self.channel_combo_box_sensor_direction.setItemText(
            0, QCoreApplication.translate("Dialog", "+Z", None)
        )
        self.channel_combo_box_sensor_direction.setItemText(
            1, QCoreApplication.translate("Dialog", "-Z", None)
        )
        self.channel_combo_box_sensor_direction.setItemText(
            2, QCoreApplication.translate("Dialog", "+Y", None)
        )
        self.channel_combo_box_sensor_direction.setItemText(
            3, QCoreApplication.translate("Dialog", "-Y", None)
        )
        self.channel_combo_box_sensor_direction.setItemText(
            4, QCoreApplication.translate("Dialog", "+X", None)
        )
        self.channel_combo_box_sensor_direction.setItemText(
            5, QCoreApplication.translate("Dialog", "-X", None)
        )

        self.channel_check_box_add.setText(
            QCoreApplication.translate("Dialog", "Add", None)
        )
        self.channel_button_submit.setText(
            QCoreApplication.translate("Dialog", "Submit", None)
        )

    # retranslateUi
