#!/bin/bash

echo "Installing Freakfox..."

INSTALL_DIR="$HOME/.local/share/freakfox"
mkdir -p "$INSTALL_DIR"

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Detected Linux system"
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y python3 python3-pip python3-pyqt5 python3-pyqt5.qtwebengine python3-pygame
    elif command -v pacman &> /dev/null; then
        sudo pacman -Syu --noconfirm python python-pip python-pyqt5 python-pyqt5-webengine python-pygame
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y python3 python3-pip python3-pyqt5 python3-pyqt5-webengine python3-pygame
    else
        echo "Unsupported Linux distribution. Please install Python3, pip, PyQt5, PyQtWebEngine, and Pygame manually."
        exit 1
    fi
    DESKTOP_DIR="$HOME/.local/share/applications"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Detected macOS system"
    if ! command -v brew &> /dev/null; then
        echo "Homebrew not found. Please install Homebrew first: https://brew.sh/"
        exit 1
    fi
    brew install python3
    pip3 install PyQt5 PyQtWebEngine pygame
    DESKTOP_DIR="$HOME/Applications"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "Detected Windows system"
    if ! command -v python &> /dev/null; then
        echo "Python not found. Please install Python 3 from https://www.python.org/downloads/"
        exit 1
    fi
    pip install PyQt5 PyQtWebEngine pygame
    DESKTOP_DIR="$USERPROFILE\\Desktop"
else
    echo "Unsupported operating system"
    exit 1
fi

pip3 install requests

echo "Downloading icons..."
curl -o "$INSTALL_DIR/freakfox_icon.png" "https://tse4.explicit.bing.net/th?id=OIP.RKC67blFYi4k7A1B7AxHuAAAAA&pid=Api"
curl -o "$INSTALL_DIR/google_icon.png" "https://www.pngmart.com/files/16/Google-Logo-PNG-Image.png"
curl -o "$INSTALL_DIR/duckduckgo_icon.png" "https://logodix.com/logo/48308.png"

echo "Copying source files..."
cp browser.py "$INSTALL_DIR/"
cp index.html "$INSTALL_DIR/"
cp style.css "$INSTALL_DIR/"
cp balance.txt "$INSTALL_DIR/"
cp *.mp3 "$INSTALL_DIR/"
cp *.jpg "$INSTALL_DIR/"

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Creating app launcher entry..."
    mkdir -p "$DESKTOP_DIR"
    cat > "$DESKTOP_DIR/freakfox.desktop" << EOL
[Desktop Entry]
Name=Freakfox
Exec=python3 $INSTALL_DIR/browser.py
Icon=$INSTALL_DIR/freakfox_icon.png
Type=Application
Terminal=false
Categories=Network;WebBrowser;
EOL
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Creating app launcher..."
    cat > "$DESKTOP_DIR/Freakfox.command" << EOL
#!/bin/bash
python3 $INSTALL_DIR/browser.py
EOL
    chmod +x "$DESKTOP_DIR/Freakfox.command"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "Creating shortcut..."
    powershell -Command "& {$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('$DESKTOP_DIR\Freakfox.lnk'); $Shortcut.TargetPath = 'python'; $Shortcut.Arguments = '$INSTALL_DIR\browser.py'; $Shortcut.WorkingDirectory = '$INSTALL_DIR'; $Shortcut.IconLocation = '$INSTALL_DIR\freakfox_icon.png'; $Shortcut.Save()}"
fi

echo "Freakfox has been successfully installed in $INSTALL_DIR"
