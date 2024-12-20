data = open("vardai.txt", "r")
lists = data.readlines()

# for line in data:
#     e = line.split()
#     list.append(" ".join(e))
# print(list)

vid = 0
for list in lists[1:]:
    zmogus = list.replace("\n","").split(";")
    vid += int(zmogus[2]) if zmogus[2] else 0
print(vid/len(lists[1:]))
