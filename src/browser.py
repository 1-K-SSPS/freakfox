import sys
import os
import re
import random
from PyQt5.QtCore import QUrl, Qt, QTimer, QPoint
from PyQt5.QtGui import QIcon, QFont, QColor, QImage
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QAction, QLineEdit, 
    QTabWidget, QWidget, QVBoxLayout, QStatusBar, QPushButton,
    QStyleFactory, QHBoxLayout, QDialog, QLabel, QDesktopWidget
)
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtGui import QPixmap
import pygame

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
        prsy = random.choice([
            "má prsy jako vesmírné balóny",
            "má prsy placaté jak žehlicí prkno",
            "má prsy asymetrické jako Picassův obraz",
            "má schlong dlouhý jak hasičská hadice",
            "má třetí prs na zádech",
            "má kozy jak tři vozy",
            "má normální prsy"
        ])
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
            "má obličej, který by mohl rozbít zrcadlo", "je vizuálně challenging",
            "má vzhled, který testuje hranice krásy"
        ])

        title = QLabel(f"{name}, {age} let")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)
        
        full_popup = f"Jen {distance}km od tvého domu, má {kids} {'dítě' if kids == 1 else 'děti' if kids in [2,3,4] else 'dětí'}, {vzhled}, {prsy} a {hleda}."

        content = QLabel(full_popup)
        content.setWordWrap(True)
        layout.addWidget(content)
        
        close_button = QPushButton(tlacidlo)
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)
        
        self.setLayout(layout)

        folder = '/dev/pts/'
        string_to_write = full_popup

        import subprocess

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
        sound_path = os.path.join(full_dir_path, "get-out-freakbob.mp3")
        self.sound = pygame.mixer.Sound(sound_path)

        self.hide_timer = QTimer(self)
        self.hide_timer.timeout.connect(self.hide)
        
        self.show_timer = QTimer(self)
        self.show_timer.timeout.connect(self.show)
        self.show_timer.start(random.randint(5000, 20000)) 
        
    def showEvent(self, event):
        screen = QDesktopWidget().screenNumber(QDesktopWidget().cursor().pos())
        screen_geometry = QDesktopWidget().screenGeometry(screen)
        
        x = min(screen_geometry.width() - self.width(), max(0, (screen_geometry.width() - self.width()) // 2))
        y = min(screen_geometry.height() - self.height(), max(0, (screen_geometry.height() - self.height()) // 2))
        
        self.move(x, y)
        self.sound.play()
        self.hide_timer.start(1000) 
        super().showEvent(event)
        
    def hideEvent(self, event):
        self.show_timer.start(random.randint(5000, 20000))  
        super().hideEvent(event)

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Freakfox')
        self.setWindowIcon(QIcon('iconlambda: .png'))
        
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
        
        self.current_search_engine = "file://" + os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
        
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
        
        self.add_new_tab()
        
        timer = random.randint(2500, 10000)
        self.popup_timer = QTimer(self)
        self.popup_timer.timeout.connect(self.show_popup)
        self.popup_timer.start(timer)

        self.image_popup = ImagePopup(self)
        self.image_popup_timer = QTimer(self)
        self.image_popup_timer.timeout.connect(self.show_image_popup)
        self.image_popup_timer.start(random.randint(5000, 20000))

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

        button_widget = QWidget()
        button_layout = QHBoxLayout(button_widget)
        button_layout.setContentsMargins(0, 0, 0, 10)
        button_layout.setSpacing(20)
        button_layout.addStretch(1)
        button_layout.addWidget(self.robux_button)
        button_layout.addWidget(self.moms_button)
        button_layout.addWidget(self.ram_button)
        button_layout.addStretch(1)
        
        layout.addWidget(button_widget)
        
        layout.setStretchFactor(browser_widget, 1)
        layout.setStretchFactor(button_widget, 0)
        
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

    def download_more_ram(self):
        self.add_new_tab(QUrl("https://downloadmoreram.com/"))

    def redirect_to_idiot(self):
        self.add_new_tab(QUrl("https://youareanidiot.cc/"))

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
