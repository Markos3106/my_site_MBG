@echo off
REM Activa el entorno virtual si existe
IF EXIST "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

REM Ejecuta el servidor de desarrollo de Django
python manage.py runserver
