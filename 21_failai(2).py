data = open("vartotojai.txt", "r")

#1.Išfiltruokite ir grąžinkite vartotojus kurių slaptažodžiuose nėra skaičių
#lektorius isloopino ir tikrino kiekvienq simboli6 bet paskui persigalvojo ir paliko boolean
'''for line in data.readlines()[1:]:
    l=line.replace("\n","").split(";") 
    if l[4].isalpha() :
     print(line,end="")''' 

#2.Išfiltruokite vartotojus, kurie neturi gimimo metų
'''for line in data.readlines()[1:]:
    l=line.split(";") 
    if l[3]:
        print(line,end="")          '''

#3.Išfiltruokite vartotojų amžiaus vidurkį
'''amziaus_suma = 0
asmenys = 0
for line in data.readlines()[1:]:
    l=line.split(";")
    if l[3] :
       amziaus_suma += 2024- int(l[3])
       asmenys += 1
print(amziaus_suma/asmenys)         '''

#4.Išfiltruokite vartotojus su neteisingais el. pašto adresais
# for line in data.readlines()[1:]:
#     l=line.split(";") 
#     '''#print(l)
#     if not "@" in l[2] :
#         print(line,end="")  cia ok gaunasi, bet lektorius su daugiau sqlygu pvz. duoda'''
#     if "@" in l[2] :
#         if len(l[2].split("@")[1].split(".")) ==2 :
#             print(line)

#5.Išfiltruokite vartotojus, kurių slaptažodžiai yra trumpesni nei 5 simboliai
'''for line in data.readlines()[1:]:
    l=line.split(";") 
    #print(len(l[4]))
    if len(l[4]) >= 5:
        print(line,end="")          '''

#6.Išfiltruokite vartotojus kurie nėra įvedę pavardės 
'''for line in data.readlines()[1:]:
    l= line.split(";")
    if len(l[1]) > 0: 
        print(line,end="")  '''