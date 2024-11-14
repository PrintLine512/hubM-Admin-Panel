# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_new_policies.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_win_new_policies(object):
    def setupUi(self, win_new_policies):
        if not win_new_policies.objectName():
            win_new_policies.setObjectName(u"win_new_policies")
        win_new_policies.resize(525, 663)
        self.gridLayout = QGridLayout(win_new_policies)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_6 = QGroupBox(win_new_policies)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_2 = QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox_6)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.btns = QDialogButtonBox(self.groupBox_6)
        self.btns.setObjectName(u"btns")
        self.btns.setOrientation(Qt.Orientation.Horizontal)
        self.btns.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)

        self.gridLayout_2.addWidget(self.btns, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_7 = QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFlat(False)
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.groupBox_7)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_8.addWidget(self.label_3)

        self.le_group = QComboBox(self.groupBox_7)
        self.le_group.setObjectName(u"le_group")

        self.horizontalLayout_8.addWidget(self.le_group)


        self.verticalLayout.addWidget(self.groupBox_7)

        self.groupBox = QGroupBox(self.groupBox_6)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.users_fullname_label = QLabel(self.groupBox)
        self.users_fullname_label.setObjectName(u"users_fullname_label")
        sizePolicy.setHeightForWidth(self.users_fullname_label.sizePolicy().hasHeightForWidth())
        self.users_fullname_label.setSizePolicy(sizePolicy)
        self.users_fullname_label.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.users_fullname_label)

        self.cb_access = QCheckBox(self.groupBox)
        self.cb_access.setObjectName(u"cb_access")
        self.cb_access.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cb_access.setChecked(True)

        self.horizontalLayout.addWidget(self.cb_access)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.groupBox_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFlat(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_ip = QLineEdit(self.groupBox_2)
        self.le_ip.setObjectName(u"le_ip")
        self.le_ip.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.le_ip.setDragEnabled(False)
        self.le_ip.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.le_ip)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_43 = QGroupBox(self.groupBox_6)
        self.groupBox_43.setObjectName(u"groupBox_43")
        self.horizontalLayout_56 = QHBoxLayout(self.groupBox_43)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_56 = QLabel(self.groupBox_43)
        self.label_56.setObjectName(u"label_56")
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        self.label_56.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_56.addWidget(self.label_56)

        self.le_pass = QLineEdit(self.groupBox_43)
        self.le_pass.setObjectName(u"le_pass")
        self.le_pass.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.horizontalLayout_56.addWidget(self.le_pass)


        self.verticalLayout.addWidget(self.groupBox_43)

        self.groupBox_8 = QGroupBox(self.groupBox_6)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_13 = QLabel(self.groupBox_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_7.addWidget(self.label_13)

        self.cb_usb_filter = QCheckBox(self.groupBox_8)
        self.cb_usb_filter.setObjectName(u"cb_usb_filter")
        self.cb_usb_filter.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cb_usb_filter.setChecked(True)

        self.horizontalLayout_7.addWidget(self.cb_usb_filter)


        self.verticalLayout.addWidget(self.groupBox_8)

        self.groupBox_5 = QGroupBox(self.groupBox_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_6.addWidget(self.label_10)

        self.cb_can_kick = QCheckBox(self.groupBox_5)
        self.cb_can_kick.setObjectName(u"cb_can_kick")
        self.cb_can_kick.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cb_can_kick.setCheckable(True)
        self.cb_can_kick.setChecked(False)

        self.horizontalLayout_6.addWidget(self.cb_can_kick)


        self.verticalLayout.addWidget(self.groupBox_5)

        self.groupBox_34 = QGroupBox(self.groupBox_6)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.horizontalLayout_43 = QHBoxLayout(self.groupBox_34)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_44 = QLabel(self.groupBox_34)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_43.addWidget(self.label_44)

        self.cb_kickable = QCheckBox(self.groupBox_34)
        self.cb_kickable.setObjectName(u"cb_kickable")
        self.cb_kickable.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cb_kickable.setChecked(True)

        self.horizontalLayout_43.addWidget(self.cb_kickable)


        self.verticalLayout.addWidget(self.groupBox_34)

        self.groupBox_42 = QGroupBox(self.groupBox_6)
        self.groupBox_42.setObjectName(u"groupBox_42")
        self.horizontalLayout_55 = QHBoxLayout(self.groupBox_42)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_55 = QLabel(self.groupBox_42)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_55.addWidget(self.label_55)

        self.le_until = QLineEdit(self.groupBox_42)
        self.le_until.setObjectName(u"le_until")

        self.horizontalLayout_55.addWidget(self.le_until)


        self.verticalLayout.addWidget(self.groupBox_42)

        self.gb_usb = QGroupBox(self.groupBox_6)
        self.gb_usb.setObjectName(u"gb_usb")
        self.gb_usb.setEnabled(False)
        self.horizontalLayout_9 = QHBoxLayout(self.gb_usb)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_14 = QLabel(self.gb_usb)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_9.addWidget(self.label_14)

        self.list_usb = QListWidget(self.gb_usb)
        self.list_usb.setObjectName(u"list_usb")
        self.list_usb.setTabKeyNavigation(True)
        self.list_usb.setProperty(u"isWrapping", False)
        self.list_usb.setResizeMode(QListView.ResizeMode.Fixed)
        self.list_usb.setViewMode(QListView.ViewMode.ListMode)
        self.list_usb.setModelColumn(0)
        self.list_usb.setSortingEnabled(True)

        self.horizontalLayout_9.addWidget(self.list_usb)


        self.verticalLayout.addWidget(self.gb_usb)

        self.groupBox_4 = QGroupBox(self.groupBox_6)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setEnabled(False)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_12 = QLabel(self.groupBox_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.label_12)

        self.cb_permit_login = QCheckBox(self.groupBox_4)
        self.cb_permit_login.setObjectName(u"cb_permit_login")
        self.cb_permit_login.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.cb_permit_login.setChecked(False)

        self.horizontalLayout_5.addWidget(self.cb_permit_login)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.groupBox_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setEnabled(False)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setEnabled(False)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.label_11)

        self.le_authmethod = QSpinBox(self.groupBox_3)
        self.le_authmethod.setObjectName(u"le_authmethod")
        self.le_authmethod.setMaximum(6)
        self.le_authmethod.setValue(4)

        self.horizontalLayout_4.addWidget(self.le_authmethod)


        self.verticalLayout.addWidget(self.groupBox_3)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox_6, 0, 0, 1, 1)

        QWidget.setTabOrder(self.le_group, self.cb_access)
        QWidget.setTabOrder(self.cb_access, self.le_ip)
        QWidget.setTabOrder(self.le_ip, self.le_pass)
        QWidget.setTabOrder(self.le_pass, self.cb_usb_filter)
        QWidget.setTabOrder(self.cb_usb_filter, self.cb_can_kick)
        QWidget.setTabOrder(self.cb_can_kick, self.cb_kickable)
        QWidget.setTabOrder(self.cb_kickable, self.le_until)
        QWidget.setTabOrder(self.le_until, self.list_usb)
        QWidget.setTabOrder(self.list_usb, self.cb_permit_login)
        QWidget.setTabOrder(self.cb_permit_login, self.le_authmethod)

        self.retranslateUi(win_new_policies)
        self.btns.accepted.connect(win_new_policies.accept)
        self.btns.rejected.connect(win_new_policies.reject)

        QMetaObject.connectSlotsByName(win_new_policies)
    # setupUi

    def retranslateUi(self, win_new_policies):
        win_new_policies.setWindowTitle(QCoreApplication.translate("win_new_policies", u"\u041d\u043e\u0432\u0430\u044f \u043f\u043e\u043b\u0438\u0442\u0438\u043a\u0430", None))
        self.groupBox_6.setTitle("")
        self.label.setText(QCoreApplication.translate("win_new_policies", u"* - \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("win_new_policies", u"\u0413\u0440\u0443\u043f\u043f\u0430*", None))
        self.le_group.setPlaceholderText(QCoreApplication.translate("win_new_policies", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0433\u0440\u0443\u043f\u043f\u0443...", None))
        self.users_fullname_label.setText(QCoreApplication.translate("win_new_policies", u"\u0414\u043e\u0441\u0442\u0443\u043f*", None))
        self.cb_access.setText("")
        self.label_2.setText(QCoreApplication.translate("win_new_policies", u"IP-\u0430\u0434\u0440\u0435\u0441\u0430*", None))
        self.le_ip.setText("")
        self.le_ip.setPlaceholderText(QCoreApplication.translate("win_new_policies", u"255.255.255.255", None))
        self.label_56.setText(QCoreApplication.translate("win_new_policies", u"\u041f\u0430\u0440\u043e\u043b\u044c*", None))
        self.le_pass.setText("")
        self.le_pass.setPlaceholderText(QCoreApplication.translate("win_new_policies", u"MyTopP@ssw0rd", None))
        self.label_13.setText(QCoreApplication.translate("win_new_policies", u"USB-\u0444\u0438\u043b\u044c\u0442\u0440*", None))
        self.cb_usb_filter.setText("")
        self.label_10.setText(QCoreApplication.translate("win_new_policies", u"Can kick", None))
        self.cb_can_kick.setText("")
        self.label_44.setText(QCoreApplication.translate("win_new_policies", u"Kickable", None))
        self.cb_kickable.setText("")
        self.label_55.setText(QCoreApplication.translate("win_new_policies", u"Until", None))
#if QT_CONFIG(tooltip)
        self.le_until.setToolTip(QCoreApplication.translate("win_new_policies", u"\u0415\u0441\u043b\u0438 \u043d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u043e - \u0434\u043e\u0441\u0442\u0443\u043f \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u0434\u0430\u043d \u0434\u043e 2024 \u0433\u043e\u0434\u0430\n"
"                                                        ", None))
#endif // QT_CONFIG(tooltip)
        self.le_until.setText("")
        self.le_until.setPlaceholderText(QCoreApplication.translate("win_new_policies", u"YYYY-MM-DD", None))
        self.label_14.setText(QCoreApplication.translate("win_new_policies", u"USB-\u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430", None))
        self.label_12.setText(QCoreApplication.translate("win_new_policies", u"Permit-Login", None))
        self.cb_permit_login.setText("")
        self.label_11.setText(QCoreApplication.translate("win_new_policies", u"Auth-Method", None))
    # retranslateUi

