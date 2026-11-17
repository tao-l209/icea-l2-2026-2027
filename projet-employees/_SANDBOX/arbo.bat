@echo off
chcp 65001 >nul
REM Se placer dans le dossier du .bat (arbo.txt sera cree ici)
cd /d "%~dp0"

if exist "C:\Program Files\Python312\python.exe" (
    "C:\Program Files\Python312\python.exe" arbo.py
) else (
    python arbo.py
)

REM Fermer la console si tout s'est bien passe, sinon rester ouverte
if errorlevel 1 (
    echo.
    echo Une erreur s'est produite.
    pause
)