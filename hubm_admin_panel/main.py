import json
import logging
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import re
import sys
import traceback
import winreg
from enum import Enum
from version import panel_version

import pandas as pd
import qdarktheme
import requests
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QTreeWidgetItem, QMessageBox, QDialog
)
from rich.console import Console
from rich.logging import RichHandler
from rich.traceback import install


from utils.utils import api_request, get_registry_value
from User.User import User
from User.CreatePolicies import CreatePolicies
from User.CreateUser import CreateUser
from User.UserExport import UserExport
from ui.ui_launch import Ui_Launch
from ui.ui_main import Ui_MainWindow


reg_key_path = r"Software\printline\hubM_ADMIN_PANEL"

console = Console()

log_file = open("C:\\Users\\mv.alekseev\\Documents\\projects\\hubM Admin Panel\\log2.log","a")
console_file = Console(force_terminal=False,file=log_file)


install(show_locals=True, console=console_file, width=300, code_width=288, extra_lines=5, locals_max_length=2000, locals_max_string=500, word_wrap=False)



logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[

        RichHandler(rich_tracebacks=True, console=console_file, locals_max_string=5000, locals_max_length=2000, show_time=True,
                    tracebacks_width=100000, tracebacks_extra_lines=10, tracebacks_word_wrap=False,
                    tracebacks_show_locals=True),
        logging.FileHandler("log.log")
    ]
)

log = logging.getLogger("rich")


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def create_or_open_key(parent_key, sub_key):
    try:
        key = winreg.OpenKey(parent_key, sub_key, 0, winreg.KEY_WRITE)
    except FileNotFoundError:
        key = winreg.CreateKey(parent_key, sub_key)
    return key

def set_registry_value(key, name, value, value_type=winreg.REG_SZ):
    winreg.SetValueEx(key, name, 0, value_type, value)

def close_registry_key(key):
    winreg.CloseKey(key)

