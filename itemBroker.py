'''The whole file is an itemBroker that consists of classes that involve 'item'.  This is because broker topology has
    been used. This means that each actor has its own entity. Each class is a major functionality in the whole system'''
import addDeleteUI
import updateStockUI
import viewStockUI
import dbBroker
import popUpBroker
import errorHandlingBroker
import sys
from PyQt4.Qt import *


'''This class is only focused on displaying the data from the database in a table widget used from Qt Designer'''
class viewStocks:


    def __init__(self):
        '''Initialises all the graphical user interfaces necessary to display the data in the table appropriately
            but also adds functionality to the button, meaning that after the button gets pressed, it will perform a
            function.'''
        self.ui = viewStockUI.Ui_viewStockWindow()
        app = viewStockUI.QtGui.QApplication(sys.argv)
        MainWindow = viewStockUI.QtGui.QMainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.loadButton.clicked.connect(self.onclick)
        MainWindow.show()

        sys.exit(app.exec_())


    def onclick(self):
        '''The onclick function is focused on making sure that the functionality of the buttons gets performed, such as;
            displaying the data from the SQL database in a table widget'''

        QTableWidget.clearContents(self.ui.tableWidget)     #When pressed clears the whole table to make sure there
                                                            # are no leftovers
        self.ui.tableWidget.setRowCount(0)      #Resets the row count in the table to 0


        '''Loops through all data in the database, creating that many rows and columns but also inputs the item 
            before it loops back. The viewStock class uses the dbBroker to connect to the database'''
        for row_number, row_data in enumerate(dbBroker.itemDB().getData("SELECT * FROM items")):

            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            '''As the status of an item is not an attribute in the database, it needs to be calculated on the Pytho side,
                the if statements make sure of that. If quantity == minimum stock, the status will change to 'Awaiting
                re-order'. If quantity < minimum stock, the status = 'Order Placed' and if quantity > minimum stock,
                the status = 'In Stock' '''
            if int(self.ui.tableWidget.item(row_number,3).text()) == int(self.ui.tableWidget.item(row_number,5).text()):
                self.ui.tableWidget.setItem(row_number,7, QTableWidgetItem("Awaiting re-order"))
            elif int(self.ui.tableWidget.item(row_number,3).text()) < int(self.ui.tableWidget.item(row_number,5).text()):
                self.ui.tableWidget.setItem(row_number, 7, QTableWidgetItem("Order Placed"))
            elif int(self.ui.tableWidget.item(row_number,3).text()) > int((self.ui.tableWidget.item(row_number,5).text())):
                self.ui.tableWidget.setItem(row_number, 7, QTableWidgetItem("In stock"))
            '''self.ui.tableWidget.item() retrieves the values from the table depending on the row and column number
                self.ui.tableWidget.setItem() sets a new value of the item depending on the row and column number'''






