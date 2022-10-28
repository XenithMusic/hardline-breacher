import sys,random

v = sys.argv
with open("systems.txt","r") as f:
    systems = exec(f.read())

print(v)
v.pop(0)
seed = int(v[0])
v.pop(0)

if v[0] == "list":
    random.seed(seed)
        random.shuffle(systems)
    i = 0
    for i in systems:
        print(i.upper())
        i += 1
        if i == 10:
            break
