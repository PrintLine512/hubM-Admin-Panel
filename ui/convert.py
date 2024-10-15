import os
import glob

# Получаем список всех файлов с расширением .ui
ui_files = glob.glob('*.ui')

# Проходим по каждому .ui файлу и создаем соответствующий .py файл
for ui_file in ui_files:
    #py_file = os.path.join(os.path.abspath('..'), ui_file.replace('.ui', '.py'))
    py_file = ui_file.replace('.ui', '.py')
    print(f"Working with {ui_file}...")
    try:
        os.system(f'pyuic6 {ui_file} -o "{py_file}"')
        print(f"Done!")
    except:
        print(f"Unexpected error!")