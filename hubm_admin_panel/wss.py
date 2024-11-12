from PySide6.QtCore import QUrl, QObject, Slot, QTimer
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QToolBar, QToolButton, QMenu
from PySide6.QtWebSockets import QWebSocket

class WebSocketClient(QObject):
    def __init__(self, url, output_widget):
        super().__init__()
        self.socket = QWebSocket()
        self.url = url
        self.output_widget = output_widget

        # Подключение сигналов
        self.socket.connected.connect(self.on_connected)
        self.socket.textMessageReceived.connect(self.on_message_received)
        self.socket.errorOccurred.connect(self.on_error)

    from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QToolButton, QMenu, QVBoxLayout, QWidget
    from PySide6.QtGui import QIcon

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            # Создаем панель инструментов
            toolbar = QToolBar()

            # Создаем кнопку для панели инструментов
            tool_button = QToolButton()
            tool_button.setText("Menu Button")
            tool_button.setIcon(QIcon("path_to_icon.png"))  # Здесь можно поставить путь к иконке

            # Создаем меню
            menu = QMenu()

            # Добавляем действия в меню
            action1 = QAction("Action 1", self)
            action2 = QAction("Action 2", self)
            action3 = QAction("Action 3", self)

            # Привязываем действия к событиям
            action1.triggered.connect(self.action1_triggered)
            action2.triggered.connect(self.action2_triggered)
            action3.triggered.connect(self.action3_triggered)

            # Добавляем действия в меню
            menu.addAction(action1)
            menu.addAction(action2)
            menu.addAction(action3)

            # Устанавливаем меню в кнопке
            tool_button.setMenu(menu)
            tool_button.setPopupMode(QToolButton.MenuButtonPopup)  # Устанавливаем кнопку с раскрывающимся меню

            # Добавляем кнопку на панель инструментов
            toolbar.addWidget(tool_button)

            # Устанавливаем панель инструментов в главное окно
            self.addToolBar(toolbar)

            # Настроим центральный виджет
            central_widget = QWidget()
            layout = QVBoxLayout(central_widget)
            self.setCentralWidget(central_widget)

            self.setWindowTitle("QToolButton with Menu Example")
            self.setGeometry(100, 100, 300, 200)

        def action1_triggered(self):
            print("Action 1 triggered")

        def action2_triggered(self):
            print("Action 2 triggered")

        def action3_triggered(self):
            print("Action 3 triggered")

    # Запуск приложения
    app = QApplication([ ])
    window = MainWindow()
    window.show()
    app.exec()
