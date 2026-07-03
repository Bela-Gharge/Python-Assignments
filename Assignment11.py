def Prime(n):                                      #Q1
    count = 0
    for i in range(1,int(n**0.5),1):
        if(n%i==0):
            count = count+i
            if(n%i != i):
                count = count + i

    if (count == 2):
        print("Prime Number")
    else :
        print("Not Prime Number")    
    

def Count(num):                                   #Q2
    print (len(num))


def Sum(no):                                      #Q3
    sum = 0
    for i in no :
        sum = sum+int(i)
    print(sum)

def Reverse(No):                                  #Q4
    for i in No [len(No)-1::-1]:
        print (i)


def Palindrome(Number):                          #Q5
    if(Number == Number[::-1]):
        print("Palindrome Number")
    else:
        print("Not Palindrome number")

def main():
    n = int(input("Enter number : "))
    Ret = Prime(n)

    num = list(input("Enter the number : "))
    Ret = Count(num)

    no = list(input("Enter Number : "))
    Ret = Sum(no)

    No = list(input("Enter number : "))
    Ret = Reverse(No)

    Number = list(input("Enter number : "))
    Ret = Palindrome(Number)

if __name__ == "__main__" :
    main()