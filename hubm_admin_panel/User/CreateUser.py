import os
from re import match as re_match

from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QDialog

from ui.ui_new_user import Ui_win_new_user


def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )


class CreateUser(QDialog):
    def __init__(self):
        super().__init__()

        # Создаем экземпляр класса Ui_win_new_policies
        self.ui = Ui_win_new_user()
        icon = QtGui.QIcon(resource_path("res/icon.png"))
        self.setWindowIcon(icon)
        # Инициализируем интерфейс дополнительного окна
        self.ui.setupUi(self)

        # self.save()
        self.ui.le_fullname.textChanged.connect(self.validate)
        self.ui.le_name.textChanged.connect(self.validate)
        self.ui.le_ip.textChanged.connect(self.validate)
        self.ui.le_pass.textChanged.connect(self.validate)
        self.ui.le_email.textChanged.connect(self.validate)
        self.ui.le_comment.textChanged.connect(self.validate)
        self.ui.cb_active.checkStateChanged.connect(self.validate)

        self.ui.btns.button(QtWidgets.QDialogButtonBox.StandardButton.Save).setEnabled(False)

    def validate(self):
        fullname = self.ui.le_fullname.text()
        name = self.ui.le_name.text()
        ip = self.ui.le_ip.text()
        password = self.ui.le_pass.text()

        fullname_valid = bool(fullname.strip())
        name_valid = bool(name.strip())
        ip_valid = re_match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
                            ip)
        password_valid = bool(password.strip())

        if fullname_valid and name_valid and ip_valid and password_valid:
            self.ui.btns.button(QtWidgets.QDialogButtonBox.StandardButton.Save).setEnabled(True)
        else:
            self.ui.btns.button(QtWidgets.QDialogButtonBox.StandardButton.Save).setEnabled(False)

    def save(self):
        values = {
            "cn": self.ui.le_fullname.text() if self.ui.le_fullname.text().strip() else None,
            "name": self.ui.le_name.text() if self.ui.le_name.text().strip() else None,
            "ip": self.ui.le_ip.text() if self.ui.le_ip.text().strip() else None,
            "password": self.ui.le_pass.text() if self.ui.le_pass.text().strip() else None,
            "email": self.ui.le_email.text() if self.ui.le_email.text().strip() else None,
            "comment": self.ui.le_comment.text() if self.ui.le_comment.text().strip() else None,
            "active": self.ui.cb_active.isChecked(),

        }
        return values
