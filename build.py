import os
#import shutil
import subprocess
import argparse

import PyInstaller.__main__
from ui.convert import convert

nsis_path = "C:\\Program Files (x86)\\NSIS"

current_directory = os.path.abspath(os.path.dirname(__file__))
os.chdir(current_directory)

def main(reconvert_ui, installer):
    if reconvert_ui:
        convert()

    #if os.path.exists("build"):
    #    shutil.rmtree("build")
    #if os.path.exists("dist"):
    #    shutil.rmtree("dist")
    res_path = os.path.join(current_directory, 'res')
    icon_path = os.path.join(res_path, 'icon.ico')

    pyinstaller_args = [
        '--name=hubM Admin Panel',
        '--onedir',
        '--noconfirm',
        '--windowed',
        f'--icon={icon_path}',
        f'--add-data={res_path};res/',
        '--exclude-module=PySide6',
        '--exclude-module=PyQt5',
        '--contents-directory=.',
        'main.py'
    ]
    PyInstaller.__main__.run(pyinstaller_args)

    if installer:
        print("Creating installer...")
        result = subprocess.run(
            [os.path.join(nsis_path, 'makensis.exe'), 'installer_script.nsi'],
            capture_output=True,
            text=True,
            cwd=current_directory,
        )

        if result.returncode != 0:
            print(f"Error during creating installer! {result.stderr}")
            return

        print(f"Result:\n{result.stdout}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Build and optionally create an installer.')
    parser.add_argument('-U', '--reconvert-ui', action='store_true', help='Reconvert the UI')
    parser.add_argument('-I', '--installer', action='store_true', help='Create installer')

    args = parser.parse_args()

    main(args.reconvert_ui, args.installer)