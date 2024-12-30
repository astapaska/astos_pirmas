from PyQt6.QtWidgets import QApplication, QMainWindow
from plius_minus import Ui_MainWindow

class Langas(QMainWindow, Ui_MainWindow) :
    # skaiciuotuvas = 0 

    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pliusas.clicked.connect(self.plius)
        self.minusas.clicked.connect(self.minus)

    def pliusas(self) :
        # self.skaiciuotuvas += 1
        # self.skaicius.setText(str(self.skaiciuotuvas))
        
        # print(int(self.skaicius.text()) + 1)
        self.skaicius.setText(str(int(self.skaicius.text()) + 1))

    def minusas(self) :
        self.skaicius.setText(str(int(self.skaicius.text()) - 1))


aplikacija = QApplication([])

langas = Langas()

langas.show()
aplikacija.exec()