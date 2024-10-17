# Form implementation generated from reading ui file 'C:\Users\mv.alekseev\Documents\projects\hubM Admin Panel\hubm_admin_panel\ui\ui_launch.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Launch(object):
    def setupUi(self, Launch):
        Launch.setObjectName("Launch")
        Launch.resize(742, 218)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/icon_connect"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Launch.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=Launch)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.le_address = QtWidgets.QLineEdit(parent=self.frame)
        self.le_address.setObjectName("le_address")
        self.horizontalLayout_3.addWidget(self.le_address)
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.le_tcp_port = QtWidgets.QLineEdit(parent=self.frame)
        self.le_tcp_port.setMaximumSize(QtCore.QSize(50, 16777215))
        self.le_tcp_port.setObjectName("le_tcp_port")
        self.horizontalLayout_3.addWidget(self.le_tcp_port)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(parent=self.frame)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.le_token = QtWidgets.QLineEdit(parent=self.frame)
        self.le_token.setText("")
        self.le_token.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.le_token.setObjectName("le_token")
        self.horizontalLayout_4.addWidget(self.le_token)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.btn_connect = QtWidgets.QPushButton(parent=self.frame)
        self.btn_connect.setCheckable(False)
        self.btn_connect.setAutoDefault(True)
        self.btn_connect.setDefault(True)
        self.btn_connect.setObjectName("btn_connect")
        self.verticalLayout_5.addWidget(self.btn_connect)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        Launch.setCentralWidget(self.centralwidget)

        self.retranslateUi(Launch)
        QtCore.QMetaObject.connectSlotsByName(Launch)
        Launch.setTabOrder(self.le_address, self.le_tcp_port)
        Launch.setTabOrder(self.le_tcp_port, self.le_token)
        Launch.setTabOrder(self.le_token, self.btn_connect)

    def retranslateUi(self, Launch):
        _translate = QtCore.QCoreApplication.translate
        Launch.setWindowTitle(_translate("Launch", "hubM Admin Panel Connect"))
        self.label_5.setText(_translate("Launch", "<html><head/><body><p>Добро пожаловать!<br/>Введите данные для подключения к серверу или используйте последние сохраненные.</p></body></html>"))
        self.label_6.setText(_translate("Launch", "Адрес:"))
        self.le_address.setPlaceholderText(_translate("Launch", "Hostname или IP"))
        self.label_7.setText(_translate("Launch", "Порт:"))
        self.le_tcp_port.setText(_translate("Launch", "5000"))
        self.label_8.setText(_translate("Launch", "Токен:"))
        self.le_token.setPlaceholderText(_translate("Launch", "Ваш токен"))
        self.btn_connect.setText(_translate("Launch", "Подключиться"))
