from PyQt5 import QtCore, QtWidgets, QtGui
from qframelesswindow import FramelessWindow, StandardTitleBar
from ui.mainWidget_ui import CentralWidget, CentralWidgetFactory
from ui.controller import Controller

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowSystemMenuHint)

        self.setWindowIcon(QtGui.QIcon("resources/icons/home.png"))

        self.centralWidget = CentralWidgetFactory.createCentralWidget(self)
        self.setCentralWidget(self.centralWidget)
        
        self.control = Controller()
        # self.data = Data()

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())