import os

from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import QDialog

from ui.ui_user_export import Ui_win_user_export


def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )


class UserExport(QDialog):
    def __init__(self):
        super().__init__()

        # Создаем экземпляр класса Ui_win_new_policies
        self.ui = Ui_win_user_export()
        icon = QtGui.QIcon(resource_path("res/icon.png"))
        self.setWindowIcon(icon)
        # Инициализируем интерфейс дополнительного окна
        self.ui.setupUi(self)

        # self.ui.btns.button(QtWidgets.QDialogButtonBox.StandardButton.Save).setEnabled(False)
        # Здесь можно добавить дополнительную логику и функциональность вашего дополнительного окна

        self.ui.cb_enable_usb_policies.checkStateChanged.connect(self.validate)
        self.ui.cb_enable_group_policies.checkStateChanged.connect(self.validate)

    def validate(self):
        if self.ui.cb_enable_group_policies.isChecked():
            self.ui.cb_enable_usb_policies.setEnabled(True)
        else:
            self.ui.cb_enable_usb_policies.setEnabled(False)
            self.ui.cb_enable_usb_policies.setCheckState(QtCore.Qt.CheckState.Unchecked)
