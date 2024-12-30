'''● https://elenta.lt/ arba ● https://www.skelbiu.lt/ arba ● https://www.aruodas.lt/
Iš tinklapio surinkti visų kategorijoje esančių skelbimų pavadinimus ir kainas, informaciją programa turi išsaugoti csv faile.
Sukurti vartotojo sąsają naudojant PyQt6 biblioteką, kurioje vartotojas įvestų norimo tinklapio adresą. 
Jei šis yra netinkamas t.y. įvedamas blogas domenas arba gaunama bloga nuorodos struktūra, vartotojui grąžinamas 
informacinis pranešimas apie netinkamai įvestą reikšmę.
Surinkus visus kategorijos duomenis vartotojui atvaizduojamas informacinis pranešimas, kuriame nurodomas visų apdorotų skelbimų
kiekis, bendra visų skelbimų vertė (kainų suma).
Pabaigtą darbo kodą patalpinti į github repozitoriją kurios adresą atsiųskite el. paštu viliusramulionisvcs@gmail.com '''
# https://elenta.lt/
# www.elenta.lt
# elenta.lt

from PyQt6.QtWidgets import QApplication, QMainWindow
from dizainas import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
     
        # į connect metodą perduodam funkciją, kurią norėsim aktyvuoti
        self.button.clicked.connect(self.ivedimas)
       
    def ivedimas(self):
        linkas = self.url.text()
        
        #print("Nuoroda: ", linkas)
        self.atsakymas.setText(f"Nurodytoje kategorijoje {linkas} yra: ")#\n {self.kiekis()} skelbimų, kuriuose nurodytų daiktų suma yra {self.suma()} Eur")
    
app = QApplication([])

window = Window()

window.show()
app.exec()


import requests
from bs4 import BeautifulSoup
from time import sleep

base_url = "https://elenta.lt"
next_url = "/skelbimai/auto-moto/zemes-ukio-technika"

# Funkcija, kuria surenkami duomenys įrašymui į failą
def insert_data(base, next) :  
    response = []
    
    data = requests.get(base + next)
    html = BeautifulSoup(data.text, "html.parser")

    data = html.select('.units-list li')
    next = html.select_one('[rel="next"]')

    for listing in data:
        
        name = listing.select_one('a.ad-hyperlink')
        name = name.text if name else "" 
        
        price = listing.select_one('.price-box')
        price = price.text.replace("€","").replace(" ","")  if price else "0"
                      
        response.append({"name" : name.replace(";",","), "price" : price, })
        
    # Vykdo palaukimą sekundžių tikslumu 
    sleep(1)
    
    if next :
        next = html.select_one('[rel="next"]').attrs['href']
        response += insert_data(base, next)

    return response

# Įrašymas į failą
f = open("skelbimai.csv", "w", encoding="utf8")

data = insert_data(base_url, next_url)
f.write("Aprasymas;Kaina\n")

price_sum = 0
count = len(data)

for listing in data :
    price_sum +=int((listing["price"]))
    f.write(";".join(listing.values()) + "\n")
print(price_sum)
print(count)