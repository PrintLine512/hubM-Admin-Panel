# Form implementation generated from reading ui file 'C:\Users\mv.alekseev\Documents\projects\hubM Admin Panel\ui\ui_new_policies.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_win_new_policies(object):
    def setupUi(self, win_new_policies):
        win_new_policies.setObjectName("win_new_policies")
        win_new_policies.resize(400, 472)
        self.gridLayout = QtWidgets.QGridLayout(win_new_policies)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_6 = QtWidgets.QGroupBox(parent=win_new_policies)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_7 = QtWidgets.QGroupBox(parent=self.groupBox_6)
        self.groupBox_7.setFlat(False)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(150, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.le_group = QtWidgets.QComboBox(parent=self.groupBox_7)
        self.le_group.setObjectName("le_group")
        self.horizontalLayout_8.addWidget(self.le_group)
        self.verticalLayout.addWidget(self.groupBox_7)
        self.groupBox = QtWidgets.QGroupBox(parent=self.groupBox_6)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.users_fullname_label = QtWidgets.QLabel(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.users_fullname_label.sizePolicy().hasHeightForWidth())
        self.users_fullname_label.setSizePolicy(sizePolicy)
        self.users_fullname_label.setMinimumSize(QtCore.QSize(150, 0))
        self.users_fullname_label.setObjectName("users_fullname_label")
        self.horizontalLayout.addWidget(self.users_fullname_label)
        self.cb_access = QtWidgets.QCheckBox(parent=self.groupBox)
        self.cb_access.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.cb_access.setText("")
        self.cb_access.setChecked(True)
        self.cb_access.setObjectName("cb_access")
        self.horizontalLayout.addWidget(self.cb_access)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.groupBox_6)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(150, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.le_ip = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.le_ip.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.le_ip.setText("")
        self.le_ip.setDragEnabled(False)
        self.le_ip.setReadOnly(False)
        self.le_ip.setObjectName("le_ip")
        self.horizontalLayout_2.addWidget(self.le_ip)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.groupBox_6)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(150, 0))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.le_authmethod = QtWidgets.QSpinBox(parent=self.groupBox_3)
        self.le_authmethod.setMaximum(6)
        self.le_authmethod.setProperty("value", 4)
        self.le_authmethod.setObjectName("le_authmethod")
        self.horizontalLayout_4.addWidget(self.le_authmethod)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_43 = QtWidgets.QGroupBox(parent=self.groupBox_6)
        self.groupBox_43.setObjectName("groupBox_43")
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout(self.groupBox_43)
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.label_56 = QtWidgets.QLabel(parent=self.groupBox_43)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        self.label_56.setMinimumSize(QtCore.QSize(150, 0))
        self.label_56.setObjectName("label_56")
        self.horizontalLayout_56.addWidget(self.label_56)
        self.le_pass = QtWidgets.QLineEdit(parent=self.groupBox_43)
        self.le_pass.setText("")
        self.le_pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.le_pass.setObjectName("le_pass")
        self.horizontalLayout_56.addWidget(self.le_pass)
        self.verticalLayout.addWidget(self.groupBox_43)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.groupBox_6)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_12.setMinimumSize(QtCore.QSize(150, 0))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.cb_permit_login = QtWidgets.QCheckBox(parent=self.groupBox_4)
        self.cb_permit_login.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.cb_permit_login.setText("")
        self.cb_permit_login.setChecked(False)
        self.cb_permit_login.setObjectName("cb_permit_login")
        self.horizontalLayout_5.addWidget(self.cb_permit_login)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.groupBox_6)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_10.setMinimumSize(QtCore.QSize(150, 0))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.cb_can_kick = QtWidgets.QCheckBox(parent=self.groupBox_5)
        self.cb_can_kick.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.cb_can_kick.setText("")
        self.cb_can_kick.setCheckable(True)
        self.cb_can_kick.setChecked(False)
        self.cb_can_kick.setObjectName("cb_can_kick")
        self.horizontalLayout_6.addWidget(self.cb_can_kick)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.groupBox_34 = QtWidgets.QGroupBox(parent=self.groupBox_6)
        self.groupBox_34.setObjectName("groupBox_34")
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout(self.groupBox_34)
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.label_44 = QtWidgets.QLabel(parent=self.groupBox_34)
        self.label_44.setMinimumSize(QtCore.QSize(150, 0))
        self.label_44.setObjectName("label_44")
        self.horizontalLayout_43.addWidget(self.label_44)
        self.cb_kickable = QtWidgets.QCheckBox(parent=self.groupBox_34)
        self.cb_kickable.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.cb_kickable.setText("")
        self.cb_kickable.setChecked(True)
        self.cb_kickable.setObjectName("cb_kickable")
        self.horizontalLayout_43.addWidget(self.cb_kickable)
        self.verticalLayout.addWidget(self.groupBox_34)
        self.groupBox_42 = QtWidgets.QGroupBox(parent=self.groupBox_6)
        self.groupBox_42.setObjectName("groupBox_42")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout(self.groupBox_42)
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.label_55 = QtWidgets.QLabel(parent=self.groupBox_42)
        self.label_55.setMinimumSize(QtCore.QSize(150, 0))
        self.label_55.setObjectName("label_55")
        self.horizontalLayout_55.addWidget(self.label_55)
        self.le_until = QtWidgets.QLineEdit(parent=self.groupBox_42)
        self.le_until.setText("")
        self.le_until.setObjectName("le_until")
        self.horizontalLayout_55.addWidget(self.le_until)
        self.verticalLayout.addWidget(self.groupBox_42)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.btns = QtWidgets.QDialogButtonBox(parent=self.groupBox_6)
        self.btns.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.btns.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Save)
        self.btns.setObjectName("btns")
        self.gridLayout_2.addWidget(self.btns, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.retranslateUi(win_new_policies)
        self.btns.accepted.connect(win_new_policies.accept) # type: ignore
        self.btns.rejected.connect(win_new_policies.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(win_new_policies)

    def retranslateUi(self, win_new_policies):
        _translate = QtCore.QCoreApplication.translate
        win_new_policies.setWindowTitle(_translate("win_new_policies", "Новая политика"))
        self.label_3.setText(_translate("win_new_policies", "Группа*"))
        self.le_group.setPlaceholderText(_translate("win_new_policies", "Выберите группу..."))
        self.users_fullname_label.setText(_translate("win_new_policies", "Доступ"))
        self.label_2.setText(_translate("win_new_policies", "IP-адреса*"))
        self.le_ip.setPlaceholderText(_translate("win_new_policies", "255.255.255.255"))
        self.label_11.setText(_translate("win_new_policies", "Auth-Method"))
        self.label_56.setText(_translate("win_new_policies", "Пароль*"))
        self.le_pass.setPlaceholderText(_translate("win_new_policies", "MyTopP@ssw0rd"))
        self.label_12.setText(_translate("win_new_policies", "Permit-Login"))
        self.label_10.setText(_translate("win_new_policies", "Can kick"))
        self.label_44.setText(_translate("win_new_policies", "Kickable"))
        self.label_55.setText(_translate("win_new_policies", "Until"))
        self.le_until.setToolTip(_translate("win_new_policies", "Если не указано - доступ будет выдан до 2024 года"))
        self.le_until.setPlaceholderText(_translate("win_new_policies", "YYYY-MM-DD"))
        self.label.setText(_translate("win_new_policies", "* - обязательное значение"))