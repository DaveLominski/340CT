import updateStockUI
import dbBroker
import sys
import popUpBroker



class updateStocks:

    def __init__(self):
        self.ui = updateStockUI.Ui_updateStockWindow()
        self.pop = popUpBroker.popUp()
        app = updateStockUI.QtGui.QApplication(sys.argv)
        MainWindow = updateStockUI.QtGui.QMainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.updateBtn.clicked.connect(self.onclick)
        MainWindow.show()

        sys.exit(app.exec_())


    def getID(self):
        return str(self.ui.itemID.displayText())

    def getName(self):
        return str(self.ui.itemName.displayText())

    def getPrice(self):
        return str(self.ui.itemPrice.displayText())

    def getQty(self):
        return str(self.ui.itemQty.displayText())

    def getArrDate(self):
        return str(self.ui.itemArrDate.displayText())

    def getMin(self):
        return str(self.ui.itemMin.displayText())

    def getMax(self):
        return str(self.ui.itemMax.displayText())



    def onclick(self):

        if self.getID() ==  str(dbBroker.itemDB().getOneData("SELECT id FROM items WHERE id = '%s'" % self.getID())):

            if self.getName() == ''and self.getPrice() == '' and self.getQty() == '' and self.getMin() == '' and self.getMax() == '' and self.getArrDate() == '':
                self.pop.errorMsg("ERROR", "No data inputted, try again")
            else:

                if self.getName() != '':
                    dbBroker.itemDB().query("UPDATE items SET name = '%s' WHERE id = '%s'" % (self.getName(), self.getID()))
                else:
                    pass

                if self.getPrice() != '':
                    dbBroker.itemDB().query("UPDATE items SET price = '%s' WHERE id = '%s'" % (self.getPrice(), self.getID()))
                else:
                    pass

                if self.getQty() != '':
                    dbBroker.itemDB().query("UPDATE items SET quantity = '%s' WHERE id = '%s'" % (self.getQty(), self.getID()))
                else:
                    pass

                if self.getMin() != '':
                    dbBroker.itemDB().query("UPDATE items SET min = '%s' WHERE id = '%s'" % (self.getMin(), self.getID()))

                if self.getMax() != '':
                    dbBroker.itemDB().query(("UPDATE items SET max = '%s' WHERE id = '%s'" % (self.getMax(), self.getID())))
                else:
                    pass

                if self.getArrDate() != '':
                    dbBroker.itemDB().query("UPDATE items SET arrival_date = '%s' WHERE id = '%s'" % (self.getArrDate(), self.getID()))
                else:
                    pass


        else:
            self.pop.errorMsg("Error", "The item ID does not exist in the database")






updateStocks()