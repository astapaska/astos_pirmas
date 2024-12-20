import requests
import mysql.connector
from bs4 import BeautifulSoup

cnx = None
try :
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="i1551")
except :
    # print(e)
    print("Prisijungimo klaida")
cur = cnx.cursor()

url = "https://www.1551.lt/automobiliu-atsargines-dalys-reikmenys/"
data = requests.get(url)

if data.status_code !=200:
    print("Nepavyko gauti duomenų")
else: 
    data = data.text

html = BeautifulSoup(data,  "html.parser")

for box in html.select(".tm-result") :
    title = box.select_one(".uk-panel-title a span").text
    description = box.select_one(".uk-margin").text
    #print(box.select_one(".uk-margin uk-hidden-small"))#description ne text
    address = box.select_one(".uk-margin-right").text
    phone = box.select_one(".uk-width-medium-3-10 a span").text

    # Nurodome sql komandinę eilutę
    cur.execute(f"INSERT INTO info (title, description, address, phone) VALUES ('{title}', '{description}', '{address}', '{phone}')")

    # Užregistruojame pakeitimus
    cnx.commit()

cnx.close()
