class Demo:
    Value = 10

    def __init__(self,No1 , No2):
        self.i = No1
        self.j = No2

    def fun(self):
        print("Inside fun ")
        print(self.i , self.j)

    def gun(self):
        print("Inside gun ")
        print(self.i , self.j)


obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()