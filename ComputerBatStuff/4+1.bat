@echo off
setlocal
echo %date% %time% >> %temp%\3+1.log
echo Computer Name: %computername% >> %temp%\3+1.log
echo.
echo 1. Install
echo 2. Uninstall
echo 3. Exit
echo 4. View Log
echo.
echo --------------------------------
set /p choice=Enter your choice:

if %choice%==1 goto install
if %choice%==2 goto uninstall
if %choice%==3 goto exit
if %choice%==4 goto viewlog

:install
// Download file from URL
echo Downloading file from URL
echo.
echo --------------------------------
url = "http://www.example.com/file.exe"
