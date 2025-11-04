# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sdlma_mp_to_nodes_gui.ui'
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
    QDialog,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLayout,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(398, 583)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSizeConstraint(
            QLayout.SizeConstraint.SetNoConstraint
        )
        self.ema_label_heading = QLabel(Dialog)
        self.ema_label_heading.setObjectName("ema_label_heading")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.ema_label_heading.sizePolicy().hasHeightForWidth()
        )
        self.ema_label_heading.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies(["Calibri"])
        font.setPointSize(15)
        font.setBold(True)
        self.ema_label_heading.setFont(font)
        self.ema_label_heading.setLayoutDirection(
            Qt.LayoutDirection.RightToLeft
        )
        self.ema_label_heading.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.ema_label_heading)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mp_to_nodes_widget = QWidget(Dialog)
        self.mp_to_nodes_widget.setObjectName("mp_to_nodes_widget")
        sizePolicy.setHeightForWidth(
            self.mp_to_nodes_widget.sizePolicy().hasHeightForWidth()
        )
        self.mp_to_nodes_widget.setSizePolicy(sizePolicy)
        self.mp_to_nodes_widget.setMinimumSize(QSize(0, 0))
        self.verticalLayoutWidget_4 = QWidget(self.mp_to_nodes_widget)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 0, 381, 581))
        self.mp_to_nodes_layout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.mp_to_nodes_layout.setObjectName("mp_to_nodes_layout")
        self.mp_to_nodes_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.mp_to_nodes_widget)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.mp_to_nodes_button_done = QPushButton(Dialog)
        self.mp_to_nodes_button_done.setObjectName("mp_to_nodes_button_done")
        self.mp_to_nodes_button_done.setEnabled(True)
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.mp_to_nodes_button_done.sizePolicy().hasHeightForWidth()
        )
        self.mp_to_nodes_button_done.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.mp_to_nodes_button_done)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.mp_to_nodes_button_done.clicked.connect(
            Dialog.mp_to_nodes_button_done_pressed
        )

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", "Dialog", None)
        )
        self.ema_label_heading.setText(
            QCoreApplication.translate("Dialog", "Channels to Nodes", None)
        )
        self.mp_to_nodes_button_done.setText(
            QCoreApplication.translate("Dialog", "Done", None)
        )

    # retranslateUi
