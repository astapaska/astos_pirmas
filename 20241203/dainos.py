import mysql.connector

cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    database="smdb")

cur = cnx.cursor()

# pavadinimas = input("Įveskite dainos pavadinimą: ")
# atlikejas = input("Įveskite atlikėją: ")
# zanras = input("Įveskite žanrą: ")
# cur.execute(f"insert into dainos (pavadinimas, atlikejas, zanras) values ('{pavadinimas}','{atlikejas}','{zanras}')")
# cur.execute("update dainos set pavadinimas='Kelias bega' where id = 4")
# cur.execute("delete from dainos where id=1")

newsong = input('Norėdami papildyti sąrašą, įveskite raidę "n".\nNeįvedus raidės bus grąžinamas dainų sąrašas.\n ')

if newsong.lower() == 'n':
    pavadinimas = input("Įveskite dainos pavadinimą: ")
    atlikejas = input("Įveskite atlikėją: ")
    zanras = input("Įveskite žanrą: ")
    cur.execute(f"insert into dainos (pavadinimas, atlikejas, zanras) values ('{pavadinimas}','{atlikejas}','{zanras}')")
else : 
    cur.execute("select * from dainos")
    data = cur.fetchall()
    for dainos in data :
        print(dainos)

cnx.commit()
cnx.close()
print("Done!!! ")

# Paleista programa atspausdina visus įrašus esančius lentelėje. Tuomet vartotojo paprašome įvesti norima veiksmą:
# N - Naujas įrašas
# E - Įrašo redagavimas
# D - Įrašo ištrynimas
# Jeigu pasirenkama E arba D raide, tuomet paprašoma įvesti norimo įrašo ID.
# Jeigu vykdomas redagavimo veiksmas, tuomet paprašoma įvesti stulpelius kuriuos norima redaguoti ir vėliau stulpelių reikšmes.
# Jeigu norima tik ištrinti įrašą, užtenka tik įrašo ID.

#Pralėskite programą:
# Leiskite ištrinti tik tuos įrašus kurie turi žanrą "Country"
# Leiskite įrašyti tik tas dainas kurių atlikėjo pavadinime yra vardas "Virgis"
# Dainų pavadinimuose išfiltruokite žodį "American" vietoje jų palikdami "Lithuanian"