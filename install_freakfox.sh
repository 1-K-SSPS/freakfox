#!/bin/bash

# Install script for Freakfox
echo " "
echo "This script is meant for Arch Linux, Debian-based distros, Fedora, or macOS."
echo " "

install_packages() {
    local distro=$1

    if [[ $distro == "arch" ]]; then
        echo "It seems you're using Arch Linux."
        echo "Choose an option:"
        echo "1 - Install Wofi"
        echo "2 - Install Python, Pip, python-pyqt5, python-pyqt5-webengine, and python-pygame"
        echo "a - Install both Wofi and Python"
        echo "n - Skip this step"

        read -r option
        case $option in
            1)
                sudo pacman -S wofi --noconfirm || { echo "Failed to install Wofi"; exit 1; }
                ;;
            2)
                sudo pacman -S python python-pip python-pyqt5 python-pyqt5-webengine python-pygame --noconfirm --needed || { echo "Failed to install Python dependencies"; exit 1; }
                ;;
            a)
                sudo pacman -S wofi python python-pip python-pyqt5 python-pyqt5-webengine python-pygame --noconfirm --needed || { echo "Failed to install packages"; exit 1; }
                ;;
            n)
                echo "Skipping installation of Wofi, Python, and Pip."
                ;;
            *)
                echo "Invalid option. Skipping installation."
                ;;
        esac
    elif [[ $distro == "debian" ]]; then
        echo "It seems you're using a Debian-based system (Debian/Ubuntu/Kali)."
        echo "Choose an option:"
        echo "1 - Install Wofi"
        echo "2 - Install Python, Pip, pyqt5-dev, and pygame"
        echo "a - Install both Wofi and Python"
        echo "n - Skip this step"

        read -r option
        case $option in
            1)
                sudo apt update && sudo apt install wofi -y || { echo "Failed to install Wofi"; exit 1; }
                ;;
            2)
                sudo apt update && sudo apt install python3 python3-pip pyqt5-dev python3-pygame -y || { echo "Failed to install Python dependencies"; exit 1; }
                ;;
            a)
                sudo apt update && sudo apt install wofi python3 python3-pip pyqt5-dev python3-pygame -y || { echo "Failed to install packages"; exit 1; }
                ;;
            n)
                echo "Skipping installation of Wofi, Python, and Pip."
                ;;
            *)
                echo "Invalid option. Skipping installation."
                ;;
        esac
    elif [[ $distro == "fedora" ]]; then
        echo "It seems you're using Fedora."
        echo "Choose an option:"
        echo "1 - Install Wofi"
        echo "2 - Install Python, Pip, PyQt5, PyQtWebEngine, and pygame"
        echo "a - Install both Wofi and Python"
        echo "n - Skip this step"

        read -r option
        case $option in
            1)
                sudo dnf install wofi -y || { echo "Failed to install Wofi"; exit 1; }
                ;;
            2)
                sudo dnf install python3 python3-pip python3-pygame -y || { echo "Failed to install Python dependencies"; exit 1; }
                pip3 install PyQt5 PyQtWebEngine || { echo "Failed to install PyQt5 and PyQtWebEngine"; exit 1; }
                ;;
            a)
                sudo dnf install wofi python3 python3-pip python3-pygame -y || { echo "Failed to install packages"; exit 1; }
                pip3 install PyQt5 PyQtWebEngine || { echo "Failed to install PyQt5 and PyQtWebEngine"; exit 1; }
                ;;
            n)
                echo "Skipping installation of Wofi, Python, and Pip."
                ;;
            *)
                echo "Invalid option. Skipping installation."
                ;;
        esac
    elif [[ $distro == "macos" ]]; then
        echo "It seems you're using macOS."
        echo "Choose an option:"
        echo "1 - Install Python and Pip using brew"
        echo "n - Skip this step"

        read -r option
        case $option in
            1)
                brew install python3 || { echo "Failed to install Python"; exit 1; }
                pip3 install PyQt5 PyQtWebEngine pygame || { echo "Failed to install Python dependencies"; exit 1; }
                ;;
            n)
                echo "Skipping installation of Python and Pip."
                ;;
            *)
                echo "Invalid option. Skipping installation."
                ;;
        esac
    else
        echo "Unsupported Linux distribution or macOS. (try installing using pip? [y/n])"
        read -r backupfallback
        if [[ $backupfallback == "y" ]]; then
            pip3 install PyQt5 PyQtWebEngine pygame --break-system-packages || { echo "Failed to install Python dependencies via pip"; exit 1; }
        else
            echo "Skipping installation."
        fi
    fi
}

# Detect distro
if grep -q "Arch" /etc/os-release; then
    install_packages "arch"
elif grep -q "Debian" /etc/os-release || grep -q "Ubuntu" /etc/os-release || grep -q "Kali" /etc/os-release; then
    install_packages "debian"
elif grep -q "Fedora" /etc/os-release; then
    install_packages "fedora"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    install_packages "macos"
else
    echo "Unsupported operating system. Please install the required packages manually."
    exit 1
fi

# Check if Python3 and Pip3 are installed
if ! command -v python3 &> /dev/null || ! command -v pip3 &> /dev/null; then
    echo "Python3 and pip3 are required to run this script. Please install them and try again."
    exit 1
fi

INSTALL_DIR=~/.local/share/freakfox
echo "Installing in directory: $INSTALL_DIR"

mkdir -p "$INSTALL_DIR" || { echo "Failed to create installation directory"; exit 1; }

echo "Downloading icons..."
curl -o "$INSTALL_DIR/freakfox_icon.png" "https://tse4.explicit.bing.net/th?id=OIP.RKC67blFYi4k7A1B7AxHuAAAAA&pid=Api" || { echo "Failed to download Freakfox icon"; exit 1; }
curl -o "$INSTALL_DIR/google_icon.png" "https://www.pngmart.com/files/16/Google-Logo-PNG-Image.png" || { echo "Failed to download Google icon"; exit 1; }
curl -o "$INSTALL_DIR/duckduckgo_icon.png" "https://logodix.com/logo/48308.png" || { echo "Failed to download DuckDuckGo icon"; exit 1; }

echo "Copying source files..."
cp src/* "$INSTALL_DIR/" || { echo "Failed to copy source files"; exit 1; }

echo "Installing necessary Python libraries..."
pip3 install -r requirements.txt || { echo "Failed to install Python libraries"; exit 1; }

echo "Creating app launcher entry..."
cat > ~/.local/share/applications/freakfox.desktop << EOL
[Desktop Entry]
Name=Freakfox
Exec=python3 $INSTALL_DIR/browser.py
Icon=$INSTALL_DIR/freakfox_icon.png
Type=Application
Terminal=false
Categories=GNOME;GTK;Network;WebBrowser;
EOL

echo " "
echo "Freakfox was successfully installed into $INSTALL_DIR"
