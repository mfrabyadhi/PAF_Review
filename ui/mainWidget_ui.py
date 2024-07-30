from PyQt5 import QtCore, QtGui, QtWidgets
from ui.loginPage_ui import LoginPage
from ui.welcomePage_ui import WelcomePage
from ui.mainPage_ui import MainPage
from ui.navigation_ui import NavigationBar

class CentralWidgetFactory:
    centralWidget = None

    @staticmethod
    def createCentralWidget(parent):
        if CentralWidgetFactory.centralWidget is None:
            CentralWidgetFactory.centralWidget = CentralWidget(parent)
        return CentralWidgetFactory.centralWidget

class CentralWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.setupUi()
    
    def setupUi(self):
        self.setObjectName("CentralWidget")
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setMinimumSize(QtCore.QSize(800, 600))

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("CW_HorizontalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.stackedWidget.setObjectName("CW_StackedWidget")
        self.stackedWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setMidLineWidth(0)
        self.stackedWidget.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.welcomePage = WelcomePage(self)
        self.stackedWidget.addWidget(self.welcomePage)

        self.loginPage = LoginPage(self)
        self.stackedWidget.addWidget(self.loginPage)

        self.mainPage = MainPage(self)
        self.stackedWidget.addWidget(self.mainPage)

        # debug
        self.stackedWidget.setCurrentIndex(2)

