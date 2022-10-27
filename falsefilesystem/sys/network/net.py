import sys,random

v = sys.argv
with open("systems.txt","r") as f:
    exec(f.read())

if v[0] == "list":
    random.seed(v[1])
    random.shuffle(systems)
    for i in range(10):
        print(systems[i].upper())
