from typing import List

from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMessageBox, QTreeWidgetItem

from ui.ui_select_user import Ui_SelectUser
from utils.utils import filter_items, resource_path


class SelectUser(QDialog):
    def __init__(self, users: List):
        super().__init__()

        # Создаем экземпляр класса Ui_win_new_policies
        self.ui = Ui_SelectUser()
        icon = QtGui.QIcon(resource_path("res/icon.png"))
        self.setWindowIcon(icon)
        # Инициализируем интерфейс дополнительного окна
        self.ui.setupUi(self)
        self.ui.treeWidget.setColumnWidth(0, 250)
        self.ui.treeWidget.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        self.ui.lineEdit.textChanged.connect(lambda: filter_items(self.ui.treeWidget, self.ui.lineEdit.text()))

        for user in users:
            item = QTreeWidgetItem([ user[ 'cn' ], user[ 'name' ] ])
            self.ui.treeWidget.addTopLevelItem(item)

    def accept(self):
        # Получаем введенные данные
        self.selected = self.ui.treeWidget.selectedItems()
        if not self.selected:
            QMessageBox.warning(self, "Ошибка", "Выберите хотя бы одного пользователя!")
            return

        super().accept()
