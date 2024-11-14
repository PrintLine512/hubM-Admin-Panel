import json
import os
import sys
import requests


session = requests.session()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


config_file = resource_path("config.json")

if os.path.exists(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
else:
    # Если файл не существует, создаем конфигурацию с подсекциями
    config = {
        "last_server": "",
        "last_cred": "",
        "servers": [ ],
        "creds": [ ]
    }

    # Запись конфигурации в файл
    with open(config_file, 'w') as file:
        json.dump(config, file, indent=4)

    print(f"Config file '{config_file}' created with default values.")