def is_valid_ip(self, ip):
    # Паттерн для проверки корректности IP-адреса
    ip_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

    # Проверяем IP-адрес с помощью регулярного выражения
    if re.match(ip_pattern, ip):
        return True
    else:
        return False


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):

        super(MainWindow, self).__init__(*args, **kwargs)


        self.setupUi(self)

        icon = QtGui.QIcon(resource_path("res/icon.png"))
        self.setWindowIcon(icon)
        self.user = None

        #self.tbl_user_policies = PolicyTableWidget(parent=self.users_tab_group_policies)
        #self.tbl_user_policies = QtWidgets.QTableWidget(parent=self.users_tab_group_policies)


        ### Connections
        self.tabs_general.tabBarClicked.connect(self.tabs_general_clicked)
        self.tabs_group.tabBarClicked.connect(self.tabs_group_clicked)
        self.tabs_users.tabBarClicked.connect(self.tabs_users_clicked)
        self.tabs_ports.tabBarClicked.connect(self.tabs_ports_clicked)
        self.list_users.itemSelectionChanged.connect(self.entry_update_user_info)
        self.le_search_user.textChanged.connect(self.search)
        self.btn_user_policies_save.clicked.connect(self.save_user_policies)
        self.btn_user_save_params.clicked.connect(self.save_user_params)
        self.btn_user_policies_create.clicked.connect(self.win_new_create_policies)
        self.btn_user_export.clicked.connect(self.win_user_export)
        self.btn_user_delete.clicked.connect(self.user_delete)
        self.btn_refresh_users_tab.clicked.connect(self.get_list_users)
        self.btn_user_create.clicked.connect(self.win_user_create)
        self.btn_about_program.triggered.connect(self.win_about_program)
        self.btn_check_update.triggered.connect(lambda: self.check_version(False))

        ###

        self.list_users.setColumnWidth(0, 200)
        self.list_users.sortByColumn(0, Qt.SortOrder.AscendingOrder)

        self.check_version(startup=True)

    def save_user_params(self):
        try:
            dict_user = {
                "cn": self.le_user_cn.text(),
                "name": self.le_user_name.text(),
                "ip": self.le_user_default_ip.text(),
                "password": self.le_user_pass.text(),
                "email": self.le_user_email.text(),
                "comment": self.le_user_comment.text(),
                "tg_id": self.le_user_tg_id.text(),
                "active": self.cb_user_active.isChecked(),
            }
            self.user.dict = dict_user
            response = (self.user.sent_params(self, dict_user))

            if response.status_code == 200:
                QMessageBox.information(self, "Информация", f"Пользователь {self.le_user_name.text()} успешно изменен!")
            else:
                QMessageBox.critical(self, "Ошибка", f"Пользователь не сохранен или сохранен с ошибками!\nОшибка: {response.status_code}"
                                                     f"\n {response.text}")

            self.update_user_info(self.le_user_name.text())

        except Exception:
            print("Exception in user code:")
            print("-" * 60)
            traceback.print_exc(file=sys.stdout)
            print("-" * 60)



    def win_user_create(self):
        win_create_user = CreateUser()
        if win_create_user.exec() == QDialog.DialogCode.Accepted:
            data = win_create_user.save()
            user = data['name']
            response = api_request(f"users/{user}", {}, json.dumps(data), "POST", "full")

            if response.status_code == 201:
                QMessageBox.information(self, "Информация", f"Пользователь {user} успешно создан!")
            else:
                QMessageBox.critical(self, "Ошибка", f"Пользователь не добавлен или добавлен с ошибками!\nОшибка: {response.status_code}"
                                                     f"\n {response.text}")
            self.get_list_users()


    def user_delete(self):
        if not self.user:
            QMessageBox.warning(self, "Ошибка", f"Пользователь не выбран!")
            return

        username = self.user.name

        dialog = QMessageBox.question(self, 'Удалить пользователя',
                                   'Вы уверены что хотите удалить пользователя?',
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                   QMessageBox.StandardButton.Yes)
        if dialog == QMessageBox.StandardButton.Yes:


            response = api_request(f"users/{username}", {}, {}, "DELETE", "full")

            if response.status_code == 200:
                QMessageBox.information(self, "Информация", f"Пользователь успешно удален!")
            # elif response.status_code == 401:
            #    QMessageBox.critical(self, "Ошибка", f"Неправильный токен!")
            else:
                QMessageBox.critical(self, "Ошибка",
                                     f"Пользователь не удален или удален с ошибками!\nОшибка: {response.status_code}"
                                                     f"\n{response.text}")
            self.list_users.setCurrentItem(None)
            self.get_list_users()


    def win_user_export(self):
        win_user_export = UserExport()
        if win_user_export.exec() == QDialog.DialogCode.Accepted:
            print(win_user_export.ui.cb_enable_usb_policies.isChecked())
            print(win_user_export.ui.cb_enable_group_policies.isChecked())

            directory = QtWidgets.QFileDialog.getSaveFileName(self, "Выберите папку", "export.xlsx")

            if directory[0]:

                data = []
                try:
                    for column in range(self.list_users.topLevelItemCount()):
                        item = self.list_users.topLevelItem(column)
                        user = User(item.text(1))
                        #user_temp = self.user(item.text)
                        data.append(user.dict)

                    print(data)
                    df = pd.DataFrame(data)
                    df.to_excel(directory[0], index=False)
                    dlg2 = QMessageBox.question(self, 'Экспорт пользователей',
                                                'Экспорт успешно завершен.\nОткрыть файл?',
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                                QMessageBox.StandardButton.Yes)
                    if dlg2 == QMessageBox.StandardButton.Yes:
                        os.startfile(directory[ 0 ])


                except Exception:
                    print("Exception in user code:")
                    print("-" * 60)
                    traceback.print_exc(file=sys.stdout)
                    print("-" * 60)



    def win_about_program(self):
        QMessageBox.information(self, 'О программе',
                                f'Версия - {panel_version}\n'
                                f'@PrintLine512')
    def check_version(self, startup):
        server = get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\PrintLine", "hubM_AP_address")
        api_port = get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\PrintLine", "hubM_AP_tcp_port")
        url = f"http://{server}:{api_port}/download/check-version"
        response = requests.get(url)
        actual_version = response.text
        if actual_version > panel_version:

            dlg = QMessageBox.question(self, 'Проверка обновления',
                                 'Обнаружена новая версия.\nСкачать?',
                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                 QMessageBox.StandardButton.Yes)
            if dlg == QMessageBox.StandardButton.Yes:
                directory = QtWidgets.QFileDialog.getSaveFileName(self, "Выберите папку", "hubM Admin Panel Installer.exe")
                if directory[0]:
                    url = f"http://{server}:{api_port}/download/latest"
                    response = requests.get(url)
                    total_size = int(response.headers.get('content-length', 0))
                    print(total_size)
                    if response.status_code == 200:
                        # Сохраняем содержимое файла
                        with open(directory[0], 'wb') as f:
                            f.write(response.content)
                        dlg2 = QMessageBox.question(self, 'Обновление',
                                                   'Обновление успешно загружено.\nПерезапустить?',
                                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                                   QMessageBox.StandardButton.Yes)
                        if dlg2 == QMessageBox.StandardButton.Yes:
                            os.startfile(directory[0])
                            sys.exit(0)
                    else:
                        print('Ошибка при скачивании файла:', response.status_code)
                else:
                    QMessageBox.critical(self, 'Ошибка',
                                         'Некорректный путь. Загрузка отменена.')
        else:
            if not startup:
                QMessageBox.information(self, 'Информация',
                                             f'Обновление не требуется.\n'
                                             f'Последняя версия - {actual_version}.')

    def tabs_general_clicked(self, index):
        match index:
            case 0:
                print("Дэшборд")
            case 1:
                print("Пользователи")
                self.clear_user_info()
                self.get_list_users()
            case 2:
                print("Группы")    
            case 3:
                print("Порты")   
            case 4:
                print("Логи")   
            case _:
                print("Некорректная вкладка")

    def tabs_group_clicked(self, index):
        match index:
            case 0:
                print("Параметры")
            case 1:
                print("Доступы") 
            case _:
                print("Некорректная вкладка")

    def tabs_users_clicked(self, index):
        match index:
            case 0:
                print("Параметры")
            case 1:
                print("Политики групп")
            case 2:
                print("Политики портов")    
            case 3:
                print("Активность")   
            case _:
                print("Некорректная вкладка")

    def tabs_ports_clicked(self, index):
        match index:
            case 0:
                print("Параметры")
            case 1:
                print("Доступы")
            case _:
                print("Некорректная вкладка")



    def get_users_json(self):
        users_raw = api_request("users")
        data = json.loads(users_raw)
        users = data["users"]
        return users
    
    def get_user_json(self, name):
        user_raw = api_request(f"users/{name}")
        user = json.loads(user_raw)
        return user

    def get_user_policies_json(self, name):
        policies_raw = api_request(f"users/{name}/policies")
        policies = json.loads(policies_raw)
        return policies

    def get_list_users(self):
        users_raw = self.get_users_json()
        self.list_users.clear()
        items = []
        for user in users_raw:
            user_item = QTreeWidgetItem([user["cn"], user["name"]])
            items.append(user_item)

        self.list_users.insertTopLevelItems(0, items)


        if self.user:
            query = self.user.name
            matching_items = self.list_users.findItems(query, Qt.MatchFlag.MatchStartsWith, 1)
            item = matching_items[ 0 ]
            self.list_users.setCurrentItem(item)


    def search(self):
        # clear current selection.
        self.list_users.setCurrentItem(None)

        query = self.le_search_user.text()
        if not query:
            # Empty string, don't search.
            return

        matching_items = self.list_users.findItems(query, Qt.MatchFlag.MatchStartsWith, 0)
        matching_items.extend(self.list_users.findItems(query, Qt.MatchFlag.MatchStartsWith, 1))

        if matching_items:

            item = matching_items[0]  # take the first
            self.list_users.setCurrentItem(item)
            self.update_user_info(item.text(1))
        else:
            matching_items = self.list_users.findItems(query, Qt.MatchFlag.MatchContains, 0)
            matching_items.extend(self.list_users.findItems(query, Qt.MatchFlag.MatchContains, 1))

            if matching_items:
                item = matching_items[0]  # take the first
                self.list_users.setCurrentItem(item)
                self.update_user_info(item.text(1))
            else:
                self.clear_user_info()

    def get_user_policies(self, name):
        policies = self.get_user_policies_json(name)
        if not policies:
            return
        return policies



    class EnumPolicies(Enum):
        access = (0, "bool")
        ip = (1, "str")
        usb_filter = (2, "bool")
        auth_method = (3, "str")
        otp_secret = (4, "str")
        password = (5, "str")
        #login_use = (6, "bool")
        kick = (7, "bool")
        kickable = (8, "bool")
        until = (9, "str")

        @classmethod
        def get(cls, name):
            enum_member = cls[name]
            return enum_member.value[0], enum_member.value[1]

        @classmethod
        def get_enum(cls, value):
            for enum_member in cls:
                if enum_member.value[0] == value:
                    return enum_member.name, enum_member.value[1]

        @classmethod
        def get_all_names(cls):
            value = {enum_member.name: enum_member.value[0] for enum_member in cls}
            return json.dumps(value)

    # Пример использования

    def save_user_policies(self):
        print("1")
        if not self.user:
            # No selected user
            return

        print("2")
        user_name = self.user.name

        for row in range(self.tbl_user_policies.rowCount()):
            row_data = {}
            for column in range(self.tbl_user_policies.columnCount()):
                item = self.tbl_user_policies.item(row, column)
                if item is not None:
                    if self.EnumPolicies.get_enum(column):
                        name, p_type = self.EnumPolicies.get_enum(column)
                        if p_type == "bool":
                            if item.cb_is_checked():
                                row_data[name] = True
                            else:
                                row_data[name] = False
                        else:
                            row_data[name] = item.text()
                    else:
                        row_data[column] = ""  # Значение пустой ячейки

            ip_address = row_data["ip"]
            if not is_valid_ip(self, ip_address):
                QMessageBox.warning(self, "Ошибка", f"Некорректный IP-адрес!")
                return
            srv = self.tbl_user_policies.verticalHeaderItem(row).text()
            response = api_request(f"users/{user_name}/policies/{srv}", {}, json.dumps(row_data), "PUT", request="full")

            if response.status_code == 200:
                pass
            elif response.status_code == 401:
                QMessageBox.critical(self, "Ошибка", f"Неправильный токен!")
            else:
                QMessageBox.critical(self, "Ошибка", f"Политика не изменена или изменена с ошибками!\nСервер: {srv}\nОшибка: {response.status_code}"
                                                     f"\n{response.text}")

        self.update_user_info(user_name)
        QMessageBox.information(self, "Информация", f"Завершено.")



    def browse_folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку", "C:/")

        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            for file_name in os.listdir(directory):  # для каждого файла в директории
                self.listWidget.addItem(file_name)   # добавить файл в listWidget

    def update_user_info(self, item):

        self.user = User(item)
        self.user.render_info(self)
        self.user.render_group_policies(self)

        #policies = self.get_user_policies(item)
        #self.apply_user_policies(policies)



    def win_new_create_policies(self):

        if not self.user:
            QMessageBox.warning(self, "Ошибка", f"Пользователь не выбран!")
            return

        username = self.user.name


        win_create_policies = CreatePolicies(self.user.ip)
        groups = self.get_groups_list_text()
        win_create_policies.ui.le_group.addItems(groups)
        if win_create_policies.exec() == QDialog.DialogCode.Accepted:
            data = win_create_policies.save()
            group = data["group"]
            response = api_request(f"users/{username}/policies/{group}", {}, json.dumps(data), "PUT", "full")

            if response.status_code == 200:
                QMessageBox.information(self, "Информация", f"Политика успешно добавлена.")
            #elif response.status_code == 401:
            #    QMessageBox.critical(self, "Ошибка", f"Неправильный токен!")
            else:
                QMessageBox.critical(self, "Ошибка", f"Политика не добавлена или добавлена с ошибками!\nОшибка: {response.status_code}"
                                                     f"\n{response.text}")

            self.update_user_info(username)

    def entry_update_user_info(self):
        item = self.list_users.currentItem()
        if not item:
            # No selected user
            return

        name = item.text(1)



        self.update_user_info(name)

    def clear_user_info(self):
        self.tbl_user_policies.setRowCount(0)
        self.le_user_cn.setText("")
        self.le_user_comment.setText("")
        self.le_user_email.setText("")
        self.le_user_default_ip.setText("")
        self.le_user_name.setText("")

    def get_groups_list_text(self):
        groups_json = json.loads(api_request("servers"))
        groups_raw = groups_json["servers"]
        groups = []
        for group in groups_raw:
            groups.append(group['name'])

        return groups

