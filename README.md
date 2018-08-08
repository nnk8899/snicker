# snicker
## INTRODUCTION
* This's just a device that monitors the work of laziness. And this project contains 4 parts:
* * client.py
    > It monitors user's mouse and keyboard events, and sends messages to the server if the user fails to operate for 10 minutes. 
* * flaskRestServer.py
    > Once the laziness is found, the server will immediately alarm and record(both in local log and local database). 
* * .bat
    > To start/stop the pid.
* * listener.vbs
    > Please move it to SARTUP, and 1_start.bat will start automatically when the computer of clients is on the boot.
