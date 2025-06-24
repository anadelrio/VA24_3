@echo off
cd /d "%~dp0"
start "" http://localhost:8000/proyecto5.html
python -m http.server
pause
