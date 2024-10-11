#!/bin/bash

echo "Installing Freakfox..."

INSTALL_DIR="$HOME/.local/share/freakfox"
mkdir -p "$INSTALL_DIR"

install_dependencies() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
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
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        if ! command -v brew &> /dev/null; then
            echo "Homebrew not found. Installing Homebrew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        brew install python3
        pip3 install PyQt5 PyQtWebEngine pygame
    else
        echo "Unsupported operating system"
        exit 1
    fi
    pip3 install requests
}

download_freakfox() {
    echo "Downloading Freakfox from GitHub..."
    curl -L -o /tmp/freakfox.zip https://github.com/1-K-SSPS/freakfox/archive/refs/heads/main.zip
    unzip -q /tmp/freakfox.zip -d /tmp
    cp -R /tmp/freakfox-main/src/* "$INSTALL_DIR"
    rm -rf /tmp/freakfox.zip /tmp/freakfox-main
}

create_launcher() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        DESKTOP_DIR="$HOME/.local/share/applications"
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
        DESKTOP_DIR="$HOME/Applications"
        mkdir -p "$DESKTOP_DIR"
        cat > "$DESKTOP_DIR/Freakfox.command" << EOL
#!/bin/bash
python3 $INSTALL_DIR/browser.py
EOL
        chmod +x "$DESKTOP_DIR/Freakfox.command"
    fi
}

install_dependencies
download_freakfox
create_launcher

echo "Freakfox has been successfully installed in $INSTALL_DIR"
