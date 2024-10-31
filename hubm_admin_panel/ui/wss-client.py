import socketio

# Создаем клиентский сокет
sio = socketio.Client()

# Определяем обработчик для события 'connect'
@sio.event
def connect():
    print("Подключен к серверу")

# Определяем обработчик для события 'disconnect'
@sio.event
def disconnect():
    print("Отключен от сервера")

# Обработчик для получения сообщений
@sio.on('message')
def handle_message(data):
    print(f"Получено сообщение: {data}")

# Определяем функцию для отправки сообщения
def send_message(message):
    sio.emit('message', message)

# Подключаемся к серверу
sio.connect('http://hubm.smt.local:5000')  # Замените URL на адрес вашего сервера

# Пример отправки сообщений
try:
    while True:
        message = input("Введите сообщение (или 'exit' для выхода): ")
        if message.lower() == 'exit':
            break
        send_message(message)
except KeyboardInterrupt:
    pass
finally:
    sio.disconnect()