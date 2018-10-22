class calculator:               
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def plus(self):
        result = self.num1 + self.num2      #to sumition one number with another number
        return result
    def minus(self):
        result = self.num1 - self.num2      #to substract one number with another number
        return result
    def divide(self):
        result = self.num1 / self.num2      #to divide on number with another number
        return result
    def multiply(self):
        result = self.num1 * self.num2      #to multiply on number with another number
        return result
def main():
    run = True              #for looping so it can run again until we tell to stop
    while run == True:
        num1 = int(input("enter 1st number: "))         #input the number
        num2 = int(input("enter 2nd number: "))         #input the number
        op = input("enter the operator: ")              #input the operator
        wat = calculator(num1,num2)
        if op == "+":
            result = wat.plus()         #to make the plus operator can work
            print(result)
        elif op == "-":
            result = wat.minus()        #to make the minus operator can work
            print(result)
        elif op == "/":
            result = wat.divide()       #to make the divide operator can work
            print(result)
        elif op == "*":
            result = wat.multiply()     #to make the multipl operator can work
            print(result)

        CONTINUE = input("Continue? yes or no ")
        if CONTINUE == "no":
            run = False                             #to stop the looping, so we can stop the program
            print("Thank You :)")


main()

