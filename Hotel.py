class Hotel:
    def __init__(self):
        self.priceSR1 = 1000
        self.priceSR2 = 1500        #to put the price
        self.priceCR1 = 700
        self.priceCR2 = 1000
        self.listRoom1 = []
        self.listRoom2 = []
        self.listRoom3 = []         #the list of the room
        self.listRoom4 = []

    def printSR1(self):
        print("$",self.priceSR1,"/day")

    def printSR2(self):
        print("$",self.priceSR2,"/day")     #for can print the price

    def printCR1(self):
        print("$",self.priceCR1,"/day")

    def printCR2 (self):
        print("$",self.priceCR2,"/day")


class Customer(Hotel):

    def check_in(self):                                 #to see available rooms
        if len(self.listRoom1) == 4:                #max 4 rooms on list room 1
            print("Room are not Occupied")
        else :                                      # to input the room no the list room 1
            roomNum = int(input("Which Room Number :"))
            self.listRoom1.append(roomNum)

    def check_in2(self):
        if len(self.listRoom2) == 4:                #max 4 rooms on list room 2
            print("Room are not Occupied")
        else :                                      # to input the room no the list room 2
            roomNum = int(input("Which Room Number :"))
            self.listRoom2.append(roomNum)

    def check_in3(self):
        if len(self.listRoom3) == 4:                #max 4 rooms on list room 3
            print("Room are not Occupied")
        else :                                      # to input the room no the list room 3
            roomNum = int(input("Which Room Number :"))
            self.listRoom3.append(roomNum)

    def check_in4(self):
        if len(self.listRoom4) == 4:                #max 4 rooms on list room 4
            print("Room are not Occupied")
        else :                                      # to input the room no the list room 4
            roomNum = int(input("Which Room Number :"))
            self.listRoom4.append(roomNum)

    def check_room(self):
        print("1. Special Room Single-Bed ($ 1000)")
        print("2. Special Room Double-Bed ($ 1500)")
        print("3. Casual Room Single-Bed  ($ 700 )")
        print("4. Casual Room Double-Bed  ($ 1000)")
        choice = int(input("Which Room?"))              #to choose to see the information about available rooms
        if choice == 1:
            print(self.listRoom1)

        elif choice == 2:
            print(self.listRoom2)

        elif choice == 3:
            print(self.listRoom3)

        elif choice == 4:
            print(self.listRoom4)


a = Customer()
run = True
while run == True:

    print("Check-in")
    print("Category of Rooms:")
    print("1. Special Room Single-Bed ($ 1000)")
    print("2. Special Room Double-Bed ($ 1500)")
    print("3. Casual Room Single-Bed  ($ 700 )")
    print("4. Casual Room Double-Bed  ($ 1000)")
    print("5. Check Room")

    choice = int(input("Choose Room :"))
    if choice == 1:                         #to choose the room and the number of the room
        a.check_in()
        a.printSR1()
        print("\nCheck-out")
        days = int(input("How Many Days?\n"))      #to book how long the room will be rent
        print("Total Revenue: $",1000*days)        #to print total price

    elif choice == 2:
        a.check_in2()
        a.printSR2()
        print("\nCheck-out")
        days = int(input("How Many Days?\n"))
        print("Total Revenue: $",1500*days)

    elif choice == 3:
        a.check_in3()
        a.printCR1()
        print("\nCheck-out")
        days = int(input("How Many Days?\n"))
        print("Total Revenue: $",700*days)

    elif choice == 4:
        a.check_in4()
        a.printCR2()
        print("\nCheck-out")
        days = int(input("How Many Days?\n"))
        print("Total Revenue: $",1000*days)

    elif choice == 5:
        a.check_room()      #to check available rooms

    Continue = input("Is there any other want to rent (Y/N)? \n")
    Continue = Continue.upper()
    if Continue == "N":                     #to end the program
        run = False


