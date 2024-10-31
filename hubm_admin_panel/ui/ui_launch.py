# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_launch.ui'
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
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from . import resources_rc

class Ui_Launch(object):
    def setupUi(self, Launch):
        if not Launch.objectName():
            Launch.setObjectName(u"Launch")
        Launch.resize(800, 260)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Launch.sizePolicy().hasHeightForWidth())
        Launch.setSizePolicy(sizePolicy)
        Launch.setMinimumSize(QSize(800, 260))
        Launch.setMaximumSize(QSize(800, 260))
        icon = QIcon()
        icon.addFile(u":/res/icon_connect", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Launch.setWindowIcon(icon)
        Launch.setDocumentMode(False)
        self.centralwidget = QWidget(Launch)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(0)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 50, 571, 71))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setTextFormat(Qt.TextFormat.RichText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 0, 632, 121))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies([u"Britannic"])
        font.setPointSize(14)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(640, 40, 71, 71))
        self.label.setMaximumSize(QSize(120, 120))
        self.label.setPixmap(QPixmap(u":/res/image/hub_fill.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)

        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.le_address = QLineEdit(self.frame)
        self.le_address.setObjectName(u"le_address")

        self.horizontalLayout_3.addWidget(self.le_address)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.le_tcp_port = QLineEdit(self.frame)
        self.le_tcp_port.setObjectName(u"le_tcp_port")
        self.le_tcp_port.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.le_tcp_port)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.le_token = QLineEdit(self.frame)
        self.le_token.setObjectName(u"le_token")
        self.le_token.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.horizontalLayout_4.addWidget(self.le_token)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.btn_connect = QPushButton(self.frame)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setCheckable(False)
        self.btn_connect.setAutoDefault(True)

        self.verticalLayout_5.addWidget(self.btn_connect)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        Launch.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.le_address, self.le_tcp_port)
        QWidget.setTabOrder(self.le_tcp_port, self.le_token)
        QWidget.setTabOrder(self.le_token, self.btn_connect)

        self.retranslateUi(Launch)

        self.btn_connect.setDefault(True)


        QMetaObject.connectSlotsByName(Launch)
    # setupUi

    def retranslateUi(self, Launch):
        Launch.setWindowTitle(QCoreApplication.translate("Launch", u"hubM Admin Panel Connect", None))
        self.label_5.setText(QCoreApplication.translate("Launch", u"<html><head/><body><p>\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0434\u043b\u044f \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f \u043a \u0441\u0435\u0440\u0432\u0435\u0440\u0443 \u0438\u043b\u0438 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043d\u044b\u0435:</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Launch", u"<html><head/><body><p><span style=\" font-size:48pt;\">hubM Admin Panel</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Launch", u"\u0410\u0434\u0440\u0435\u0441:", None))
        self.le_address.setPlaceholderText(QCoreApplication.translate("Launch", u"Hostname \u0438\u043b\u0438 IP", None))
        self.label_7.setText(QCoreApplication.translate("Launch", u"\u041f\u043e\u0440\u0442:", None))
        self.le_tcp_port.setText(QCoreApplication.translate("Launch", u"5000", None))
        self.label_8.setText(QCoreApplication.translate("Launch", u"\u0422\u043e\u043a\u0435\u043d:", None))
        self.le_token.setText("")
        self.le_token.setPlaceholderText(QCoreApplication.translate("Launch", u"\u0412\u0430\u0448 \u0442\u043e\u043a\u0435\u043d", None))
        self.btn_connect.setText(QCoreApplication.translate("Launch", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
    # retranslateUi

