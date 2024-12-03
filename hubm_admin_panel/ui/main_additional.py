import json
import os
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QThread, QUrl
from PySide6.QtGui import QScreen, QPixmap, QIcon
from PySide6.QtMultimedia import QSoundEffect, QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QLabel, QWidget, QApplication, QVBoxLayout, QMessageBox
from urllib.request import urlopen, ProxyHandler, build_opener, install_opener


from typing import TYPE_CHECKING, LiteralString

from Tools.scripts.make_ctype import method

from utils.utils import api_request

if TYPE_CHECKING:
    from main import MainWindow
from ui.ui_notifications import Ui_Notifications
from ui.ui_notification import Ui_Notification

class CheckLabel(QLabel):
    def __init__(self, text_on: str, text_off: str, state: bool, parent=None):
        super().__init__(parent=parent)
        self.state = None
        self.text_on = text_on
        self.text_off = text_off
        #self.setState(state)
        self.setText("Нет информации")


    def setState(self, state: bool):
        if state:
            self.state = state
            self.setStyleSheet(f"color: green;")
            self.setText(self.text_on)
        else:
            self.state = state
            self.setStyleSheet(f"color: red;")
            self.setText(self.text_off)

    def state(self):
        return self.state

class Downloader(QThread):
    no_proxy_handler = ProxyHandler({})
    opener = build_opener(no_proxy_handler)
    install_opener(opener)


    def __init__(self, url, filename):
        super().__init__()
        self._url = url
        self._filename = filename

    def run(self):
        readBytes = 0
        chunkSize = 1024
        with urlopen(self._url) as r:
            with open(self._filename, "wb") as f:
                while True:
                    chunk = r.read(chunkSize)
                    if not chunk:
                        break
                    f.write(chunk)
                    readBytes += len(chunk)
        self.succeeded.emit()



class DownloadDialog():
    def __init__(self, download_url, save_path, parent: "Notifications"):
        super().__init__(parent)
        #self.resize(300, 100)
        self.save_path = save_path
        self.parent = parent

        self.downloader = Downloader(download_url, self.save_path)
        self.downloader.succeeded.connect(self.downloadSucceeded)
        #self.downloader.finished.connect(self.close)
        self.downloader.start()

    def downloadSucceeded(self):

        self.parent.add_notification(icon="info", title="Обновление",
                              content="Обновление загружено.\nОткрыть?",
                              add_button=True, btn_icon="download", btn_text="Скачать", btn_action=self.open)


    def open(self):
        os.startfile(self.save_path)
        QApplication.quit()
        sys.exit()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Notifications(QWidget):
    def __init__(self, parent: 'MainWindow', ui):
        super().__init__(parent=parent)
        self.ui = Ui_Notifications()  # Инициализация интерфейса
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.is_download_notify_exist = False
        self.usb_errors = []
        self.server_errors = []
        self.ui_main = ui


        sound = resource_path("res/notification.wav")

        self.notification_sound = QSoundEffect()
        self.notification_sound.setSource(QUrl.fromLocalFile(sound))  # Укажите свой файл
        self.notification_sound.setVolume(0.5)
        #self.ui.scroll_area_contents.focusOutEvent = self.focusOutEvent_n
        self.ui.scroll_area.focusOutEvent = self.focusOutEvent_n

        #self.setWindowOpacity(0.5)

        #self.notification_layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        #self.notification_layout.setContentsMargins(0, 0, 0, 0)
        #self.notification_layout.setSpacing(10)

        #self.add_notification(icon="error", title="Ошибка", content="Ошибка USB порта - 1-1.1.5.9.2",
        #                      add_button=True, btn_icon="reset", btn_text="Сбросить ошибку")
        #self.add_notification(icon="info", title="Обновление", content="Обнаружено обновление.\nСкачать?\nСкачать?\nСкачать?\nСкачать?\nСкачать?\nСкачать?\nСкачать?\nСкачать?\nСкачать?\nСкачать?\nСкачать?\nСкачать?")
        #self.add_notification(icon="info", title="Обновление", content="Обнаружено обновление.\nСкачать в фоновом режиме?",
        #                      add_button=True, btn_icon="download", btn_text="Скачать")

    def focusOutEvent_n(self, event):
        """Переопределяем обработчик события потери фокуса."""
        super().focusOutEvent(event)  # Обрабатываем базовое событие
        self.switch_show() # Генерируем сигнал

    def switch_show(self):
        self.adjust()
        self.stick_to_parent()
        if self.isHidden():
            self.show()
            self.ui.scroll_area.setFocus()
            self.ui.scroll_area_contents.setFocus()
            self.setFocus()
            self.ui_main.btn_information_icon_set()
        else:
            self.hide()


    def add_notification(self, icon, title, content, add_button=False, btn_icon=None, btn_text=None, btn_action=None, btn_close_action=None):
        """Добавить новое уведомление"""
        notify = Notification(self, icon=icon, title=title, content=content, add_button=add_button, btn_icon=btn_icon, btn_text=btn_text, btn_action=btn_action, btn_close_action=lambda: btn_close_action)
        self.ui.scroll_area_contents.layout().addWidget(notify)
        self.adjust()

    def add_usb_error_notify(self, usb_ports):
        for usb_port in usb_ports:
            if usb_port not in self.usb_errors:
                print(f"CREATOR: {usb_port}")
                notify = UsbErrorNotification(self, usb_port)
                self.ui.scroll_area_contents.layout().addWidget(notify)
                self.adjust()
                self.usb_errors.append(usb_port)
                self.notification_sound.play()
                self.ui_main.btn_information_icon_set("red")
                QApplication.alert(self.ui_main)


    def usb_errors_del(self, usb_port):
        self.usb_errors.remove(usb_port)


    def add_download_notify(self):
        if not self.is_download_notify_exist:
            self.add_notification(icon="info", title="Обновление",
                                  content="Обнаружено обновление.\nСкачать в фоновом режиме?",
                                  add_button=True, btn_icon="download", btn_text="Скачать", btn_action=self.process_download)
            self.is_download_notify_exist = True

    def process_download(self, url):
        download_path = os.path.join(os.path.expanduser("~"), "Downloads",
                                     "hubM Admin Panel Installer.exe")
        directory_raw = QtWidgets.QFileDialog.getSaveFileName(self.parent().ui, "Выберите папку", download_path)
        directory = directory_raw[ 0 ]
        if directory:
            download_dialog = DownloadDialog(url, directory, self.parent().ui)
            download_dialog.exec()

        else:
            QMessageBox.critical(self.parent().ui, 'Ошибка',
                                 'Некорректный путь. Загрузка отменена.')



    def stick_to_parent(self):
        """Прилепить к правому краю родительского окна"""
        # Получаем геометрию родительского окна
        parent_geometry = self.parent().geometry()
        parent_global_position = self.parent().mapToGlobal(parent_geometry.topLeft())

        # Вычисляем новые координаты
        x = parent_global_position.x() + parent_geometry.width() - self.width()
        y = parent_global_position.y() - 40

        # Перемещаем виджет
        self.move(x, y)

    def adjust(self):
        self.ui.scroll_area_contents.adjustSize()
        #self.ui.scroll_area.adjustSize()
        print("ADJUST")



