from PyQt5 import QtCore, QtGui, QtWidgets 
from ui.deviceContent_ui import DeviceContent
from ui.dataContent_ui import DataContent
from typing import Union

class MainPage(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.setupUi() 

    def setupUi(self):
        self.setObjectName("MainPage")
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setStyleSheet("background-color: rgb(255, 255, 255)")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("MP_HorizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.menuWidget = MenuWidget(self)
        self.horizontalLayout.addWidget(self.menuWidget, 1)

        self.contentWidget = QtWidgets.QStackedWidget(self)
        self.contentWidget.setObjectName("MP_ContentWidget")
        self.contentWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.contentWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.contentWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.contentWidget.setLineWidth(0)
        self.contentWidget.setMidLineWidth(0)
        self.contentWidget.setContentsMargins(0, 0, 0, 0)

        self.deviceContent = DeviceContent(self)
        self.contentWidget.addWidget(self.deviceContent)

        self.dataContent = DataContent(self)
        self.contentWidget.addWidget(self.dataContent)

        self.horizontalLayout.addWidget(self.contentWidget, 4)

    def changePage(self, index:Union[int, QtWidgets.QWidget]):
        self.contentWidget.setCurrentIndex(index)

class MenuWidgetState:
    Opened = 0
    Closed = 1

class MenuWidget(QtWidgets.QWidget):
    changePageSignal:QtCore.pyqtSignal = QtCore.pyqtSignal(QtWidgets.QWidget)
    state:MenuWidgetState = MenuWidgetState.Closed

    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.setupUi() 

    def setupUi(self):
        self.setObjectName("MenuWidget")
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setMinimumSize(QtCore.QSize(200, 600))
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("MW_HorizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_1.setObjectName("MW_verticalLayout_1")
        self.verticalLayout_1.setContentsMargins(0, 0, 10, 0)
        self.verticalLayout_1.setSpacing(0)
        self.verticalLayout_1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.deviceButton = QtWidgets.QPushButton("Devices") # change to custom widget
        self.deviceButton.setObjectName("MW_DeviceButton")
        self.deviceButton.setFont(QtGui.QFont("Arial", 16))
        self.deviceButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_1.addWidget(self.deviceButton)

        self.editButton = QtWidgets.QPushButton("Edit") # change to custom widget
        self.editButton.setObjectName("MW_EditButton")
        self.editButton.setFont(QtGui.QFont("Arial", 16))
        self.editButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_1.addWidget(self.editButton)

        self.dataButton = QtWidgets.QPushButton("Data") # change to custom widget
        self.dataButton.setObjectName("MW_DataButton")
        self.dataButton.setFont(QtGui.QFont("Arial", 16))
        self.dataButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_1.addWidget(self.dataButton)

        self.rawDataButton = QtWidgets.QPushButton("Raw Data") # change to custom widget
        self.rawDataButton.setObjectName("MW_RawDataButton")
        self.rawDataButton.setFont(QtGui.QFont("Arial", 16))
        self.rawDataButton.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_1.addWidget(self.rawDataButton)

        self.horizontalLayout.addLayout(self.verticalLayout_1)
        
        self.expandButton = QtWidgets.QPushButton(">")
        self.expandButton.setObjectName("MW_ExpandButton")
        self.expandButton.setFont(QtGui.QFont("Arial", 16))
        self.expandButton.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.expandButton.setMinimumSize(QtCore.QSize(50, 50))
        self.expandButton.setMaximumSize(QtCore.QSize(50, 50))
        self.horizontalLayout.addWidget(self.expandButton)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255), 1, QtCore.Qt.SolidLine))
        painter.drawLine(self.width() - 1, 0, self.width() - 1, self.height())

        super().paintEvent(event)
