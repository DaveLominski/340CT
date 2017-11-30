'''The whole file is a userBroker that consists of classes that involve 'user'.  This is because broker topology has
    been used. This means that each actor has its own entity. Each class is a major functionality in the whole system'''
import logInUI
import dbBroker
import sys
import popUpBroker

'''Class that is focused on allowing the user to log-in to the system'''
class logIn:
    '''Initialises all the graphical user interfaces necessary to display the log-in window
        but also adds functionality to the button, meaning that after the button gets pressed, it will perform a
        function.'''
    def __init__(self):
        self.ui = logInUI.Ui_logInWindow()
        self.pop = popUpBroker.popUp()
        app = logInUI.QtGui.QApplication(sys.argv)
        MainWindow = logInUI.QtGui.QMainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.logInButton.clicked.connect(self.onclick)
        MainWindow.show()

        sys.exit(app.exec_())

    '''All of the functions below retrieve information entered by the user in the system. These have to be separate and
        can't be re-used in different functions as different UI files would conflict'''
    def getUsername(self):
        return str(self.ui.usr.displayText())

    def getPassword(self):
        return str(self.ui.pwd.displayText())


    def onclick(self):
        '''The onclick function is focused on making sure that the functionality of the buttons gets performed, such as;
            validating, handling the errors, logging in a user and displaying pop up messages.
            All connections to the database are done using the dbBroker.
            All error and success pop up messages are using popUpBroker'''
        if (self.ui.usr.cursorPosition()) == 0 or (self.ui.pwd.cursorPosition()) == 0:
            self.pop.errorMsg("Error", "One of the fields is empty")    #If one of the fields is empty display an error message

        else:
            if self.getUsername() == str(dbBroker.userDB().getData("SELECT username FROM users WHERE username ='%s'" % self.getUsername())):
                #If user exists in a database continue
                if self.getPassword() == str(dbBroker.userDB().getData("SELECT password FROM users WHERE username = '%s'" % self.getUsername())):
                    self.pop.successMsg("Success", "You have been logged in") #If password entered matches the user display
                                                                              #a success message and log-in a user

                else:
                    self.pop.errorMsg("Error", "Wrong Password")    #If password doesn't match, display an error message

            else:
                self.pop.errorMsg("Error", "Username does not exist")   #If username doesn't exist, display a success message





