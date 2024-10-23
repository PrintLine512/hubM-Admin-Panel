import os
from re import match as re_match

from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QDialog

from ui.ui_new_policies import Ui_win_new_policies


def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )

class CreatePolicies(QDialog):
    def __init__(self, default_ip):
        super().__init__()
        # Создаем экземпляр класса Ui_win_new_policies
        self.ui = Ui_win_new_policies()
        icon = QtGui.QIcon(resource_path("res/icon.png"))
        self.setWindowIcon(icon)
        # Инициализируем интерфейс дополнительного окна
        self.ui.setupUi(self)
        self.save()
        if default_ip:
            self.ui.le_ip.setText(default_ip)
        self.ui.le_ip.textChanged.connect(self.validate)
        self.ui.le_group.currentTextChanged.connect(self.validate)
        self.ui.le_until.textChanged.connect(self.validate)
        self.ui.le_pass.textChanged.connect(self.validate)

        self.ui.btns.button(QtWidgets.QDialogButtonBox.StandardButton.Save).setEnabled(False)

    def validate(self):
        ip = self.ui.le_ip.text()
        until = self.ui.le_until.text()
        group = self.ui.le_group.currentText()
        password = self.ui.le_pass.text()

        ip_valid = re_match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip)
        until_valid = re_match(r"\d{4}-\d{2}-\d{2}", until) if until else True
        group_valid = bool(group.strip())
        password_valid = bool(password.strip())

        if ip_valid and until_valid and group_valid and password_valid:
            self.ui.btns.button(QtWidgets.QDialogButtonBox.StandardButton.Save).setEnabled(True)
        else:
            self.ui.btns.button(QtWidgets.QDialogButtonBox.StandardButton.Save).setEnabled(False)

    def validate1(self):
        # Получаем значения из полей ввода
        ip = self.ui.le_ip.text()
        until = self.ui.le_until.text()
        group = self.ui.le_group.currentText()

        if re_match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip):
            if until == "" or re_match(r"\d{4}-\d{2}-\d{2}", until):
                if group.strip():
                    self.ui.btns.button(QtWidgets.QDialogButtonBox.StandardButton.Save).setEnabled(True)
                else:
                    self.ui.btns.button(QtWidgets.QDialogButtonBox.StandardButton.Save).setEnabled(False)
            else:
                self.ui.btns.button(QtWidgets.QDialogButtonBox.StandardButton.Save).setEnabled(False)

        else:
            self.ui.btns.button(QtWidgets.QDialogButtonBox.StandardButton.Save).setEnabled(False)

    def save(self):
        values = {
            "group": self.ui.le_group.currentText() if self.ui.le_group.currentText().strip() else None,
            "access": self.ui.cb_access.isChecked(),
            "ip": self.ui.le_ip.text() if self.ui.le_ip.text().strip() else None,
            "auth_method": self.ui.le_authmethod.text() if self.ui.le_authmethod.text().strip() else None,
            "password": self.ui.le_pass.text() if self.ui.le_pass.text().strip() else None,
            "permit_login": self.ui.cb_permit_login.isChecked(),
            "can_kick": self.ui.cb_can_kick.isChecked(),
            "kickable": self.ui.cb_kickable.isChecked(),
            "until": self.ui.le_until.text() if self.ui.le_until.text().strip() else None
        }
        return values

