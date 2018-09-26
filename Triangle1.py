def main():

    for x in range(1,6): # it will make the stars go down
        for z in range(1,int(x)+1,1): # it will make the  star increase one by one
            print("*",end="") #it will print the stars and make the stars to make a line that from left to the right
        print() # it make the stars can be show

if __name__=="__main__":
    main()
