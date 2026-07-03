Rectangle = lambda No1,No2 :No1*No2                        #Q1

Circle = lambda r : 3.14*r*r                               #Q2

def PerfectNumber(No):                                     #Q3
    Sum = 0
    for i in range(1,No,1):
        if(No%i == 0):
            Sum +=i
        
    if(Sum==No):
        print(True)
    else:
        print(False)


def BinaryEquivalent(Number):                              #Q4
        print(Number%2)

def GradeCalci(Marks):                                     #Q5
    if(Marks>=75):
        print("Distinction")
    elif(Marks<75 and Marks>=60):
        print("First Class")
    elif(Marks<60 and Marks>=50):
        print("Second Class")
    else:
        print("Fail")



def main () :
    Length = int(input("Enter Length : "))
    Width = int(input("Enter Width : "))
    Ret = Rectangle(Length,Width)
    print("Area of rectangle is : " ,Ret)

    Radius = int(input("Enter Radius : "))
    Ret = Circle(Radius)
    print("Area of Circle is : ",Ret)

    No = int(input("Enter number : "))
    Ret  = PerfectNumber(No)

    Number = int(input("Enter the number to be converted : "))
    Ret = BinaryEquivalent(Number)

    Marks = int(input("Enter your marks : "))
    Ret = GradeCalci(Marks)
 



if __name__ == "__main__" :
    main()