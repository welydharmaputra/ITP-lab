print("================================================================================ \n "
    "                           Toll Payment Systems \n "
    "                            PT Jasa Marga, Tbk.\n"
    "================================================================================")

class Vehicle:
    def __init__(self,carPrice,busPrice,truckPrice):
        self.carPrice = carPrice                        #for put the price
        self.busPrice = busPrice
        self.truckPrice = truckPrice

    def printCar(self):
        print (self.carPrice)                           #for the price can be call

    def printBus(self):
        print(self.busPrice)

    def printTruck(self):
        print(self.truckPrice)

carPrice = 6000
busPrice = 8000
truckPrice = 10000
a = Vehicle(carPrice,busPrice,truckPrice)               #to call the code from class
run = True                                              # for looping, so we can go back and run it again
while run == True:

    print("Category of vehicle:")
    print("1. Car (RP 6000)")
    print("2. Bus (RP 8000)")
    print("3. Truck (RP 10000)")
    choice = int(input("enter vehicle :"))

    if choice == 1:                                     #for choosing the vehicle
        a.printCar()

    elif choice == 2:
        a.printBus()

    elif choice == 3:
        a.printTruck()

    Continue = input("Is there any other vehicle (Y/N)? \n")
    Continue = Continue.upper()
    if Continue == "N":                                         #for end the program
        run = False
        print("<exit program>")

