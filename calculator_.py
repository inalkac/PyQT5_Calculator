from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys
from MainWindow import Ui_MainWindow

class CalcApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(CalcApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_equal.clicked.connect(self.count)
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
        
        
    def convertText(self, textToConvert):
        charList = list(textToConvert)
        number1=[]
        number2=[]
        index = 0
        if charList[0] == '-':
                number1.append(charList[index])
        while charList[index] not in ['+','-','*','/']:
            number1.append(charList[index])
            index+=1
        sign = charList[index]
        index+=1
        if charList[index] == '-':
                number2.append(charList[index])
        while index< len(charList):
            number2.append(charList[index])
            index+=1
        number1 = ''.join(number1)
        number2 = ''.join(number2)
        return [number1, sign, number2]
    def count(self):
        x = self.convertText(self.ui.text_line.text())
        if x[1] == '+':
            result = int(x[0]) + int(x[2])
        elif x[1] == '-':
            result = int(x[0]) - int(x[2])
        elif x[1] == "*":
            result = int(x[0]) * int(x[2])
        elif x[1] == '/':
            result = int(x[0]) / int(x[2])
        self.ui.text_line.setText(str(result))
    def clear(self):
        self.ui.text_line.clear()
        self.ui.text_line.setFocus()
    def btnInput(self):
        text =self.ui.text_line.text() + self.sender().text()
        self.ui.text_line.setText(text)
    def keyPressEvent(self, event):
        if event.key() in [QtCore.Qt.Key_Equal, QtCore.Qt.Key_Enter]:
            self.count()
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = CalcApp()
    win.show()
    sys.exit(app.exec_())
app()