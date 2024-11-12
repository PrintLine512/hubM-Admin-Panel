import json
import re
import sys
import traceback
from typing import TYPE_CHECKING

from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QBrush, QColor
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QTreeWidgetItem

if TYPE_CHECKING:
    from main import MainWindow
from utils.utils import api_request


def is_valid_ip(ip):
    # Паттерн для проверки корректности IP-адреса
    ip_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

    # Проверяем IP-адрес с помощью регулярного выражения
    if re.match(ip_pattern, ip):
        return True
    else:
        return False


class Policy:
    def __init__(self):
        self.dict = {
            "access": None,
            "auth_method": None,
            "ip": None,
            "ips": None,
            "timeout_session": None,
            "otp_secret": None,
            "password": None,
            "until": None,
            "kick": None,
            "kickable": None,
            "usb_filter": None,
            "server_name": None
        }

    def update(self, dict):
        filtered_dict = {key: value for key, value in dict.items() if key in self.dict}
        self.dict.update(filtered_dict)


class PolicyTableWidgetItem(QTableWidgetItem):
    def __init__(self, main, current_column, value, checkbox=False, password_echo=False, password_echo_mode=True, *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.checkbox = checkbox
        self.password_echo = password_echo
        if self.checkbox:
            self.item = CheckBoxWidget()
            self.item.checkbox.setChecked(value)
            main.tbl_user_policies.setCellWidget(0, current_column, self.item)

        elif self.password_echo:
            self.item = QtWidgets.QLineEdit()
            self.item.setFrame(False)
            self.item.setEchoMode((
                                      QtWidgets.QLineEdit.EchoMode.Normal if password_echo_mode else QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit))
            self.item.setText(value)
            self.setText(value)
            main.tbl_user_policies.setCellWidget(0, current_column, self.item)

        else:
            self.setText(value)

    def cb_is_checked(self):
        if self.checkbox:
            return self.item.checkbox.isChecked()
        else:
            return None

    def set_echo(self, echo_mode: "QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit"):
        self.item.setEchoMode(echo_mode)

    def get_text(self):
        if self.password_echo:
            return self.item.text()
        else:
            return self.text()


class PolicyTreeWidgetItem(QTreeWidgetItem):
    def __init__(self, server_item, ui: "MainWindow", current_column, name, value, checkbox=False, password_echo=False,
                 password_echo_mode=True, *args, **kwargs):
        super().__init__(server_item, *args, **kwargs)
        self.checkbox = checkbox
        self.ui = ui
        self.password_echo = password_echo
        self.setText(0, str(name))
        self.setFlags(self.flags() & ~QtCore.Qt.ItemFlag.ItemIsSelectable)

        if self.checkbox:
            self.setCheckState(1, QtCore.Qt.CheckState.Checked if value else QtCore.Qt.CheckState.Unchecked)

        else:
            self.setText(1, str(value))
            self.item = QtWidgets.QLineEdit()
            self.item.setText(str(value))
            self.item.setFrame(False)
            self.item.setStyleSheet("""
            QLineEdit {
                background-color: #202124;          /* Фоновый цвет */
                /* border: none; */  
                /* selection-background-color: #202124;   /* Цвет выделения */
                /* selection-color: red;                 /* Цвет текста при выделении */
            }
        """)
            self.ui.tree_user_policies.setItemWidget(self, 1, self.item)

        if self.password_echo:
            self.item.setEchoMode((
                                      QtWidgets.QLineEdit.EchoMode.Normal if password_echo_mode else QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit))

    def cb_is_checked(self):
        if self.checkbox:
            self.checkState(1)
            return True if self.checkState(1) == QtCore.Qt.CheckState.Checked else False
        else:
            return None

    def set_echo(self, echo_mode: "QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit"):
        self.item.setEchoMode(echo_mode)

    def get_text(self):
        if not self.checkbox:
            return self.item.text()


class PolicyTableWidget(QtWidgets.QTableWidget):
    def __init__(self, name, checkbox=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        print(self.name)
        if checkbox:
            pass

    def get_name(self):
        return self.name


class CheckBoxWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.checkbox = QtWidgets.QCheckBox()
        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.checkbox)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)


