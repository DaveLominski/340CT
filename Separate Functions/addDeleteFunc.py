import addDeleteUI
import sys
import dbBroker
import popUpBroker



class addDeleteItems():

    def __init__(self):


        self.ui = addDeleteUI.Ui_addDeleteWindow()
        self.pop = popUpBroker.popUp()
        app = addDeleteUI.QtGui.QApplication(sys.argv)
        MainWindow = addDeleteUI.QtGui.QMainWindow()
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
                dbBroker.itemDB().query("INSERT INTO items (id, name) VALUES ('%s', '%s')" % (self.getID(), self.getName()))

        elif self.addDelete() == 'Delete Product':
            if self.getName() != '':
                self.pop.errorMsg("Error", "Only enter an item ID!")

            elif self.getID() == '':
                self.pop.errorMsg("Error", "Please enter an item ID!")

            else:
                if self.getID() != str(dbBroker.itemDB().getOneData("SELECT id FROM items WHERE id = '%s'" % self.getID())):
                    self.pop.errorMsg("Error", "Item ID not found in the database!")

                else:
                    dbBroker.itemDB().query("DELETE FROM items WHERE id = '%s'" % (self.getID()))









addDeleteItems()

