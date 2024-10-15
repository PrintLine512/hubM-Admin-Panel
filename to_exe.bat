rmdir /s /q build
rmdir /s /q dist
pyinstaller -d=imports --noconfirm --onedir --contents-directory "." --windowed  --name "hubM Admin Panel" --exclude="PySide6" --exclude="PyQt5" --icon "res/icon.ico" --add-data "res;res/" "main.py