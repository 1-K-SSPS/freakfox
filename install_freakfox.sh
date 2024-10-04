#!/bin/bash

echo " "
echo "This script is meant for Arch Linux, Debian-based distros, Fedora, or macOS."
echo " "

pip_install() {
    echo "Creating and activating virtual environment..."
    python3 -m venv "$INSTALL_DIR/venv" || { echo "Failed to create virtual environment"; exit 1; }
    source "$INSTALL_DIR/venv/bin/activate" || { echo "Failed to activate virtual environment"; exit 1; }

    echo "Installing necessary Python libraries..."
    pip install PyQt5 PyQtWebEngine pygame || { echo "Failed to install Python libraries"; exit 1; }

    deactivate
}

install_packages() {
    local distro=$1

    if [[ $distro == "arch" ]]; then
        echo "It seems you're using Arch Linux."
        echo "Choose an option:"
        echo "1 - Install Wofi"
        echo "2 - Install Python and venv, python-pyqt5 python-pyqt5-webengine python-pygame"
        echo "a - Install both Wofi and Python"
        echo "n - Skip this step"

        read -r option
        case $option in
        1)
            sudo pacman -S wofi --noconfirm || { echo "Failed to install Wofi"; exit 1; }

            ;;
        2)
            sudo pacman -S python python-pip python-virtualenv python-pyqt5 python-pyqt5-webengine python-pygame --noconfirm --needed || { echo "Failed to install Python"; exit 1; }

            ;;
        a)
            sudo pacman -S wofi python python-pip python-virtualenv python-pyqt5 python-pyqt5-webengine python-pygame --noconfirm --needed || { echo "Failed to install packages"; exit 1; }

            ;;
        n)
            echo "Skipping installation of Wofi and Python."

            ;;
        *)
            echo "Invalid option. Skipping installation."

            ;;
        esac
    elif [[ $distro == "debian" ]]; then
        echo "It seems you're using a Debian-based system (Debian/Ubuntu/Kali)."
        echo "Choose an option:"
        echo "1 - Install Wofi"
        echo "2 - Install Python and venv, python3-pyqt5 python3-pyqt5.qtwebengine python3-pygame"
        echo "a - Install both Wofi and Python"
        echo "n - Skip this step"

        read -r option
        case $option in
        1)
            sudo apt update && sudo apt install wofi -y || { echo "Failed to install Wofi"; exit 1; }

            ;;
        2)
            sudo apt update && sudo apt install python3 python3-pip python3-venv python3-pyqt5 python3-pyqt5.qtwebengine python3-pygame -y || { echo "Failed to install Python"; exit 1; }

            ;;
        a)
            sudo apt update && sudo apt install wofi python3 python3-pip python3-venv install python3-pyqt5 python3-pyqt5.qtwebengine python3-pygame -y || { echo "Failed to install packages"; exit 1; }

            ;;
        n)
            echo "Skipping installation of Wofi and Python."

            ;;
        *)
            echo "Invalid option. Skipping installation."

            ;;
        esac
    elif [[ $distro == "fedora" ]]; then
        echo "It seems you're using Fedora."
        echo "Choose an option:"
        echo "1 - Install Wofi"
        echo "2 - Install Python and venv"
        echo "a - Install both Wofi and Python"
        echo "n - Skip this step"

        read -r option
        case $option in
        1)
            sudo dnf install wofi -y || { echo "Failed to install Wofi"; exit 1; }

            ;;
        2)
            sudo dnf install python3 python3-pip python3-virtualenv -y || { echo "Failed to install Python"; exit 1; }

            ;;
        a)
            sudo dnf install wofi python3 python3-pip python3-virtualenv -y || { echo "Failed to install packages"; exit 1; }

            ;;
        n)
            echo "Skipping installation of Wofi and Python."

            ;;
        *)
            echo "Invalid option. Skipping installation."

            ;;
        esac
        pip_install
    elif [[ $distro == "macos" ]]; then
        echo "It seems you're using macOS."
        echo "Choose an option:"
        echo "1 - Install Python and Homebrew"
        echo "n - Skip this step"

        read -r option
        case $option in
        1)
            # Check if Homebrew is installed
            if ! command -v brew &>/dev/null; then
                echo "Installing Homebrew..."
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" || { echo "Failed to install Homebrew"; exit 1; }
            fi

            brew install python3 || { echo "Failed to install Python"; exit 1; }

            ;;
        n)
            echo "Skipping installation of Python."

            ;;
        *)
            echo "Invalid option. Skipping installation."

            ;;
        esac
        pip_install
    else
        echo "Unsupported Linux distribution. Please install Python 3 and venv manually."
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

# Check if Python3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Python3 is required to run this script. Please install it and try again."
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




if [[ "$OSTYPE" == "darwin"* ]]; then
    APPS_DIR="$HOME/Applications"
    mkdir -p "$APPS_DIR"

    echo "Creating app launcher for macOS..."
    mkdir -p "$APPS_DIR/Freakfox.app/Contents/MacOS"
    mkdir -p "$APPS_DIR/Freakfox.app/Contents/Resources"

    cat >"$APPS_DIR/Freakfox.app/Contents/Info.plist" << EOL
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>Freakfox</string>
    <key>CFBundleIconFile</key>
    <string>freakfox_icon.png</string>
    <key>CFBundleIdentifier</key>
    <string>com.freakfox.app</string>
    <key>CFBundleName</key>
    <string>Freakfox</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
</dict>
</plist>
EOL

    cat >"$APPS_DIR/Freakfox.app/Contents/MacOS/Freakfox" << EOL
#!/bin/bash
source "$INSTALL_DIR/venv/bin/activate"
python3 $INSTALL_DIR/browser.py
deactivate
EOL
    chmod +x "$APPS_DIR/Freakfox.app/Contents/MacOS/Freakfox"

    cp "$INSTALL_DIR/freakfox_icon.png" "$APPS_DIR/Freakfox.app/Contents/Resources/"
else
    echo "Creating app launcher entry..."
    cat >~/.local/share/applications/freakfox.desktop << EOL
[Desktop Entry]
Name=Freakfox
Exec=bash -c "source $INSTALL_DIR/venv/bin/activate && python3 $INSTALL_DIR/browser.py && deactivate"
Icon=$INSTALL_DIR/freakfox_icon.png
Type=Application
Terminal=false
Categories=GNOME;GTK;Network;WebBrowser;
Path=$INSTALL_DIR
EOL
fi

echo " "
echo "Freakfox was successfully installed into $INSTALL_DIR"
