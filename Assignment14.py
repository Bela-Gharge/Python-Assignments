Square = lambda N : N*N                               #Q1

Cube = lambda N : N*N*N                               #Q2

MaxNumber = lambda N1,N2 : N1>N2                      #Q3

MinNumber = lambda N1,N2 : N1<N2                      #Q4

CheckEven = lambda N :N%2==0                          #Q5

CheckOdd = lambda N : N%2!=0                          #Q6

Divisiblity = lambda N : N%5==0                       #Q7

Add = lambda N1,N2 : N1+N2                            #Q8

Multiply = lambda N1,N2 : N1*N2                       #Q9

Largest = lambda N1,N2,N3 : N1 if(N1>N2 and N1>N3) else (N2 if(N2>N3) else N3 )


def main():
    No = int(input("Enter the number : "))
    Ret = Square(No)
    print(f"Square of {No} is {Ret}")

    
    No = int(input("Enter the number : "))
    Ret = Cube(No)
    print(f"Cube of {No} is {Ret}")

    
    No1 = int(input("Enter number 1 : "))
    No2 = int(input("Enter number 2 : "))
    Ret = MaxNumber(No1,No2)
    if (Ret == True):
        print(f"The max number is {No1}")
    else:
        print(f"The max number is {No2}")
              
    
    No1 = int(input("Enter number 1 : "))
    No2 = int(input("Enter number 2 : "))
    Ret = MinNumber(No1,No2)
    if (Ret == True):
        print(f"The min number is {No1}")
    else:
        print(f"The min number is {No2}")

    
    No = int(input("Enter the number : "))
    Ret = CheckEven(No)
    if(Ret == True):
        print("True")
    else : 
        print("False")


    No = int(input("Enter the number : "))
    Ret = CheckOdd(No)
    if(Ret == True):
        print(f"{No} is Odd Number")
    else : 
        print(f"{No} is Even Number")


    No = int(input("Enter the number : "))
    Ret = Divisiblity(No)
    if(Ret == True):
        print(f"{No} is divisible by 5 ")
    else : 
        print(f"{No} is not divisible by 5")


    No1 = int(input("Enter number 1 : "))
    No2 = int(input("Enter number 2 : "))
    Ret = Add(No1,No2)
    print(f"The sum is {Ret}")


    No1 = int(input("Enter number 1 : "))
    No2 = int(input("Enter number 2 : "))
    Ret = Multiply(No1,No2)
    print(f"The product is {Ret}")
    
    No1 = int(input("Enter number 1 : "))
    No2 = int(input("Enter number 2 : "))
    No3 = int(input("Enter number 3 : "))
    Ret = Largest(No1,No2,No3)
    print(f"Greatest number is {Ret}")
    

     


if __name__ == "__main__":
    main()