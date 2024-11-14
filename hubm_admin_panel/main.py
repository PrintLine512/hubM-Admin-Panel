import gc
import json
import logging
import os
import sys
import traceback

from urllib.request import urlopen, ProxyHandler, build_opener, install_opener

import pandas as pd
import qdarktheme
import requests
from PySide6.QtGui import QIcon
from cryptography.fernet import InvalidToken
from packaging import version
from qdarktheme.qtpy.QtWidgets import QApplication

import utils.utils

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt, QThread, Signal, QSize, QTimer
from PySide6.QtWidgets import (
    QTreeWidgetItem, QMessageBox, QDialog, QVBoxLayout, QLabel, QProgressBar, QPushButton
)

from rich.console import Console
from rich.logging import RichHandler
from rich.traceback import install

from version import panel_version
from enum import Enum
from utils.utils import api_request, filter_items
from User.User import User
from User.CreatePolicies import CreatePolicies
from User.CreateUser import CreateUser
from User.UserExport import UserExport
from Groups.master import Groups, group_search

from ui import launch_dialogs
from ui.ui_launch import Ui_Launch
from ui.ui_main import Ui_MainWindow

from utils.utils import config

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

def handle_file_download(file_data):
    # Обработка загруженного файла
    with open('run', "wb") as file:
        file.write(file_data)
    print("Файл успешно загружен и сохранен!")

class Downloader(QThread):
    no_proxy_handler = ProxyHandler({})
    opener = build_opener(no_proxy_handler)
    install_opener(opener)
    setTotalProgress = Signal(int)
    setCurrentProgress = Signal(int)
    succeeded = Signal()

    def __init__(self, url, filename):
        super().__init__()
        self._url = url
        self._filename = filename

    def run(self):
        readBytes = 0
        chunkSize = 1024
        with urlopen(self._url) as r:
            self.setTotalProgress.emit(int(r.info()["Content-Length"]))
            with open(self._filename, "wb") as f:
                while True:
                    chunk = r.read(chunkSize)
                    if not chunk:
                        break
                    f.write(chunk)
                    readBytes += len(chunk)
                    self.setCurrentProgress.emit(readBytes)
        self.succeeded.emit()



