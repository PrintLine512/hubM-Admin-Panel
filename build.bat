@echo off
:: Путь к вашему виртуальному окружению
set VENV_PATH=venv

:: Путь к вашему Python файлу

:: Активируем виртуальное окружение
call %VENV_PATH%\Scripts\activate.bat

:: Запускаем Python файл
python build.py %1 %2

:: Деактивируем виртуальное окружение (по желанию)
deactivate