# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_user_export.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QSizePolicy, QWidget)

class Ui_win_user_export(object):
    def setupUi(self, win_user_export):
        if not win_user_export.objectName():
            win_user_export.setObjectName(u"win_user_export")
        win_user_export.resize(345, 148)
        self.gridLayout = QGridLayout(win_user_export)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_6 = QGroupBox(win_user_export)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_2 = QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.groupBox_6)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.label_2)

        self.cb_enable_group_policies = QCheckBox(self.groupBox)
        self.cb_enable_group_policies.setObjectName(u"cb_enable_group_policies")
        self.cb_enable_group_policies.setEnabled(True)
        self.cb_enable_group_policies.setMaximumSize(QSize(20, 16777215))
        self.cb_enable_group_policies.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cb_enable_group_policies.setChecked(False)

        self.horizontalLayout.addWidget(self.cb_enable_group_policies)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox_6)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.label_3)

        self.cb_enable_usb_policies = QCheckBox(self.groupBox_4)
        self.cb_enable_usb_policies.setObjectName(u"cb_enable_usb_policies")
        self.cb_enable_usb_policies.setEnabled(False)
        self.cb_enable_usb_policies.setMaximumSize(QSize(20, 16777215))
        self.cb_enable_usb_policies.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cb_enable_usb_policies.setCheckable(True)
        self.cb_enable_usb_policies.setChecked(False)

        self.horizontalLayout_5.addWidget(self.cb_enable_usb_policies)


        self.gridLayout_3.addWidget(self.groupBox_4, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 2)

        self.btns = QDialogButtonBox(self.groupBox_6)
        self.btns.setObjectName(u"btns")
        self.btns.setOrientation(Qt.Orientation.Horizontal)
        self.btns.setCenterButtons(False)

        self.gridLayout_2.addWidget(self.btns, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_6, 0, 0, 1, 1)


        self.retranslateUi(win_user_export)
        self.btns.rejected.connect(win_user_export.reject)
        self.btns.accepted.connect(win_user_export.accept)

        QMetaObject.connectSlotsByName(win_user_export)
    # setupUi

    def retranslateUi(self, win_user_export):
        win_user_export.setWindowTitle(QCoreApplication.translate("win_user_export", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439", None))
        self.groupBox_6.setTitle("")
        self.label_2.setText(QCoreApplication.translate("win_user_export", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043f\u043e\u043b\u0438\u0442\u0438\u043a\u0438 \u0433\u0440\u0443\u043f\u043f", None))
        self.cb_enable_group_policies.setText("")
        self.label_3.setText(QCoreApplication.translate("win_user_export", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043f\u043e\u043b\u0438\u0442\u0438\u043a\u0438 USB-\u043f\u043e\u0440\u0442\u043e\u0432", None))
        self.cb_enable_usb_policies.setText("")
    # retranslateUi

