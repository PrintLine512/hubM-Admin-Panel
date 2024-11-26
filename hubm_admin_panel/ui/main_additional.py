import os
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QThread
from PySide6.QtGui import QScreen, QPixmap, QIcon
from PySide6.QtWidgets import QLabel, QWidget, QApplication, QVBoxLayout, QMessageBox
from urllib.request import urlopen, ProxyHandler, build_opener, install_opener


from typing import TYPE_CHECKING, LiteralString

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


class Notifications(QWidget):
    def __init__(self, parent: 'MainWindow'):
        super().__init__(parent=parent)
        self.ui = Ui_Notifications()  # Инициализация интерфейса
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.is_download_notify_exist = False
        #self.setWindowOpacity(0.5)

        #self.notification_layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        #self.notification_layout.setContentsMargins(0, 0, 0, 0)
        #self.notification_layout.setSpacing(10)

        #self.add_notification(icon="error", title="Ошибка", content="Ошибка USB порта - 1-1.1.5.9.2",
        #                      add_button=True, btn_icon="reset", btn_text="Сбросить ошибку")
        #self.add_notification(icon="info", title="Обновление", content="Обнаружено обновление.\nСкачать?\nСкачать?\nСкачать?\nСкачать?\nСкачать?\nСкачать?\nСкачать?\nСкачать?\nСкачать?\nСкачать?\nСкачать?\nСкачать?")
        #self.add_notification(icon="info", title="Обновление", content="Обнаружено обновление.\nСкачать в фоновом режиме?",
        #                      add_button=True, btn_icon="download", btn_text="Скачать")

    def switch_show(self):
        self.stick_to_parent()
        if self.isHidden():
            self.show()
        else:
            self.hide()

    def add_notification(self, icon, title, content, add_button=False, btn_icon=None, btn_text=None, btn_action=None):
        """Добавить новое уведомление"""
        notify = Notification(self, icon=icon, title=title, content=content, add_button=add_button, btn_icon=btn_icon, btn_text=btn_text, btn_action=btn_action)
        self.ui.scroll_area_contents.layout().addWidget(notify)
        self.adjust()

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
    def __init__(self, parent: 'Notifications', icon, title, content, add_button=False, btn_icon=None, btn_text=None, btn_action=None):
        super().__init__(parent=parent)
        self.ui = Ui_Notification()  # Инициализация интерфейса
        self.ui.setupUi(self)

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

        self.ui.btn_close.clicked.connect(lambda: (self.close(), parent.adjust()))
        if add_button:
            self.ui.btn_2.setEnabled(True)
            self.ui.btn_2.setText(btn_text)
            if btn_icon == "download":
                self.ui.btn_2.setIcon(QIcon(QIcon.fromTheme(u"emblem-downloads")))
            elif btn_icon == "reset":
                self.ui.btn_2.setIcon(QIcon(QIcon.fromTheme(u"view-restore")))

            self.ui.btn_2.clicked.connect(btn_action)