class DownloadDialog(QDialog):
    def __init__(self, download_url, save_path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Downloading Update")
        #self.resize(300, 100)
        self.save_path = save_path
        layout = QVBoxLayout(self)

        self.label = QLabel("Downloading file...", self)
        layout.addWidget(self.label)

        self.progressBar = QProgressBar(self)
        layout.addWidget(self.progressBar)

        self.downloader = Downloader(download_url, self.save_path)
        self.downloader.setTotalProgress.connect(self.progressBar.setMaximum)
        self.downloader.setCurrentProgress.connect(self.progressBar.setValue)
        self.downloader.succeeded.connect(self.downloadSucceeded)
        self.downloader.finished.connect(self.close)
        self.downloader.start()

    def downloadSucceeded(self):
        dlg2 = QMessageBox.question(self, 'Обновление',
                                    'Обновление успешно загружено.\nПерезапустить?',
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                    QMessageBox.StandardButton.Yes)
        if dlg2 == QMessageBox.StandardButton.Yes:
            os.startfile(self.save_path)
            QApplication.quit()
            sys.exit()


def check_version(ui: "QtWidgets.QMainWindow", startup):
    url = f"https://api.github.com/repos/PrintLine512/hubM-Admin-Panel/releases/latest"
    proxies = {
        "http": "",
        "https": "",
    }
    try:
        response = requests.get(url=url, proxies=proxies)
        # Проверяем успешность запроса по статусу ответа
        if response.status_code == 200:
            # MainWindow().tbl_user_policies = PolicyTableWidget(name="Try3", parent=MainWindow().users_tab_group_policies)
            try:
                data = response.json()
                actual_version = data[ 'tag_name' ]
                # if not startup:
                #    QMessageBox.information(ui, 'Информация',
                #                            f'Программа запущена через интерпретатор Python.\n'
                #                            f'Если необходимо обновление, воспользуйтесь инструментом pip.\n'
                #                            f'прим.: "pip install hubm-admin-panel --upgrade"')
                #    return

                if version.parse(actual_version) > version.parse(panel_version):

                    dlg = QMessageBox.question(ui, 'Проверка обновления',
                                               f'Обнаружена новая версия - {actual_version}\nСкачать?',
                                               QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                               QMessageBox.StandardButton.Yes)
                    if dlg == QMessageBox.StandardButton.Yes:
                        download_path = os.path.join(os.path.expanduser("~"), "Downloads",
                                                     "hubM Admin Panel Installer.exe")
                        directory_raw = QtWidgets.QFileDialog.getSaveFileName(ui, "Выберите папку", download_path)
                        directory = directory_raw[0]
                        if directory:
                            url = data[ 'assets' ][ 0 ][ 'browser_download_url' ]
                            print(url)
                            print(directory)
                            download_dialog = DownloadDialog(url, directory, ui)
                            download_dialog.exec()

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


        else:
            QMessageBox.critical(ui, "Ошибка", f"Ошибка: {response.status_code}"
                                               f"\n{response.text}")

    except requests.ConnectionError as e:
        QMessageBox.critical(ui, "Ошибка", f"Проверьте сетевое соединение!\n {e}")



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):

        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)



        icon_path = resource_path("res/icon.png")
        icon = QtGui.QIcon(icon_path)
        self.setWindowIcon(icon)


        ####
        self.btn_refresh_users_tab = QPushButton(self.users_list_layout)
        self.btn_refresh_users_tab.setFixedSize(16, 16)
        self.btn_refresh_users_tab.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.btn_refresh_users_tab.setStyleSheet("""
                    QPushButton {
                        border-radius: 8px;   /* Радиус равен половине ширины и высоты */
                        background-color: #202124;  /* Изменение цвета при наведении */
                        
                    }
                    QPushButton:hover {
                        background-color: #2d3b53;
                    }
                    QPushButton:pressed {
                        background-color: #3a4c69;  /* Изменение цвета при нажатии */
                    }
                """)
        ###
        self.btn_refresh_groups_tab = QPushButton(self.user_group_list_layout)
        self.btn_refresh_groups_tab.setFixedSize(16, 16)
        self.btn_refresh_groups_tab.setIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.btn_refresh_groups_tab.setStyleSheet("""
                            QPushButton {
                                border-radius: 8px;   /* Радиус равен половине ширины и высоты */
                                background-color: #202124;  /* Изменение цвета при наведении */

                            }
                            QPushButton:hover {
                                background-color: #2d3b53;
                            }
                            QPushButton:pressed {
                                background-color: #3a4c69;  /* Изменение цвета при нажатии */
                            }
                        """)
        ###
        self.btn_information = QPushButton(self)
        self.btn_information.setFixedSize(24, 24)
        self.btn_information.setIconSize(QSize(24, 24))
        self.btn_information.setFlat(False)
        self.icon_info = QIcon()
        self.icon_info.addFile(u":/res/icons/icon-hr.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.icon_info_red = QIcon()
        self.icon_info.addFile(u":/res/icons/icon-hr-red.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_information.setIcon(self.icon_info)
        self.btn_information.setStyleSheet("""
                                    QPushButton {
                                        border-radius: 12px;   /* Радиус равен половине ширины и высоты */
                                        background-color: #202124;  /* Изменение цвета при наведении */

                                    }
                                    QPushButton:hover {
                                        background-color: #2d3b53;
                                    }
                                    QPushButton:pressed {
                                        background-color: #3a4c69;  /* Изменение цвета при нажатии */
                                    }
                                """)
        ###
        ####

        self.user = User(self)
        self.groups = Groups(self)

        ### Connections
        self.tabs_general.currentChanged.connect(self.tabs_general_clicked)
        self.tabs_group.tabBarClicked.connect(self.tabs_group_clicked)
        self.tabs_users.tabBarClicked.connect(self.tabs_users_clicked)
        self.list_users.itemSelectionChanged.connect(self.entry_update_user_info)
        self.le_search_user.textChanged.connect(lambda: filter_items(self.list_users, self.le_search_user.text()))
        self.le_search_group.textChanged.connect(lambda: filter_items(self.list_groups, self.le_search_group.text()))
        self.btn_user_policies_create.clicked.connect(self.win_new_create_policies)
        self.btn_user_policies_delete.clicked.connect(self.user_policy_delete)
        self.btn_user_export.clicked.connect(self.win_user_export)
        self.btn_user_delete.clicked.connect(self.user_delete)
        self.btn_refresh_users_tab.clicked.connect(self.get_list_users)
        self.btn_user_create.clicked.connect(self.win_user_create)
        self.btn_about_program.triggered.connect(self.win_about_program)
        self.btn_check_update.triggered.connect(lambda: check_version(self, False))
        self.DevButton1.clicked.connect(self.get_class)
        self.DevButton2.clicked.connect(self.get_class2)
        # self.list_groups.itemSelectionChanged.connect(self.group_render)
        # self.btn_group_restart.clicked.connect(self.group_restart)
        ###

        self.list_users.setColumnWidth(0, 200)
        self.list_groups.setColumnWidth(0, 200)
        self.list_users.sortByColumn(0, Qt.SortOrder.AscendingOrder)

        QTimer.singleShot(0, self.resize_custom)


    def resize_custom(self):
        self.btn_refresh_users_tab.move(self.users_list_layout.width() - self.btn_refresh_users_tab.width(), 4)
        self.btn_refresh_groups_tab.move(self.user_group_list_layout.width() - self.btn_refresh_groups_tab.width(), 4)
        self.btn_information.move(self.centralwidget.width() - self.btn_information.width(), 3)



    def resizeEvent(self, event):
        self.resize_custom()

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
                # self.list_users.setCurrentItem(None)
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

                data = [ ]
                order = [ ]
                try:
                    if not win_user_export.ui.cb_enable_group_policies.isChecked():
                        order = [ 'cn', 'name', 'email', 'ip', 'comment', 'active' ]

                        response = api_request("users/", request="full")
                        data = json.loads(response.text)[ 'users' ]

                    if win_user_export.ui.cb_enable_group_policies.isChecked() and not win_user_export.ui.cb_enable_usb_policies.isChecked():
                        order = [ 'cn', 'name', 'email', 'ip', 'comment', 'active', 'groups' ]

                        response = api_request("users/?type=servers", request="full")
                        data = json.loads(response.text)[ 'users' ]
                        for user in data:
                            # Получаем группы пользователя
                            # user['active'] = "True" if user['active'] else "False"
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
                            # user['active'] = "True" if user['active'] else "False"

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
        # if self.groups is not None:
        #    print("DELETE")
        #    del self.groups
        # self.groups = Groups(self)
        self.groups.render_groups(self)

    def tabs_general_clicked(self, index):
        match index:
            case 0:
                print("Дэшборд")
                # print(self.tabs_general.currentWidget().objectName())
            case 1:
                print("Пользователи")
                # print(self.tabs_general.currentWidget().objectName())
                self.clear_user_info()
                self.get_list_users()
            case 2:
                print("Группы")
                # print(self.tabs_general.currentWidget().objectName())
                self.groups.refresh()
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
        otp_secret = (4, "password")
        password = (5, "password")
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
        def get_type(cls, type):
            data = [ ]
            for enum_member in cls:
                if enum_member.value[ 1 ] == type:
                    value = {'name': enum_member.name, 'id': enum_member.value[ 0 ]}
                    data.append(value)
            return data

        @classmethod
        def get_all_names_with_type(cls):
            value = {enum_member.name: enum_member.value[ 1 ] for enum_member in cls}
            return json.dumps(value)

        @classmethod
        def get_all_names_with_index(cls):
            value = {enum_member.name: enum_member.value[ 0 ] for enum_member in cls}
            return json.dumps(value)

    def update_user_info(self, item):
        self.user.init(item)

    def win_new_create_policies(self):
        if not self.user:
            QMessageBox.warning(self, "Ошибка", f"Пользователь не выбран!")
            return

        username = self.user.name

        win_create_policies = CreatePolicies(self.user.dict[ 'ip' ])
        groups = self.get_groups_list_text()
        win_create_policies.ui.le_group.addItems(groups)
        if win_create_policies.exec() == QDialog.DialogCode.Accepted:
            data = win_create_policies.save()
            group = data[ "group" ]
            usb_list = data[ "usb_allowed" ]
            for usb in usb_list:
                response = api_request(f"users/{username}/ports/{usb}", {}, json.dumps(data), "POST", "full")
                if response.status_code == 200:
                    # QMessageBox.information(self, "Информация", f"Политика успешно добавлена.")
                    pass
                elif response.status_code == 409:
                    # QMessageBox.critical(self, "Ошибка", f"Неправильный токен!")
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
    def __init__(self, *args, **kwargs):
        super(Launch, self).__init__(*args, **kwargs)
        self.setupUi(self)
        icon = QtGui.QIcon(resource_path("res/icon.png"))
        self.setWindowIcon(icon)

        self.cred_username = None
        self.cred_userpass = None
        self.cred_label = None

        # self.cb_creds.currentTextChanged.connect(self.change_cred)

        self.load_creds()
        self.load_servers()

        self.btn_connect.clicked.connect(self.to_connect)
        self.btn_creds_delete.clicked.connect(self.delete_cred)
        self.btn_server_delete.clicked.connect(self.delete_server)
        self.btn_creds_new.clicked.connect(self.create_cred)
        self.btn_server_new.clicked.connect(self.create_server)
        self.cb_creds.currentTextChanged.connect(self.validator)
        self.cb_servers.currentTextChanged.connect(self.validator)
        self.menu_update.triggered.connect(lambda: check_version(self, startup=False))
        self.menu_connect.triggered.connect(self.to_connect)
        self.menu_reset_creds.triggered.connect(lambda: (utils.utils.delete_creds(), self.load_creds()))
        self.menu_reset_servers.triggered.connect(lambda: (utils.utils.delete_servers(), self.load_servers()))
        self.menu_reset_all_profiles.triggered.connect(lambda: (utils.utils.delete_all_profiles(), self.load_creds(), self.load_servers()))
        self.menu_reset_master_password.triggered.connect(lambda: QMessageBox.information(self, "Информация",
                    "Сброс мастер пароля не возможен. Если он был утерян, необходимо удалить профиль к которому он был привязан."))
        self.validator()


    def validator(self):
        if self.cb_creds.currentText() != "" and self.cb_servers.currentText() != "":
            self.btn_connect.setEnabled(True)
        else:
            self.btn_connect.setEnabled(False)

    def load_creds(self):
        self.cb_creds.clear()
        if config[ "creds" ]:
            for cred in config[ "creds" ]:
                self.cb_creds.addItem(cred[ "label" ])

        if config[ "last_cred" ]:
            last_cred = config[ "last_cred" ]

            # Получаем пароль для last_cred из словаря creds
            for cred in config[ "creds" ]:
                if cred[ "label" ] == last_cred:
                    self.cb_creds.setCurrentText(cred[ "label" ])
                    break

    def load_servers(self):
        self.cb_servers.clear()
        if config[ "servers" ]:
            for server in config[ "servers" ]:
                self.cb_servers.addItem(server[ "label" ])

        if config[ "last_server" ]:
            last_server = config[ "last_server" ]

            # Получаем пароль для last_cred из словаря creds
            for server in config[ "servers" ]:
                if server[ "label" ] == last_server:
                    self.cb_servers.setCurrentText(server[ "label" ])
                    break

    def create_cred(self):
        if not config[ "creds" ]:
            dialog = launch_dialogs.MasterPasswordSetDialog()  # Открываем диалог добавления сервера
            if dialog.exec():  # exec() вернет True, если диалог завершен успешно
                utils.utils.master_password = dialog.master_password
            else:
                return
        else:
            dialog = launch_dialogs.MasterPasswordGetDialog()
            if dialog.exec():  # exec() вернет True, если диалог завершен успешно
                utils.utils.master_password = dialog.master_password
            else:
                return
        dialog = launch_dialogs.CredDialog()
        if dialog.exec():  # exec() вернет True, если диалог завершен успешно
            username = dialog.username
            password = utils.utils.encrypt_data(dialog.password, utils.utils.master_password)
            label = dialog.label

            # Проверка уникальности имени пользователя
            if any(cred[ "label" ] == label for cred in config[ "creds" ]):
                QMessageBox.warning(self, "Ошибка", "Профиль подключения уже существует!")
            else:
                # Добавляем нового пользователя в конфиг
                new_cred = {
                    "username": username,
                    "password": password,
                    "label": label
                }
                config[ "creds" ].append(new_cred)
                utils.utils.write_config()
                self.load_creds()
                QMessageBox.information(self, "Информация", f"Новый профиль подключения добавлен: {label}")

    def create_server(self):
        dialog = launch_dialogs.ServerDialog()  # Открываем диалог добавления сервера
        if dialog.exec():  # exec() вернет True, если диалог завершен успешно
            label = dialog.label
            address = dialog.address
            port = dialog.port

            # Проверка уникальности названия сервера
            if any(server[ "label" ] == label for server in config[ "servers" ]):
                QMessageBox.warning(self, "Ошибка", "Профиль сервера уже существует!")
            else:
                # Добавляем новый сервер в конфиг
                new_server = {
                    "label": label,
                    "address": address,
                    "port": port
                }
                config[ "servers" ].append(new_server)
                utils.utils.write_config()
                self.load_servers()  # Обновляем список серверов в интерфейсе
                QMessageBox.information(self, "Информация", f"Новый профиль сервера добавлен: {label}")

    def delete_cred(self):
        # Получаем текущий выбранный label
        label = self.cb_creds.currentText()

        # Диалог подтверждения
        reply = QMessageBox.question(
            self,
            "Подтверждение удаления",
            f"Вы действительно хотите удалить профиль подключения '{label}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        # Проверяем, подтвердил ли пользователь удаление
        if reply == QMessageBox.StandardButton.Yes:
            # Удаляем учетные данные и обновляем список, если удаление прошло успешно
            if utils.utils.delete_cred(label):
                self.load_creds()
                QMessageBox.information(self, "Удалено", f"Профиль подключения '{label}' успешно удален.")
            else:
                QMessageBox.warning(self, "Ошибка", f"Профиль подключения '{label}' не найден.")

    def delete_server(self):
        # Получаем текущий выбранный label
        label = self.cb_servers.currentText()

        # Диалог подтверждения
        reply = QMessageBox.question(
            self,
            "Подтверждение удаления",
            f"Вы действительно хотите удалить профиль сервера '{label}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        # Проверяем, подтвердил ли пользователь удаление
        if reply == QMessageBox.StandardButton.Yes:
            # Удаляем учетные данные и обновляем список, если удаление прошло успешно
            if utils.utils.delete_server(label):
                self.load_servers()
                QMessageBox.information(self, "Удалено", f"Профиль сервера '{label}' успешно удален.")
            else:
                QMessageBox.warning(self, "Ошибка", f"Профиль сервера '{label}' не найден.")

    def to_connect(self):
        config[ "last_cred" ] = self.cb_creds.currentText()
        config[ "last_server" ] = self.cb_servers.currentText()
        utils.utils.write_config()
        dialog = launch_dialogs.MasterPasswordGetDialog()  # Открываем диалог добавления сервера
        if dialog.exec():  # exec() вернет True, если диалог завершен успешно
            utils.utils.master_password = dialog.master_password
        else:
            return

        try:
            response = api_request("servers/", request="full")
            # Проверяем успешность запроса по статусу ответа
            if response.status_code == 200:
                # MainWindow().tbl_user_policies = PolicyTableWidget(name="Try3", parent=MainWindow().users_tab_group_policies)
                try:
                    self.new_window = MainWindow()
                    self.new_window.show()
                    self.close()
                except Exception as e:
                    log.exception("Error!")
                    # console.print_exception(show_locals=True)
                    # console.print_exception(show_locals=True)
                    # print(console.export_html())
                    QMessageBox.critical(self, "Ошибка", f"{e}")

            elif response.status_code == 401:
                QMessageBox.critical(self, "Ошибка", f"Некорректные учетные данные! {response.status_code}"
                                                     f"\n{response.text}")
            elif response.status_code == 403:
                QMessageBox.critical(self, "Ошибка", f"Не хватает прав! {response.status_code}"
                                                     f"\n{response.text}")
            else:
                QMessageBox.critical(self, "Ошибка", f"Ошибка: {response.status_code}"
                                                     f"\n{response.text}")



        except requests.Timeout:
            QMessageBox.critical(self, "Ошибка", "Превышен таймаут ожидания!")

        except requests.ConnectTimeout:
            QMessageBox.critical(self, "Ошибка", "Превышен таймаут ожидания!")

        except requests.ConnectionError:
            QMessageBox.critical(self, "Ошибка", "Проверьте сетевое соединение!")

        except InvalidToken:
            QMessageBox.critical(self, "Ошибка", "Некорректный мастер пароль!")


app = QtWidgets.QApplication(sys.argv)
qdarktheme.setup_theme()
window = Launch()
window.show()
check_version(window, True)

app.exec()
