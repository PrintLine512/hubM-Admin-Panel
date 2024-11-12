import os
import re

from PySide6 import QtGui
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFrame, QSpacerItem, \
    QSizePolicy, QHBoxLayout


def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )


class CredDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        icon = QtGui.QIcon(resource_path("res/icon.png"))
        self.setWindowIcon(icon)
        self.setFixedSize(500, 165)
        # Устанавливаем заголовок окна
        self.setWindowTitle("Добавить новый профиль подключения")

        # Инициализируем возвращаемые данные
        self.username = None
        self.password = None
        self.label = None

        # Компоновка
        layout = QVBoxLayout()

        # Поле для ввода названия профиля
        label_layout = QHBoxLayout()
        label = QLabel("Название профиля:")
        label.setFixedWidth(125)
        label_layout.addWidget(label)
        self.label_input = QLineEdit(self)
        label_layout.addWidget(self.label_input)
        layout.addLayout(label_layout)

        # Поле для ввода имени пользователя
        label_layout = QHBoxLayout()
        label = QLabel("Имя пользователя:")
        label.setFixedWidth(125)
        label_layout.addWidget(label)
        self.username_input = QLineEdit(self)
        label_layout.addWidget(self.username_input)
        layout.addLayout(label_layout)

        # Поле для ввода пароля
        label_layout = QHBoxLayout()
        label = QLabel("Пароль:")
        label.setFixedWidth(125)
        label_layout.addWidget(label)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        label_layout.addWidget(self.password_input)
        layout.addLayout(label_layout)

        layout.addItem(QSpacerItem(4, 4, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)  # Горизонтальная линия
        separator.setFrameShadow(QFrame.Shadow.Sunken)  # Вдавленная тень для эффекта
        layout.addWidget(separator)

        # Кнопка для подтверждения
        add_button = QPushButton("Добавить")
        add_button.clicked.connect(self.accept)  # Принять и закрыть диалог
        layout.addWidget(add_button)

        # Установка компоновки
        self.setLayout(layout)

    def accept(self):
        # Получаем введенные данные
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        label = self.label_input.text().strip()

        # Проверяем, что поля не пустые
        if not username or not password or not label:
            QMessageBox.warning(self, "Ошибка", "Название профиля, имя пользователя и пароль не могут быть пустыми.")
            return

        # Устанавливаем возвращаемые данные
        self.username = username
        self.password = password
        self.label = label

        # Закрываем диалог с флагом успешного завершения
        super().accept()


class ServerDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        icon = QtGui.QIcon(resource_path("res/icon.png"))
        self.setWindowIcon(icon)
        self.setFixedSize(500, 165)
        self.setWindowTitle("Добавить новый профиль сервера")

        # Инициализируем возвращаемые данные
        self.label = None
        self.address = None
        self.port = None

        # Компоновка
        layout = QVBoxLayout()

        # Поле для ввода названия сервера
        label_layout = QHBoxLayout()
        label = QLabel("Название профиля:")
        label.setFixedWidth(125)
        label_layout.addWidget(label)
        self.label_input = QLineEdit(self)
        label_layout.addWidget(self.label_input)
        layout.addLayout(label_layout)

        # Поле для ввода адреса сервера
        label_layout = QHBoxLayout()
        label = QLabel("Адрес сервера:")
        label.setFixedWidth(125)
        label_layout.addWidget(label)
        self.address_input = QLineEdit(self)
        label_layout.addWidget(self.address_input)
        layout.addLayout(label_layout)

        # Поле для ввода порта
        label_layout = QHBoxLayout()
        label = QLabel("Порт:")
        label.setFixedWidth(125)
        label_layout.addWidget(label)
        self.port_input = QLineEdit(self)
        self.port_input.setValidator(QtGui.QIntValidator())  # Ограничиваем ввод только чисел
        label_layout.addWidget(self.port_input)
        layout.addLayout(label_layout)

        layout.addItem(QSpacerItem(4, 4, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)  # Горизонтальная линия
        separator.setFrameShadow(QFrame.Shadow.Sunken)  # Вдавленная тень для эффекта
        layout.addWidget(separator)

        # Кнопка для подтверждения
        add_button = QPushButton("Добавить")
        add_button.clicked.connect(self.accept)
        layout.addWidget(add_button)

        # Установка компоновки
        self.setLayout(layout)

    def accept(self):
        # Получаем введенные данные
        label = self.label_input.text().strip()
        address = self.address_input.text().strip()
        port = self.port_input.text().strip()

        # Проверяем, что поля не пустые
        if not label or not address or not port:
            QMessageBox.warning(self, "Ошибка", "Название профиля, адрес и порт не могут быть пустыми.")
            return

        if not self.is_valid_address(address):
            QMessageBox.warning(self, "Ошибка", "Введите корректный IP-адрес или доменное имя.")
            return

        # Устанавливаем возвращаемые данные
        self.label = label
        self.address = address
        self.port = port

        # Закрываем диалог с флагом успешного завершения
        super().accept()

    def is_valid_address(self, address):
        # Регулярное выражение для проверки IP-адреса или доменного имени
        ip_pattern = re.compile(
            r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
        hostname_pattern = re.compile(r'^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z]{2,})+$')

        # Проверяем, соответствует ли введенный адрес одному из шаблонов
        return bool(ip_pattern.match(address) or hostname_pattern.match(address))