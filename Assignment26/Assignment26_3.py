class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter Number 1 : "))
        self.Value2 = int(input("Enter Number 2 : "))

    def Addition(self):
        return(self.Value1+self.Value2)

    def Subtraction(self):
        return(self.Value1-self.Value2)

    def Multiplication(self):
        return(self.Value1*self.Value2)

    def Division(self):
        return(self.Value1/self.Value2)


obj1 = Arithmetic()
obj1.Accept()
print("Addition is : ",obj1.Addition())
print("Subtraction is : ",obj1.Subtraction())
print("Multiplication is : ",obj1.Multiplication())
print("Division is : ",obj1.Division())

obj2 = Arithmetic()
obj2.Accept()
print("Addition is : ",obj2.Addition())
print("Subtraction is : ",obj2.Subtraction())
print("Multiplication is : ",obj2.Multiplication())
print("Division is : ",obj2.Division())

obj3 = Arithmetic()
obj3.Accept()
print("Addition is : ",obj3.Addition())
print("Subtraction is : ",obj3.Subtraction())
print("Multiplication is : ",obj3.Multiplication())
print("Division is : ",obj3.Division())


