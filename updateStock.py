# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updateStock.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_updateStockWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1045, 726)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.smartMartLabel = QtGui.QLabel(self.centralwidget)
        self.smartMartLabel.setGeometry(QtCore.QRect(220, 10, 621, 121))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.smartMartLabel.setFont(font)
        self.smartMartLabel.setObjectName(_fromUtf8("smartMartLabel"))
        self.smartMartLabel_2 = QtGui.QLabel(self.centralwidget)
        self.smartMartLabel_2.setGeometry(QtCore.QRect(397, 110, 251, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.smartMartLabel_2.setFont(font)
        self.smartMartLabel_2.setObjectName(_fromUtf8("smartMartLabel_2"))
        self.itemID = QtGui.QLineEdit(self.centralwidget)
        self.itemID.setGeometry(QtCore.QRect(420, 210, 191, 51))
        self.itemID.setObjectName(_fromUtf8("itemID"))
        self.itemName = QtGui.QLineEdit(self.centralwidget)
        self.itemName.setGeometry(QtCore.QRect(210, 310, 191, 51))
        self.itemName.setObjectName(_fromUtf8("itemName"))
        self.itemPrice = QtGui.QLineEdit(self.centralwidget)
        self.itemPrice.setGeometry(QtCore.QRect(210, 390, 191, 51))
        self.itemPrice.setObjectName(_fromUtf8("itemPrice"))
        self.itemMin = QtGui.QLineEdit(self.centralwidget)
        self.itemMin.setGeometry(QtCore.QRect(650, 390, 191, 51))
        self.itemMin.setObjectName(_fromUtf8("itemMin"))
        self.itemArrDate = QtGui.QLineEdit(self.centralwidget)
        self.itemArrDate.setGeometry(QtCore.QRect(650, 310, 191, 51))
        self.itemArrDate.setObjectName(_fromUtf8("itemArrDate"))
        self.itemMax = QtGui.QLineEdit(self.centralwidget)
        self.itemMax.setGeometry(QtCore.QRect(650, 470, 191, 51))
        self.itemMax.setObjectName(_fromUtf8("itemMax"))
        self.itemQty = QtGui.QLineEdit(self.centralwidget)
        self.itemQty.setGeometry(QtCore.QRect(210, 470, 191, 51))
        self.itemQty.setObjectName(_fromUtf8("itemQty"))
        self.smartMartLabel_3 = QtGui.QLabel(self.centralwidget)
        self.smartMartLabel_3.setGeometry(QtCore.QRect(330, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.smartMartLabel_3.setFont(font)
        self.smartMartLabel_3.setObjectName(_fromUtf8("smartMartLabel_3"))
        self.smartMartLabel_4 = QtGui.QLabel(self.centralwidget)
        self.smartMartLabel_4.setGeometry(QtCore.QRect(130, 320, 71, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.smartMartLabel_4.setFont(font)
        self.smartMartLabel_4.setObjectName(_fromUtf8("smartMartLabel_4"))
        self.smartMartLabel_5 = QtGui.QLabel(self.centralwidget)
        self.smartMartLabel_5.setGeometry(QtCore.QRect(520, 480, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.smartMartLabel_5.setFont(font)
        self.smartMartLabel_5.setObjectName(_fromUtf8("smartMartLabel_5"))
        self.smartMartLabel_6 = QtGui.QLabel(self.centralwidget)
        self.smartMartLabel_6.setGeometry(QtCore.QRect(530, 400, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.smartMartLabel_6.setFont(font)
        self.smartMartLabel_6.setObjectName(_fromUtf8("smartMartLabel_6"))
        self.smartMartLabel_7 = QtGui.QLabel(self.centralwidget)
        self.smartMartLabel_7.setGeometry(QtCore.QRect(140, 400, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.smartMartLabel_7.setFont(font)
        self.smartMartLabel_7.setObjectName(_fromUtf8("smartMartLabel_7"))
        self.smartMartLabel_8 = QtGui.QLabel(self.centralwidget)
        self.smartMartLabel_8.setGeometry(QtCore.QRect(500, 320, 141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.smartMartLabel_8.setFont(font)
        self.smartMartLabel_8.setObjectName(_fromUtf8("smartMartLabel_8"))
        self.smartMartLabel_9 = QtGui.QLabel(self.centralwidget)
        self.smartMartLabel_9.setGeometry(QtCore.QRect(100, 480, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.smartMartLabel_9.setFont(font)
        self.smartMartLabel_9.setObjectName(_fromUtf8("smartMartLabel_9"))
        self.updateBtn = QtGui.QPushButton(self.centralwidget)
        self.updateBtn.setGeometry(QtCore.QRect(457, 560, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.updateBtn.setFont(font)
        self.updateBtn.setObjectName(_fromUtf8("updateBtn"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.smartMartLabel.setBuddy(self.itemID)
        self.smartMartLabel_3.setBuddy(self.itemID)
        self.smartMartLabel_4.setBuddy(self.itemName)
        self.smartMartLabel_5.setBuddy(self.itemMax)
        self.smartMartLabel_6.setBuddy(self.itemMin)
        self.smartMartLabel_7.setBuddy(self.itemPrice)
        self.smartMartLabel_8.setBuddy(self.itemArrDate)
        self.smartMartLabel_9.setBuddy(self.itemQty)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.smartMartLabel.setText(_translate("MainWindow", "Smart-Mart Stock Monitoring System", None))
        self.smartMartLabel_2.setText(_translate("MainWindow", "Updating items", None))
        self.smartMartLabel_3.setText(_translate("MainWindow", "item_id", None))
        self.smartMartLabel_4.setText(_translate("MainWindow", "Name", None))
        self.smartMartLabel_5.setText(_translate("MainWindow", "Maximum", None))
        self.smartMartLabel_6.setText(_translate("MainWindow", "Minimum ", None))
        self.smartMartLabel_7.setText(_translate("MainWindow", "Price", None))
        self.smartMartLabel_8.setText(_translate("MainWindow", "Arrival Date", None))
        self.smartMartLabel_9.setText(_translate("MainWindow", "Quantity", None))
        self.updateBtn.setText(_translate("MainWindow", "Update", None))

    '''Error  message box, that shows up if there is an error'''

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


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_updateStockWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

