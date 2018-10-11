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

class TollBooth(Vehicle):
    def __init__(self,carPrice,busPrice,truckPrice,countCar,countBus,countTruck):
        Vehicle.__init__(self,carPrice,busPrice,truckPrice)
        self.countCar = countCar                        #for put the number of how much the vehicles get in
        self.countBus = countBus
        self.countTruck = countTruck

    def calculation(self):
        x = self.countCar * self.carPrice               #for knowing the total of the price
        y = self.countBus * self.busPrice
        z = self.countTruck * self.truckPrice
        calculate = x + y + z
        return calculate

    def printAll(self):
        x = self.countCar                                #for knowing how much the vehicles get in
        y = self.countBus
        z = self.countTruck
        twenty = 20
        print(twenty*"-")
        print("car\t\tbus\t\ttruck")
        print(twenty*"-")
        print(str(x)+"\t\t"+str(y)+"\t\t"+str(z))
        print(twenty*"-")




countCar = 0
countBus = 0
countTruck = 0
carPrice = 6000
busPrice = 8000
truckPrice = 10000
a = Vehicle(carPrice,busPrice,truckPrice)              #to call the code from the class
run = True                                             # for looping, so we can go back and run it again
while run == True:

    print("Category of vehicle:")
    print("1. Car (RP 6000)")
    print("2. Bus (RP 8000)")
    print("3. Truck (RP 10000)")
    choice = int(input("enter vehicle :"))
    if choice == 1:
        a.printCar()
        countCar +=1                        #to increase how much vehicles that get in
    elif choice == 2:
        a.printBus()
        countBus += 1

    elif choice == 3:
        a.printTruck()
        countTruck += 1

    Continue = input("Is there any other vehicle (Y/N)? \n")
    Continue = Continue.upper()
    if Continue == "N":                     #to end the program
        run = False
        print("<exit program>")

b = TollBooth(carPrice,busPrice,truckPrice,countCar,countBus,countTruck)    #to call the price and how much the vehicles so we can print it

b.printAll()
print("Total Revenue:",b.calculation())

