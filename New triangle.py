def main():

 for x in range(1,6): # it will make the stars go down
        for z in range(1,int(x)+1,1): # it will make the  star increase one by one
            print("*",end="") #it will print the stars and make the stars to make a line that from left to the right
        print() # it make the stars can be show
if __name__=="__main__":
    main()

print("\n")

def main():

    for x in range(1,6): # it will make the stars go down
        for y in range(1,6-int(x)): # it will make the space
            print(" ",end="")

        for z in range(1,int(x)+1,1): #it will make the stars and increase the stars one by one
            print("*",end="")
        print()

if __name__=="__main__":
    main()

print("\n")

def main():

    for x in range(1,7): # it will make the stars go down
        for z in range(1,7-int(x),1): # it will make the stars and decrease the stars one by one
            print("*",end="")
        print()

if __name__=="__main__":
    main()

print("\n")

def main():

    for x in range(1,7): # it will make the stars go down
        for y in range(1,int(x)+1):# it will make the space
            print(" ",end="")

        for z in range(1,7-int(x),1): # it will make the stars that from 7 stars go to 1 on star
            print("*",end="")
        print()

if __name__=="__main__":
    main()

print("\n")

def main():

    for x in range (1,6): # it will make the stars go down
        for y in range (1,6-x): #it will make the spaces
            print(" ",end="")
        for z in range(2, int(x)*2+1): # it will make make the stars and increase the stars two by one
            print("*", end="")
        print()

if __name__=="__main__":
    main()

print("\n")

def main():

    for x in range (1,6): # it will make the stars go down
        for y in range (1,6-x):
            print(" ",end="")
        for z in range(2, int(x)*2+1):
            print("*", end="")
        print()

    for d in range (1,6): # it will make the stars go down
        for k in range(1,int(d)+1):  #it will make the left-below side or te diamond with space
            print(" ",end="")
        for k in range(2,6-int(d),1): #it will print the lefe-below stars of diamond
             print("*",end="")
        for m in range(1,6-int(d),1): #it will print the right-below stars of diamond
             print("*",end="")
        print()

if __name__=="__main__":
    main()
