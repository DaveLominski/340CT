'''The whole file is a popUpBroker that consists of classes that involve 'pop up boxes'.  This is because broker topology has
    been used. This means that each actor has its own entity. Each class is a major functionality in the whole system'''
from PyQt4.Qt import *

'''Class that is responsible for display pop up messages to the user'''
class popUp:


    def errorMsg(self, title, message):
        '''Error message box that pops up to the user. Creates a new pop up whenever the function from the popUpBroker
            class has been called. Takes an input when calling a class - string'''
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        msg.setText(title)
        msg.setInformativeText(message)  # Sets the information inside the box
        msg.setWindowTitle(title)  # Sets the title of the message box
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()




    def successMsg(self, title, message):
        '''Error message box that pops up to the user. Creates a new pop up whenever the function from the popUpBroker
            class has been called. Takes an input when calling a class - string'''
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText(title)
        msg.setInformativeText(message)  # Sets the information inside the box
        msg.setWindowTitle(title)  # Sets the title of the message box
        msg.setStandardButtons(QMessageBox.Ok)

        msg.exec_()
