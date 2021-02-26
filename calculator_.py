from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys
from MainWindow import Ui_MainWindow
import methods
import countMethods

class CalcApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(CalcApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_equal.clicked.connect(self.showCountResult)
        self.ui.btn_ce.clicked.connect(self.clear)
        self.ui.text_line.textChanged.connect(self.textChanged)
        self.showClickResult()
        
    def showClickResult(self):
        regExp = QtCore.QRegExp("btn_([0-9])|(add)|(sub)|(mul)|(div)")
        buttons = self.ui.centralwidget.findChildren(QtWidgets.QPushButton,regExp)
        for i in buttons:
            i.clicked.connect(self.btnInput)
    def showCountResult(self):
        self.ui.text_line.setText(countMethods.count(self.ui.text_line.text()))
    def clear(self):
        self.ui.text_line.clear()
        self.ui.text_line.setFocus()
    def btnInput(self):
        text =self.ui.text_line.text() + self.sender().text()
        self.ui.text_line.setText(text)
    def keyPressEvent(self, event):
        if event.key() in [QtCore.Qt.Key_Equal, QtCore.Qt.Key_Enter]:
            self.showCountResult()
    def textChanged(self):
        self.ui.text_line.setText(methods.verifyText(self.ui.text_line.text()))
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = CalcApp()
    win.show()
    sys.exit(app.exec_())
app()