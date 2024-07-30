from PyQt5 import QtCore, QtGui, QtWidgets

class WelcomePage(QtWidgets.QWidget):
    changePageSignal:QtCore.pyqtSignal = QtCore.pyqtSignal(int)

    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("WelcomePage")
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self) 
        self.horizontalLayout.setObjectName("WP_HorizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.imageWidget = QtWidgets.QLabel(self)
        self.imageWidget.setObjectName("WP_ImageWidget")

        img = QtGui.QPixmap("resources/images/welcome.jpg")
        self.imageWidget.setPixmap(img)
        self.imageWidget.setAlignment(QtCore.Qt.AlignCenter)
        self.imageWidget.setScaledContents(True)
        self.horizontalLayout.addWidget(self.imageWidget)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("WP_VerticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.welcomeLabel = QtWidgets.QLabel("Welcome to the App")
        self.welcomeLabel.setObjectName("WP_WelcomeLabel")
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setFont(QtGui.QFont("Arial", 24))
        self.verticalLayout.addWidget(self.welcomeLabel)

        spacer = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacer)

        self.welcomeButton = QtWidgets.QPushButton("Get Started")
        self.welcomeButton.setObjectName("WP_WelcomeButton")
        self.welcomeButton.setFont(QtGui.QFont("Arial", 16))
        self.welcomeButton.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.welcomeButton.setMinimumSize(QtCore.QSize(200, 50))
        self.welcomeButton.setMaximumSize(QtCore.QSize(200, 50))
        self.verticalLayout.addWidget(self.welcomeButton)
        self.verticalLayout.setAlignment(self.welcomeButton, QtCore.Qt.AlignCenter)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.welcomeButton.clicked.connect(self.on_welcomeButton_clicked)

    @QtCore.pyqtSlot()
    def on_welcomeButton_clicked(self):
        self.changePageSignal.emit(1)
