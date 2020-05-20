from PySide2.QtWidgets import *
from random import *

class IsenCycles(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Cycles de l'ISEN Yncrea Ouest")
        self.setMinimumSize(500,300)
        self.layout= QVBoxLayout()

        self.button = QPushButton("Changer le cycle")
        self.label = QLabel()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.buttonClicked)

     
        self.setLayout(self.layout)

    def buttonClicked(self):
        self.liste = ["CSI", "CIR", "BIOST", "CENT", "BIAST", "EST"]

        self.random = randint(0,5)
        self.label.setText(self.liste[self.random])



if __name__ == "__main__":
   app = QApplication([])
   ihm = IsenCycles()
   ihm.show()
   app.exec_()