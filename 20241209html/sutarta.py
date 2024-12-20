import requests
import mysql.connector
from bs4 import BeautifulSoup
#from time import sleep

cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="elenta")
cur = cnx.cursor()

# Adreso priskyrimas
base_url = "https://sutarta.lt/skelbimai/garso-vaizdo-foto-technika/vaizdo-video-technika"

# Pateikiame užklausą
data = requests.get(base_url)

# Konvertuojame HTML kodą į objektą
html = BeautifulSoup(data.text, "html.parser")

for listing in html.select(".list li"):
    if listing.select_one(".list-media"):
      continue

    time = listing.select_one('div.list-date').text
    photo = listing.select_one('img')
    description = listing.select_one('div .desc-title').text
    category = listing.select_one(".section-category a").text
    price = listing.select_one('div .desc .section').text
    print(f"Paskelbimo laikas: {time} Aprasymas: {description} foto: {photo} \n kategorija: {category} \n kaina: {price}") #
    

   # sleep(1)
# cur.execute(f"INSERT INTO skelbimu_info (description) VALUES ('{description}')")

# # Užregistruojame pakeitimus
# cnx.commit()
# cnx.close()

# def get_data(base, next) :  
#     response = []
#     data = requests.get(base + next)
#     data = html.select('.list li')
#     data = data.text