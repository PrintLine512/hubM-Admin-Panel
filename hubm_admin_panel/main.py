import gc
import json
import logging
import os
import re
import sys
import traceback
import winreg
from urllib.request import urlopen

import pandas as pd
import qdarktheme
import requests

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtWidgets import (
    QTreeWidgetItem, QMessageBox, QDialog, QProgressDialog
)
from rich.console import Console
from rich.logging import RichHandler
from rich.traceback import install

from version import panel_version
from enum import Enum
from utils.utils import api_request, get_registry_value, set_registry_value, close_registry_key, create_or_open_key
from User.User import User
from User.CreatePolicies import CreatePolicies
from User.CreateUser import CreateUser
from User.UserExport import UserExport
from Groups.master import Groups, group_search

from ui.ui_launch import Ui_Launch
from ui.ui_main import Ui_MainWindow

reg_key_path = r"Software\printline\hubM_ADMIN_PANEL"

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    running_from_pyinstaller = True
else:
    running_from_pyinstaller = False

console = Console()

log_file = open("log2.log", "a")
console_file = Console(force_terminal=False, file=log_file)

install(show_locals=True, console=console, width=300, code_width=288, extra_lines=5, locals_max_length=2000,
        locals_max_string=500, word_wrap=False)

logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[

        RichHandler(rich_tracebacks=True, console=console_file, locals_max_string=5000, locals_max_length=2000,
                    show_time=True,
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


def is_valid_ip(self, ip):
    # Паттерн для проверки корректности IP-адреса
    ip_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

    # Проверяем IP-адрес с помощью регулярного выражения
    if re.match(ip_pattern, ip):
        return True
    else:
        return False


def check_version(ui: "QtWidgets.QMainWindow", startup):
    server = get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\PrintLine", "hubM_AP_address")
    api_port = get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\PrintLine", "hubM_AP_tcp_port")
    url = f"http://{server}:{api_port}/download/check-version"
    response = requests.get(url)
    try:
        response = api_request(request="full", full_uri=True, uri=url)
        # Проверяем успешность запроса по статусу ответа
        if response.status_code == 200:
            # MainWindow().tbl_user_policies = PolicyTableWidget(name="Try3", parent=MainWindow().users_tab_group_policies)
            try:
                actual_version = response.text
                if not running_from_pyinstaller and not startup:
                    QMessageBox.information(ui, 'Информация',
                                            f'Программа запущена через интерпретатор Python.\n'
                                            f'Если необходимо обновление, воспользуйтесь инструментом pip.\n'
                                            f'прим.: "pip install hubm-admin-panel --upgrade"')
                    return

                if not running_from_pyinstaller and actual_version > panel_version:

                    dlg = QMessageBox.question(ui, 'Проверка обновления',
                                               f'Обнаружена новая версия - {actual_version}\nСкачать?',
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                               QMessageBox.StandardButton.Yes)
                    if dlg == QMessageBox.StandardButton.Yes:
                        download_path = os.path.join(os.path.expanduser("~"), "Downloads",
                                                     "hubM Admin Panel Installer.exe")
                        directory = QtWidgets.QFileDialog.getSaveFileName(ui, "Выберите папку", download_path)

                        if directory[ 0 ]:
                            url = f"http://{server}:{api_port}/download/latest"
                            response = requests.get(url)
                            total_size = int(response.headers.get('content-length', 0))
                            print(total_size)
                            if response.status_code == 200:
                                # Сохраняем содержимое файла
                                with open(directory[ 0 ], 'wb') as f:
                                    f.write(response.content)
                                dlg2 = QMessageBox.question(ui, 'Обновление',
                                                            'Обновление успешно загружено.\nПерезапустить?',
                                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                                            QMessageBox.StandardButton.Yes)
                                if dlg2 == QMessageBox.StandardButton.Yes:
                                    os.startfile(directory[ 0 ])
                                    print("Exit")

                                    ui.close()
                                    sys.exit()

                            else:
                                print('Ошибка при скачивании файла:', response.status_code)
                        else:
                            QMessageBox.critical(ui, 'Ошибка',
                                                 'Некорректный путь. Загрузка отменена.')

                else:
                    if not startup:
                        QMessageBox.information(ui, 'Информация',
                                                f'Обновление не требуется.\n'
                                                f'Последняя версия - {actual_version}.')
            except:
                log.exception("Error!")
                # console.print_exception(show_locals=True)
                # console.print_exception(show_locals=True)
                # print(console.export_html())

        elif response.status_code == 401:
            QMessageBox.critical(ui, "Ошибка", f"Неправильный токен!")
        else:
            QMessageBox.critical(ui, "Ошибка", f"Ошибка: {response.status_code}"
                                                 f"\n{response.text}")

    except requests.ConnectionError:
        QMessageBox.critical(ui, "Ошибка", "Проверьте сетевое соединение!")



class Downloader(QThread):
    # Signal for the window to establish the maximum value
    # of the progress bar.
    setTotalProgress = Signal(int)
    # Signal to increase the progress.
    setCurrentProgress = Signal(int)
    # Signal to be emitted when the file has been downloaded successfully.
    succeeded = Signal()

    def __init__(self, url, filename):
        super().__init__()
        self.url = url
        self.filename = filename

    def run(self):
        # url = "https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe"
        # filename = "python-3.7.2.exe"
        readBytes = 0
        chunkSize = 1024
        # Open the URL address.
        with urlopen(self.url) as r:
            print(self.url)
            # Tell the window the amount of bytes to be downloaded.
            self.setTotalProgress.emit(int(r.info()[ "Content-Length" ]))
            with open(self.filename, "ab") as f:
                while True:
                    # Read a piece of the file we are downloading.
                    chunk = r.read(chunkSize)
                    # If the result is `None`, that means data is not
                    # downloaded yet. Just keep waiting.
                    if chunk is None:
                        continue
                    # If the result is an empty `bytes` instance, then
                    # the file is complete.
                    elif chunk == b"":
                        break
                    # Write into the local file the downloaded chunk.
                    f.write(chunk)
                    readBytes += chunkSize
                    # Tell the window how many bytes we have received.
                    self.setCurrentProgress.emit(readBytes)
        # If this line is reached then no exception has ocurred in
        # the previous lines.

        self.succeeded.emit()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):

        super(MainWindow, self).__init__(*args, **kwargs)


        self.setupUi(self)

        icon_path = resource_path("res/icon.png")
        icon = QtGui.QIcon(icon_path)
        self.setWindowIcon(icon)
        self.user = User(self)
        #self.groups = None
        self.groups = Groups(self)

        # self.tbl_user_policies = PolicyTableWidget(parent=self.users_tab_group_policies)
        # self.tbl_user_policies = QtWidgets.QTableWidget(parent=self.users_tab_group_policies)

        ### Connections
        self.tabs_general.currentChanged.connect(self.tabs_general_clicked)
        self.tabs_group.tabBarClicked.connect(self.tabs_group_clicked)
        self.tabs_users.tabBarClicked.connect(self.tabs_users_clicked)
        self.tabs_ports.tabBarClicked.connect(self.tabs_ports_clicked)
        self.list_users.itemSelectionChanged.connect(self.entry_update_user_info)
        self.le_search_user.textChanged.connect(self.search)
        self.le_search_group.textChanged.connect(lambda: group_search(self))
        self.btn_user_policies_save.clicked.connect(self.save_user_policies)
        self.btn_user_save_params.clicked.connect(self.save_user_params)
        self.btn_user_policies_create.clicked.connect(self.win_new_create_policies)
        self.btn_user_policies_delete.clicked.connect(self.user_policy_delete)
        self.btn_user_export.clicked.connect(self.win_user_export)
        self.btn_user_delete.clicked.connect(self.user_delete)
        self.btn_refresh_users_tab.clicked.connect(self.get_list_users)
        #self.btn_refresh_groups_tab.clicked.connect(self.group_init)
        self.btn_user_create.clicked.connect(self.win_user_create)
        self.btn_about_program.triggered.connect(self.win_about_program)
        self.btn_check_update.triggered.connect(lambda: check_version(self, False))
        self.DevButton1.clicked.connect(self.get_class)
        self.DevButton2.clicked.connect(self.get_class2)
        #self.list_groups.itemSelectionChanged.connect(self.group_render)
        #self.btn_group_restart.clicked.connect(self.group_restart)
        ###

        self.list_users.setColumnWidth(0, 200)
        self.list_users.sortByColumn(0, Qt.SortOrder.AscendingOrder)



    def group_restart(self):
        self.groups.restart_selected(self)

    def group_render(self):
        print("2112")
        self.groups.render_groups(self)

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
                QMessageBox.critical(self, "Ошибка",
                                     f"Пользователь не сохранен или сохранен с ошибками!\nОшибка: {response.status_code}"
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
            user = data[ 'name' ]
            response = api_request(f"users/{user}", {}, json.dumps(data), "POST", "full")

            if response.status_code == 201:
                QMessageBox.information(self, "Информация", f"Пользователь {user} успешно создан!")
            else:
                QMessageBox.critical(self, "Ошибка",
                                     f"Пользователь не добавлен или добавлен с ошибками!\nОшибка: {response.status_code}"
                                     f"\n {response.text}")
            self.get_list_users()

    def user_delete(self):
        if not self.user:
            QMessageBox.warning(self, "Ошибка", f"Пользователь не выбран!")
            return

        username = self.user.name

        dialog = QMessageBox.question(self, 'Удалить пользователя',
                                      f'Вы уверены что хотите удалить пользователя {username}?',
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                      QMessageBox.StandardButton.No)
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

    def user_policy_delete(self):
        try:
            row = self.tbl_user_policies.currentItem().row()
            header = self.tbl_user_policies.verticalHeaderItem(row)
            groupname = header.text()

            dialog = QMessageBox.question(self, 'Удалить политику',
                                          f'Вы уверены что хотите удалить политику для группы {groupname}?',
                                          QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                          QMessageBox.StandardButton.No)
            if dialog == QMessageBox.StandardButton.Yes:
                username = self.user.name
                response = api_request(f"users/{username}/policies/{groupname}", {}, {}, "DELETE", "full")

                if response.status_code == 200:
                    QMessageBox.information(self, "Информация", f"Политика успешно удален!")
                # elif response.status_code == 401:
                #    QMessageBox.critical(self, "Ошибка", f"Неправильный токен!")
                else:
                    QMessageBox.critical(self, "Ошибка",
                                         f"Политика не удалена или удалена с ошибками!\nОшибка: {response.status_code}"
                                         f"\n{response.text}")
                #self.list_users.setCurrentItem(None)
                self.get_list_users()

        except Exception:
            QMessageBox.warning(self, "Ошибка", f"Некорректная политика!")

    def win_user_export(self):
        win_user_export = UserExport()
        if win_user_export.exec() == QDialog.DialogCode.Accepted:
            print(win_user_export.ui.cb_enable_usb_policies.isChecked())
            print(win_user_export.ui.cb_enable_group_policies.isChecked())
            export_path = os.path.join(os.path.expanduser("~"), "Documents", "export.xlsx")
            directory = QtWidgets.QFileDialog.getSaveFileName(self, "Выберите папку", export_path, ".xlsx")

            if directory[ 0 ]:

                data = []
                order = []
                try:
                    if not win_user_export.ui.cb_enable_group_policies.isChecked():
                        order = [ 'cn', 'name', 'email', 'ip', 'comment', 'active']

                        response = api_request("users/", request="full")
                        data = json.loads(response.text)[ 'users' ]


                    if win_user_export.ui.cb_enable_group_policies.isChecked() and not win_user_export.ui.cb_enable_usb_policies.isChecked():
                        order = [ 'cn', 'name', 'email', 'ip', 'comment', 'active', 'groups' ]

                        response = api_request("users/?type=servers", request="full")
                        data = json.loads(response.text)[ 'users' ]
                        for user in data:
                            # Получаем группы пользователя
                            #user['active'] = "True" if user['active'] else "False"
                            groups = user[ 'groups' ]
                            group_names = [ group_name for group_name in groups.keys() ]  # Получаем только имена групп

                            # Объединяем группы в одну строку
                            user_groups = ', '.join(group_names)
                            user[ 'groups' ] = f"Группы: {user_groups}"

                    if win_user_export.ui.cb_enable_usb_policies.isChecked():
                        order = [ 'cn', 'name', 'email', 'ip', 'comment', 'active', 'groups' ]

                        response = api_request("users/?type=servers", request="full")
                        data = json.loads(response.text)[ 'users' ]
                        for user in data:
                            #user['active'] = "True" if user['active'] else "False"

                            # print(f"User: {user[ 'cn' ]}, ID: {user[ 'id' ]}")

                            # Получаем группы пользователя
                            groups = user[ 'groups' ]
                            group_usb_mapping = [ ]  # Список для хранения групп с их USB-портами

                            # Проходимся по каждой группе
                            for group_name, group_info in groups.items():
                                usb_names = [ usb[ 'name' ] for usb in
                                              group_info.get('usb', [ ]) ]  # Получаем имена USB-портов
                                group_usb_mapping.append(
                                    f"Группа - {group_name}, USB: {', '.join(usb_names)}")  # Формируем строку

                            # Объединяем группы в одну строку
                            user_groups = '; '.join(group_usb_mapping)
                            # print(f"Группы: {user_groups}")
                            user[ 'groups' ] = user_groups

                    df = pd.DataFrame(data, columns=order)
                    df.to_excel(directory[ 0 ], index=False)

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

    def initDownload(self, url, filename):

        pd = QProgressDialog("Operation in progress.", "Cancel", 0, 100)
        # pd.canceled.connect(self.cancel)
        # Run the download in a new thread.
        self.downloader = Downloader(url, filename)

        # Connect the signals which send information about the download
        # progress with the proper methods of the progress bar.
        self.downloader.setTotalProgress.connect(pd.setMaximum)
        self.downloader.setCurrentProgress.connect(pd.setValue)
        # Qt will invoke the `succeeded()` method when the file has been
        # downloaded successfully and `downloadFinished()` when the
        # child thread finishes.
        self.downloader.succeeded.connect(lambda: self.progressBar.setValue(pd.maximum()))
        self.downloader.finished.connect(lambda: self.downloadFinished(filename))
        self.downloader.start()

    def downloadSucceeded(self, pd):
        # Set the progress at 100%.
        self.progressBar.setValue(pd.maximum())

    def downloadFinished(self, filename):
        # Restore the button.
        # Delete the thread when no longer needed.
        dlg2 = QMessageBox.question(self, 'Обновление',
                                    'Обновление успешно загружено.\nПерезапустить?',
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                    QMessageBox.StandardButton.Yes)
        if dlg2 == QMessageBox.StandardButton.Yes:
            os.startfile(filename)
            sys.exit(0)
        del self.downloader

    def get_class(self):
        try:
            all_objects = [ obj for obj in gc.get_objects() if isinstance(obj, Groups) ]
            for obj in all_objects:
                print(obj.__class__)
                refs = gc.get_referrers(obj)
                print(refs)
                print(refs.__class__)
                print(refs.__class__.__name__)
        except:
            pass

    def get_class2(self):
        try:
            all_objects = [ obj for obj in gc.get_objects() if isinstance(obj, User) ]
            for obj in all_objects:
                print(obj.__class__)
                refs = gc.get_referrers(obj)
                print(refs)
                print(refs.__class__)
                print(refs.__class__.__name__)
        except:
            pass
        
    def group_init(self):
        #if self.groups is not None:
        #    print("DELETE")
        #    del self.groups
        #self.groups = Groups(self)
        self.groups.render_groups(self)

    def tabs_general_clicked(self, index):
        match index:
            case 0:
                print("Дэшборд")
                #print(self.tabs_general.currentWidget().objectName())
            case 1:
                print("Пользователи")
                #print(self.tabs_general.currentWidget().objectName())
                self.clear_user_info()
                self.get_list_users()
            case 2:
                print("Группы")
                #print(self.tabs_general.currentWidget().objectName())
                self.groups.refresh(self)
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
                self.user.render_usb_policies()
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
        users = data[ "users" ]
        return users

    def get_list_users(self):
        users_raw = self.get_users_json()
        self.list_users.setCurrentItem(None)
        self.list_users.clear()
        items = [ ]
        for user in users_raw:
            user_item = QTreeWidgetItem([ user[ "cn" ], user[ "name" ] ])
            items.append(user_item)

        self.list_users.insertTopLevelItems(0, items)

        if self.user:
            query = self.user.name
            print(query)
            matching_items = self.list_users.findItems(query, Qt.MatchFlag.MatchStartsWith, 1)
            item = matching_items[ 0 ]
            self.list_users.setCurrentItem(item)

    def search(self):
        # clear current selection.
        print("SEARCH")
        self.list_users.setCurrentItem(None)

        query = self.le_search_user.text()
        if not query:
            # Empty string, don't search.
            return

        matching_items = self.list_users.findItems(query, Qt.MatchFlag.MatchStartsWith, 0)
        matching_items.extend(self.list_users.findItems(query, Qt.MatchFlag.MatchStartsWith, 1))

        if matching_items:

            item = matching_items[ 0 ]  # take the first
            self.list_users.setCurrentItem(item)
            self.update_user_info(item.text(1))
        else:
            matching_items = self.list_users.findItems(query, Qt.MatchFlag.MatchContains, 0)
            matching_items.extend(self.list_users.findItems(query, Qt.MatchFlag.MatchContains, 1))

            if matching_items:
                item = matching_items[ 0 ]  # take the first
                self.list_users.setCurrentItem(item)
                self.update_user_info(item.text(1))
            else:
                self.clear_user_info()

    class EnumPolicies(Enum):
        access = (0, "bool")
        ip = (1, "str")
        usb_filter = (2, "bool")
        auth_method = (3, "str")
        otp_secret = (4, "str")
        password = (5, "str")
        # login_use = (6, "bool")
        kick = (7, "bool")
        kickable = (8, "bool")
        until = (9, "str")

        @classmethod
        def get(cls, name):
            enum_member = cls[ name ]
            return enum_member.value[ 0 ], enum_member.value[ 1 ]

        @classmethod
        def get_enum(cls, value):
            for enum_member in cls:
                if enum_member.value[ 0 ] == value:
                    return enum_member.name, enum_member.value[ 1 ]

        @classmethod
        def get_all_names(cls):
            value = {enum_member.name: enum_member.value[ 0 ] for enum_member in cls}
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
                                row_data[ name ] = True
                            else:
                                row_data[ name ] = False
                        else:
                            row_data[ name ] = item.text()
                    else:
                        row_data[ column ] = ""  # Значение пустой ячейки

            ip_address = row_data[ "ip" ]
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
                QMessageBox.critical(self, "Ошибка",
                                     f"Политика не изменена или изменена с ошибками!\nСервер: {srv}\nОшибка: {response.status_code}"
                                     f"\n{response.text}")

        self.update_user_info(user_name)
        QMessageBox.information(self, "Информация", f"Завершено.")

    def update_user_info(self, item):

        self.user.init(item)
        self.user.init_group_policies()
        # policies = self.get_user_policies(item)
        # self.apply_user_policies(policies)

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
            group = data[ "group" ]
            usb_list = data["usb_allowed"]
            for usb in usb_list:
                response = api_request(f"users/{username}/ports/{usb}", {}, json.dumps(data), "POST", "full")
                if response.status_code == 200:
                    #QMessageBox.information(self, "Информация", f"Политика успешно добавлена.")
                    pass
                elif response.status_code == 409:
                    #QMessageBox.critical(self, "Ошибка", f"Неправильный токен!")
                    pass
                else:
                    QMessageBox.critical(self, "Ошибка",
                                         f"Доступ к порту не добавлен или добавлен с ошибками!\nОшибка: {response.status_code}"
                                         f"\n{response.text}")

            response = api_request(f"users/{username}/policies/{group}", {}, json.dumps(data), "PUT", "full")

            if response.status_code == 200:
                QMessageBox.information(self, "Информация", f"Политика успешно добавлена.")
            # elif response.status_code == 401:
            #    QMessageBox.critical(self, "Ошибка", f"Неправильный токен!")
            else:
                QMessageBox.critical(self, "Ошибка",
                                     f"Политика не добавлена или добавлена с ошибками!\nОшибка: {response.status_code}"
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
        groups_raw = groups_json[ "servers" ]
        groups = [ ]
        for group in groups_raw:
            groups.append(group[ 'name' ])

        return groups


class Launch(QtWidgets.QMainWindow, Ui_Launch):
    def __init__(self, *args, obj=None, **kwargs):
        super(Launch, self).__init__(*args, **kwargs)
        self.setupUi(self)
        icon = QtGui.QIcon(resource_path("res/icon.png"))
        self.setWindowIcon(icon)

        reg_address_value = get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\PrintLine", "hubM_AP_address")
        reg_tcp_port_value = get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\PrintLine", "hubM_AP_tcp_port")
        reg_token_value = get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\PrintLine", "hubM_AP_token")


        self.le_address.setText(reg_address_value)
        self.le_tcp_port.setText(reg_tcp_port_value)
        self.le_token.setText(reg_token_value)

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
                # MainWindow().tbl_user_policies = PolicyTableWidget(name="Try3", parent=MainWindow().users_tab_group_policies)
                try:
                    self.new_window = MainWindow()
                    self.new_window.show()
                    self.close()
                except:
                    log.exception("Error!")
                    # console.print_exception(show_locals=True)
                    # console.print_exception(show_locals=True)
                    # print(console.export_html())

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
window.show()
check_version(window, True)

app.exec()