class Notification(QWidget):
    def __init__(self, parent: 'Notifications', icon, title, content, add_button=False, btn_icon=None, btn_text=None, btn_action=None, btn_close_action=None):
        super().__init__(parent=parent)
        self.ui = Ui_Notification()  # Инициализация интерфейса
        self.ui.setupUi(self)
        print(f"CREATOR: {btn_action}")

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        if icon == "info":
            self.ui.lb_icon.setPixmap(QPixmap(u":/res/icons/icon-hr.png.png"))
        elif icon == "error":
            self.ui.lb_icon.setPixmap(QPixmap(u":/res/icons/icon-red-hr.png"))
        else:
            raise ValueError

        self.ui.lb_title.setText(title)
        self.ui.lb_content.setText(content)
        if not btn_close_action:
            self.ui.btn_close.clicked.connect(lambda: (self.close(), parent.adjust()))
        else:
            self.ui.btn_close.clicked.connect(btn_close_action)
        if add_button:
            self.ui.btn_2.setEnabled(True)
            self.ui.btn_2.setText(btn_text)
            if btn_icon == "download":
                self.ui.btn_2.setIcon(QIcon(QIcon.fromTheme(u"emblem-downloads")))
            elif btn_icon == "reset":
                self.ui.btn_2.setIcon(QIcon(QIcon.fromTheme(u"view-restore")))

            self.ui.btn_2.clicked.connect(btn_action)

class UsbErrorNotification(Notification):
    def __init__(self, parent: 'Notifications', usb_port):
        # Вызов конструктора родительского класса
        icon="error"
        title="Ошибка"
        content=f"Ошибка USB порта - {usb_port}!\nПерезагрузите или переподключите его."
        add_button=True
        btn_icon="reset"
        btn_text="Сбросить ошибку"
        btn_action=self.reset_error
        btn_close_action = self.close_error
        self.usb_port = usb_port
        self.parent_n = parent

        super().__init__(parent, icon, title, content, add_button, btn_icon, btn_text, btn_action, btn_close_action)

    def close_error(self):
        self.close()
        self.parent_n.adjust()
        self.parent_n.usb_errors_del(self.usb_port)


    def reset_error(self):
        data = {
            "usb-ports": [
                {"virtual_port": self.usb_port}
            ]
        }

        response = api_request(f"errors", new_data=json.dumps(data), new_headers={}, method='DELETE', request="full")

        if response.status_code == 200:
            QMessageBox.information(self, "Информация",
                                    f"Ошибка была успешно сброшена.")
            self.close_error()
        else:
            QMessageBox.critical(self, "Ошибка",
                                 f"Ошибка: {response.status_code}"
                                 f"\n {response.text}")








