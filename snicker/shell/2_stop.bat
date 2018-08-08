@echo off
 
if exist app.pid (echo "[%date% %time%] Stopping..."
  python -c "import os; os.system('taskkill /F /PID %%s' %% open('app.pid').read());"
  del app.pid
)else (echo "[%date% %time%] Stopped.."
ping -n 3 localhost >nul
)
