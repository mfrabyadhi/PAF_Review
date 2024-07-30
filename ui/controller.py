from PyQt5 import QtCore, QtGui, QtWidgets
from ui.mainWidget_ui import CentralWidget, CentralWidgetFactory

class Controller(QtCore.QObject):
    def __init__(self):
        self.centralWidget = CentralWidgetFactory.createCentralWidget(None)

        self.centralWidget.welcomePage.changePageSignal.connect(lambda page: self.changePage(page))
        self.centralWidget.loginPage.loginSignal.connect(lambda username, password: self.login(username, password))
        self.centralWidget.mainPage.menuWidget.changePageSignal.connect(lambda page: self.centralWidget.mainPage.changePage(page))

    def changePage(self, page:int):
        print(f"Changing page to {page}")
        self.centralWidget.stackedWidget.setCurrentIndex(page)

    def login(self, username:str, password:str):
        print(f"Username: {username}, Password: {password}")

        self.changePage(2)