'''This class is responsible for updating the stocks in the database.'''
class updateStocks:
    '''Initialises the graphical user interface and opens the window showing up the form to fill out to update an item.
        Uses simple QLineEdit boxes to insert data, and a simple button to confirm all the changes. Also adds the full
        functionality to the button'''
    def __init__(self):
        self.ui = updateStockUI.Ui_updateStockWindow()
        self.pop = popUpBroker.popUp()
        self.err = errorHandlingBroker.errorHandling()
        app = updateStockUI.QtGui.QApplication(sys.argv)
        MainWindow = updateStockUI.QtGui.QMainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.updateBtn.clicked.connect(self.onclick)
        MainWindow.show()

        sys.exit(app.exec_())


    '''All of the functions below retrieve information entered by the user in the system. These have to be separate and
        can't be re-used in different functions as different UI files would conflict'''
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
        '''The onclick function is focused on making sure that the functionality of the buttons gets performed, such as;
            validating, handling the errors, and updating the items in the database and displaying pop up messages.
            All connections to the database are done using the dbBroker. All the validation has been done using the
            errorHandling broker. All error and success pop up messages are using popUpBroker'''

        if self.getID() ==  str(dbBroker.itemDB().getOneData("SELECT id FROM items WHERE id = '%s'" % self.getID())):
        #Checks if the itemID entered exists in the database, if it does it continues

            if self.getName() == ''and self.getPrice() == '' and self.getQty() == '' and self.getMin() == '' and self.getMax() == '' and self.getArrDate() == '':
            #If all of the boxes are empty, display an error message
                self.pop.errorMsg("ERROR", "No data inputted, try again")
            else:
                if self.getName() != '':    #if user input not empty continue
                    if self.err.hasLetters(self.getName()) == True:     #validates if input only consists of letters
                        dbBroker.itemDB().query("UPDATE items SET name = '%s' WHERE id = '%s'" % (self.getName(), self.getID()))
                        self.ui.itemName.clear()    #update the database and clear the entry for further updates
                    else:
                        self.pop.errorMsg("ERROR", "Name should not include any numbers")
                        self.ui.itemName.clear()        #Display an error message and clear the entry
                else:
                    pass

                if self.getPrice() != '':   #if user input not empty continue
                    if self.err.isPrice(self.getPrice()) == True:   #validates if input is using the correct PRICE format
                        dbBroker.itemDB().query("UPDATE items SET price = '%s' WHERE id = '%s'" % (self.getPrice(), self.getID()))
                        self.ui.itemPrice.clear()       #update the database and clear the entry for further updates
                    else:
                        self.pop.errorMsg("ERROR", "Wrong price format has been entered")
                        self.ui.itemPrice.clear()       #Display an error message and clear the entry
                else:
                    pass

                if self.getQty() != '':     #if user input not empty continue
                    if self.err.onlyNumbers(self.getQty()) == True:     #validates if only numbers have been used
                        dbBroker.itemDB().query("UPDATE items SET quantity = '%s' WHERE id = '%s'" % (self.getQty(), self.getID()))
                        self.ui.itemQty.clear()     #update the database and clear the entry for further updates
                    else:
                        self.pop.errorMsg("ERROR", "Only numbers allowed in the quantity box")
                        self.ui.itemQty.clear()     #Display an error message and clear the entry
                else:
                   pass

                if self.getMin() != '':     #if user input not empty continue
                    if self.err.onlyNumbers(self.getMin()) == True:     #validates if only numbers have been used
                        dbBroker.itemDB().query("UPDATE items SET min = '%s' WHERE id = '%s'" % (self.getMin(), self.getID()))
                        self.ui.itemMin.clear()     #update the database and clear the entry for further updates
                    else:
                        self.pop.errorMsg("ERROR", "Only number allowed in the Minimum box")
                        self.ui.itemMin.clear()     #Display an error message and clear the entry
                else:
                    pass

                if self.getMax() != '':     #if user input not empty continue
                    if self.err.onlyNumbers(self.getMax()):     #validates if only numbers have been used
                        dbBroker.itemDB().query(("UPDATE items SET max = '%s' WHERE id = '%s'" % (self.getMax(), self.getID())))
                        self.ui.itemMax.clear()     #update the database and clear the entry for further updates
                    else:
                        self.pop.errorMsg("ERROR", "Only number allowed in the Maximum box")
                        self.ui.itemMax.clear()     #Display an error message and clear the entry
                else:
                    pass

                if self.getArrDate() != '':     #if user input not empty continue
                    if self.err.isDate(self.getArrDate()):      #validates if correct DATE format has been used
                        dbBroker.itemDB().query("UPDATE items SET arrival_date = '%s' WHERE id = '%s'" % (self.getArrDate(), self.getID()))
                        self.ui.itemArrDate.clear()     #update the database and clear the entry for further updates
                    else:
                        self.pop.errorMsg("ERROR", "Wrong date format has been entered")
                        self.ui.itemArrDate.clear()     #Display an error message and clear the entry
                else:
                    pass

                self.ui.itemID.clear()      #Clear the itemID at the end



        else:
            self.pop.errorMsg("Error", "The item ID does not exist in the database")    #Display an error message


'''Responsible for adding and deleting items to and from the database respectively'''
class addDeleteItems():


    def __init__(self):
        '''Initialises the graphical user interface and opens the window showing up the form to add or delete items in the database.
            Uses simple QLineEdit boxes to insert data, and a drop down menu to choose what the user wants to do.
            Also adds the full functionality to the button'''


        self.ui = addDeleteUI.Ui_addDeleteWindow()
        self.pop = popUpBroker.popUp()
        app = addDeleteUI.QtGui.QApplication(sys.argv)
        MainWindow = addDeleteUI.QtGui.QMainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.addDeleteBtn.clicked.connect(self.onclick)
        MainWindow.show()

        sys.exit(app.exec_())

    '''All of the functions below retrieve information entered by the user in the system. These have to be separate and
        can't be re-used in different functions as different UI files would conflict'''
    def getID(self):
        return str(self.ui.itemID.displayText())

    def getName(self):
        return str(self.ui.itemName.displayText())

    def addDelete(self):
        return str(self.ui.comboBox.currentText())


    def onclick(self):
        '''The onclick function is focused on making sure that the functionality of the buttons gets performed, such as;
            handling the errors, adding or deleting the items in the database and displaying pop up messages.
            All connections to the database are done using the dbBroker. All error and success pop up messages
            are using popUpBroker'''

        if self.addDelete() == 'Add Product':       #if add option has been chosen in the drop down menu continue
            if self.getID() == '' or self.getName() == '':
                self.pop.errorMsg("Error", "Missing Data")      #If both boxes empty, display an error message

            else:
                dbBroker.itemDB().query("INSERT INTO items (id, name) VALUES ('%s', '%s')" % (self.getID(), self.getName()))
                self.pop.successMsg("Success", "An item has been added successfully")       #If both boxes filled out, add an item
                                                                                            #and display a success message


        elif self.addDelete() == 'Delete Product':      #if delete option has been chosen in the drop down menu continue
            if self.getName() != '':
                self.pop.errorMsg("Error", "Only enter an item ID!")        #If itemName entered, display an error message

            elif self.getID() == '':
                self.pop.errorMsg("Error", "Please enter an item ID!")     #If itemID not entered, display an error message

            else:

                if self.getID() != str(dbBroker.itemDB().getOneData("SELECT id FROM items WHERE id = '%s'" % self.getID())):
                    self.pop.errorMsg("Error", "Item ID not found in the database!")    #If itemID entered but not in
                                                                                        #database, display an error message

                else:
                    dbBroker.itemDB().query("DELETE FROM items WHERE id = '%s'" % (self.getID()))
                    self.pop.successMsg("Success", "An item has been deleted successfully") #If itemID entered and in
                                                                                            #database, display a success message


