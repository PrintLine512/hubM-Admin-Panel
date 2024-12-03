# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_notifications.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Notifications(object):
    def setupUi(self, Notifications):
        if not Notifications.objectName():
            Notifications.setObjectName(u"Notifications")
        Notifications.resize(438, 145)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Notifications.sizePolicy().hasHeightForWidth())
        Notifications.setSizePolicy(sizePolicy)
        Notifications.setWindowOpacity(1.000000000000000)
        Notifications.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(Notifications)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scroll_area = QScrollArea(Notifications)
        self.scroll_area.setObjectName(u"scroll_area")
        sizePolicy.setHeightForWidth(self.scroll_area.sizePolicy().hasHeightForWidth())
        self.scroll_area.setSizePolicy(sizePolicy)
        self.scroll_area.setMinimumSize(QSize(420, 0))
        self.scroll_area.setMaximumSize(QSize(420, 16777215))
        self.scroll_area.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll_area.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scroll_area.setWidgetResizable(False)
        self.scroll_area_contents = QWidget()
        self.scroll_area_contents.setObjectName(u"scroll_area_contents")
        self.scroll_area_contents.setGeometry(QRect(0, -275, 400, 400))
        sizePolicy.setHeightForWidth(self.scroll_area_contents.sizePolicy().hasHeightForWidth())
        self.scroll_area_contents.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.scroll_area_contents)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scroll_area.setWidget(self.scroll_area_contents)

        self.verticalLayout.addWidget(self.scroll_area)


        self.retranslateUi(Notifications)

        QMetaObject.connectSlotsByName(Notifications)
    # setupUi

    def retranslateUi(self, Notifications):
        Notifications.setWindowTitle(QCoreApplication.translate("Notifications", u"Form", None))
    # retranslateUi

