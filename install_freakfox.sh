#!/bin/bash

# Install script for Freakfox
echo " "
echo "Arch linux is recommended for using this script, it will not work on windows and can have issues on other distros"
echo " "

install_packages() {
    local distro=$1

    if [[ $distro == "arch" ]]; then
        echo "It seems you're using Arch Linux. You can install Wofi, Python, and Pip using pacman."
        echo "Choose an option:"
        echo "1 - Install Wofi"
        echo "2 - Install Python, Pip, python-pyqt5, python-pyqt5-webengine, and python-pygame (required dependencies)"
        echo "a - Install both Wofi and Python"
        echo "n - Skip this step"

        read -r option
        if [[ $option == "1" ]]; then
            sudo pacman -S wofi --noconfirm
        elif [[ $option == "2" ]]; then
            sudo pacman -S python python-pip python-pyqt5 python-pyqt5-webengine python-pygame --noconfirm --needed
        elif [[ $option == "a" ]]; then
            sudo pacman -S wofi python python-pip python-pyqt5 python-pyqt5-webengine python-pygame --noconfirm --needed
        elif [[ $option == "n" ]]; then
            echo "Skipping installation of Wofi, Python, and Pip."
        else
            echo "Invalid option. Skipping installation of Wofi, Python, and Pip."
        fi
    elif [[ $distro == "debian" ]]; then
        echo "It seems you're using a Debian-based system (Debian/Ubuntu/Kali). You can install Wofi, Python, and Pip using apt. (this can have issues)"
        echo "Choose an option:"
        echo "1 - Install Wofi"
        echo "2 - Install Python, Pip, pyqt5-dev, and pygame"
        echo "a - Install both Wofi and Python"
        echo "n - Skip this step"

        read -r option
        if [[ $option == "1" ]]; then
            sudo apt update && sudo apt install wofi -y
        elif [[ $option == "2" ]]; then
            sudo apt update && sudo apt install python3 python3-pip pyqt5-dev python3-pygame -y
        elif [[ $option == "a" ]]; then
            sudo apt update && sudo apt install wofi python3 python3-pip pyqt5-dev python3-pygame -y
        elif [[ $option == "n" ]]; then
            echo "Skipping installation of Wofi, Python, and Pip."
        else
            echo "Invalid option. Skipping installation of Wofi, Python, and Pip."
        fi

    elif [[ $distro == "fedora" ]]; then
        echo "It seems you're using Fedora. You can install Wofi, Python, and Pip using dnf. (this script was not yet tested on fedora)"
        echo "Choose an option:"
        echo "1 - Install Wofi"
        echo "2 - Install Python, Pip, PyQt5, PyQtWebEngine, and pygame"
        echo "a - Install both Wofi and Python"
        echo "n - Skip this step"

        read -r option
        if [[ $option == "1" ]]; then
            sudo dnf install wofi -y
        elif [[ $option == "2" ]]; then
            sudo dnf install python3 python3-pip python3-pygame -y
            pip3 install PyQt5 PyQtWebEngine
        elif [[ $option == "a" ]]; then
            sudo dnf install wofi python3 python3-pip python3-pygame -y
            pip3 install PyQt5 PyQtWebEngine
        elif [[ $option == "n" ]]; then
            echo "Skipping installation of Wofi, Python, and Pip."
        else
            echo "Invalid option. Skipping installation of Wofi, Python, and Pip."
        fi
    else
        echo "Unsupported Linux distribution. (try installing using pip? [y/n])"
        read -r backupfallback
        if [[ $backupfallback == "y" ]]; then
            pip3 install PyQt5 PyQtWebEngine pygame --break-system-packages
        fi
    fi
}

if grep -q "Arch" /etc/os-release; then
    install_packages "arch"
elif grep -q "Debian" /etc/os-release || grep -q "Ubuntu" /etc/os-release || grep -q "Kali" /etc/os-release; then
    install_packages "debian"
elif grep -q "Fedora" /etc/os-release; then
    install_packages "fedora"
else
    echo "Unsupported Linux distribution. Please install the required packages manually."
fi

if ! command -v python3 &> /dev/null || ! command -v pip3 &> /dev/null
then
    echo "Python3 and pip3 are required to run this script. Please install them and try again."
    exit 1
fi

INSTALL_DIR=~/.local/share/freakfox
echo "Installing in directory: $INSTALL_DIR"

mkdir -p "$INSTALL_DIR"

echo "Downloading icons..."
curl -o $INSTALL_DIR/freakfox_icon.png "https://tse4.explicit.bing.net/th?id=OIP.RKC67blFYi4k7A1B7AxHuAAAAA&pid=Api"
curl -o $INSTALL_DIR/google_icon.png "https://www.pngmart.com/files/16/Google-Logo-PNG-Image.png"
curl -o $INSTALL_DIR/duckduckgo_icon.png "https://logodix.com/logo/48308.png"

echo "Copying source files..."

cp src/* $INSTALL_DIR/

echo "Installing necessary Python libraries..."

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
echo " "
echo "Freakfox was sucessfully installed into $INSTALL_DIR "
