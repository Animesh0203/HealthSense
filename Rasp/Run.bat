@echo off
:loop
echo %password% | scp noct@172.20.10.6:/home/noct/dht22/data.csv D:\Tkinter-Designer-master\build\Rasp
timeout /t 5 >nul
goto loop
