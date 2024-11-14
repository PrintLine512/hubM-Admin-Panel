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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
from . import resources_rc

class Ui_Launch(object):
    def setupUi(self, Launch):
        if not Launch.objectName():
            Launch.setObjectName(u"Launch")
        Launch.resize(800, 270)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Launch.sizePolicy().hasHeightForWidth())
        Launch.setSizePolicy(sizePolicy)
        Launch.setMinimumSize(QSize(800, 270))
        Launch.setMaximumSize(QSize(800, 270))
        icon = QIcon()
        icon.addFile(u":/res/icon_connect", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Launch.setWindowIcon(icon)
        Launch.setDocumentMode(False)
        self.menu_reset_servers = QAction(Launch)
        self.menu_reset_servers.setObjectName(u"menu_reset_servers")
        self.menu_reset_creds = QAction(Launch)
        self.menu_reset_creds.setObjectName(u"menu_reset_creds")
        self.menu_update = QAction(Launch)
        self.menu_update.setObjectName(u"menu_update")
        icon1 = QIcon(QIcon.fromTheme(u"emblem-downloads"))
        self.menu_update.setIcon(icon1)
        self.menu_reset_all_profiles = QAction(Launch)
        self.menu_reset_all_profiles.setObjectName(u"menu_reset_all_profiles")
        self.menu_reset_master_password = QAction(Launch)
        self.menu_reset_master_password.setObjectName(u"menu_reset_master_password")
        self.menu_connect = QAction(Launch)
        self.menu_connect.setObjectName(u"menu_connect")
        icon2 = QIcon(QIcon.fromTheme(u"utilities-system-monitor"))
        self.menu_connect.setIcon(icon2)
        self.centralwidget = QWidget(Launch)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
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
        self.label.setGeometry(QRect(670, 50, 71, 71))
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
        self.label_6.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_3.addWidget(self.label_6)

        self.cb_servers = QComboBox(self.frame)
        self.cb_servers.setObjectName(u"cb_servers")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cb_servers.sizePolicy().hasHeightForWidth())
        self.cb_servers.setSizePolicy(sizePolicy3)
        self.cb_servers.setMaxVisibleItems(15)
        self.cb_servers.setMaxCount(15)
        self.cb_servers.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)

        self.horizontalLayout_3.addWidget(self.cb_servers)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.btn_server_new = QPushButton(self.frame)
        self.btn_server_new.setObjectName(u"btn_server_new")
        icon3 = QIcon(QIcon.fromTheme(u"folder-new"))
        self.btn_server_new.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.btn_server_new)

        self.btn_server_delete = QPushButton(self.frame)
        self.btn_server_delete.setObjectName(u"btn_server_delete")
        icon4 = QIcon(QIcon.fromTheme(u"edit-delete"))
        self.btn_server_delete.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.btn_server_delete)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.label_8)

        self.cb_creds = QComboBox(self.frame)
        self.cb_creds.setObjectName(u"cb_creds")
        sizePolicy3.setHeightForWidth(self.cb_creds.sizePolicy().hasHeightForWidth())
        self.cb_creds.setSizePolicy(sizePolicy3)
        self.cb_creds.setMaxVisibleItems(15)
        self.cb_creds.setMaxCount(15)
        self.cb_creds.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)

        self.horizontalLayout_4.addWidget(self.cb_creds)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.btn_creds_new = QPushButton(self.frame)
        self.btn_creds_new.setObjectName(u"btn_creds_new")
        icon5 = QIcon(QIcon.fromTheme(u"contact-new"))
        self.btn_creds_new.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.btn_creds_new)

        self.btn_creds_delete = QPushButton(self.frame)
        self.btn_creds_delete.setObjectName(u"btn_creds_delete")
        self.btn_creds_delete.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.btn_creds_delete)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.btn_connect = QPushButton(self.frame)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setIcon(icon2)
        self.btn_connect.setCheckable(False)
        self.btn_connect.setAutoDefault(True)

        self.verticalLayout_5.addWidget(self.btn_connect)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        Launch.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(Launch)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menu)
        self.menu_2.setObjectName(u"menu_2")
        icon6 = QIcon(QIcon.fromTheme(u"document-properties"))
        self.menu_2.setIcon(icon6)
        Launch.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.btn_connect, self.cb_creds)
        QWidget.setTabOrder(self.cb_creds, self.btn_creds_new)
        QWidget.setTabOrder(self.btn_creds_new, self.btn_creds_delete)

        self.menuBar.addAction(self.menu.menuAction())
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.menu_update)
        self.menu.addAction(self.menu_connect)
        self.menu_2.addAction(self.menu_reset_servers)
        self.menu_2.addAction(self.menu_reset_creds)
        self.menu_2.addAction(self.menu_reset_all_profiles)
        self.menu_2.addAction(self.menu_reset_master_password)

        self.retranslateUi(Launch)

        self.btn_connect.setDefault(True)


        QMetaObject.connectSlotsByName(Launch)
    # setupUi

    def retranslateUi(self, Launch):
        Launch.setWindowTitle(QCoreApplication.translate("Launch", u"hubM Admin Panel Connect", None))
        self.menu_reset_servers.setText(QCoreApplication.translate("Launch", u"\u0421\u0431\u0440\u043e\u0441 \u043f\u0440\u043e\u0444\u0438\u043b\u0435\u0439 \u0441\u0435\u0440\u0432\u0435\u0440\u0430", None))
        self.menu_reset_creds.setText(QCoreApplication.translate("Launch", u"\u0421\u0431\u0440\u043e\u0441 \u043f\u0440\u043e\u0444\u0438\u043b\u0435\u0439 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.menu_update.setText(QCoreApplication.translate("Launch", u"\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.menu_reset_all_profiles.setText(QCoreApplication.translate("Launch", u"\u0421\u0431\u0440\u043e\u0441 \u0432\u0441\u0435\u0445 \u043f\u0440\u043e\u0444\u0438\u043b\u0435\u0439", None))
        self.menu_reset_master_password.setText(QCoreApplication.translate("Launch", u"\u0421\u0431\u0440\u043e\u0441 \u043c\u0430\u0441\u0442\u0435\u0440 \u043f\u0430\u0440\u043e\u043b\u044f", None))
        self.menu_connect.setText(QCoreApplication.translate("Launch", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.label_5.setText(QCoreApplication.translate("Launch", u"<html><head/><body><p>\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u043b\u044f \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u044f \u0441 \u0441\u0435\u0440\u0432\u0435\u0440\u043e\u043c:</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Launch", u"<html><head/><body><p><span style=\" font-size:48pt;\">hubM Admin Panel</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Launch", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c \u0441\u0435\u0440\u0432\u0435\u0440\u0430:", None))
        self.btn_server_new.setText("")
        self.btn_server_delete.setText("")
        self.label_8.setText(QCoreApplication.translate("Launch", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f:", None))
        self.btn_creds_new.setText("")
        self.btn_creds_delete.setText("")
        self.btn_connect.setText(QCoreApplication.translate("Launch", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.menu.setTitle(QCoreApplication.translate("Launch", u"\u041c\u0435\u043d\u044e", None))
        self.menu_2.setTitle(QCoreApplication.translate("Launch", u"\u0421\u0431\u0440\u043e\u0441 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a", None))
    # retranslateUi

