from PySide6.QtCore import QUrl, QObject, Slot, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
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

    def connect(self):
        self.output_widget.append("Connecting to WebSocket server...")
        self.socket.open(QUrl(self.url))

    @Slot()
    def on_connected(self):
        self.output_widget.append("Connected to server!")
        self.socket.sendTextMessage("Hello, WebSocket Server!")

    @Slot(str)
    def on_message_received(self, message):
        self.output_widget.append(f"Received message: {message}")

    @Slot()
    def on_error(self, error):
        self.output_widget.append(f"Error: {self.socket.errorString()}")

    def close(self):
        if self.socket.state() == QWebSocket.ConnectedState:
            self.socket.close()

class WebSocketClientWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WebSocket Client")
        self.resize(400, 300)

        # Виджеты
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.connect_button = QPushButton("Connect to WebSocket Server")

        # Макет
        layout = QVBoxLayout()
        layout.addWidget(self.output)
        layout.addWidget(self.connect_button)
        self.setLayout(layout)

        # Инициализация WebSocket клиента
        self.client = WebSocketClient("ws://hubm.smt.local:5000/socket.io/?transport=websocket", self.output)
        # Подключение сигнала к кнопке
        self.connect_button.clicked.connect(self.client.connect)

    def closeEvent(self, event):
        self.client.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication([])

    window = WebSocketClientWindow()
    window.show()
    app.exec()
