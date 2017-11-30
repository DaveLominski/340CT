'''A UI file created by  Qt Designer software
    Broker topology means that each part of the user interface has its own file, this means that there should not be
    any name conflicts between the files'''

from PyQt4 import QtCore, QtGui
from viewStockUI import Ui_viewStockWindow


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

class Ui_MainWindow(object):



    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1045, 726)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.smartMartLabel = QtGui.QLabel(self.centralwidget)
        self.smartMartLabel.setGeometry(QtCore.QRect(212, 10, 621, 121))
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
        self.viewStocksBtn = QtGui.QPushButton(self.centralwidget)
        self.viewStocksBtn.setGeometry(QtCore.QRect(422, 240, 201, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.viewStocksBtn.setFont(font)
        self.viewStocksBtn.setObjectName(_fromUtf8("viewStocksBtn"))
        self.smartMartLabel_2 = QtGui.QLabel(self.centralwidget)
        self.smartMartLabel_2.setGeometry(QtCore.QRect(427, 110, 191, 51))
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
        self.updateStocksBtn = QtGui.QPushButton(self.centralwidget)
        self.updateStocksBtn.setGeometry(QtCore.QRect(422, 310, 201, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.updateStocksBtn.setFont(font)
        self.updateStocksBtn.setObjectName(_fromUtf8("updateStocksBtn"))
        self.addDelBtn = QtGui.QPushButton(self.centralwidget)
        self.addDelBtn.setGeometry(QtCore.QRect(422, 370, 201, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.addDelBtn.setFont(font)
        self.addDelBtn.setObjectName(_fromUtf8("addDelBtn"))
        self.quitBtn = QtGui.QPushButton(self.centralwidget)
        self.quitBtn.setGeometry(QtCore.QRect(422, 430, 201, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.quitBtn.setFont(font)
        self.quitBtn.setObjectName(_fromUtf8("quitBtn"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.smartMartLabel.setText(_translate("MainWindow", "Smart-Mart Stock Monitoring System", None))
        self.viewStocksBtn.setText(_translate("MainWindow", "View Stocks", None))
        self.smartMartLabel_2.setText(_translate("MainWindow", "Main Menu", None))
        self.updateStocksBtn.setText(_translate("MainWindow", "Update Stocks", None))
        self.addDelBtn.setText(_translate("MainWindow", "Add/Delete Orders", None))
        self.quitBtn.setText(_translate("MainWindow", "Quit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

