import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

my_app=QApplication([])
loader=QUiLoader()

my_window=loader.load("calculator.ui")
def sum():        
    global amell
    amell="+"
    number=my_window.lineEdit.text()
    number+="+"
    my_window.lineEdit.setText(number)
def sub():   
    global amell
    amell="-"
    number=my_window.lineEdit.text()
    number+="-"
    my_window.lineEdit.setText(number)

def division():  
    global amell
    amell="/"
    number=my_window.lineEdit.text()
    number+="/"
    my_window.lineEdit.setText(number)

def multi():      
    global amell
    amell="*"
    number=my_window.lineEdit.text()
    number+="*"
    my_window.lineEdit.setText(number)
    
def sin():
    global amell
    amell="sin"
    number=my_window.lineEdit.text()
    number2=math.sin(int(number))
    my_window.lineEdit.setText(str(number2))
def cos():
    global amell
    amell="cos"
    number=my_window.lineEdit.text()
    number2=math.cos(int(number))
    my_window.lineEdit.setText(str(number2))
def tan():
    global amell
    amell="tan"
    number=my_window.lineEdit.text()
    number2=math.tan(int(number))
    my_window.lineEdit.setText(str(number2))
def cot():
    global amell
    amell="cot"
    number=my_window.lineEdit.text()
    number2=math.cot(int(number))
    my_window.lineEdit.setText(str(number2))
def log():
    global amell
    amell="log"
    number=my_window.lineEdit.text()
    number2=math.log(int(number))
    my_window.lineEdit.setText(str(number2))
def c():
    my_window.lineEdit.setText("")
def equal():        #مساوی
    if amell=="+":
        answer=my_window.lineEdit.text().split("+")
        c=0
        for i in answer:
            c+=int(i)
        my_window.lineEdit.setText(str(c))
    elif amell=="-":
        answer=my_window.lineEdit.text().split("-")
        c=int(answer[0])
        c-=int(answer[1])
        my_window.lineEdit.setText(str(c))
    elif amell=="*":
        answer=my_window.lineEdit.text().split("*")
        c=int(answer[0])
        c*=int(answer[1])
        my_window.lineEdit.setText(str(c))
    elif amell=="/":
        answer=my_window.lineEdit.text().split("/")
        c=int(answer[0])
        c//=int(answer[1])
        my_window.lineEdit.setText(str(c))
def write(number):
    b=str(my_window.lineEdit.text())
    c=b+str(number)
    my_window.lineEdit.setText(c)
my_window.pu1.clicked.connect(partial(write,1))
my_window.pu2.clicked.connect(partial(write,2))
my_window.pu3.clicked.connect(partial(write,3))
my_window.pu4.clicked.connect(partial(write,4))
my_window.pu5.clicked.connect(partial(write,5))
my_window.pu6.clicked.connect(partial(write,6))
my_window.pu7.clicked.connect(partial(write,7))
my_window.pu8.clicked.connect(partial(write,8))
my_window.pu9.clicked.connect(partial(write,9))
my_window.pu0.clicked.connect(partial(write,0))
my_window.pusum.clicked.connect(sum)
my_window.puequal.clicked.connect(equal)
my_window.pusub.clicked.connect(sub)
my_window.pumulti.clicked.connect(multi)
my_window.pudivi.clicked.connect(division)
my_window.pusin.clicked.connect(sin)
my_window.pucos.clicked.connect(cos)
my_window.putan.clicked.connect(tan)
my_window.pucot.clicked.connect(cot)
my_window.pulog.clicked.connect(log)
my_window.puc.clicked.connect(c)

my_window.show()

my_app.exec()
