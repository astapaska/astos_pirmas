from PyQt6.QtWidgets import QApplication, QMainWindow
from dizainas import Ui_mainWindow

class Window(QMainWindow, Ui_mainWindow):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        
        # į connect metodą perduodam funkcija, kuria norėsim aktyvuoti
        self.mygtukas.clicked.connect(self.ivedimas)
       
    def ivedimas(self):
        amzius = 2024 - int(self.metai.text())
        
        print("Metai: ", amzius)

        self.atsakymas.setText(f"Gerbiamasis (-oji) {self.vardas.text()}{self.pavarde.text()} jūsų amžius yra {amzius}")
        
    
app = QApplication([])

window = Window()

window.show()
app.exec()
