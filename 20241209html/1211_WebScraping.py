import requests

url ="https://www.thecocktaildb.com/api/json/v1/1/search.php?s="
search_code = input("Įveskite paieškos frazę: ").strip()
search =f"{url}{search_code}"

# search = input("Įveskite norimo kokteilio pavadinimą: ")
# url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={search}"

response = requests.get(search)

data = response.json()
#f = open("dataholic.txt", "w")
#print(data)
for drink in  data["drinks"]:
    print(f"Pavadinimas: {drink["strDrink"]}, Tipas: {drink["strAlcoholic"]}, Kategorija {drink["strCategory"]}")
    #f.write(f"Pavadinimas: {drink["strDrink"]}, Tipas: {drink["strAlcoholic"]}, Kategorija {drink["strCategory"]}\n")