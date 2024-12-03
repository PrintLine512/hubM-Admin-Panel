import json
import os
from typing import TYPE_CHECKING, Literal

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QTreeWidgetItem, QMessageBox, QSizePolicy
)

from ui import launch_dialogs
from ui.main_additional import CheckLabel
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


class Groups:
    def __init__(self, ui: 'MainWindow'):
        self.groups = [ ]
        self.ui = ui
        self.current_group = None

        self.lb_group_active = CheckLabel("Запущена", "Остановлена", False)
        self.lb_group_active.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.ui.frame_group_status.addWidget(self.lb_group_active)

        # self.update_list(ui)
        # self.render_groups(ui)
        self.ui.list_group_usb.setColumnWidth(0, 250)
        self.ui.list_groups.currentItemChanged.connect(lambda selected: self.render_group(selected))
        self.ui.btn_group_restart.clicked.connect(lambda: self.action("restart"))
        self.ui.btn_group_start.clicked.connect(lambda: self.action("start"))
        self.ui.btn_group_stop.clicked.connect(lambda: self.action("stop"))
        self.ui.btn_group_usb_add.clicked.connect(self.usb_add)
        self.ui.btn_group_usb_remove.clicked.connect(self.usb_remove)
        self.ui.btn_refresh_groups_tab.clicked.connect(self.refresh)
        self.ui.btn_group_save.clicked.connect(self.save)

        self.ui.list_group_usb.sortByColumn(0, Qt.SortOrder.AscendingOrder)

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
        usb_ports = [ {'name': item[ 'name' ], 'virtual_port': item[ 'virtual_port' ]} for item in
                      json.loads(response.text) ]

        dialog = launch_dialogs.SelectPort(usb_ports)  # Открываем диалог добавления сервера
        if dialog.exec():  # exec() вернет True, если диалог завершен успешно
            for item in dialog.selected:
                usb_port = QTreeWidgetItem([ item.text(0), item.text(1) ])
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
                                f'Выберите хотя бы один USB-порт!')

    def save(self):
        if self.current_group is None:
            QMessageBox.warning(self.ui, 'Управление группой',
                                f'Сначала выберите группу!')
            return
        if self.current_group.active:
            QMessageBox.warning(self.ui, 'Управление группой',
                                f'Группа должна быть остановлена!')
            return
        dialog = QMessageBox.question(self.ui, 'Управление группой',
                                      f'Вы уверены что хотите сохранить изменения?\n',
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
                                    f"Группа {self.ui.le_group_name.text()} успешно изменена!")
        else:
            QMessageBox.critical(self.ui, "Ошибка",
                                 f"Группа не изменена или изменена с ошибками!\nОшибка: {response.status_code}"
                                 f"\n {response.text}")

        self.refresh()

    def refresh(self):
        old_group = self.current_group.name if self.current_group else None
        self.update_list()
        self.render_groups()
        if old_group:
            match = self.ui.list_groups.findItems(old_group, Qt.MatchFlag.MatchExactly, 0)
            if match:
                self.ui.list_groups.setCurrentItem(match[ 0 ])

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
                    usb_list=group[ "usb_list" ],
                    active=group[ "active" ]
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
        usb_list = [ ]
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
        self.lb_group_active.setState(True if self.current_group.active else False)

        items = [ ]
        for usb in self.current_group.usb_list:
            item = QTreeWidgetItem([ usb[ "name" ], usb[ "virtual_port" ] ])
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

            group = self.current_group
            response = group.action(action)

            if response.status_code == 200:
                QMessageBox.information(self.ui, 'Управление группой',
                                        f'Запрос на действие успешно отправлен.')
            elif response.status_code == 500:
                QMessageBox.warning(self.ui, 'Управление группой',
                                    f"Ошибка: некорректное состояние!\n"
                                    f"Группа {group.name} уже находится в этом состояние.")
            else:
                QMessageBox.critical(self.ui, 'Управление группой',
                                     f"Ошибка: {response.status_code}"
                                     f"\n{response.text}")
        self.refresh()

    def get_group(self, group_name):
        for group in self.groups:
            if group.name == group_name:
                return group


class Group:
    def __init__(self, id, ip, ip_check, login, name, tcp_port, password, usb_list, active):
        self.id = id
        self.ip = ip
        self.ip_check = ip_check
        self.login = login
        self.name = name
        self.tcp_port = tcp_port
        self.password = password
        self.usb_list = usb_list
        self.active = active

    def action(self, action):
        response = api_request(uri=f"servers/{self.name}/{action}", request="full")
        return response
