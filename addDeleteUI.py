'''A UI file created by  Qt Designer software
    Broker topology means that each part of the user interface has its own file, this means that there should not be
    any name conflicts between the files'''

from PyQt4 import QtCore, QtGui


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

class Ui_addDeleteWindow(object):
    def setupUi(self, addDeleteWindow):
        addDeleteWindow.setObjectName(_fromUtf8("addDeleteWindow"))
        addDeleteWindow.resize(1045, 726)
        self.centralwidget = QtGui.QWidget(addDeleteWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.smartMartLabel = QtGui.QLabel(self.centralwidget)
        self.smartMartLabel.setGeometry(QtCore.QRect(212, 0, 621, 91))
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
        self.smartMartLabel_2.setGeometry(QtCore.QRect(352, 100, 341, 51))
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
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(427, 170, 191, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.itemID = QtGui.QLineEdit(self.centralwidget)
        self.itemID.setGeometry(QtCore.QRect(220, 340, 191, 51))
        self.itemID.setObjectName(_fromUtf8("itemID"))
        self.itemName = QtGui.QLineEdit(self.centralwidget)
        self.itemName.setGeometry(QtCore.QRect(690, 340, 191, 51))
        self.itemName.setObjectName(_fromUtf8("itemName"))
        self.smartMartLabel_3 = QtGui.QLabel(self.centralwidget)
        self.smartMartLabel_3.setGeometry(QtCore.QRect(120, 350, 91, 31))
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
        self.smartMartLabel_4.setGeometry(QtCore.QRect(610, 350, 71, 31))
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
        self.addDeleteBtn = QtGui.QPushButton(self.centralwidget)
        self.addDeleteBtn.setGeometry(QtCore.QRect(422, 490, 201, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.addDeleteBtn.setFont(font)
        self.addDeleteBtn.setObjectName(_fromUtf8("addDeleteBtn"))
        addDeleteWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(addDeleteWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        addDeleteWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(addDeleteWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        addDeleteWindow.setStatusBar(self.statusbar)
        self.smartMartLabel_3.setBuddy(self.itemID)
        self.smartMartLabel_4.setBuddy(self.itemName)

        self.retranslateUi(addDeleteWindow)
        QtCore.QMetaObject.connectSlotsByName(addDeleteWindow)

    def retranslateUi(self, addDeleteWindow):
        addDeleteWindow.setWindowTitle(_translate("addDeleteWindow", "Add/Delete", None))
        self.smartMartLabel.setText(_translate("addDeleteWindow", "Smart-Mart Stock Monitoring System", None))
        self.smartMartLabel_2.setText(_translate("addDeleteWindow", "Add/Delete Products", None))
        self.comboBox.setItemText(0, _translate("addDeleteWindow", "Add Product", None))
        self.comboBox.setItemText(1, _translate("addDeleteWindow", "Delete Product", None))
        self.smartMartLabel_3.setText(_translate("addDeleteWindow", "item_id", None))
        self.smartMartLabel_4.setText(_translate("addDeleteWindow", "Name", None))
        self.addDeleteBtn.setText(_translate("addDeleteWindow", "Add/Delete", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    addDeleteWindow = QtGui.QMainWindow()
    ui = Ui_addDeleteWindow()
    ui.setupUi(addDeleteWindow)
    addDeleteWindow.show()
    sys.exit(app.exec_())

