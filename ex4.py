from PySide2.QtWidgets import *
from random import *

class Calculator(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Calculator")
        self.setMinimumSize(400,300)
        self.layout= QGridLayout()




        self.panel = QLineEdit("0")

        self.buttonC = QPushButton("C")
        self.buttonCE= QPushButton("CE")

        self.button7 = QPushButton("7")
        self.button8 = QPushButton("8")
        self.button9 = QPushButton("9")
        self.buttonDIV = QPushButton("/")

        self.button4 = QPushButton("4")
        self.button5 = QPushButton("5")
        self.button6 = QPushButton("6")
        self.buttonMULT = QPushButton("*")

        self.button1 = QPushButton("1")
        self.button2 = QPushButton("2")
        self.button3 = QPushButton("3")
        self.buttonSOUST = QPushButton("-")

        self.button0 = QPushButton("0")
        self.buttonDEC = QPushButton(",")
        self.buttonEGA = QPushButton("=")
        self.buttonADD = QPushButton("+")



        self.layout.addWidget(self.panel, 0,0, 1,4)

        self.layout.addWidget(self.buttonC, 1,0,1,2)
        self.buttonC.clicked.connect(self.buttonCLicked("C"))

        self.layout.addWidget(self.buttonCE, 1,2,1,2)
        self.buttonCE.clicked.connect(self.buttonCLicked("CE"))


        self.layout.addWidget(self.button7, 2,0,1,1)
        self.button7.clicked.connect(self.buttonCLicked("7"))

        self.layout.addWidget(self.button8, 2,1,1,1)
        self.button8.clicked.connect(self.buttonCLicked("8"))

        self.layout.addWidget(self.button9, 2,2,1,1)
        self.button9.clicked.connect(self.buttonCLicked("9"))

        self.layout.addWidget(self.buttonDIV, 2,3,1,1)
        self.buttonDIV.clicked.connect(self.buttonCLicked("/"))



        self.layout.addWidget(self.button4, 3,0,1,1)
        self.button4.clicked.connect(self.buttonCLicked("4"))

        self.layout.addWidget(self.button5, 3,1,1,1)
        self.button5.clicked.connect(self.buttonCLicked("5"))

        self.layout.addWidget(self.button6, 3,2,1,1)
        self.button6.clicked.connect(self.buttonCLicked("6"))

        self.layout.addWidget(self.buttonMULT, 3,3,1,1)
        self.buttonMULT.clicked.connect(self.buttonCLicked("*"))



        self.layout.addWidget(self.button1, 4,0,1,1)
        self.button1.clicked.connect(self.buttonCLicked("1"))

        self.layout.addWidget(self.button2, 4,1, 1,1)
        self.button2.clicked.connect(self.buttonCLicked("2"))

        self.layout.addWidget(self.button3, 4,2,1,1)
        self.button3.clicked.connect(self.buttonCLicked("3"))

        self.layout.addWidget(self.buttonSOUST,4,3,1,1)
        self.buttonSOUST.clicked.connect(self.buttonCLicked("-"))



        self.layout.addWidget(self.button0, 5,0,1,1)
        self.button0.clicked.connect(self.buttonCLicked("0"))

        self.layout.addWidget(self.buttonDEC, 5,1, 1,1)
        self.buttonDEC.clicked.connect(self.buttonCLicked(","))

        self.layout.addWidget(self.buttonEGA, 5,2,1,1)
        self.buttonEGA.clicked.connect(self.buttonCLicked("="))

        self.layout.addWidget(self.buttonADD, 5,3,1,1)
        self.buttonADD.clicked.connect(self.buttonCLicked("+"))



        self.setLayout(self.layout)


    def buttonCLicked(self, resultat):
        if resultat == "7":
            self.panel.setText("7")
        elif resultat == "8":
            self.panel.setText("8")
        elif resultat == "0":
            self.panel.setText("0")



if __name__ == "__main__":
   app = QApplication([])
   ihm = Calculator()
   ihm.show()
   app.exec_()


