import os
import shutil
import subprocess
import click
import PyInstaller.__main__

current_directory = os.path.abspath(os.path.dirname(__file__))
nsis_path = "C:\\Program Files (x86)\\NSIS"
os.chdir(current_directory)

@click.command()
@click.option("--installer/--no-installer", "-I/-i", is_flag=True, show_default=True, default=False, help="Create installer",
              prompt="Do you want to create installer?")
@click.option("--reconvert-ui/--no-reconvert-ui", "-U/-u", is_flag=True, show_default=True, default=False, help="Reconvert the UI",
              prompt="Do you want to re-convert the UI?")
def cli(reconvert_ui, installer):
    if reconvert_ui:
        click.echo("Re-converting UI...")
        result = subprocess.run(
            ['python', 'convert.py'],
            capture_output=True,
            text=True,
            cwd=os.path.join(current_directory, "ui"),
                       )
        if result.returncode != 0:
            click.echo(f"Error during converting! {result.stderr}")
            return

        click.echo(f"Result:\n{result.stdout}")

    print(os.path.join(current_directory, 'installer_script.nsi'))


    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists("dist"):
        shutil.rmtree("dist")

    pyinstaller_args = [
        '--name=hubM Admin Panel',
        '--onedir',
        '--noconfirm',
        '--windowed',
        '--icon=res/icon.ico',
        '--add-data=res;res/',
        '--exclude-module=PySide6',
        '--exclude-module=PyQt5',
        '--contents-directory=.',
        'main.py'
    ]
    PyInstaller.__main__.run(pyinstaller_args)

    if installer:
        click.echo("Creating installer...")
        result = subprocess.run(
            [os.path.join(nsis_path, 'makensis.exe'), 'installer_script.nsi'],
            capture_output=True,
            text=True,
                       )

        if result.returncode != 0:
            click.echo(f"Error during creating installer! {result.stderr}")
            return

        click.echo(f"Result:\n{result.stdout}")

if __name__ == '__main__':
    cli()