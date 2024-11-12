import os

rcc = "C:\\Users\\mv.alekseev\\AppData\\Local\\pypoetry\\Cache\\virtualenvs\\hubm-admin-panel-lCPXPe4P-py3.11\\Lib\\site-packages\\PySide6\\rcc.exe"


# Получаем список всех файлов с расширением .ui
def convert_res():
    current_directory = os.path.abspath(os.path.dirname(__file__))
    resource_in = (os.path.join(current_directory, 'resources.qrc'))
    resource_out = (os.path.join(current_directory, 'resources_rc.py'))

    print(f"Converting resources...")
    try:
        os.system(f'{rcc} "{resource_in}" -o "{resource_out}" -g "python"')
        # print(f"pyuic6 \"{ui_file}\" -o \"{py_file}\"")
        print(f"Done!")
    except:
        print(f"Unexpected error!")


if __name__ == '__main__':
    convert_res()
