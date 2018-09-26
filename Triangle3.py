def main():

    for x in range(1,7): # it will make the stars go down
        for z in range(1,7-int(x),1): # it will make the stars and decrease the stars one by one
            print("*",end="")
        print()

if __name__=="__main__":
    main()
