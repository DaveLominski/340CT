'''A UI file created by  Qt Designer software
    Broker topology means that each part of the user interface has its own file, this means that there should not be
    any name conflicts between the files'''

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

class Ui_logInWindow(object):
    def setupUi(self, logInWindow):
        logInWindow.setObjectName(_fromUtf8("logInWindow"))
        logInWindow.resize(1045, 726)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(logInWindow.sizePolicy().hasHeightForWidth())
        logInWindow.setSizePolicy(sizePolicy)
        logInWindow.setMinimumSize(QtCore.QSize(1045, 726))
        logInWindow.setMaximumSize(QtCore.QSize(1045, 726))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../Python36/Lib/site-packages/PyQt4/examples/widgets/icons/images/qt_extended_48x48.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        logInWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(logInWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.smartMartLabel = QtGui.QLabel(self.centralwidget)
        self.smartMartLabel.setGeometry(QtCore.QRect(212, 0, 621, 121))
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
        self.logInLabel = QtGui.QLabel(self.centralwidget)
        self.logInLabel.setGeometry(QtCore.QRect(482, 250, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.logInLabel.setFont(font)
        self.logInLabel.setObjectName(_fromUtf8("logInLabel"))
        self.usr = QtGui.QLineEdit(self.centralwidget)
        self.usr.setGeometry(QtCore.QRect(387, 300, 271, 31))
        self.usr.setObjectName(_fromUtf8("usr"))
        self.pwd = QtGui.QLineEdit(self.centralwidget)
        self.pwd.setGeometry(QtCore.QRect(387, 350, 271, 31))
        self.pwd.setObjectName(_fromUtf8("pwd"))
        self.usernameLabel = QtGui.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(220, 280, 131, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.passwordLabel = QtGui.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(220, 330, 131, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.logInButton = QtGui.QPushButton(self.centralwidget)
        self.logInButton.setGeometry(QtCore.QRect(462, 400, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.logInButton.setFont(font)
        self.logInButton.setObjectName(_fromUtf8("logInButton"))
        logInWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(logInWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        logInWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(logInWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        logInWindow.setStatusBar(self.statusbar)

        self.retranslateUi(logInWindow)
        QtCore.QMetaObject.connectSlotsByName(logInWindow)

    def retranslateUi(self, logInWindow):
        logInWindow.setWindowTitle(_translate("logInWindow", "Smart-Mart System", None))
        self.smartMartLabel.setText(_translate("logInWindow", "Smart-Mart Stock Monitoring System", None))
        self.logInLabel.setText(_translate("logInWindow", "Log-in", None))
        self.usernameLabel.setText(_translate("logInWindow", "Username", None))
        self.passwordLabel.setText(_translate("logInWindow", "Password", None))
        self.logInButton.setText(_translate("logInWindow", "Log-in", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    logInWindow = QtGui.QMainWindow()
    ui = Ui_logInWindow()
    ui.setupUi(logInWindow)
    logInWindow.show()
    sys.exit(app.exec_())

