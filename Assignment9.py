def Display() :                                #Q1
    print("Jay Ganesh!!!")

def ChkGreater(No1,No2):                       #Q2
    if(No1>No2):
        print("No 1 is greater.")
    elif(No2>No1) :
        print("No2 is greater.")
    else :
        print("No 1 is equal to No 2.")    


Square = lambda No : No*No                       #Q3

Cube = lambda NO : NO*NO*NO                      #Q4

def Divisiblity (Number):                        #Q5
    if(Number % 3 == 0 and Number% 5== 0):
        print("Divisible by both 3 and 5")
    elif(Number % 3 == 0):
        print("Divisible by 3")
    elif(Number % 5 == 0): 
        print("Divisible by 5")
    else :
        print("Divisible by neither of them.")

    


def main () : 
    Display()
    print("-"*20)
    
    No1 = int(input("Enter No 1 : "))
    No2 = int(input("Enter No 2 : "))
    ChkGreater(No1,No2)
    print("-"*20)
    
    No = int(input("Enter Number : "))
    Ret = Square(No)
    print("Square of number is : " , Ret)
    print("-"*20)

    NO = int(input("Enter Number : "))
    Ret1 = Cube(NO)
    print("Cube of Number is : ",Ret1)
    print("-"*20)

    Number = int(input("Enter Number : "))
    Ret2 = Divisiblity(Number)
    print("The numbers is : " , Ret2)

if __name__ == "__main__" :
    main()