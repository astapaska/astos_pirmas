# a - append
# r - read
# w - write
'''
data = open("pomegiai.txt", "a")
zinute = input("Iveskite zinute")
data.write(zinute +"\n")    '''

data = open("U2.txt", "r")
data=data.readlines()
sokejai = int(data[0].split()[0])
teisejai = int(data[0].split()[1])

# print(sokejai, teisejai)
# print(data[1:])

for idx in range(1, sokejai *4, 3):
    vardai = data[idx].replace("\n","") 
    technika = data[idx + 1].replace("\n","").split()
    artistiskumas = data[idx + 2].replace("\n","").split()

    technikaMin = min(list(map(int, technika)))
    technikaMax = max(list(map(int, technika)))
    
    technika = sum(list(map(int, technika)))-technikaMin - technikaMax
    print(vardai , technika)

### pasibaigti iš failo
