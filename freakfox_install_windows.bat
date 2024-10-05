@echo off
setlocal enabledelayedexpansion

echo Installing Freakfox...

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Downloading and installing Python...
    powershell -Command "& {Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe' -OutFile '%TEMP%\python-installer.exe'}"
    %TEMP%\python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    set "PATH=%PATH%;C:\Program Files\Python39;C:\Program Files\Python39\Scripts"
)

set "INSTALL_DIR=%LOCALAPPDATA%\Freakfox"
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

echo Downloading files from GitHub...
powershell -Command "& {Invoke-WebRequest -Uri 'https://github.com/1-K-SSPS/freakfox/archive/refs/heads/main.zip' -OutFile '%TEMP%\freakfox.zip'}"
powershell -Command "& {Add-Type -AssemblyName System.IO.Compression.FileSystem; [System.IO.Compression.ZipFile]::ExtractToDirectory('%TEMP%\freakfox.zip', '%TEMP%\freakfox')}"
xcopy /E /I /Y "%TEMP%\freakfox\freakfox-main\src" "%INSTALL_DIR%"

echo Installing dependencies...
python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install PyQt5 PyQtWebEngine pygame requests

echo Creating start menu shortcut...
powershell -Command "& {$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%APPDATA%\Microsoft\Windows\Start Menu\Programs\Freakfox.lnk'); $Shortcut.TargetPath = 'pythonw.exe'; $Shortcut.Arguments = '%INSTALL_DIR%\browser.py'; $Shortcut.WorkingDirectory = '%INSTALL_DIR%'; $Shortcut.IconLocation = '%INSTALL_DIR%\freakfox_icon.png,0'; $Shortcut.Save()}"

echo Freakfox has been successfully installed!
echo You can now launch it from the Start Menu.

pause
