import sys
import os
import random
from PyQt5.QtCore import QUrl, Qt, QTimer, QPoint
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QAction, QLineEdit, 
    QTabWidget, QWidget, QVBoxLayout, QStatusBar, QPushButton,
    QStyleFactory, QHBoxLayout, QDialog, QLabel, QDesktopWidget, QComboBox,
    QListView, QScrollBar
)
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

class PopupDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Popup")
        self.setFixedSize(300, 200)
        
        layout = QVBoxLayout()
        
        age = random.randint(18, 100)
        name = random.choice(["Anna", "Eva", "Katerina", "Lucie", "Petra", "Jana", "Martina", "Veronika", "Tereza", "Barbora", "Eliska", "Prcna", "skibidak", "Adolf Hitler", "Petr", "Jarda", "Petříček", "Potrat", "Semeno"])
        kids = random.randint(0, 5)
        distance = random.randint(1, 10)
        prsy = random.choice(["má velké prsy", "má malé prsy", "má prsy jako kráva"])
        tlacidlo = random.choice(["Kontaktovat 👅", "Freakovat 💋", "Oplodnit 🥵", "Vyplnit 🤰"])
        hleda = random.choice(["hledá tatínka", "hledá zábavu", "hledá velké shlongy"])

        title = QLabel(f"{name}, {age} let")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)
        
        content = QLabel(f"Jen {distance}km od tvého domu, má {kids} {'dítě' if kids == 1 else 'děti' if kids in [2,3,4] else 'dětí'}, je velmi krásná, {prsy} a {hleda}.")
        content.setWordWrap(True)
        layout.addWidget(content)
        
        close_button = QPushButton(tlacidlo)
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)
        
        self.setLayout(layout)

    def showEvent(self, event):
        screen = QDesktopWidget().screenNumber(QDesktopWidget().cursor().pos())
        screen_geometry = QDesktopWidget().screenGeometry(screen)

        x = random.randint(0, screen_geometry.width() - self.width())
        y = random.randint(0, screen_geometry.height() - self.height())

        self.move(x, y)

        super().showEvent(event)

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Freakfox')
        self.setWindowIcon(QIcon('icon.png'))
        
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
        
        self.current_search_engine = "http://freakfox.wz.cz:8080/"
        self.add_search_engine_selector()
        
        self.url_bar = QLineEdit()
        self.url_bar.setStyleSheet("""
            background-color: #2b2b2b;
            color: #ffffff;
            border: 1px solid #3a3a3a;
            padding: 5px;
            border-radius: 15px;
        """)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.toolbar.addWidget(self.url_bar)
        
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
        button_layout.setContentsMargins(0, 0, 10, 10)
        button_layout.setSpacing(10)
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

    def add_search_engine_selector(self):
        self.search_engine_selector = QComboBox()
        self.search_engine_selector.addItem(QIcon("$INSTALL_DIR/freakfox/freakfox_icon.png"), "FreakFox")
        self.search_engine_selector.addItem(QIcon("$INSTALL_DIR/freakfox/google_icon.png"), "Google")
        self.search_engine_selector.addItem(QIcon("$INSTALL_DIR/freakfox/duckduckgo_icon.png"), "DuckDuckGo")
        self.search_engine_selector.currentIndexChanged.connect(self.change_search_engine)
        self.search_engine_selector.setStyleSheet("""
            QComboBox {
                background-color: #2b2b2b;
                color: #ffffff;
                border: none;
                border-radius: 15px;
                padding: 5px;
                font-weight: bold;
                font-size: 14px;
            }
            QComboBox:hover {
                background-color: #3a3a3a;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 30px;
                border-left: none;
                border-top-right-radius: 15px;
                border-bottom-right-radius: 15px;
            }
            QComboBox::down-arrow {
                image: url(down_arrow.png);
                width: 16px;
                height: 16px;
            }
            QComboBox QAbstractItemView {
                background-color: #2b2b2b;
                color: #ffffff;
                selection-background-color: #3a3a3a;
                border: none;
                outline: none;
            }
            QComboBox QAbstractItemView::item {
                height: 30px;
                padding-left: 10px;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #3a3a3a;
            }
            QComboBox QListView {
                background-color: #2b2b2b;
            }
        """)
        self.search_engine_selector.setFixedSize(150, 30)
        
       
        view = QListView()
        view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.search_engine_selector.setView(view)
        
        
        self.search_engine_selector.view().setFixedHeight(int(45 * 1.5))
        
        self.toolbar.addWidget(self.search_engine_selector)

    def change_search_engine(self, index):
        if index == 0:
            self.current_search_engine = "http://freakfox.wz.cz:8080/"
        elif index == 1:
            self.current_search_engine = "https://www.google.com/search?q="
        elif index == 2:
            self.current_search_engine = "https://duckduckgo.com/?q="
        
        
        for i in range(self.tabs.count()):
            browser = self.tabs.widget(i).findChild(QWebEngineView)
            if browser.url().toString().startswith(self.current_search_engine):
                browser.setUrl(QUrl(self.current_search_engine))
                self.tabs.setCurrentIndex(i)
                return
        
        
        self.add_new_tab(QUrl(self.current_search_engine), "Search Engine")

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
            self.popup_disabler.setText("Enable Popups")
        else:
            self.popup_timer.start(random.randint(2500, 10000))
            self.popup_disabler.setText("Disable Popups")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())