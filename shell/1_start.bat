@echo off
if exist app.pid (echo "[%date% %time%] Running.."
ping -n 3 localhost >nul
exit
)else ( echo "[%date% %time%] Starting.."
start pythonw ../py/client.py
ping -n 3 localhost >nul
3_status.bat
ping -n 3 localhost >nul
)
