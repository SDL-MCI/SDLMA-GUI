# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sdlma_meas_gui.ui'
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
        Dialog.resize(377, 741)
        self.verticalLayoutWidget_5 = QWidget(Dialog)
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 0, 361, 731))
        self.ema_layout_setup = QVBoxLayout(self.verticalLayoutWidget_5)
        self.ema_layout_setup.setObjectName("ema_layout_setup")
        self.ema_layout_setup.setContentsMargins(0, 0, 0, 0)
        self.ema_label_heading = QLabel(self.verticalLayoutWidget_5)
        self.ema_label_heading.setObjectName("ema_label_heading")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ema_label_heading.sizePolicy().hasHeightForWidth()
        )
        self.ema_label_heading.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies(["Calibri"])
        font.setPointSize(15)
        font.setBold(True)
        self.ema_label_heading.setFont(font)
        self.ema_label_heading.setLayoutDirection(
            Qt.LayoutDirection.RightToLeft
        )
        self.ema_label_heading.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ema_layout_setup.addWidget(self.ema_label_heading)

        self.ema_label_name = QLabel(self.verticalLayoutWidget_5)
        self.ema_label_name.setObjectName("ema_label_name")
        self.ema_label_name.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.ema_label_name.sizePolicy().hasHeightForWidth()
        )
        self.ema_label_name.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies(["Calibri"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.ema_label_name.setFont(font1)
        self.ema_label_name.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ema_label_name.setAlignment(
            Qt.AlignmentFlag.AlignBottom
            | Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
        )

        self.ema_layout_setup.addWidget(self.ema_label_name)

        self.ema_line_edit_name = QLineEdit(self.verticalLayoutWidget_5)
        self.ema_line_edit_name.setObjectName("ema_line_edit_name")
        self.ema_line_edit_name.setEnabled(True)

        self.ema_layout_setup.addWidget(self.ema_line_edit_name)

        self.ema_label_sampling_freq = QLabel(self.verticalLayoutWidget_5)
        self.ema_label_sampling_freq.setObjectName("ema_label_sampling_freq")
        self.ema_label_sampling_freq.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.ema_label_sampling_freq.sizePolicy().hasHeightForWidth()
        )
        self.ema_label_sampling_freq.setSizePolicy(sizePolicy)
        self.ema_label_sampling_freq.setFont(font1)
        self.ema_label_sampling_freq.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight
        )
        self.ema_label_sampling_freq.setAlignment(
            Qt.AlignmentFlag.AlignBottom
            | Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
        )

        self.ema_layout_setup.addWidget(self.ema_label_sampling_freq)

        self.ema_line_edit_sampling_freq = QLineEdit(
            self.verticalLayoutWidget_5
        )
        self.ema_line_edit_sampling_freq.setObjectName(
            "ema_line_edit_sampling_freq"
        )
        self.ema_line_edit_sampling_freq.setEnabled(False)

        self.ema_layout_setup.addWidget(self.ema_line_edit_sampling_freq)

        self.ema_label_exc_signals = QLabel(self.verticalLayoutWidget_5)
        self.ema_label_exc_signals.setObjectName("ema_label_exc_signals")
        self.ema_label_exc_signals.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.ema_label_exc_signals.sizePolicy().hasHeightForWidth()
        )
        self.ema_label_exc_signals.setSizePolicy(sizePolicy)
        self.ema_label_exc_signals.setFont(font1)
        self.ema_label_exc_signals.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight
        )
        self.ema_label_exc_signals.setAlignment(
            Qt.AlignmentFlag.AlignBottom
            | Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
        )

        self.ema_layout_setup.addWidget(self.ema_label_exc_signals)

        self.ema_list_exc_signals = QListView(self.verticalLayoutWidget_5)
        self.ema_list_exc_signals.setObjectName("ema_list_exc_signals")
        self.ema_list_exc_signals.setEnabled(True)
        self.ema_list_exc_signals.setSelectionMode(
            QAbstractItemView.SelectionMode.NoSelection
        )

        self.ema_layout_setup.addWidget(self.ema_list_exc_signals)

        self.ema_label_resp_signals = QLabel(self.verticalLayoutWidget_5)
        self.ema_label_resp_signals.setObjectName("ema_label_resp_signals")
        self.ema_label_resp_signals.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.ema_label_resp_signals.sizePolicy().hasHeightForWidth()
        )
        self.ema_label_resp_signals.setSizePolicy(sizePolicy)
        self.ema_label_resp_signals.setFont(font1)
        self.ema_label_resp_signals.setLayoutDirection(
            Qt.LayoutDirection.LeftToRight
        )
        self.ema_label_resp_signals.setAlignment(
            Qt.AlignmentFlag.AlignBottom
            | Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
        )

        self.ema_layout_setup.addWidget(self.ema_label_resp_signals)

        self.ema_list_resp_signals = QListView(self.verticalLayoutWidget_5)
        self.ema_list_resp_signals.setObjectName("ema_list_resp_signals")
        self.ema_list_resp_signals.setEnabled(True)
        self.ema_list_resp_signals.setSelectionMode(
            QAbstractItemView.SelectionMode.NoSelection
        )

        self.ema_layout_setup.addWidget(self.ema_list_resp_signals)

        self.ema_button_add = QPushButton(self.verticalLayoutWidget_5)
        self.ema_button_add.setObjectName("ema_button_add")
        self.ema_button_add.setEnabled(False)

        self.ema_layout_setup.addWidget(self.ema_button_add)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.ema_layout_setup.addLayout(self.horizontalLayout)

        self.ema_label_heading.raise_()
        self.ema_label_name.raise_()
        self.ema_line_edit_name.raise_()
        self.ema_list_resp_signals.raise_()
        self.ema_label_resp_signals.raise_()
        self.ema_list_exc_signals.raise_()
        self.ema_label_exc_signals.raise_()
        self.ema_button_add.raise_()
        self.ema_line_edit_sampling_freq.raise_()
        self.ema_label_sampling_freq.raise_()

        self.retranslateUi(Dialog)
        self.ema_list_exc_signals.doubleClicked.connect(
            Dialog.ema_list_exc_signals_double_clicked
        )
        self.ema_list_resp_signals.doubleClicked.connect(
            Dialog.ema_list_resp_signals_double_clicked
        )
        self.ema_button_add.clicked.connect(Dialog.ema_button_add_pressed)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", "Dialog", None)
        )
        self.ema_label_heading.setText(
            QCoreApplication.translate("Dialog", "Measurement", None)
        )
        self.ema_label_name.setText(
            QCoreApplication.translate("Dialog", "Namee", None)
        )
        self.ema_line_edit_name.setText("")
        self.ema_label_sampling_freq.setText(
            QCoreApplication.translate(
                "Dialog", "Sampling Frequency / Hz", None
            )
        )
        self.ema_line_edit_sampling_freq.setText("")
        self.ema_label_exc_signals.setText(
            QCoreApplication.translate("Dialog", "Exc Signals", None)
        )
        self.ema_label_resp_signals.setText(
            QCoreApplication.translate("Dialog", "Resp Signals", None)
        )
        self.ema_button_add.setText(
            QCoreApplication.translate("Dialog", "Add", None)
        )

    # retranslateUi
