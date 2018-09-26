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