class Launch(QtWidgets.QMainWindow, Ui_Launch):
    def __init__(self, *args, obj=None, **kwargs):
        super(Launch, self).__init__(*args, **kwargs)
        self.setupUi(self)

        reg_address_value = get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\PrintLine", "hubM_AP_address")
        reg_tcp_port_value = get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\PrintLine", "hubM_AP_tcp_port")
        reg_token_value = get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\PrintLine", "hubM_AP_token")
        self.le_address.setText(reg_address_value)
        self.le_tcp_port.setText(reg_tcp_port_value)
        self.le_token.setText(reg_token_value)
        icon = QtGui.QIcon(resource_path("res/icon.png"))
        self.setWindowIcon(icon)

        self.btn_connect.clicked.connect(self.to_connect)
        self.le_address.returnPressed.connect(self.to_connect)
        self.le_tcp_port.returnPressed.connect(self.to_connect)
        self.le_token.returnPressed.connect(self.to_connect)

    def to_connect(self):
        address = self.le_address.text()
        tcp_port = self.le_tcp_port.text()
        token = self.le_token.text()

        try:
            # Открываем родительский ключ
            parent_key_path = r"HKEY_CURRENT_USER\Software\PrintLine"
            parent_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software", 0, winreg.KEY_WRITE)
            # Создаем или открываем ключ
            key = create_or_open_key(parent_key, "PrintLine")
            # Закрываем родительский ключ
            close_registry_key(parent_key)

            # Устанавливаем значение ключа
            set_registry_value(key, "hubM_AP_address", address)
            set_registry_value(key, "hubM_AP_tcp_port", tcp_port)
            set_registry_value(key, "hubM_AP_token", token)



            # Закрываем ключ
            close_registry_key(key)
        except Exception as e:
            print("Ошибка:", e)


        try:
            response = api_request("users/", request="full")
            # Проверяем успешность запроса по статусу ответа
            if response.status_code == 200:
                #MainWindow().tbl_user_policies = PolicyTableWidget(name="Try3", parent=MainWindow().users_tab_group_policies)
                try:
                    self.new_window = MainWindow()
                    self.new_window.show()
                    self.close()
                except:
                    log.exception("Error!")
                    #console.print_exception(show_locals=True)
                    #console.print_exception(show_locals=True)
                    #print(console.export_html())

            elif response.status_code == 401:
                QMessageBox.critical(self, "Ошибка", f"Неправильный токен!")
            else:
                QMessageBox.critical(self, "Ошибка", f"Ошибка: {response.status_code}"
                                                     f"\n{response.text}")

        except requests.ConnectionError:
            QMessageBox.critical(self, "Ошибка", "Проверьте сетевое соединение!")





app = QtWidgets.QApplication(sys.argv)

qdarktheme.setup_theme()

window = Launch()


#app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt6'))

window.show()
app.exec()