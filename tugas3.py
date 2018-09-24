def main():

    for x in range(1,7):
        for z in range(1,7-int(x),1):
            print("*",end="")
        print()

if __name__=="__main__":
    main()
