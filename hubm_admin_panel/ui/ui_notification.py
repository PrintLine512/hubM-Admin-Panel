# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_notification.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from . import resources_rc

class Ui_Notification(object):
    def setupUi(self, Notification):
        if not Notification.objectName():
            Notification.setObjectName(u"Notification")
        Notification.resize(382, 120)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Notification.sizePolicy().hasHeightForWidth())
        Notification.setSizePolicy(sizePolicy)
        Notification.setMinimumSize(QSize(382, 120))
        Notification.setMaximumSize(QSize(385, 300))
        self.gridLayout = QGridLayout(Notification)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalFrame = QFrame(Notification)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lb_icon = QLabel(self.horizontalFrame)
        self.lb_icon.setObjectName(u"lb_icon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_icon.sizePolicy().hasHeightForWidth())
        self.lb_icon.setSizePolicy(sizePolicy1)
        self.lb_icon.setMinimumSize(QSize(30, 30))
        self.lb_icon.setMaximumSize(QSize(30, 30))
        self.lb_icon.setPixmap(QPixmap(u":/res/icons/icon-hr.png.png"))
        self.lb_icon.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.lb_icon)

        self.line = QFrame(self.horizontalFrame)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 75))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_title = QLabel(self.horizontalFrame)
        self.lb_title.setObjectName(u"lb_title")
        sizePolicy.setHeightForWidth(self.lb_title.sizePolicy().hasHeightForWidth())
        self.lb_title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lb_title.setFont(font)

        self.verticalLayout.addWidget(self.lb_title)

        self.lb_content = QLabel(self.horizontalFrame)
        self.lb_content.setObjectName(u"lb_content")
        sizePolicy.setHeightForWidth(self.lb_content.sizePolicy().hasHeightForWidth())
        self.lb_content.setSizePolicy(sizePolicy)
        self.lb_content.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lb_content.setWordWrap(True)

        self.verticalLayout.addWidget(self.lb_content)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.btn_2 = QPushButton(self.horizontalFrame)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy2)
        self.btn_2.setMaximumSize(QSize(16777215, 30))
        self.btn_2.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_close = QPushButton(self.horizontalFrame)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMaximumSize(QSize(30, 30))
        self.btn_close.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditClear))
        self.btn_close.setIcon(icon)
        self.btn_close.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.horizontalFrame, 0, 4, 1, 1)


        self.retranslateUi(Notification)

        QMetaObject.connectSlotsByName(Notification)
    # setupUi

    def retranslateUi(self, Notification):
        Notification.setWindowTitle(QCoreApplication.translate("Notification", u"Form", None))
        self.lb_icon.setText("")
        self.lb_title.setText(QCoreApplication.translate("Notification", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a", None))
        self.lb_content.setText(QCoreApplication.translate("Notification", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.btn_2.setText("")
        self.btn_close.setText("")
    # retranslateUi

