import json
import os
from typing import TYPE_CHECKING

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QTreeWidgetItem, QMessageBox
)

from utils.utils import api_request

if TYPE_CHECKING:
    from main import MainWindow


def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )

def group_search(ui: 'MainWindow'):
    # clear current selection.
    ui.list_groups.setCurrentItem(None)

    query = ui.le_search_group.text()
    if not query:
        # Empty string, don't search.
        return

    matching_items = ui.list_groups.findItems(query, Qt.MatchFlag.MatchStartsWith, 0)
    #matching_items.extend(ui.list_groups.findItems(query, Qt.MatchFlag.MatchStartsWith, 1))

    if matching_items:

        item = matching_items[0]  # take the first
        ui.list_groups.setCurrentItem(item)
        #self.update_user_info(item.text(1))
    else:
        matching_items = ui.list_groups.findItems(query, Qt.MatchFlag.MatchContains, 0)
        #matching_items.extend(ui.list_groups.findItems(query, Qt.MatchFlag.MatchContains, 1))

        if matching_items:
            item = matching_items[0]  # take the first
            ui.list_groups.setCurrentItem(item)
            #self.update_user_info(item.text(1))
        #else:
        #    self.clear_user_info()

class Groups:
    def __init__(self, ui: 'MainWindow'):
        self.groups = []
        self.update_list(ui)
        self.render_groups(ui)
        ui.list_groups.itemSelectionChanged.connect(lambda: Groups.render_group(self, ui))
        ui.btn_group_restart.clicked.connect(lambda: self.restart_selected(ui))


    def update_list(self, ui):
        print("Updating list")
        response = api_request(uri="servers", method="GET", request="full")
        if response.status_code == 200:
            groups = json.loads(response.text)['servers']
            print(groups)

            for group in groups:
                new_group = Group(
                    id=group["id"],
                    ip=group["ip"],
                    ip_check=group["ip_check"],
                    login=group["login"],
                    name=group["name"],
                    tcp_port=group["tcp_port"],
                    password=group["password"]
                )
                self.groups.append(new_group)
        else:
            QMessageBox.critical(ui, "Ошибка",
                                 f"Ошибка: {response.status_code}"
                                 f"\n{response.text}")

    def render_groups(self, ui: 'MainWindow'):
        ui.list_groups.clear()
        items = []
        for group in self.groups:
            item = QTreeWidgetItem([group.name])
            items.append(item)

        ui.list_groups.insertTopLevelItems(0, items)

    def render_group(self, ui: 'MainWindow'):
        ui.le_group_name.clear()
        ui.le_group_port.clear()
        ui.le_group_login.clear()
        ui.le_group_password.clear()
        #group_selection = ui.list_groups.currentItem()
        group = self.get_group(ui.list_groups.currentItem().text(0))
        ui.le_group_name.setText(group.name)
        ui.le_group_port.setText(str(group.tcp_port))
        ui.le_group_login.setText(group.login)
        ui.le_group_password.setText(group.password)

    def restart_selected(self, ui: 'MainWindow'):
        dialog = QMessageBox.question(ui, 'Перезагрузка группы',
                                   'Вы уверены что хотите перезагрузить группу?',
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                   QMessageBox.StandardButton.Yes)

        if dialog == QMessageBox.StandardButton.Yes:
            group = self.get_group(ui.list_groups.currentItem().text(0))
            response = group.restart()

            if response.status_code == 200:
                QMessageBox.information(ui, 'Перезагрузка группы',
                                        f'Запрос на перезагрузку отправлен.')
            else:
                QMessageBox.critical(ui, 'Перезагрузка группы',
                                     f"Ошибка: {response.status_code}"
                                     f"\n{response.text}")



    def get_group(self, group_name):
        for group in self.groups:
            if group.name == group_name:
                return group


class Group:
    def __init__(self, id, ip, ip_check, login, name, tcp_port, password):
        self.id = id
        self.ip = ip
        self.ip_check = ip_check
        self.login = login
        self.name = name
        self.tcp_port = tcp_port
        self.password = password

    def restart(self):
        response = api_request(uri=f"servers/{self.name}/restart", request="full")
        return response