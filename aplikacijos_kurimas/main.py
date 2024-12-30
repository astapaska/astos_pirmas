from PyQt6.QtWidgets import QApplication, QMainWindow
from dizainas import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pirmas_mygtukas.clicked.connect(self.pirmas_paspaudimas)
        self.antras_mygtukas.clicked.connect(self.antras_paspaudimas)
        self.trecias_mygtukas.clicked.connect(self.trecias_paspaudimas)

    def pirmas_paspaudimas(self):
        self.zinute.setText("Pirmas mygtukas paspaustas")

    def antras_paspaudimas(self):
        self.zinute.setText("Antras mygtukas paspaustas")

    def trecias_paspaudimas(self):
        self.zinute.setText("Trecias mygtukas paspaustas")

app = QApplication([])

window = Window()

window.show()
app.exec()
