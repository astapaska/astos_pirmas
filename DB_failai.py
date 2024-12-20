# CREATE  READ UPDATE DELETE

# def create_task(task) :
#     data = open("db.txt", "r")
#     id = data.readlines()[0].replace("\n", "")
#     # Uždaro failą
#     data.close() 
#     data = open("db.txt", "a", encoding="utf8")
#     data.write(f"{id};{task};0\n")

def create_task(task) :
    # Atidaromas failas perskaitymui
    f = open("db.txt", "r", encoding="utf8")

    # Paimamos faile esančios eilutės liste
    data = f.readlines()

    # Uždaro failą
    f.close() 

    # "w - write"
    f = open("db.txt", "w", encoding="utf8")

    # Patalpinam naują eilutę sąraše
    data.append(f"{data[0].replace("\n", "")};{task};0\n")

    # Padidiname Sekančio indentifikatoriaus reikšmę
    data[0] = str(int(data[0].replace("\n", "")) + 1) + "\n"

    # Visą tekstą išssaugome faile
    f.write("".join(data))  

    # Uždarome failą
    f.close()

create_task(input("Įveskite užduotį:"))

def del_line(opa):
    file = open("db.txt", "w", encoding="utf8")
    data = file.readlines()
    file.close()

    file = open("db.txt", "w", encoding="utf8")
    data 