def main():

    for x in range(1,6): # it will make the stars go down
        for y in range(1,6-int(x)): # it will make the space
            print(" ",end="")

        for z in range(1,int(x)+1,1): #it will make the stars and increase the stars one by one
            print("*",end="")
        print()

if __name__=="__main__":
    main()
