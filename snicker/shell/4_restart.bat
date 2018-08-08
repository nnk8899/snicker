@echo off
if exist app.pid (echo "[%date% %time%] Stopping..."
  python -c "import os; os.system('taskkill /F /PID %%s' %% open('app.pid').read());"
  del app.pid
)else (echo "[%date% %time%] Stopped.."
ping -n 3 localhost >nul
)
 
if exist app.pid (echo "[%date% %time%] Running.."
ping -n 3 localhost >nul
exit
)else ( echo "[%date% %time%] Starting.."
start pythonw ../py/client.py
ping -n 3 localhost >nul
3_status.bat
ping -n 3 localhost >nul
)
