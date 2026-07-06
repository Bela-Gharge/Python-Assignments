from functools import reduce 

square = lambda N : N*N                               #Q1

CheckEven = lambda N : (N%2==0)                       #Q2

CheckOdd = lambda N : (N%2 != 0 )                     #Q3

Addition = lambda N1 , N2 : N1+N2                     #Q4

Max = lambda N1 , N2 : N1 if (N1>N2) else N2          #Q5

Min = lambda N1 , N2 : N2 if(N1>N2) else N1           #Q6
    
Greater5 = lambda N : len(N)>5                        #Q7

Divisiblity = lambda N : (N % 3==0 and N% 5==0)       #Q8

Multiply = lambda N1 , N2 : N1*N2                     #Q9

EvenNumbers = lambda N : len(N%2 == 0)                #Q10

def main():
    Data = [1,2,3,4,5,6,7,8,9,10]
    MData = list(map(square , Data))
    print(f"After squaring data is {MData}")

    Data = [1,2,3,4,5,6,7,8,9,10]
    FData = list(filter(CheckEven,Data))
    print(f"Even numbers are {FData}")

    Data = [1,2,3,4,5,6,7,8,9,10]
    FData = list(filter(CheckOdd,Data))
    print(f"Odd numbers are {FData}")

    Data = [1,2,3,4,5,6,7,8,9,10]
    RData = reduce(Addition,Data)
    print(f"Total of all elements is {RData}")

    Data = [1,2,3,4,5,6,7,8,9,10]
    RData = reduce(Max,Data)
    print(f"Maximum number of the elements is {RData}")

    Data = [1,2,3,4,5,6,7,8,9,10]
    RData = reduce(Min,Data)
    print(f"Minimum number of the elements is {RData}")

    Data = ["Bela" , "Sujeet" , "Tanuja" , "Purva" , "Brahma" , "Shivaji" , "Gharge"]
    FData = filter(Greater5,Data)
    print(f"Words having more than 5 letter are {list(FData)}")

    Data = [1,2,3,4,5,6,7,8,9,10, 15]
    FData = list(filter(Divisiblity,Data))
    print(f"Numbers divisible by 3 and 5 are {FData}")

    Data = [1,2,3,4,5,6,7,8,9,10]
    RData = reduce(Multiply,Data)
    print(f"Product of all the elements is {RData}")

    Data = [1,2,3,4,5,6,7,8,9,10]
    FData = list(filter(CheckEven,Data))
    print(f"Even numbers are {FData}")



if __name__ == "__main__":
    main()