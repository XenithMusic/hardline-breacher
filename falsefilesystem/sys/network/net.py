import sys,random

v = sys.argv
with open("systems.txt","r") as f:
    systems = eval(f.read())

v.pop(0)
seed = int(v[0])
v.pop(0)

if v[0] == "list":
    random.seed(seed)
    random.shuffle(systems)
    for i in systems[:9]:
        print(i["name"].upper() + " (" + i["ip"] + ")")
if v[0] == "log":
    print('a')
    random.seed(seed)
    random.shuffle(systems)
    if v[1] in systems[:9]:
        eval("from othersystems." + v[1].lower() + " import *")
        login(input("username: "),input("password: "))
        access()
