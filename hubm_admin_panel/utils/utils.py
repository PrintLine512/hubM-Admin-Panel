import winreg
import requests

api_version = "v1"

def get_registry_value(parent_key, sub_key, name):
    try:
        key = winreg.OpenKey(parent_key, sub_key, 0, winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(key, name)
        winreg.CloseKey(key)
        return value
    except FileNotFoundError:
        return None


TOKEN = get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\PrintLine", "hubM_AP_token")
server = get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\PrintLine", "hubM_AP_address")
api_port = get_registry_value(winreg.HKEY_CURRENT_USER, "Software\\PrintLine", "hubM_AP_tcp_port")
api_base_dir = f":{api_port}/api/{api_version}"

def api_request(uri, new_headers=None, new_data=None, method="GET", request="basic", ):
    if new_data is None:
        new_data = {}
    if new_headers is None:
        new_headers = {}
    url = f"http://{server}{api_base_dir}/{uri}"
    print(url)
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": TOKEN,
        **new_headers
    }
    # data = {
    #    **new_data
    # }
    if method == "GET":
        response = requests.get(url, headers=headers, data=new_data)
    elif method == "PUT":
        response = requests.put(url, headers=headers, data=new_data)
    elif method == "POST":
        response = requests.post(url, headers=headers, data=new_data)
    elif method == "DELETE":
        response = requests.delete(url, headers=headers, data=new_data)
    else:
        return

    if request == "basic":
        return response.text
    elif request == "full":
        return response
    else:
        return response.text





