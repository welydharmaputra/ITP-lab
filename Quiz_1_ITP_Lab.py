bools= True
comTop={}
comMid={}
comBot={}

def Put(x,y,z):
    x[y]=z
def take(x,y):
    print(x[y],x[x[y]])
def showContent(x):
    for a,b in x:
        print(a,":",b)
def freeze(x,y):
    x[y]=0
def chill(x,y):
    x[y]=x[y]-10
def fresh(x,y):
    x[y]="Fresh"
def getWater():
    print()
while bools==True:
    print("Choose your compartment:\n1.Top\n2.Middle\n3.Bottom\n")
    compart=input("Pick:\n")
    if compart=="1":
        compart2=input("Put/Take:\n")
        if compart2.lower()=="put":
            compart3=input("What are you putting:\n")
            compart4=input("what is its temperature:\n")
            compart5=input("Is it fresh(Y/N):\n")
        elif compart2.lower()=="take":
            compart3=input("What are you taking:\n")
        else:
            print("Wrong input")
    elif compart2=="2":
        if compart2.lower()=="put":
            compart3=input("What are you putting:\n")
            compart4=input("what is its temperature:\n")
            compart5=input("Is it fresh(Y/N):\n")
        elif compart2.lower()=="take":
            compart3=input("What are you taking:\n")
        else:
            print("Wrong input")
    elif compart2=="3":
        if compart2.lower()=="put":
            compart3=input("What are you putting:\n")
            compart4=input("what is its temperature:\n")
            compart5=input("Is it fresh(Y/N):\n")
        elif compart2.lower()=="take":
            compart3=input("What are you taking:\n")
        else:
            print("Wrong input")
    else:
        print("Wrong input")
