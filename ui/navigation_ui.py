from PyQt5 import QtCore, QtWidgets, QtGui

class NavigationBar(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.setupUi()

    def setupUi(self):
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.setMinimumSize(QtCore.QSize(0, 30))
        self.setMaximumSize(QtCore.QSize(16777215, 30))
        self.setObjectName("NavigationBar")
        # self.setStyleSheet("background-color: rgb(10, 255, 255);")
        
        self.setStyleSheet("QPushButton { background-color: rgb(255, 255, 10); border: none; }")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("NB_HorizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.homeButton = QtWidgets.QPushButton(self)
        self.homeButton.setObjectName("NB_HomeButton")
        self.homeButton.setMinimumSize(QtCore.QSize(30, 30))
        self.homeButton.setMaximumSize(QtCore.QSize(30, 30))
        # self.homeButton.setIcon(QtGui.QIcon("resources/icons/home.png"))   
        # self.homeButton.setIconSize(QtCore.QSize(30, 30))
        self.homeButton.setFlat(True)
        self.horizontalLayout.addWidget(self.homeButton)

        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("NB_Label")
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setText("Home")
        self.horizontalLayout.addWidget(self.label)

        spacer = QtWidgets.QSpacerItem(40, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer)

        self.minimizeButton = QtWidgets.QPushButton(self)
        self.minimizeButton.setObjectName("NB_MinimizeButton")
        self.minimizeButton.setMinimumSize(QtCore.QSize(30, 30))
        self.minimizeButton.setMaximumSize(QtCore.QSize(30, 30))
        self.minimizeButton.setFlat(True)
        self.horizontalLayout.addWidget(self.minimizeButton)

        self.sizeButton = QtWidgets.QPushButton(self)
        self.sizeButton.setObjectName("NB_SizeButton")
        self.sizeButton.setMinimumSize(QtCore.QSize(30, 30))
        self.sizeButton.setMaximumSize(QtCore.QSize(30, 30))
        self.sizeButton.setFlat(True)
        self.horizontalLayout.addWidget(self.sizeButton)
        
        self.closeButton = QtWidgets.QPushButton(self)
        self.closeButton.setObjectName("NB_CloseButton")
        self.closeButton.setMinimumSize(QtCore.QSize(30, 30))
        self.closeButton.setMaximumSize(QtCore.QSize(30, 30))
        self.closeButton.setFlat(True)
        self.horizontalLayout.addWidget(self.closeButton)

        

