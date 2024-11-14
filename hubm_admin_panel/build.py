import argparse
import os
# import shutil
import subprocess
import tomllib

import PyInstaller.__main__

from hubm_admin_panel.ui.convert_res import convert_res
from hubm_admin_panel.ui.convert_ui import convert_ui

nsis_path = "C:\\Program Files (x86)\\NSIS"

current_directory = os.path.abspath(os.path.dirname(__file__))
previous_dir = os.path.join(current_directory, "..")


def main(reconvert_ui, reconvert_resource, no_installer):
    if reconvert_ui:
        convert_ui()

    if reconvert_resource:
        convert_res()

    # if os.path.exists("build"):
    #    shutil.rmtree("build")
    # if os.path.exists("dist"):
    #    shutil.rmtree("dist")
    main_path = os.path.join(current_directory, "main.py")
    dist_path = os.path.join(previous_dir, 'dist')
    work_path = os.path.join(previous_dir, 'build')
    # spec_path = os.path.join(previous_dir, 'spec')
    res_path = os.path.join(previous_dir, 'res')
    icon_path = os.path.join(res_path, 'icon.ico')
    toml_path = os.path.join(previous_dir, 'pyproject.toml')
    version_path = os.path.join(current_directory, 'version.py')

    with open(toml_path, "rb") as f:
        data = tomllib.load(f)

    version = data[ "tool" ][ "poetry" ][ "version" ]
    with open(version_path, "w") as f:
        f.write(f"panel_version=\"{version}\"")

    pyinstaller_args = [
        '--name=hubM Admin Panel',
        '--onedir',
        '--noconfirm',
        '--windowed',
        f'--icon={icon_path}',
        f'--add-data={res_path};res/',
        f'--distpath={dist_path}',
        f'--workpath={work_path}',
        f'--specpath={work_path}',
        '--exclude-module=PyQt6',
        '--exclude-module=PyQt5',
        '--contents-directory=.',
        f'{main_path}'
    ]
    PyInstaller.__main__.run(pyinstaller_args)

    if not no_installer:
        print("Creating installer...")
        installer_script_path = os.path.join(previous_dir, "installer_script.nsi")
        result = subprocess.run(
            [ os.path.join(nsis_path, 'makensis.exe'), installer_script_path ],
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
    parser.add_argument('-i', '--no-installer', action='store_true', help='Create installer')
    parser.add_argument('-R', '--reconvert-resource', action='store_true', help='Reconvert the resource')

    args = parser.parse_args()

    main(args.reconvert_ui, args.reconvert_resource, args.no_installer)
