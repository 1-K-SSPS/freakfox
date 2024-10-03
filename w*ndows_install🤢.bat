@echo off
REM Install script for Freakfox on Windows

echo Installing Freakfox...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3 from https://www.python.org/ or the Microsoft Store.
    exit /b 1
)

REM Install Python dependencies
echo Installing necessary Python libraries...
pip install PyQt5 PyQtWebEngine pygame || (
    echo Failed to install required Python libraries. Please check your Python and pip installation.
    exit /b 1
)

REM Create installation directory
set INSTALL_DIR=%LOCALAPPDATA%\Freakfox
echo Installing into directory: %INSTALL_DIR%
mkdir "%INSTALL_DIR%" || (
    echo Failed to create installation directory.
    exit /b 1
)

REM Download icons
echo Downloading icons...
powershell -Command "Invoke-WebRequest -Uri 'https://tse4.explicit.bing.net/th?id=OIP.RKC67blFYi4k7A1B7AxHuAAAAA&pid=Api' -OutFile '%INSTALL_DIR%\freakfox_icon.png'" || (
    echo Failed to download Freakfox icon.
    exit /b 1
)
powershell -Command "Invoke-WebRequest -Uri 'https://www.pngmart.com/files/16/Google-Logo-PNG-Image.png' -OutFile '%INSTALL_DIR%\google_icon.png'" || (
    echo Failed to download Google icon.
    exit /b 1
)
powershell -Command "Invoke-WebRequest -Uri 'https://logodix.com/logo/48308.png' -OutFile '%INSTALL_DIR%\duckduckgo_icon.png'" || (
    echo Failed to download DuckDuckGo icon.
    exit /b 1
)

REM Copy source files
echo Copying source files...
xcopy /s /y "src\*" "%INSTALL_DIR%" || (
    echo Failed to copy source files.
    exit /b 1
)

REM Create a desktop shortcut for Freakfox
echo Creating desktop shortcut...
set SHORTCUT_PATH=%USERPROFILE%\Desktop\Freakfox.lnk
powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%SHORTCUT_PATH%'); $s.TargetPath = 'python.exe'; $s.Arguments = '%INSTALL_DIR%\browser.py'; $s.IconLocation = '%INSTALL_DIR%\freakfox_icon.png'; $s.Save()" || (
    echo Failed to create a desktop shortcut.
    exit /b 1
)

echo Freakfox was successfully installed.
pause
