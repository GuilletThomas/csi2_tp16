from PySide2.QtWidgets import *

class IHM(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.layout = QHBoxLayout()

        self.progressBar = QProgressBar()
        self.slider = QSlider()

        self.layout.addWidget(self.progressBar)
        self.layout.addWidget(self.slider)

        self.slider.valueChanged.connect(self.OnSlider)


        self.setLayout(self.layout)

    def OnSlider(self):
        val = self.slider.value()
        self.progressBar.setValue(val)



if __name__ == "__main__":
   app = QApplication([])
   ihm = IHM()
   ihm.show()
   app.exec_()