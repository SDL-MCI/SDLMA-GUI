# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sdlma_teds_gui.ui'
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
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from custom_widgets.teds_widget import PyMATedsWidget


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(530, 1037)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 20, 451, 761))
        self.teds_layout_main = QVBoxLayout(self.verticalLayoutWidget)
        self.teds_layout_main.setObjectName("teds_layout_main")
        self.teds_layout_main.setContentsMargins(0, 0, 0, 0)
        self.teds_label_heading = QLabel(self.verticalLayoutWidget)
        self.teds_label_heading.setObjectName("teds_label_heading")
        font = QFont()
        font.setFamilies(["Arial"])
        font.setPointSize(15)
        font.setBold(True)
        self.teds_label_heading.setFont(font)
        self.teds_label_heading.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.teds_layout_main.addWidget(self.teds_label_heading)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.teds_button_new = QPushButton(self.verticalLayoutWidget)
        self.teds_button_new.setObjectName("teds_button_new")

        self.horizontalLayout.addWidget(self.teds_button_new)

        self.teds_button_load = QPushButton(self.verticalLayoutWidget)
        self.teds_button_load.setObjectName("teds_button_load")

        self.horizontalLayout.addWidget(self.teds_button_load)

        self.teds_layout_main.addLayout(self.horizontalLayout)

        self.teds_widget_main = PyMATedsWidget(self.verticalLayoutWidget)
        self.teds_widget_main.setObjectName("teds_widget_main")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.teds_widget_main.sizePolicy().hasHeightForWidth()
        )
        self.teds_widget_main.setSizePolicy(sizePolicy1)
        self.teds_widget_main.setMinimumSize(QSize(250, 250))
        self.teds_scroll_area = QScrollArea(self.teds_widget_main)
        self.teds_scroll_area.setObjectName("teds_scroll_area")
        self.teds_scroll_area.setGeometry(QRect(10, 0, 431, 671))
        sizePolicy1.setHeightForWidth(
            self.teds_scroll_area.sizePolicy().hasHeightForWidth()
        )
        self.teds_scroll_area.setSizePolicy(sizePolicy1)
        self.teds_scroll_area.setMinimumSize(QSize(0, 499))
        self.teds_scroll_area.setMaximumSize(QSize(16777215, 16777215))
        self.teds_scroll_area.setWidgetResizable(True)
        self.teds_scroll_area_content = QWidget()
        self.teds_scroll_area_content.setObjectName("teds_scroll_area_content")
        self.teds_scroll_area_content.setGeometry(QRect(0, 0, 429, 18))
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.teds_scroll_area_content.sizePolicy().hasHeightForWidth()
        )
        self.teds_scroll_area_content.setSizePolicy(sizePolicy2)
        self.teds_scroll_area_content.setMinimumSize(QSize(0, 0))
        self.teds_layout_data = QVBoxLayout(self.teds_scroll_area_content)
        self.teds_layout_data.setObjectName("teds_layout_data")
        self.teds_scroll_area.setWidget(self.teds_scroll_area_content)

        self.teds_layout_main.addWidget(self.teds_widget_main)

        self.teds_button_save = QPushButton(self.verticalLayoutWidget)
        self.teds_button_save.setObjectName("teds_button_save")

        self.teds_layout_main.addWidget(self.teds_button_save)

        self.retranslateUi(Dialog)
        self.teds_button_load.clicked.connect(
            self.teds_widget_main.teds_button_load_pressed
        )

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", "Dialog", None)
        )
        self.teds_label_heading.setText(
            QCoreApplication.translate("Dialog", "Teds Editor", None)
        )
        self.teds_button_new.setText(
            QCoreApplication.translate("Dialog", "Create New Teds File", None)
        )
        self.teds_button_load.setText(
            QCoreApplication.translate(
                "Dialog", "Load Existing Teds File", None
            )
        )
        self.teds_button_save.setText(
            QCoreApplication.translate("Dialog", "Save", None)
        )

    # retranslateUi
