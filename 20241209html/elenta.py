import requests
import mysql.connector
from bs4 import BeautifulSoup
from time import sleep

cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="elenta")

cur = cnx.cursor()

base_url = "https://elenta.lt"
next_url = "/skelbimai/nt/butai"

def insert_data(base, next) :  
    response = []
    data = requests.get(base + next)
    html = BeautifulSoup(data.text, "html.parser")

    '''kitas budas, bet geriau
    html = BeautifulSoup(data.text, "html.parser")
    html.find_all('li', )'''

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

        # response.append({
        #       "name" : name,
        #       "photo_adr": photo_adr,
        #     "price" : price,
        #     "address": address,
        #     "description": description        })

    sleep(1)
   
    # Užregistruojame pakeitimus
    cnx.commit()
    # Vykdo palaukimą sekundžių tikslumu 
    
    if next :
        next = html.select_one('[rel="next"]').attrs['href']
        response += insert_data(base, next)

    return response

insert_data(base_url, next_url)
# for data in response: 
#     print(data)
#     cur.execute(f"INSERT INTO info (name, description, address, price, photo_adress) VALUES ('{data.name}', '{data.description}', '{data.address}', '{data.price}','{data.photo_adr}')")
#     # Užregistruojame pakeitimus
#     cnx.commit()



cnx.close()