class User:
    def __init__(self, ui: 'MainWindow'):

        self.alt_view_mode = False
        self.user_usb_checklist = {}
        self.user_policies_normal_echo = False
        self.name = None

        self.dict = {}
        self.servers = [ ]
        self.group_policies = [ ]
        self.ui = ui

        self.ui.btn_user_save_params.clicked.connect(self.save_user_params)
        self.ui.btn_user_policies_save.clicked.connect(self.save_user_policies)
        self.ui.btn_user_ports_save.clicked.connect(self.save_user_usb)
        self.ui.btn_show_pass.toggled.connect(lambda: self.switch_echo(self.ui.le_user_pass))
        self.ui.btn_show_tg_code.toggled.connect(lambda: self.switch_echo(self.ui.le_user_tg_code))
        self.ui.btn_show_user_policies.toggled.connect(self.switch_user_policies_echo)
        self.ui.btn_change_view_user_policies.clicked.connect(self.change_view)

        self.ui.tree_user_policies.setColumnWidth(0, 200)

    def init(self, user):
        user_data_raw = api_request(f"users/{user}")
        self.dict = json.loads(user_data_raw)
        self.name = self.dict.get("name")
        self.servers = self.dict.get("servers")
        self.group_policies = [ ]
        for server in self.servers:
            if server.get('policy'):
                policy = server[ 'policy' ]
                self.group_policies.append({**policy, "server_name": server[ 'name' ]})

        self.render_info()
        self.render_group_policies()
        self.render_usb_policies()

    def render_group_policies(self):
        self.ui.tree_user_policies.clear()
        self.ui.tbl_user_policies.setRowCount(0)
        enum_name_type = json.loads(self.ui.EnumPolicies.get_all_names_with_type())
        for policy in self.group_policies:
            self.ui.tbl_user_policies.insertRow(0)
            self.ui.tbl_user_policies.setVerticalHeaderItem(0, QTableWidgetItem(policy[ 'server_name' ]))

            server_item = QtWidgets.QTreeWidgetItem(self.ui.tree_user_policies)  ###########
            server_item.setText(0, policy[ 'server_name' ])  ###########
            font = QFont()
            font.setBold(True)
            server_item.setFont(0, font)
            server_item.setExpanded(True)  ###########
            server_item.setFlags(server_item.flags() & ~QtCore.Qt.ItemFlag.ItemIsSelectable)
            server_item.setCheckState(0, QtCore.Qt.CheckState.Checked if policy[
                'access' ] else QtCore.Qt.CheckState.Unchecked)
            server_item.setFirstColumnSpanned(True)
            server_item.setBackground(0, QBrush(QColor("#48536f")))

            try:
                for column in enum_name_type:
                    id_enum, type_enum = self.ui.EnumPolicies.get(column)
                    value = policy[ column ]
                    if column == "access":
                        item = PolicyTableWidgetItem(self.ui, current_column=id_enum, checkbox=True, value=value)
                        self.ui.tbl_user_policies.setItem(0, id_enum, item)
                        self.ui.tbl_user_policies.resizeColumnToContents(id_enum)

                    elif type_enum == "bool":
                        PolicyTreeWidgetItem(server_item, self.ui, current_column=id_enum, value=value, name=column,
                                             checkbox=True)

                        item = PolicyTableWidgetItem(self.ui, current_column=id_enum, checkbox=True, value=value)
                        self.ui.tbl_user_policies.setItem(0, id_enum, item)
                        self.ui.tbl_user_policies.resizeColumnToContents(id_enum)


                    elif type_enum == "password":
                        PolicyTreeWidgetItem(
                            server_item, self.ui, current_column=id_enum, value=value, name=column,
                            password_echo=True, password_echo_mode=self.user_policies_normal_echo)

                        item = PolicyTableWidgetItem(self.ui, current_column=id_enum, value=str(value),
                                                     password_echo=True,
                                                     password_echo_mode=self.user_policies_normal_echo)
                        self.ui.tbl_user_policies.setItem(0, id_enum, item)
                    else:
                        PolicyTreeWidgetItem(server_item, self.ui, current_column=id_enum, value=str(value),
                                             name=column)

                        item = PolicyTableWidgetItem(self.ui, current_column=id_enum, value=str(value))
                        self.ui.tbl_user_policies.setItem(0, id_enum, item)

                self.ui.tree_user_policies.resizeColumnToContents(1)

            except Exception:
                print("Exception in user code:")
                print("-" * 60)
                traceback.print_exc(file=sys.stdout)
                print("-" * 60)

    def change_view(self):
        self.alt_view_mode = not self.alt_view_mode
        self.ui.stack_user_policies.setCurrentIndex(1 if self.alt_view_mode else 0)

    def render_usb_policies(self):
        self.ui.tbl_user_ports.clear()
        for server in self.servers:
            server_item = QtWidgets.QTreeWidgetItem(self.ui.tbl_user_ports)
            server_item.setText(0, server[ 'name' ])
            server_item.setExpanded(True)
            font = QFont()
            font.setBold(True)
            server_item.setFont(0, font)
            server_item.setFirstColumnSpanned(True)
            server_item.setBackground(0, QBrush(QColor("#48536f")))

            if server.get('usb_ports'):
                usb_ports = server[ 'usb_ports' ]
                for usb in usb_ports:
                    item = QtWidgets.QTreeWidgetItem(server_item)
                    item.setCheckState(0, QtCore.Qt.CheckState.Checked if usb[
                        'access' ] else QtCore.Qt.CheckState.Unchecked)
                    item.setText(0, usb[ 'name' ])
                    item.setToolTip(0, usb[ 'virtual_port' ])
                    self.user_usb_checklist.update({usb[ 'virtual_port' ]: usb[ 'access' ]})

    def render_info(self):
        self.ui.cb_user_active.setChecked(self.dict[ 'active' ])
        self.ui.le_user_cn.setText(self.dict[ 'cn' ])
        self.set_str_value(self.ui.le_user_comment, self.dict[ "comment" ])
        self.ui.le_user_email.setText(self.dict[ 'email' ])
        self.ui.le_user_default_ip.setText(self.dict[ 'ip' ])
        self.ui.le_user_name.setText(self.dict[ 'name' ])
        self.ui.le_user_pass.setText(self.dict[ 'password' ])
        self.set_str_value(self.ui.le_user_tg_id, self.dict[ "tg_id" ])
        self.set_str_value(self.ui.le_user_tg_code, self.dict[ "tg_code" ])

    def set_str_value(self, line: "QtWidgets.QLineEdit", value):
        if value is not None:
            line.setText(str(value))
        else:
            line.setText("")

    def get_str_value(self, value):
        if value == "":
            return None
        else:
            return value

    def sent_params(self, data):
        response = api_request(f"users/{self.name}", {}, json.dumps(data), "PUT", "full")
        return response

    def save_user_params(self):

        try:
            dict_user = {
                "cn": self.ui.le_user_cn.text(),
                "name": self.ui.le_user_name.text(),
                "ip": self.ui.le_user_default_ip.text(),
                "password": self.ui.le_user_pass.text(),
                "email": self.ui.le_user_email.text(),
                "comment": self.ui.le_user_comment.text(),
                "tg_id": self.get_str_value(self.ui.le_user_tg_id.text()),
                "tg_code": self.ui.le_user_tg_code.text(),
                "active": self.ui.cb_user_active.isChecked(),
            }
            response = (self.sent_params(dict_user))

            if response.status_code == 200:
                QMessageBox.information(self.ui, "Информация",
                                        f"Пользователь {self.ui.le_user_name.text()} успешно изменен!")
            else:
                QMessageBox.critical(self.ui, "Ошибка",
                                     f"Пользователь не сохранен или сохранен с ошибками!\nОшибка: {response.status_code}"
                                     f"\n {response.text}")

            self.init(self.ui.le_user_name.text())

        except Exception:
            print("Exception in user code:")
            print("-" * 60)
            traceback.print_exc(file=sys.stdout)
            print("-" * 60)

    def policy_to_save(self):
        policies_data = [ ]
        enum_name_type = json.loads(self.ui.EnumPolicies.get_all_names_with_type())
        enum_name_index = json.loads(self.ui.EnumPolicies.get_all_names_with_index())
        if self.alt_view_mode:
            for index in range(self.ui.tree_user_policies.topLevelItemCount()):
                policy_data = Policy()
                server = self.ui.tree_user_policies.topLevelItem(index)
                policy_data.update({'server_name': server.text(0)})

                for policy_name, policy_type in enum_name_type.items():
                    if policy_name == "access":
                        value = True if server.checkState(0) == Qt.CheckState.Checked else False
                        policy_data.update({"access": True if server.checkState(0) == Qt.CheckState.Checked else False})

                    for index in range(server.childCount()):
                        policy = server.child(index)
                        if policy_name == policy.text(0):

                            if policy_type == "bool":
                                policy_data.update({policy_name: True if policy.cb_is_checked() == True else False})
                            else:
                                policy_data.update({policy_name: self.get_str_value(policy.get_text())})

                if not policy_data.dict[ "ip" ] or not is_valid_ip(policy_data.dict[ "ip" ]):
                    QMessageBox.warning(self.ui, "Ошибка", f"Некорректный IP-адрес!")
                    return
                policies_data.append(policy_data)
        else:
            for server_index in range(self.ui.tbl_user_policies.rowCount()):
                policy_data = Policy()
                policy_data.update({'server_name': self.ui.tbl_user_policies.verticalHeaderItem(server_index).text()})
                for policy_name, policy_index in enum_name_index.items():
                    for column in range(self.ui.tbl_user_policies.columnCount()):
                        policy = self.ui.tbl_user_policies.item(server_index, column)
                        if column == policy_index:
                            policy_index, policy_type = self.ui.EnumPolicies.get(policy_name)

                            if policy_type == "bool":
                                policy_data.update({policy_name: True if policy.cb_is_checked() == True else False})
                            else:
                                policy_data.update({policy_name: self.get_str_value(policy.get_text())})

                if not policy_data.dict[ "ip" ] or not is_valid_ip(policy_data.dict[ "ip" ]):
                    QMessageBox.warning(self.ui, "Ошибка", f"Некорректный IP-адрес!")
                    return
                policies_data.append(policy_data)

        print(policies_data)
        return policies_data

    def save_user_policies(self):
        policies = self.policy_to_save()
        for policy in policies:

            response = api_request(f"users/{self.name}/policies/{policy.dict[ 'server_name' ]}",
                                   {}, json.dumps(policy.dict), "PUT", request="full")

            if response.status_code == 200:
                pass
            elif response.status_code == 401:
                QMessageBox.critical(self.ui, "Ошибка", f"Неправильный токен!")
            else:
                QMessageBox.critical(self.ui, "Ошибка",
                                     f"Политика не изменена или изменена с ошибками!\nСервер: {policy.dict[ 'server_name' ]}\nОшибка: {response.status_code}"
                                     f"\n{response.text}")

        self.init(self.name)
        QMessageBox.information(self.ui, "Информация", f"Завершено.")

    def get_usb_status(self, server_item: "QtWidgets.QTreeWidgetItem"):
        ports = [ ]
        for index in range(server_item.childCount()):
            item = server_item.child(index)
            access = True if item.checkState(0) == QtCore.Qt.CheckState.Checked else False
            virtual_port = item.toolTip(0)
            usb = {"virtual_port": virtual_port, "access": access}
            ports.append(usb)
        return ports

    def save_user_usb(self):
        update_list = {}
        for index in range(self.ui.tbl_user_ports.topLevelItemCount()):
            server = self.ui.tbl_user_ports.topLevelItem(index)
            update_list.update({item[ 'virtual_port' ]: item[ 'access' ] for item in self.get_usb_status(server)
                                if item[ 'access' ] != self.user_usb_checklist[ item[ 'virtual_port' ] ]})

        if update_list:
            response = api_request(f"users/{self.name}/ports", {}, json.dumps(update_list), "PUT", "full")

            if response.status_code == 200:
                QMessageBox.information(self.ui, "Информация", f"Доступы для портов {self.name} успешно обновлены.")
            # elif response.status_code == 401:
            #    QMessageBox.critical(self, "Ошибка", f"Неправильный токен!")
            else:
                QMessageBox.critical(self.ui, "Ошибка",
                                     f"Доступы не обновлены или обновлены с ошибками!\nОшибка: {response.status_code}"
                                     f"\n{response.text}")

            self.user_usb_checklist.update(update_list)
            self.init(self.name)
        else:
            QMessageBox.critical(self.ui, "Ошибка",
                                 f"Нет изменений для обновления!")

    def switch_echo(self, ui_item: "QtWidgets.QLineEdit"):
        if ui_item.echoMode() == QtWidgets.QLineEdit.EchoMode.Normal:
            ui_item.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        else:
            ui_item.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)

    def switch_user_policies_echo(self, checked):
        enums = self.ui.EnumPolicies.get_type("password")
        column_id_list = {enum[ 'id' ] for enum in enums}
        for index in range(self.ui.tree_user_policies.topLevelItemCount()):
            server = self.ui.tree_user_policies.topLevelItem(index)
            for index in range(server.childCount()):
                policy = server.child(index)
                if policy.password_echo:
                    policy.set_echo(
                        QtWidgets.QLineEdit.EchoMode.Normal if checked else QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)

        for row in range(self.ui.tbl_user_policies.rowCount()):
            for column in column_id_list:
                policy = self.ui.tbl_user_policies.item(row, column)
                if policy.password_echo:
                    policy.set_echo(
                        QtWidgets.QLineEdit.EchoMode.Normal if checked else QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.user_policies_normal_echo = checked
