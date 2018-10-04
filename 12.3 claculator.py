class calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def plus(self):
        result = self.num1 + self.num2
        return result
    def minus(self):
        result = self.num1 - self.num2
        return result
    def divide(self):
        result = self.num1 / self.num2
        return result
    def multiply(self):
        result = self.num1 * self.num2
        return result
def main():
    run = True
    while run == True:
        num1 = int(input("enter 1st number: "))
        num2 = int(input("enter 2nd number: "))
        op = input("enter the operator: ")
        wat = calculator(num1,num2)
        if op == "+":
            result = wat.plus()
            print(result)
        elif op == "-":
            result = wat.minus()
            print(result)
        elif op == "/":
            result = wat.divide()
            print(result)
        elif op == "*":
            result = wat.multiply()
            print(result)

        CONTINUE = input("Continue? [yes/no] ")
        if CONTINUE == "no":
            run = False
            print("Thank You :)")


main()

