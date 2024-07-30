from PyQt5 import QtCore, QtGui, QtWidgets

class LoginPage(QtWidgets.QWidget):
    loginSignal:QtCore.pyqtSignal = QtCore.pyqtSignal(str, str)

    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("LoginPage")
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        
        self.gridLayout = QtWidgets.QGridLayout(self)  
        self.gridLayout.setObjectName("LP_GridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("LP_CentralWidget")
        self.centralWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.centralWidget.setMinimumSize(QtCore.QSize(400, 600))
        self.centralWidget.setMaximumSize(QtCore.QSize(400, 600))
        self.centralWidget.setStyleSheet("#LP_CentralWidget {background-color: rgb(255, 255, 255); border: 1px solid black; border-radius: 10px;}")

        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_1.setObjectName("LP_VerticalLayout_1")
        self.verticalLayout_1.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_1.setSpacing(0)
        self.verticalLayout_1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.loginMenuLabel = QtWidgets.QLabel("Login")
        self.loginMenuLabel.setObjectName("LP_LoginMenuLabel")
        self.loginMenuLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loginMenuLabel.setFont(QtGui.QFont("Arial", 24))
        self.verticalLayout_1.addWidget(self.loginMenuLabel)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("LP_HorizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.usernameLabel = QtWidgets.QLabel("Username")
        self.usernameLabel.setObjectName("LP_UsernameLabel")
        self.usernameLabel.setFont(QtGui.QFont("Arial", 16))
        self.horizontalLayout_2.addWidget(self.usernameLabel)

        self.usernameLineEdit = QtWidgets.QLineEdit()
        self.usernameLineEdit.setObjectName("LP_UsernameLineEdit")
        self.usernameLineEdit.setFont(QtGui.QFont("Arial", 16))
        self.usernameLineEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.horizontalLayout_2.addWidget(self.usernameLineEdit)

        self.verticalLayout_1.addLayout(self.horizontalLayout_2)

        self.horizontalLayout2_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout2_2.setObjectName("LP_HorizontalLayout2_2")
        self.horizontalLayout2_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout2_2.setSpacing(0)
        self.horizontalLayout2_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.passwordLabel = QtWidgets.QLabel("Password")
        self.passwordLabel.setObjectName("LP_PasswordLabel")
        self.passwordLabel.setFont(QtGui.QFont("Arial", 16))
        self.horizontalLayout2_2.addWidget(self.passwordLabel)

        self.passwordLineEdit = QtWidgets.QLineEdit()
        self.passwordLineEdit.setObjectName("LP_PasswordLineEdit")
        self.passwordLineEdit.setFont(QtGui.QFont("Arial", 16))
        self.passwordLineEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.horizontalLayout2_2.addWidget(self.passwordLineEdit)

        self.verticalLayout_1.addLayout(self.horizontalLayout2_2)

        self.loginButton = QtWidgets.QPushButton("Login")
        self.loginButton.setObjectName("LP_LoginButton")
        self.loginButton.setFont(QtGui.QFont("Arial", 16))
        self.loginButton.setMinimumSize(QtCore.QSize(200, 50))
        self.loginButton.setMaximumSize(QtCore.QSize(200, 50))
        self.verticalLayout_1.addWidget(self.loginButton, 0, QtCore.Qt.AlignCenter)

        spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_1.insertItem(0, spacer)
        spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_1.insertItem(4, spacer)
        spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_1.addItem(spacer)
        self.verticalLayout_1.setStretch(0, 2)
        self.verticalLayout_1.setStretch(6, 2)

        self.gridLayout.addWidget(self.centralWidget, 1, 1, 1, 1)

        horizontalspacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(horizontalspacer, 1, 0, 1, 1)
        horizontalspacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(horizontalspacer, 1, 2, 1, 1)
        verticalspacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(verticalspacer, 0, 1, 1, 1)
        verticalspacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(verticalspacer, 2, 1, 1, 1)

        self.loginButton.clicked.connect(self.on_loginButton_clicked)

    @QtCore.pyqtSlot()
    def on_loginButton_clicked(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        self.loginSignal.emit(username, password)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(self.rect(), QtGui.QPixmap("resources/images/login.jpg"))

        super().paintEvent(event)

