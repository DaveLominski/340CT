import logInWindow
import dbConnection
import sys

class logIn:
    def __init__(self):
        self.ui = logInWindow.Ui_logInWindow()
        app = logInWindow.QtGui.QApplication(sys.argv)
        MainWindow = logInWindow.QtGui.QMainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.logInButton.clicked.connect(self.onclick)
        MainWindow.show()

        sys.exit(app.exec_())

    def getUsername(self):
        return str(self.ui.usr.displayText())

    def getPassword(self):
        return str(self.ui.pwd.displayText())

    def onclick(self):



        if (self.ui.usr.cursorPosition()) == 0 or (self.ui.pwd.cursorPosition()) == 0:
            self.ui.errorMsg("Error", "One of the fields is empty")

        else:
            if self.getUsername() in str(dbConnection.userDB().getData("SELECT username FROM users WHERE username ='%s'" % self.getUsername())):
                if self.getPassword() == str(dbConnection.userDB().getData("SELECT password FROM users WHERE username = '%s'" % self.getUsername())):
                    self.ui.successMsg("Success", "You have been logged in")

                else:
                    self.ui.errorMsg("Error", "Wrong Password")

            else:
                self.ui.errorMsg("Error", "Username does not exist")





logIn()