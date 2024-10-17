If you want to create installer, please check before "nsis_path" in hubm_admin_panel/build.py
Run hubm_admin_panel/build.py only in venv
Built would be in dist

```````````````````````````````````
usage: build.py [-h] [-U] [-I]
Build and optionally create an installer.

options:
  -h, --help          show this help message and exit
  -U, --reconvert-ui  Reconvert the UI
  -I, --installer     Create installer
```````````````````````````````````

build.bat can fast build in venv, it pass args