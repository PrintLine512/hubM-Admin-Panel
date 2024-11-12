import json
from typing import Literal

from . import config, config_file
from . import session

api_version = "v2"


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
            "password": cred_pass
        }

        response = session.post(f"http://{server_address}:{server_port}/login", json=login_data, headers=headers,
                                proxies=proxies)

        if response.status_code == 200:
            print("Login successful!")
            return True
        else:
            print(f"Login failed with status code {response.status_code}")
            return False

    if method == "GET":
        response = session.get(url, headers=headers, data=new_data, proxies=proxies)
    elif method == "PUT":
        response = session.put(url, headers=headers, data=new_data, proxies=proxies)
    elif method == "POST":
        response = session.post(url, headers=headers, data=new_data, proxies=proxies)
    elif method == "DELETE":
        response = session.delete(url, headers=headers, data=new_data, proxies=proxies)
    else:
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
            if request == "basic":
                return response.text
            elif request == "full":
                return response
            else:
                return response.text

        # Проверка на доступ (403 Forbidden)
    elif response.status_code == 403:
        print(f"Access denied: {response.status_code}")
        return "Error: Forbidden access. You don't have permission to access this resource."

    if request == "basic":
        return response.text
    elif request == "full":
        return response
    else:
        return response.text
