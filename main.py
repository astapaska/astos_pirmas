import mysql.connector
# Connect to server
cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="",
    database="world_countries")

cur = cnx.cursor()    
cur.execute("SELECT * FROM country_data")

data = cur.fetchall()
print(data)
