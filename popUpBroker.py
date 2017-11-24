from PyQt4.Qt import *

class popUp:


    def errorMsg(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        msg.setText(title)
        msg.setInformativeText(message)  # Sets the information inside the box
        msg.setWindowTitle(title)  # Sets the title of the message box
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


    '''Success message box that shows up if the customer has been successfully removed from the database'''


    def successMsg(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText(title)
        msg.setInformativeText(message)  # Sets the information inside the box
        msg.setWindowTitle(title)  # Sets the title of the message box
        msg.setStandardButtons(QMessageBox.Ok)

        msg.exec_()
