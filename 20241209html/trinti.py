import mysql.connector
cnx = None
try :
    # Prisijungimas prie serverio:
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="i1551")
except :
    # print(e)
    print("Prisijungimo klaida")

# Kursoriaus sukūrimas
cur = cnx.cursor()

title = input("Įveskite firmos pavadinimą: ")
description = input("Įveskite aprašymą: ")
address = input("Įveskite adresą: ")
phone = input("Reikia telefono nr: ")

# Nurodome sql komandinę eilutę
#cur.execute(f"INSERT INTO info (title, description, address, phone) VALUES ('{title}', '{description}', '{address}, '{phone}')")
cur.execute(f"INSERT INTO info (title) VALUES ('{title}')")

# Užregistruojame pakeitimus
cnx.commit()

# Prisijungimo uždarymas
cnx.close()