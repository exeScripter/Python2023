@echo off
setlocal
echo. > %temp%\3+1.bat
echo Computer Name: %computername% >> %temp%\3+1.bat
echo User Name: %username% >> %temp%\3+1.bat
echo ------------------------------ >> %temp%\3+1.bat
echo Computer Bat Stuff >> %temp%\3+1.bat
echo ------------------------------ >> %temp%\3+1.bat
echo. >> %temp%\3+1.bat
echo 1. Flood script
echo 2. Messager script
echo 3. Shutdown script
echo 4. Credits
echo 5. Exit
echo.
set /p choice=Enter your choice:
if %choice%==1 goto 1
if %choice%==2 goto 2
if %choice%==3 goto 3
if %choice%==4 goto 4
if %choice%==5 goto 5

:1
echo You have chosen the flood script
echo (It's yet not done, so you can't use it)
set /p choice=Do you want to continue? (N)
echo.
if %choice%==N goto 5
if %choice%==n goto 5

:2
echo You have chosen the messager script
echo.
set /p host=Enter the hostname or IP address of the computer you want to send the message to:
set /p message=Enter the message you want to send:
set /p time=Enter the time you want to send the message (in seconds):
set /p loop=Enter the number of times you want to send the message:
echo.
echo The message will be sent to %host%.
echo The message is: %message%
echo The message will be sent every %time% seconds.
echo The message will be sent %loop% times.
echo.

:loop
msg /SERVER:%host% * /TIME:%time% "%message%"
set /a loop=%loop%-1
if %loop%==0 goto 5
goto loop


:3
echo You have chosen the shutdown script
echo.
set /p host=Enter the hostname of the computer you want to shutdown:
set /p time=Enter the time you want to shutdown the computer (in seconds):
echo.
echo The computer %host% will be shutdown in %time% seconds.
echo.
shutdown /m %host% /s /t %time%
goto 5

:4
echo You have chosen the credits
echo.
echo This script was made by: naroors#0001
echo.

:5
echo Press any key to exit...
pause >nul
exit





