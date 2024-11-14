import json
import os
from typing import TYPE_CHECKING, Literal

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QTreeWidgetItem, QMessageBox
)

from ui import launch_dialogs
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
    # matching_items.extend(ui.list_groups.findItems(query, Qt.MatchFlag.MatchStartsWith, 1))

    if matching_items:

        item = matching_items[ 0 ]  # take the first
        ui.list_groups.setCurrentItem(item)
        # self.update_user_info(item.text(1))
    else:
        matching_items = ui.list_groups.findItems(query, Qt.MatchFlag.MatchContains, 0)
        # matching_items.extend(ui.list_groups.findItems(query, Qt.MatchFlag.MatchContains, 1))

        if matching_items:
            item = matching_items[ 0 ]  # take the first
            ui.list_groups.setCurrentItem(item)
            # self.update_user_info(item.text(1))
        # else:
        #    self.clear_user_info()


class Groups:
    def __init__(self, ui: 'MainWindow'):
        self.groups = [ ]
        self.ui = ui
        self.current_group = None
        # self.update_list(ui)
        # self.render_groups(ui)
        ui.list_group_usb.setColumnWidth(0, 250)
        ui.list_groups.currentItemChanged.connect(lambda selected: Groups.render_group(self, selected))
        ui.btn_group_restart.clicked.connect(lambda: self.action("restart"))
        ui.btn_group_start.clicked.connect(lambda: self.action("start"))
        ui.btn_group_stop.clicked.connect(lambda: self.action("stop"))
        ui.btn_group_usb_add.clicked.connect(self.usb_add)
        ui.btn_group_usb_remove.clicked.connect(self.usb_remove)
        ui.btn_refresh_groups_tab.clicked.connect(self.refresh)
        ui.btn_group_save.clicked.connect(self.save)

    def __del__(self):
        print(f"{__class__} del")


    def sent_params(self, data):
        response = api_request(f"servers/{self.current_group.name}", {}, json.dumps(data), "PUT", "full")
        return response

    def usb_add(self):
        if self.current_group is None:
            QMessageBox.warning(self.ui, 'Управление группой',
                                f'Сначала выберите группу!')
            return
        response = api_request(uri=f"usb_ports/free", request="full")
        usb_ports = [ {'name': item[ 'name' ], 'virtual_port': item[ 'virtual_port' ]} for item in json.loads(response.text) ]

        dialog = launch_dialogs.SelectPort(usb_ports)  # Открываем диалог добавления сервера
        if dialog.exec():  # exec() вернет True, если диалог завершен успешно
            for item in dialog.selected:
                usb_port = QTreeWidgetItem([item.text(0), item.text(1)])
                self.ui.list_group_usb.addTopLevelItem(usb_port)

        else:
            return

    def usb_remove(self):
        selected = self.ui.list_group_usb.selectedItems()
        if selected:
            for item in selected:
                index = self.ui.list_group_usb.indexOfTopLevelItem(item)
                if index != -1:
                    self.ui.list_group_usb.takeTopLevelItem(index)

        else:
            QMessageBox.warning(self.ui, 'Управление группой',
                                f'Сначала выберите USB-порт!')

    def save(self):
        if self.current_group is None:
            QMessageBox.warning(self.ui, 'Управление группой',
                                f'Сначала выберите группу!')
            return
        dialog = QMessageBox.question(self.ui, 'Управление группой',
                                      f'Вы уверены что хотите сохранить изменения?\n'
                                      f'Группа будет перезапущена.',
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                      QMessageBox.StandardButton.Yes)
        if dialog == QMessageBox.StandardButton.No:
            return

        dict_server = {
            "name": self.ui.le_group_name.text(),
            "ip": self.ui.le_group_ip.text(),
            "password": self.ui.le_group_password.text(),
            "login": self.ui.le_group_login.text(),
            "tcp_port": self.ui.le_group_port.text(),
            "usb_list": self.get_ui_usb()
        }
        response = (self.sent_params(dict_server))
        if response.status_code == 200:
            QMessageBox.information(self.ui, "Информация",
                                    f"Группа {self.ui.le_user_name.text()} успешно изменена!")
        else:
            QMessageBox.critical(self.ui, "Ошибка",
                                 f"Группа не изменена или  изменена с ошибками!\nОшибка: {response.status_code}"
                                 f"\n {response.text}")

        old_group = self.current_group.name

        self.refresh()
        print(self.current_group.name)
        match = self.ui.list_groups.findItems(old_group, Qt.MatchFlag.MatchExactly, 0)
        if match:
            print(match[0].text(0))
            self.ui.list_groups.setCurrentItem(match[0])


    def refresh(self):
        self.update_list()
        self.render_groups()

    def update_list(self):
        print("Updating list")
        response = api_request(uri="servers", method="GET", request="full")
        if response.status_code == 200:
            groups = json.loads(response.text)[ 'servers' ]
            self.groups = [ ]
            for group in groups:
                new_group = Group(
                    id=group[ "id" ],
                    ip=group[ "ip" ],
                    ip_check=group[ "ip_check" ],
                    login=group[ "login" ],
                    name=group[ "name" ],
                    tcp_port=group[ "tcp_port" ],
                    password=group[ "password" ],
                    usb_list=group["usb_list"]
                )
                self.groups.append(new_group)
        else:
            QMessageBox.critical(self.ui, "Ошибка",
                                 f"Ошибка: {response.status_code}"
                                 f"\n{response.text}")

    def render_groups(self):
        print("Render groups")
        self.ui.list_groups.clear()

        items = [ ]
        for group in self.groups:
            item = QTreeWidgetItem([ group.name, str(group.tcp_port) ])
            items.append(item)

        self.ui.list_groups.insertTopLevelItems(0, items)

    def get_ui_usb(self):
        usb_list = []
        if not self.ui.list_group_usb.topLevelItemCount():
            return
        for index in range(self.ui.list_group_usb.topLevelItemCount()):
            usb = self.ui.list_group_usb.topLevelItem(index)
            usb_list.append(usb.text(1))
        return usb_list


    def render_group(self, selected):
        self.ui.le_group_name.clear()
        self.ui.le_group_port.clear()
        self.ui.le_group_login.clear()
        self.ui.le_group_password.clear()
        self.ui.le_group_ip.clear()
        self.ui.list_group_usb.clear()
        self.current_group = self.get_group(selected.text(0))
        self.ui.le_group_name.setText(self.current_group.name)
        self.ui.le_group_port.setText(str(self.current_group.tcp_port))
        self.ui.le_group_login.setText(self.current_group.login)
        self.ui.le_group_password.setText(self.current_group.password)
        self.ui.le_group_ip.setText(self.current_group.ip)

        items = [ ]
        for usb in self.current_group.usb_list:
            item = QTreeWidgetItem([ usb["name"], usb["virtual_port"] ])
            items.append(item)

        self.ui.list_group_usb.insertTopLevelItems(0, items)


    def action(self, action: Literal[ "start", "stop", "restart" ]):
        if self.current_group is None:
            QMessageBox.warning(self.ui, 'Управление группой',
                                f'Сначала выберите группу!')
            return
        dialog = QMessageBox.question(self.ui, 'Управление группой',
                                      f'Вы уверены что хотите совершить это действие - {action}?',
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                      QMessageBox.StandardButton.Yes)

        if dialog == QMessageBox.StandardButton.Yes:

            group = self.get_group(self.ui.list_groups.currentItem().text(0))
            response = group.action(action)

            if response.status_code == 200:
                QMessageBox.information(self.ui, 'Управление группой',
                                        f'Запрос на действие успешно отправлен.')
            elif response.status_code == 500:
                QMessageBox.warning(self.ui, 'Управление группой',
                                    f"Ошибка: некорректное состояние!\n"
                                    f"Группа {group.name} уже включена или выключена.")
            else:
                QMessageBox.critical(self.ui, 'Управление группой',
                                     f"Ошибка: {response.status_code}"
                                     f"\n{response.text}")

    def get_group(self, group_name):
        for group in self.groups:
            if group.name == group_name:
                return group


class Group:
    def __init__(self, id, ip, ip_check, login, name, tcp_port, password, usb_list):
        self.id = id
        self.ip = ip
        self.ip_check = ip_check
        self.login = login
        self.name = name
        self.tcp_port = tcp_port
        self.password = password
        self.usb_list = usb_list

    def action(self, action):
        response = api_request(uri=f"servers/{self.name}/{action}", request="full")
        return response
