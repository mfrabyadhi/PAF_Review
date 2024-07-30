from PyQt5 import QtCore, QtGui, QtWidgets

class DeviceContent(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("DeviceContent")
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setMinimumSize(QtCore.QSize(600, 400))
        
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("DC_GridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.deviceCards = []

        for i in range(4):
            deviceCard = DeviceCard(self)
            deviceCard.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            self.deviceCards.append(deviceCard)
            self.gridLayout.addWidget(deviceCard, i // 2, i % 2)
            print(i // 2, i % 2)

    def showEvent(self, event):
        super().showEvent(event)

        
        

class DeviceCard(QtWidgets.QAbstractButton):
    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.setupUi()
        self.state = DeviceCardState.Collapsed
        
    def setupUi(self):
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setMinimumSize(QtCore.QSize(100, 100))

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.deviceNameLabel = QtWidgets.QLabel("Device Name")
        self.deviceNameLabel.setObjectName("DC_DeviceNameLabel")
        self.deviceNameLabel.setFont(QtGui.QFont("Arial", 16)) 
        self.deviceNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.deviceNameLabel)
        
        self.deviceIdLabel = QtWidgets.QLabel("Device ID: 123456")
        self.deviceIdLabel.setObjectName("DC_DeviceIdLabel")
        self.deviceIdLabel.setFont(QtGui.QFont("Arial", 12))
        self.deviceIdLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.deviceIdLabel)

        self.deviceStatusLabel = QtWidgets.QLabel("Status: Offline")
        self.deviceStatusLabel.setObjectName("DC_DeviceStatusLabel")
        self.deviceStatusLabel.setFont(QtGui.QFont("Arial", 12))
        self.deviceStatusLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.deviceLocationLabel = QtWidgets.QLabel("Location: 6.1234, 7.1234")
        self.deviceLocationLabel.setObjectName("DC_DeviceLocationLabel")
        self.deviceLocationLabel.setFont(QtGui.QFont("Arial", 12))
        self.deviceLocationLabel.setAlignment(QtCore.Qt.AlignCenter)

    def setData(self, data):
        pass

class DeviceCardState:
    class Collapsed:
        size = QtCore.QSize(100, 100)
    class Expanded:
        size = QtCore.QSize(400, 400)