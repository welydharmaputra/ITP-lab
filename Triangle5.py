for x in range (1,6): # it will make the stars go down
    for y in range (1,6-x): #it will make the spaces
        print(" ",end="")
    for z in range(2, int(x)*2+1): # it will make make the stars and increase the stars two by two
        print("*", end="")
    print()
