from bs4 import BeautifulSoup
from selenium import webdriver # naršyklės kontroleris
from selenium.webdriver.chrome.options import Options #Naršyklės

opcijos = Options()
# Incognito mode
opcijos.add_argument('--incognito')
# Nustatome, jog mums neatidarinėtų naršyklės:
opcijos.add_argument('--headless')

driver = webdriver.Chrome(options=opcijos)
url = "https://www.baldoras.lt/katalogas/valgomojo-stalai/"
driver.get(url) #puslapio atsisiuntimas

source = driver.page_source # pasiimam puslapio html kodą

bs = BeautifulSoup(source, 'html.parser') 
print(bs.select_one('.product-card__prices').text)

prices = bs.select('.product-card__prices')

count = 0
sum = 0

# def get_links(url):
i = 1
while i < 4 :
    new_url = f"{url}{i}"
    print(new_url)
    driver.get(new_url) #puslapio atsisiuntimas
    source = driver.page_source # pasiimam puslapio html kodą
    bs = BeautifulSoup(source, 'html.parser') 
    prices = bs.select('.product-card__prices')

    for price in prices:
        #avg = 0
        sum += int(price.text.strip().replace("€",""))
        count += 1 
    i+=1

print(f"Vidurkis: {(sum/count):.0f} Eur")
