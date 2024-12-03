import json
import os
from typing import TYPE_CHECKING

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox, QTreeWidgetItem, QSizePolicy

from ui.main_additional import CheckLabel
from utils.utils import api_request
from .dialogs import SelectUser


def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )


if TYPE_CHECKING:
    from main import MainWindow


class UsbList:
    def __init__(self, ui: 'MainWindow'):
        self.usb_list = [ ]
        self.ui = ui
        self.current_usb = None

        self.lb_usb_active = CheckLabel("Включен", "Выключен", False)
        self.lb_usb_active.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.ui.frame_usb_status.addWidget(self.lb_usb_active)

        self.ui.list_usb.setColumnWidth(0, 150)
        self.ui.list_usb.setColumnWidth(1, 50)
        self.ui.list_usb_access.setColumnWidth(0, 200)
        self.ui.list_usb.currentItemChanged.connect(lambda selected: self.render_usb(selected))

        self.ui.btn_usb_permission_add.clicked.connect(self.usb_permission_add)
        self.ui.btn_usb_permission_remove.clicked.connect(self.usb_permission_remove)
        self.ui.btn_usb_save.clicked.connect(self.usb_save)
        self.ui.btn_usb_group_clear.clicked.connect(lambda: self.ui.combo_usb_group.setCurrentText(None))
        self.ui.btn_usb_restart.clicked.connect(lambda: self.usb_action("restart"))
        self.ui.btn_usb_start.clicked.connect(lambda: self.usb_action("on"))
        self.ui.btn_usb_stop.clicked.connect(lambda: self.usb_action("off"))
        self.ui.btn_refresh_usb_ports_tab.clicked.connect(self.refresh)

        self.ui.list_usb.sortByColumn(1, Qt.SortOrder.AscendingOrder)

    def refresh(self):
        old_usb = self.current_usb.virtual_port if self.current_usb else None
        self.update_list()
        self.render_usb_list()
        if old_usb:
            match = self.ui.list_usb.findItems(old_usb, Qt.MatchFlag.MatchExactly, 1)
            if match:
                self.current_usb = self.get_usb(old_usb)
                self.ui.list_usb.setCurrentItem(match[ 0 ])

    def update_list(self):
        self.ui.combo_usb_group.clear()
        print("Updating list")
        response = api_request(uri="usb_ports", method="GET", request="full")
        if response.status_code == 200:
            usb_list = json.loads(response.text)
            self.usb_list = [ ]
            for usb in usb_list:
                new_usb = Usb(
                    id=usb[ "id" ],
                    active=usb[ "active" ],
                    server_id=usb[ "server_name" ],
                    server_name=usb[ "server_name" ],
                    virtual_port=usb[ "virtual_port" ],
                    bus=usb[ "bus" ],
                    name=usb[ "name" ],
                    users=usb[ "users" ],
                    device=usb[ 'device' ]
                )
                self.usb_list.append(new_usb)

            response = api_request(uri="servers", method="GET", request="full")
            if response.status_code == 200:
                groups_raw = json.loads(response.text)[ 'servers' ]
                groups = [ ]
                for group in groups_raw:
                    groups.append(group[ "name" ])
                groups.append("")
                self.ui.combo_usb_group.addItems(groups)
            else:
                QMessageBox.critical(self.ui, "Ошибка",
                                     f"Ошибка: {response.status_code}"
                                     f"\n{response.text}")
        else:
            QMessageBox.critical(self.ui, "Ошибка",
                                 f"Ошибка: {response.status_code}"
                                 f"\n{response.text}")

    def render_usb_list(self):
        print("Render groups")
        self.ui.list_usb.clear()

        items = [ ]
        for usb in self.usb_list:
            item = QTreeWidgetItem([ usb.name, usb.virtual_port, usb.server_name ])
            items.append(item)

        self.ui.list_usb.insertTopLevelItems(0, items)

    def render_usb(self, selected):
        self.ui.list_usb_access.clear()

        if selected:
            self.current_usb = self.get_usb(selected.text(1))

        self.ui.le_usb_name.setText(self.current_usb.name)
        self.ui.lb_usb_device.setText(self.current_usb.device)
        self.ui.le_usb_virtual_port.setText(str(self.current_usb.virtual_port))
        self.ui.le_usb_bus.setText(str(self.current_usb.bus))
        # self.ui.cb_usb_active.setCheckState(Qt.CheckState.Checked if self.current_usb.active else Qt.CheckState.Unchecked)
        self.lb_usb_active.setState(True if self.current_usb.active else False)
        self.ui.combo_usb_group.setCurrentText(self.current_usb.server_name)
        usb_access_items = [ ]
        for user in self.current_usb.users:
            item = QTreeWidgetItem([ user[ 'user_cn' ], user[ 'user_name' ] ])
            usb_access_items.append(item)
        self.ui.list_usb_access.addTopLevelItems(usb_access_items)

    def get_usb(self, virtual_port):
        for usb in self.usb_list:
            if usb.virtual_port == virtual_port:
                return usb

    def usb_permission_add(self):
        if self.current_usb is None:
            QMessageBox.warning(self.ui, 'Управление USB-портами',
                                f'Сначала выберите USB-порт!')
            return
        response = api_request(uri=f"users", request="full")
        users_raw = json.loads(response.text)[ 'users' ]
        current_users = {
            self.ui.list_usb_access.topLevelItem(index).text(1)
            for index in range(self.ui.list_usb_access.topLevelItemCount())
        }
        users = [
            {'name': item[ 'name' ], 'cn': item[ 'cn' ]}
            for item in users_raw
            if item[ 'name' ] not in current_users
        ]

        dialog = SelectUser(users)  # Открываем диалог добавления сервера
        if dialog.exec():  # exec() вернет True, если диалог завершен успешно
            for item in dialog.selected:
                user = QTreeWidgetItem([ item.text(0), item.text(1) ])
                self.ui.list_usb_access.addTopLevelItem(user)

    def usb_permission_remove(self):
        selected = self.ui.list_usb_access.selectedItems()
        if selected:
            for item in selected:
                index = self.ui.list_usb_access.indexOfTopLevelItem(item)
                if index != -1:
                    self.ui.list_usb_access.takeTopLevelItem(index)

        else:
            QMessageBox.warning(self.ui, 'Управление USB-портами',
                                f'Сначала выберите USB-порт!')
            return

    def usb_action(self, action):
        if self.current_usb is None:
            QMessageBox.warning(self.ui, 'Управление USB-портами',
                                f'Сначала выберите USB-порт!')
            return

        dialog = QMessageBox.question(self.ui, 'Управление USB-портами',
                                      f'Вы уверены что хотите совершить действие power-{action}?',
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                      QMessageBox.StandardButton.Yes)

        if dialog == QMessageBox.StandardButton.Yes:
            response = api_request(uri=f"usb_ports/{self.current_usb.virtual_port}/power?action={action}", method="GET",
                                   request="full")
            if response.status_code == 200:
                QMessageBox.information(self.ui, "Информация",
                                        f"Запрос power-{action} успешно обработан!")
            else:
                QMessageBox.critical(self.ui, "Ошибка",
                                     f"Запрос power-{action} не обработан или обработан с ошибками!\nОшибка: {response.status_code}"
                                     f"\n {response.text}")
            self.refresh()

    def usb_save(self):
        if self.current_usb is None:
            QMessageBox.warning(self.ui, 'Управление USB-портами',
                                f'Сначала выберите USB-порт!')
        data = {
            "name": self.ui.le_usb_name.text().strip() or None,
            "virtual_port": self.ui.le_usb_virtual_port.text().strip() or None,
            "bus": self.ui.le_usb_bus.text().strip() or None,
            "server_name": self.ui.combo_usb_group.currentText().strip() or None,
            "users": [
                {"user_name": self.ui.list_usb_access.topLevelItem(index).text(1)}
                for index in range(self.ui.list_usb_access.topLevelItemCount())
            ]
        }
        response = api_request(f"usb_ports/{self.current_usb.virtual_port}", {}, json.dumps(data), "PUT", "full")
        if response.status_code == 200:
            QMessageBox.information(self.ui, "Информация",
                                    f"USB-порт {self.current_usb.virtual_port} успешно изменен!")
        else:
            QMessageBox.critical(self.ui, "Ошибка",
                                 f"USB-порт {self.current_usb.virtual_port} не изменен или изменен с ошибками!\nОшибка: {response.status_code}"
                                 f"\n {response.text}")
        self.refresh()


class Usb:
    def __init__(self, id, active, server_id, server_name, virtual_port, bus, name, users, device):
        self.id = id
        self.active = active
        self.server_id = server_id
        self.server_name = server_name
        self.virtual_port = virtual_port
        self.bus = bus
        self.name = name
        self.users = users
        self.device = device
