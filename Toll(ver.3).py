print("================================================================================ \n "
    "                           Toll Payment Systems \n "
    "                            PT Jasa Marga, Tbk.\n"
    "================================================================================")

class Vehicle:
    def __init__(self,carPrice,busPrice,truckPrice,carPrice2,busPrice2,truckPrice2): #to put the price
        self.carPrice = carPrice
        self.busPrice = busPrice
        self.truckPrice = truckPrice
        self.CarPrice2 = carPrice2
        self.BusPrice2 = busPrice2
        self.TruckPrice2 = truckPrice2

    def printCar(self):
        print (self.carPrice)               #for the price can be call

    def printBus(self):
        print(self.busPrice)

    def printTruck(self):
        print(self.truckPrice)

    def printCar2(self):
        print (self.CarPrice2)

    def printBus2(self):
        print(self.BusPrice2)

    def printTruck2(self):
        print(self.TruckPrice2)

class TollBooth(Vehicle):
    def __init__(self,carPrice,busPrice,truckPrice,countCar,countBus,countTruck,countCar2,countBus2,countTruck2,
                 CarPrice2,BusPrice2,TruckPrice2):
        Vehicle.__init__(self,carPrice,busPrice,truckPrice,CarPrice2,BusPrice2,TruckPrice2)
        self.countCar = countCar                    #for put the number of how much the vehicles get in
        self.countBus = countBus
        self.countTruck = countTruck
        self.countCar2 = countCar2
        self.countBus2 = countBus2
        self.countTruck2 = countTruck2

    def calculation(self):
        x = self.countCar * self.carPrice           #for knowing the total of the price on Meruya
        y = self.countBus * self.busPrice
        z = self.countTruck * self.truckPrice
        calculate = x + y + z
        return calculate

    def printAll(self):
        x = self.countCar                           #for knowing how much the vehicles get in, on meruya
        y = self.countBus
        z = self.countTruck
        twenty = 20
        print("Location : Meruya")
        print(twenty*"-")
        print("car\t\tbus\t\ttruck")
        print(twenty*"-")
        print(str(x)+"\t\t"+str(y)+"\t\t"+str(z))
        print(twenty*"-")

    def calculation2(self):
        r = self.countCar2 * self.CarPrice2         #for knowing the total of the price on Pondok Aren
        t = self.countBus2 * self.BusPrice2
        n = self.countTruck2 * self.TruckPrice2
        calculate2 = r + t + n
        return calculate2

    def printAll2(self):
        r = self.countCar2                          #for knowing how much the vehicles get in, on Pondok Aren
        t = self.countBus2
        n = self.countTruck2
        twenty = 20
        print("Location: Pondok Aren")
        print(twenty*"-")
        print("car\t\tbus\t\ttruck")
        print(twenty*"-")
        print(str(r)+"\t\t"+str(t)+"\t\t"+str(n))
        print(twenty*"-")


countCar2 = 0       #the counter on Meruya
countBus2 = 0
countTruck2 = 0
CarPrice2 = 18000       #the price on Meruya
BusPrice2 = 20000
TruckPrice2 = 25000
countCar = 0           #the counter on Pondok Aren
countBus = 0
countTruck = 0
carPrice = 6000         # the price on Pondok Aren
busPrice = 8000
truckPrice = 10000
a = Vehicle(carPrice,busPrice,truckPrice,CarPrice2,BusPrice2,TruckPrice2)       #to call the code from the class
run = True                        # for looping, so we can go back and run it again
while run == True:

    print("Category of vehicle:")
    print("1. Car (RP 6000)")
    print("2. Bus (RP 8000)")
    print("3. Truck (RP 10000)")
    choice = int(input("enter vehicle :"))
    if choice == 1:
        a.printCar()
        countCar +=1                #to increase how much vehicles that get in, on Meruya

    elif choice == 2:
        a.printBus()
        countBus += 1

    elif choice == 3:
        a.printTruck()
        countTruck += 1

    Continue = input("Is there any other vehicle (Y/N)? \n")
    Continue = Continue.upper()
    if Continue == "N":             #so we can go to the next gate
        continuE = input("Is there any other Toll gate location (Y/N)? \n")
        continuE = continuE.upper()
        if continuE == "N":          #for en this program
            run = False
        if continuE == "Y":
            Main = True
            while Main == True:
                print()
                print("location of toll gate: Pondok Aren")
                print("Category of vehicle:")
                print("1. Car (RP 18000)")
                print("2. Bus (RP 20000)")
                print("3. Truck (RP 25000)")
                choise = int(input("enter vehicle :"))
                if choise == 1:
                    a.printCar2()
                    countCar2 +=1           #to increase how much vehicles that get in, on Pondok Aren

                if choise == 2:
                    a.printBus2()
                    countBus2 +=1

                if choise == 3:
                    a.printTruck2()
                    countTruck2 +=1

                ContinuE = input("Is there any other vehicle (Y/N)? \n")
                ContinuE = ContinuE.upper()
                if ContinuE == "N":
                    Main = False
                    run = False
        elif continuE == "N":
            run = False
    if Continue == "N":
        run = False

b = TollBooth(carPrice,busPrice,truckPrice,countCar,countBus,countTruck,countCar2,countBus2,countTruck2,
              CarPrice2,BusPrice2,TruckPrice2)          #to call the price and how much the vehicles so we can print it

b.printAll()
print("Total Revenue: RP",b.calculation())
print()
b.printAll2()
print("Total Revenue: RP",b.calculation2())
print()
print("GRAND Revenue: RP",b.calculation()+b.calculation2())
print()
print("<exit program>")
