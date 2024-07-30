from PyQt5 import QtCore, QtGui, QtWidgets
import pandas 

class DataContent(QtWidgets.QWidget):
    reviewData:pandas.DataFrame = None

    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("DataContent")
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setMinimumSize(QtCore.QSize(600, 400))

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("DC_verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.dataTable = QtWidgets.QTableWidget(self)
        self.dataTable.setObjectName("DC_DataTable")
        self.dataTable.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.dataTable.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.dataTable.setFrameShadow(QtWidgets.QFrame.Plain)
        self.dataTable.setLineWidth(0)
        self.dataTable.setMidLineWidth(0)
        self.dataTable.setContentsMargins(0, 0, 0, 0)
        
        self.reviewData = pandas.read_csv("data/data.txt")
        
        self.dataTable.setColumnCount(len(self.reviewData.columns))
        self.dataTable.setRowCount(len(self.reviewData.index))

        self.dataTable.setHorizontalHeaderLabels(self.reviewData.columns)

        for i in range(len(self.reviewData.index)):
            for j in range(len(self.reviewData.columns)):
                self.dataTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.reviewData.iloc[i, j])))   

        self.verticalLayout.addWidget(self.dataTable)

        self.saveButton = QtWidgets.QPushButton(self)
        self.saveButton.setObjectName("DC_SaveButton")
        self.saveButton.setText("Save")
        self.saveButton.setFixedSize(QtCore.QSize(100, 30))
        self.verticalLayout.addWidget(self.saveButton, 0, QtCore.Qt.AlignRight)

        self.saveButton.clicked.connect(self.saveData)
        
    def saveData(self):
        # excel to document folder
        name = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "C:\\Users\\", "Excel Files (*.xlsx)")
        if name[0] != "":
            self.reviewData.to_excel(name[0])
            print("Data Saved")
        else:
            print("Save Cancelled")