import json
from typing import Literal, TYPE_CHECKING

import requests
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QTreeWidget
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
import os
from . import config, config_file
from . import session



master_password = None
api_version = "v2"


def filter_items(list: "QTreeWidget", query_raw):
    query = query_raw.strip().lower()  # Получаем текст из строки поиска и приводим к нижнему регистру

    # Если строка пустая, показываем все элементы
    if not query:
        show_all_items(list)
        return

    for i in range(list.topLevelItemCount()):
        item = list.topLevelItem(i)
        match_found = filter_item(item, query)
        item.setHidden(not match_found)  # Скрываем элемент, если нет совпадения


def filter_item(item, query) -> bool:
    match = query in item.text(0).lower() or query in item.text(1).lower()
    return match


def show_all_items(list):
    """Показывает все элементы в QTreeWidget."""
    for i in range(list.topLevelItemCount()):
        list.topLevelItem(i).setHidden(False)


def generate_key_from_password(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# Шифрование данных
def encrypt_data(data, password):
    salt = os.urandom(16)
    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    # Кодируем соль и зашифрованные данные в base64 для сохранения в JSON
    return base64.b64encode(salt + encrypted_data).decode()

# Дешифровка данных
def decrypt_data(encrypted_data_b64, password):
    # Декодируем из base64 обратно в байты
    encrypted_data = base64.b64decode(encrypted_data_b64)
    salt = encrypted_data[:16]  # Извлекаем соль
    encrypted_data = encrypted_data[16:]
    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()

def delete_servers():
    config["servers"] = []
    write_config()

def delete_creds():
    config["creds"] = []
    write_config()

def delete_all_profiles():
    config["servers"] = []
    config["creds"] = []
    write_config()


def delete_cred(label):
    # Найти индекс элемента с указанным label
    for i, cred in enumerate(config[ "creds" ]):
        if cred[ "label" ] == label:
            # Удаляем элемент по найденному индексу
            config[ "creds" ].pop(i)
            write_config()
            return True
    return False  # Возвращаем False, если учетные данные не найдены


def delete_server(label):
    # Найти индекс элемента с указанным label
    for i, server in enumerate(config[ "servers" ]):
        if server[ "label" ] == label:
            # Удаляем элемент по найденному индексу
            config[ "servers" ].pop(i)
            write_config()
            return True
    return False  # Возвращаем False, если учетные данные не найдены


def write_config():
    with open(config_file, 'w') as file:
        json.dump(config, file, indent=4)


def api_request(uri, new_headers=None, new_data=None,
                method: Literal[ "GET", "PUT", "POST", "DELETE" ] = "GET",
                request: Literal[ 'basic', 'full' ] = "basic", full_uri=False):
    server_address = None
    server_port = None
    QApplication.setOverrideCursor(Qt.BusyCursor)

    if config[ "last_server" ]:
        last_server = config[ "last_server" ]

        # Получаем пароль для last_cred из словаря creds
        for server in config[ "servers" ]:
            if server[ "label" ] == last_server:
                server_address = server[ "address" ]
                server_port = server[ "port" ]
                break

    if config[ "last_cred" ]:
        last_cred = config[ "last_cred" ]

        # Получаем пароль для last_cred из словаря creds
        for cred in config[ "creds" ]:
            if cred[ "label" ] == last_cred:
                cred_user = cred[ "username" ]
                cred_pass = cred[ "password" ]
                break

    api_base_dir = f":{server_port}/api/{api_version}"

    if new_data is None:
        new_data = {}
    if new_headers is None:
        new_headers = {}
    if full_uri:
        url = uri
    else:
        url = f"http://{server_address}{api_base_dir}/{uri}"

    print(url)
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        **new_headers
    }
    # data = {
    #    **new_data
    # }
    proxies = {
        "http": "",
        "https": "",
    }

    def login():
        login_data = {
            "username": cred_user,
            "password": decrypt_data(cred_pass, master_password)
        }

        response = session.post(f"http://{server_address}:{server_port}/login", json=login_data, headers=headers,
                                proxies=proxies)

        if response.status_code == 200:
            print("Login successful!")
            return True
        else:
            print(f"Login failed with status code {response.status_code}")
            return False

    try:
        if method == "GET":
            response = session.get(url, headers=headers, data=new_data, proxies=proxies)
        elif method == "PUT":
            response = session.put(url, headers=headers, data=new_data, proxies=proxies)
        elif method == "POST":
            response = session.post(url, headers=headers, data=new_data, proxies=proxies)
        elif method == "DELETE":
            response = session.delete(url, headers=headers, data=new_data, proxies=proxies)
        else:
            QApplication.restoreOverrideCursor()
            return
    except requests.ConnectTimeout:
        QApplication.restoreOverrideCursor()
        raise requests.ConnectTimeout

    except requests.Timeout:
        QApplication.restoreOverrideCursor()
        raise requests.Timeout

    except Exception as e:
        print(e)
        QApplication.restoreOverrideCursor()
        return

    if response.status_code == 401:
        print("Authorization required. Attempting to log in...")
        if login():
            # Повторяем запрос после успешной авторизации
            if method == "GET":
                response = session.get(url, headers=headers, data=new_data, proxies=proxies)
            elif method == "PUT":
                response = session.put(url, headers=headers, data=new_data, proxies=proxies)
            elif method == "POST":
                response = session.post(url, headers=headers, data=new_data, proxies=proxies)
            elif method == "DELETE":
                response = session.delete(url, headers=headers, data=new_data, proxies=proxies)
        else:
            print("Failed to log in, cannot access the resource.")
            QApplication.restoreOverrideCursor()
            if request == "basic":
                return response.text
            elif request == "full":
                return response
            else:
                return response.text

        # Проверка на доступ (403 Forbidden)
    elif response.status_code == 403:
        print(f"Access denied: {response.status_code}")
        QApplication.restoreOverrideCursor()
        return "Error: Forbidden access. You don't have permission to access this resource."

    QApplication.restoreOverrideCursor()

    if request == "basic":
        return response.text
    elif request == "full":
        return response
    else:
        return response.text
