def Vowels (Letter):                                    #Q1
    if(Letter == 'a' or Letter == 'e' or Letter == 'i' or Letter == 'o' or Letter == 'u' ):
        print("It is a vowel.")
    else :
        print("It is a consonant")


def Factors(No):                                        #Q2
    for i in range(1,No+1,1):
        if(No%i==0):
            print(i)


Add = lambda No1,No2 : No1+No2                          #Q3
Diff = lambda No1,No2 : No1-No2
Pro = lambda No1,No2 : No1*No2
Div = lambda No1,No2 : No1/No2

def Numbers(Num):                                       #Q4
    for i in range(1,Num+1,1):
        print(i)


def Reverse(Num1):                                      #Q5
    for i in range(Num1, 0,-1):
        print(i)
    
def main():
    Letter = input("Enter letter : ")
    Ret = Vowels(Letter)

   
    No = int(input("Enter number : "))
    Ret = Factors(No)

   
    No1 = int(input("Enter Number 1 :"))
    No2 = int(input("Enter Number 2 :"))
    Ret = Add(No1,No2)
    print("Addition is: " , Ret)
    
    Ret = Diff(No1,No2)
    print("Subtraction is: " , Ret)

    Ret = Pro(No1,No2)
    print("Multiplication is : ",Ret)

    Ret = Div(No1,No2)
    print("Division is : ",Ret)
    

    Num = int(input("Enter number : "))
    Ret = Numbers(Num)


    Num1 = int(input("Enter number : "))
    Ret = Reverse(Num1)

if __name__ == "__main__":
    main()