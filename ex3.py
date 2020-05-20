from PySide2.QtWidgets import *

class IHM(QWidget):
    def __init__(self, click):
        QWidget.__init__(self)
        self.click = click

        self.setWindowTitle("IHM")
        self.setMinimumSize(600, 400)
        self.layout = QVBoxLayout()

        self.panel = QTextEdit("Le nombre de clics va etre affiche ici")


        self.button = QPushButton("Changez mon texte !")
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.panel)

        self.button.clicked.connect(self.numberClick)

        self.setLayout(self.layout)

    def numberClick(self):
        self.click += 1
        self.button.setText(str("Click"+str(self.click)))
        self.panel.setText("Click"+str(self.click))




if __name__ == "__main__":
   app = QApplication([])
   ihm = IHM(0)
   ihm.show()
   app.exec_()


