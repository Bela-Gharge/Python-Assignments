def Multiplication(No):                        #Q1
    for i in range(1,11,):
        print(i*No)


def NaturalNumbers(NO):                        #Q2
    Sum = 0 
    for i in range(1,NO+1,1):
        Sum = Sum + i
    print(Sum)


def FactorialSum(Nums):                       #Q3
    factorial = 1
    for i in range(1,Nums+1,1):
        factorial = factorial*i
    print(factorial)


def EvenNumbers(Number):                      #Q4
    for i in range(0,Number , 1 ):
        if(i%2==0):
            print (i)


def OddNumber(Num):                           #Q5
    for i in range(0,Num,):
        if(i%2 != 0):
            print(i)



def main() : 
    No = int(input("Enter Number : "))
    Ret = Multiplication(No)
    print("Multiplication table is : ",Ret)
    print("-"*20)

    NO = int(input("Enter Number : "))
    Ret1 = NaturalNumbers(NO)
    print("Sum of Natural Numbers upto" , NO , "is : " , Ret1)

    Nums = int(input("Enter Number : "))
    Ret4 = FactorialSum(Nums)

    Number = int(input("Enter Number : "))
    Ret2 = EvenNumbers(Number)
    print("Even numbers are : " , Ret2)

    Num = int(input("Enter Num : "))
    Ret3 = OddNumber(Num)

if __name__ == "__main__":
    main()