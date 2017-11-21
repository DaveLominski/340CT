import viewStock
import dbConnection
import sys
from PyQt4.Qt import *



class viewStocks:

    def __init__(self):
        self.ui = viewStock.Ui_viewStockWindow()
        app = viewStock.QtGui.QApplication(sys.argv)
        MainWindow = viewStock.QtGui.QMainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.loadButton.clicked.connect(self.onclick)
        MainWindow.show()

        sys.exit(app.exec_())


    def onclick(self):


        QTableWidget.clearContents(self.ui.tableWidget)
        self.ui.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(dbConnection.itemDB().getData("SELECT * FROM items")):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))








viewStocks()
