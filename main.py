
import sys
import os
import math

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
    point= False
    hadAnsr=False
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
            self.ui.btn_pi.clicked.connect(partial(self.setNumber,3.1415926535897932384626433832795))

            self.ui.btn_point.clicked.connect(self.P)

            self.ui.btn_sum.clicked.connect(partial(self.setOperator,'+')) 
            self.ui.btn_sub.clicked.connect(partial(self.setOperator,'-')) 
            self.ui.btn_div.clicked.connect(partial(self.setOperator,'/')) 
            self.ui.btn_multi.clicked.connect(partial(self.setOperator,'*'))
            self.ui.btn_mod.clicked.connect(partial(self.setOperator,'mod'))

            self.ui.btn_root.clicked.connect(partial(self.setOperator2,'√'))
            self.ui.btn_Square.clicked.connect(partial(self.setOperator2,'x²'))
            self.ui.btn_log.clicked.connect(partial(self.setOperator2,'log'))
            self.ui.btn_factorial.clicked.connect(partial(self.setOperator2,'n!'))
            self.ui.btn_fractional.clicked.connect(partial(self.setOperator2,'1/x'))
            self.ui.btn_absolute.clicked.connect(partial(self.setOperator2,'|x|'))
            self.ui.btn_eq.clicked.connect(self.answer)
            self.ui.btn_c.clicked.connect(self.C)
    def P(self):
        self.point=True
    def C(self):
        self.ui.out.setText(" ")
        self.firstNum = 0
        self.secoundNum = 0
        self.Answer =  0
        self.operator = '='
        self.flag = True
        self.point=False
        self.hadAnsr=False
    def numberOfD(self, num):
        temp=str(num)
        i=1
        for j in range (len(temp)):
            if temp[j]=='.':
                i=len(temp)-j
        return i
    def setNumber2(self,num):
        if self.flag is True :
            self.firstNum = self.firstNum + num/math.pow(10,self.numberOfD(self.firstNum))
            self.ui.out.setText(str(self.firstNum))
            
        elif self.hadAnsr is True :
            self.firstNum=self.Answer
            self.Answer=0
            self.secoundNum=0
            
            self.secoundNum = self.secoundNum + num/math.pow(10,self.numberOfD(self.secoundNum))
            self.ui.out.setText(str(self.firstNum)+str(self.operator)+str(self.secoundNum))
            self.hadAnsr=False

        else:
           
            self.secoundNum = self.secoundNum + num/math.pow(10,self.numberOfD(self.secoundNum)) 
            self.ui.out.setText(str(self.firstNum)+str(self.operator)+str(self.secoundNum))

    def setNumber(self,num):
        if self.point is False:
            if self.flag is True :
                self.firstNum = self.firstNum*10 + num
                self.ui.out.setText(str(self.firstNum))
            elif self.hadAnsr is True :
                self.firstNum=self.Answer
                self.Answer=0
                self.secoundNum=0
                self.secoundNum = self.secoundNum*10 + num 
                self.ui.out.setText(str(self.firstNum)+str(self.operator)+str(self.secoundNum))
                self.hadAnsr=False
            else:
                self.secoundNum = self.secoundNum*10 + num 
                self.ui.out.setText(str(self.firstNum)+str(self.operator)+str(self.secoundNum))
        else:
            self.setNumber2(num)
 
    def setOperator(self,op):
        self.operator=op
        if self.hadAnsr is True:
            self.ui.out.setText(str(self.Answer)+str(self.operator))
        else:
            self.ui.out.setText(str(self.firstNum)+str(self.operator))
        self.flag=False
        self.point=False
    def setOperator2(self,op):
        if self.flag is True:
            if op=='√':
                self.firstNum=math.sqrt(self.firstNum)
            elif op=='x²':
                self.firstNum=self.firstNum*self.firstNum
            elif op=='log':
                 self.firstNum=math.log10(self.firstNum)
            elif op=='n!':
                for i in range(1 , self.firstNum):
                    self.firstNum=self.firstNum*i
            elif op=='1/x':
                self.firstNum=1/self.firstNum
            elif op=='|x|':
                if self.firstNum<0:
                    self.firstNum= -1*self.firstNum
            self.ui.out.setText(str(self.firstNum))
        elif self.hadAnsr is False:
            if op=='√':
                self.secoundNum=math.sqrt(self.secoundNum)
            elif op=='x²':
                self.secoundNum=self.secoundNum*self.secoundNum
            elif op=='log':
                 self.secoundNum=math.log10(self.secoundNum)
            elif op=='n!':
                for i in range(1 , self.secoundNum):
                    self.secoundNum=self.secoundNum*i
            elif op=='1/x':
                self.secoundNum=1/self.secoundNum
            elif op=='|x|':
                if self.secoundNum<0:
                    self.secoundNum= -1*self.secoundNum
            self.ui.out.setText(str(self.firstNum)+str(self.operator)+str(self.secoundNum))
        elif self.hadAnsr is True :
            if op=='√':
                self.Answer=math.sqrt(self.Answer)
            elif op=='x²':
                self.Answer=self.Answer*self.Answer
            elif op=='log':
                 self.Answer=math.log10(self.Answer)
            elif op=='n!':
                for i in range(1 , self.Answer):
                    self.Answer=self.Answer*i
            elif op=='1/x':
                self.Answer=1/self.Answer
            elif op=='|x|':
                if self.Answer<0:
                    self.Answer= -1*self.Answer
            self.ui.out.setText(str(self.Answer))

    def answer(self):
        if self.operator=="+":
            self.Answer = self.firstNum + self.secoundNum
        elif self.operator=="-":
            self.Answer = self.firstNum - self.secoundNum
        elif self.operator=="/":
            self.Answer = self.firstNum/self.secoundNum
        elif self.operator=="*":
            self.Answer = self.firstNum*self.secoundNum
        elif self.operator=="mod":
            self.Answer=self.firstNum%self.secoundNum
        self.hadAnsr=True
        self.ui.out.setText(str(self.Answer))

if __name__ == "__main__":
    app = QApplication([])
    widget = main()
    sys.exit(app.exec_())
