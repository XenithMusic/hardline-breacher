import os

class Terminal:
    def __init__(this,color):
        this.accseed = 318144
        this.cmds = {"man":this.man,"help":this.man,"echo":this.echo,"exit":this.exit,"quit":this.exit,"run":this.run}
        this.color = color
        this.prompt = "$"
        this.exit = False
        this.activepath = "~/usr/"
        x = color
        for i in "0 1 2 3 4 5 6 7 8 9 a b c d e f".split(' '):
            x = x.replace(i,"")
        if x == "":
            os.system('color ' + color)
        else:
            print("Invalid color provided.")

    def man(this,x):
        if x == []:
            for i,j in this.cmds.items():
                print(i.upper())

    def run(this,x):
        x = "\"" + os.getcwd() + "/falsefilesystem" + this.activepath[1:] + x[0] + "\" " + str(this.accseed) + " " + " ".join(x[1:])
        x = x.replace("/","\\")
        print(x)
        os.system(x)

    def echo(this,x):
        x = " ".join(x)
        x = x.replace("=>",">")
        x = x.replace(" >",">")
        x = x.replace("> ",">")
        if ">" in x:
            x = x.split(">")
            with open(x[1],"w") as f:
                f.write(x[0])
        else:
            print(x)

    def exit(this,x):
        this.exit = True

    def parse(this,x:str):
        x = x.lower()
        y = x.split(' ')
        for i,j in this.cmds.items():
            if x.startswith(i):
                j(y[1:])
                return
        y = "run " + x
        y = y.split(" ")
        this.run(y[1:])

    def it(this,responselistener=None):
        a = input(this.prompt)
        r = this.parse(a)
        print()
