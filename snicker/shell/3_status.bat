@echo off
if exist app.pid (echo "[%date% %time%] Runningg...")else (echo "[%date% %time%] Stopped..")
ping -n 3 localhost >nul
