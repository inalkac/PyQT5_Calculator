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
        self.ui.btn_0.clicked.connect(self.btnInput)
        self.ui.btn_1.clicked.connect(self.btnInput)
        self.ui.btn_2.clicked.connect(self.btnInput)
        self.ui.btn_3.clicked.connect(self.btnInput)
        self.ui.btn_4.clicked.connect(self.btnInput)
        self.ui.btn_5.clicked.connect(self.btnInput)
        self.ui.btn_6.clicked.connect(self.btnInput)
        self.ui.btn_7.clicked.connect(self.btnInput)
        self.ui.btn_8.clicked.connect(self.btnInput)
        self.ui.btn_9.clicked.connect(self.btnInput)
        self.ui.btn_add.clicked.connect(self.btnInput)
        self.ui.btn_sub.clicked.connect(self.btnInput)
        self.ui.btn_mul.clicked.connect(self.btnInput)
        self.ui.btn_div.clicked.connect(self.btnInput)
        self.ui.text_line.textChanged.connect(self.textChanged)
        
        
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