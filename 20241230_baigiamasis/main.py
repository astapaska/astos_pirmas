'''● https://elenta.lt/ arba ● https://www.skelbiu.lt/ arba ● https://www.aruodas.lt/
Iš tinklapio surinkti visų kategorijoje esančių skelbimų pavadinimus ir kainas, informaciją programa turi išsaugoti csv faile.
Sukurti vartotojo sąsają naudojant PyQt6 biblioteką, kurioje vartotojas įvestų norimo tinklapio adresą. 
Jei šis yra netinkamas t.y. įvedamas blogas domenas arba gaunama bloga nuorodos struktūra, vartotojui grąžinamas 
informacinis pranešimas apie netinkamai įvestą reikšmę.
Surinkus visus kategorijos duomenis vartotojui atvaizduojamas informacinis pranešimas, kuriame nurodomas visų apdorotų skelbimų
kiekis, bendra visų skelbimų vertė (kainų suma).
Pabaigtą darbo kodą patalpinti į github repozitoriją kurios adresą atsiųskite el. paštu viliusramulionisvcs@gmail.com '''
# yra validus URL
# puslapis turi egzistuoti (grįžta 200)
# domenas yra elenta.lt + kategorija (prasideda /skelbimai)

import requests
from PyQt6.QtWidgets import QApplication, QMainWindow
from dizainas import Ui_MainWindow
from bs4 import BeautifulSoup
from time import sleep

# Funkcija linko validavimui
def validate_url(input_url):
    try:
        requests.get(input_url)
    except:
        return False
    
    data = requests.get(input_url)

    if data.status_code != 200 :
        return False
    if input_url.startswith("https://elenta.lt/skelbimai"):
        return True
    else : return False

# Funkcija, kuria surenkami duomenys įrašymui į failą
def get_data(base, next) :  
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
        response += get_data(base, next)

    return response    

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
     
        # į connect metodą perduodam funkciją, kurią norėsim aktyvuoti
        self.button.clicked.connect(self.ivedimas)
       
    def ivedimas(self):
        linkas = self.url.text()
        if validate_url(linkas) == False :
            self.atsakymas.setText("Įveskite teisingą puslapio adresą")
            return
               
        base_url = "https://elenta.lt"
        next_url = linkas.replace("https://elenta.lt","") 

        # Įrašymas į failą
        f = open("skelbimai.csv", "w", encoding="utf8")

        data = get_data(base_url, next_url)
        f.write("Aprasymas;Kaina\n")

        price_sum = 0
        count = len(data)

        for listing in data :
            price_sum +=int((listing["price"]))
            f.write(";".join(listing.values()) + "\n")
        print(price_sum)
        print(count)
        
        # Atsakymas vartotojui
        self.atsakymas.setText(f"Nurodytoje kategorijoje yra: \n{count} skelbimų, kuriuose nurodytų daiktų suma yra {price_sum} Eur")
    
app = QApplication([])

window = Window()

window.show()
app.exec()
