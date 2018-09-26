def main():

    for x in range(1,7): # it will make the stars go down
        for y in range(1,int(x)+1):# it will make the space
            print(" ",end="")

        for z in range(1,7-int(x),1): # it will make the stars that from 7 stars go to 1 on star
            print("*",end="")
        print()

if __name__=="__main__":
    main()
