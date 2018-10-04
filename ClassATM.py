accountList = ['Frank']
pinsList = ['2265']
balancesList = [500000]

import sys
#customer class, for all the services of the customer
class CustomerServices:
    def __init__(self,accountID,pin):
        #constructor
        self.accountID = accountID
        self.pin = pin

    def login(self):
        #login function
        global accountList
        global pinsList
        found = False
        for account in accountList:
            if account == self.accountID:
                print(self.accountID)
                found = True
                x = accountList.index(account)
                if pinsList[x] == self.pin:
                    print("Logged in!")
                    return True
                else:
                    print("Incorrect pin")
                    return False
        if found == False:
            print("Data not found")
            sys.exit()
            return False

    def withdraw(self,amount):
        global accountList
        global balancesList
        found = False
        for account in accountList:
            if account == self.accountID:
                index = accountList.index(account)
                balancesList[index] -= amount
                found = True
        if found == False:
            print("Account not found")
            return False

    def debit(self,amount):
        global accountList
        global balancesList
        for account in accountList:
            if account == self.accountID:
                index = accountList.index(account)
                balancesList[index] -= amount
                return True
                

    def deposit(self,amount):
        global accountList
        global balancesList
        found = False
        for account in accountList:
            if account == self.accountID:
                index = accountList.index(account)
                balancesList[index] += amount
                found = True
        if found == False:
            print("Account not found")
            return False

    def transfer(self,amount):
        global accountList
        global balancesList
        found = False
        transferID = input("Input transfer ID: ")
        for account in accountList:
            for account in accountList:
                if account == self.accountID:
                    index = accountList.index(account)
                    balancesList[index] -= amount
                    for account in accountList:
                        if account == transferID:
                            index = accountList.index(account)
                            balancesList[index] += amount
                            found = True
                            return True
        if found == False:
            print("ID not found")
            return False
        
                    
                

    
                
#Account class to create an account         
class Account:
    
    def createaccount(self):
        # creates an account
        global accountList
        global pinsList
        global balancesList
        accountID = input("Please input your desired ID:")
        pin = input("Please register a pin: ")
        pincheck = input("Input the pin again")
        if pin == pincheck:
            print("Account creation success!")
            print("Your balance will start at 0.")
            balance = 0
            accountList.append(accountID)
            pinsList.append(pin)
            balancesList.append(0)
        else:
            print("Pins were not the same")
            return False



#main code
def main():
    ID = input("Input your ID: ")
    pin = input("Input pin: ")
    member = CustomerServices(ID,pin)
    loggingin = member.login()
    service = True
    while service == True:
        if loggingin == True:
            z = int(input("Choose your transaction.\n1. Withdraw\n2. Deposit\n3. Transfer\n4. Debit\n"))
            if z == 1:
                amount = int(input("Input amount: "))
                member.withdraw(amount)
            elif z == 2:
                amount = int(input("Input amount: "))
                member.deposit(amount)
            elif z == 3:
                amount = int(input("Input amount: "))
                member.transfer(amount)
            elif z == 4:
                amount = int(input("Input amount: "))
                member.debit(amount)
        servicing = int(input("1. Continue\n2. Stop"))
        if servicing == 1:
            service = True
        elif servicing == 2:
            service = False

        print(accountList,pinsList,balancesList)
            

x = int(input("What would you like to do?\n1. Create Account\n2. Login\nInput a number.\n"))

if x == 1:
    new = Account()
    newAcc = new.createaccount()
    main()
elif x == 2:
    main()


        
        
            


        



    
