'''The whole file is an mainMenuBroker that consists of classes that involve 'menu'.  This is because broker topology has
    been used. This means that each actor has its own entity. Each class is a major functionality in the whole system'''
import mainMenuUI
import sys




'''A class that takes care of the navigation in the application and all the functionalities when the buttons are pushed
and events ran. Once the buttons are pushed, the new widnows will open depending on the buttons pushed'''
class mainMenuBroker:

    def __init__(self):
        '''Initiliasing all the Graphical User Interface using the mainMenuUI.py file, and also connecting the buttons
        to a function below'''
        self.ui = mainMenuUI.Ui_MainWindow()
        app = mainMenuUI.QtGui.QApplication(sys.argv)
        MainWindow = mainMenuUI.QtGui.QMainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.viewStocksBtn.clicked.connect(self.onclick) #connects the buttons to onclick function
        self.ui.updateStocksBtn.clicked.connect(self.onclick)
        self.ui.addDelBtn.clicked.connect(self.onclick)
        self.ui.quitBtn.clicked.connect(self.onclick)
        self.ui.viewStocksBtn.setCheckable(True)    #sets the buttons to the state where it allows to push it
        self.ui.updateStocksBtn.setCheckable(True)
        self.ui.addDelBtn.setCheckable(True)
        self.ui.quitBtn.setCheckable(True)
        MainWindow.show()

        sys.exit(app.exec_())


    def onclick(self):
        '''A function that takes care of assigning what each of the buttons will do after being pressed.
            Also visual help for a user to see when the button gets clicked'''

        if self.ui.viewStocksBtn.isChecked():
            self.ui.viewStocksBtn.setCheckable(False) #Setting the button to show that it has been clicked
            self.ui.viewStocksBtn.setCheckable(True)  #Setting the status of the button so it's clickable again

        elif self.ui.updateStocksBtn.isChecked():
            self.ui.updateStocksBtn.setCheckable(False)
            self.ui.updateStocksBtn.setCheckable(True)

        elif self.ui.addDelBtn.isChecked():
            self.ui.addDelBtn.setCheckable(False)
            self.ui.addDelBtn.setCheckable(True)

        elif self.ui.quitBtn.isChecked():
            self.ui.quitBtn.setCheckable(False)
            self.ui.quitBtn.setCheckable(True)

