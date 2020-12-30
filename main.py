
import sys
import os

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from functools import partial

class main(QWidget):
    firstNum = 0
    secoundNum = 0
    Answer =  0
    operator = '='
    flag = True
    def __init__(self):
        super(main, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load('form.ui')
        self.ui.show()
        self.start()
   
    def start(self):
            self.ui.btn_0.clicked.connect(partial(self.setNumber,0))
            self.ui.btn_1.clicked.connect(partial(self.setNumber,1))
            self.ui.btn_2.clicked.connect(partial(self.setNumber,2))
            self.ui.btn_3.clicked.connect(partial(self.setNumber,3))
            self.ui.btn_4.clicked.connect(partial(self.setNumber,4))
            self.ui.btn_5.clicked.connect(partial(self.setNumber,5))
            self.ui.btn_6.clicked.connect(partial(self.setNumber,6))
            self.ui.btn_7.clicked.connect(partial(self.setNumber,7))
            self.ui.btn_8.clicked.connect(partial(self.setNumber,8))
            self.ui.btn_9.clicked.connect(partial(self.setNumber,9))
            self.ui.btn_sum.clicked.connect(partial(self.setOperator,'+')) 
            self.ui.btn_sub.clicked.connect(partial(self.setOperator,'-')) 
            self.ui.btn_div.clicked.connect(partial(self.setOperator,'/')) 
            self.ui.btn_multi.clicked.connect(partial(self.setOperator,'*'))
            self.ui.btn_eq.clicked.connect(self.answer)
            self.ui.btn_c.clicked.connect(self.C)

    def C(self):
        self.ui.out.setText(" ")
        self.firstNum = 0
        self.secoundNum = 0
        self.Answer =  0
        self.operator = '='
        self.flag = True
    def setNumber(self,num):
        if self.flag is True :
            self.firstNum = self.firstNum*10 + num
            self.ui.out.setText(str(self.firstNum))
        elif not self.Answer==0:
            self.firstNum=self.Answer
            self.Answer=0
            self.secoundNum=0
            self.secoundNum = self.secoundNum*10 + num 
            self.ui.out.setText(str(self.firstNum)+str(self.operator)+str(self.secoundNum))
        else:
            self.secoundNum = self.secoundNum*10 + num 
            self.ui.out.setText(str(self.firstNum)+str(self.operator)+str(self.secoundNum))
 
    def setOperator(self,op):
        self.operator=op
        if not self.Answer==0:
            self.ui.out.setText(str(self.Answer)+str(self.operator))
        else:
            self.ui.out.setText(str(self.firstNum)+str(self.operator))
        self.flag=False
    def answer(self):
        if self.operator=="+":
            self.Answer = self.firstNum + self.secoundNum
        elif self.operator=="-":
            self.Answer = self.firstNum - self.secoundNum
        elif self.operator=="/":
            self.Answer = self.firstNum/self.secoundNum
        elif self.operator=="*":
            self.Answer = self.firstNum*self.secoundNum
        self.ui.out.setText(str(self.Answer))

if __name__ == "__main__":
    app = QApplication([])
    widget = main()
    sys.exit(app.exec_())
