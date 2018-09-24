for x in range (1,6):
    for y in range (1,6-x):
        print(" ",end="")
    for z in range(2, int(x)*2+1):
        print("*", end="")
    print()
