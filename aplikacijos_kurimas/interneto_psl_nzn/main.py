from PyQt6.QtWidgets import QApplication, QMainWindow
from dizainas import Ui_MainWindow
import requests
from bs4 import BeautifulSoup
from time import sleep

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        # į connect metodą perduodam funkcija, kuria norėsim aktyvuoti
        self.button.clicked.connect(self.rezultatas)
       
    def rezultatas(self):
        link = self.url.text()
        self.atsakymas.setText(f"Nuoroda: {link}")

    base_url = "https://elenta.lt"
    next_url = "/skelbimai/nt/butai"

    def insert_data(base, next) :  
        response = []
        data = requests.get(base + next)
        html = BeautifulSoup(data.text, "html.parser")

        data = html.select('.units-list li')
        next = html.select_one('[rel="next"]')

        for listing in data:
            
            name = listing.select_one('a.ad-hyperlink')
            name = name.text if name else ""

            photo_adr = listing.select_one('img')
            photo_adr = photo_adr.attrs['src'] if photo_adr else ""

            price = listing.select_one('.price-box')
            price = price.text if price else "0"
            
            address = listing.select_one(".location-box")
            address = address.attrs["title"].replace("adresas", "").replace("vieta", "").strip() if address else "Nenurodyta"
            
            description = listing.select_one("p")
            description = description.text if description else ""
            
            cur.execute(f"INSERT INTO skelbimu_info (name, description, address, price, photo_adr) VALUES ('{name}', '{description}', '{address}', '{price}','{photo_adr}')")


            # Vykdo palaukimą sekundžių tikslumu   
            sleep(1)
    

        
        if next :
            next = html.select_one('[rel="next"]').attrs['href']
            response += insert_data(base, next)

        return response   





    
app = QApplication([])

window = Window()

window.show()
app.exec()