import addDelete
import sys
import dbConnection
import popUpBroker



class addDeleteItems():

    def __init__(self):


        self.ui = addDelete.Ui_addDeleteWindow()
        self.pop = popUpBroker.popUp()
        app = addDelete.QtGui.QApplication(sys.argv)
        MainWindow = addDelete.QtGui.QMainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.addDeleteBtn.clicked.connect(self.onclick)
        MainWindow.show()

        sys.exit(app.exec_())

    def getID(self):
        return str(self.ui.itemID.displayText())

    def getName(self):
        return str(self.ui.itemName.displayText())

    def addDelete(self):
        return str(self.ui.comboBox.currentText())

    def onclick(self):

        if self.addDelete() == 'Add Product':
            if self.getID() == '' or self.getName() == '':
                self.pop.errorMsg("Error", "Missing Data")

            else:
                dbConnection.itemDB().query("INSERT INTO items (id, name) VALUES ('%s', '%s')" % (self.getID(), self.getName()))

        elif self.addDelete() == 'Delete Product':
            if self.getName() != '':
                self.pop.errorMsg("Error", "Only enter an item ID!")

            elif self.getID() == '':
                self.pop.errorMsg("Error", "Please enter an item ID!")

            else:
                if self.getID() != str(dbConnection.itemDB().getOneData("SELECT id FROM items WHERE id = '%s'" % self.getID())):
                    self.pop.errorMsg("Error", "Item ID not found in the database!")

                else:
                    dbConnection.itemDB().query("DELETE FROM items WHERE id = '%s'" % (self.getID()))









addDeleteItems()

