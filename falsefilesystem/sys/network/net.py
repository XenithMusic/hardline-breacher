import sys,random

v = sys.argv
with open("systems.txt","r") as f:
    systems = exec(f.read())

if v[0] == "list":
    random.seed(v[1])
    random.shuffle(systems)
    i = 0
    for i in systems:
        print(i.upper())
        i += 1
        if i == 10:
            break
