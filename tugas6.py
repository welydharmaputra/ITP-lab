for x in range (1,6):
    for y in range (1,6-x):
        print(" ",end="")
    for z in range(2, int(x)*2+1):
        print("*", end="")
    print()

for d in range (1,6):
    for k in range(1,int(d)+1):
        print(" ",end="")
    for k in range(2,6-int(d),1):
         print("*",end="")
    for m in range(1,6-int(d),1):
         print("*",end="")
    print()
