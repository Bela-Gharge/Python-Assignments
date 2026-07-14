from functools import reduce

def Prime(n):                                      
    count = 0
    for i in range(1,int(n**0.5+1),1):
        if(n%i==0):
            count = count+1
            if(n//i != i):
                count = count + 1

    if (count == 2):
        return True
    else :
        return False  


Multiply = lambda N : N*2


Max = lambda N1,N2 : N1 if(N1>N2) else N2


def main():
    Data = []

    Limit = int(input("Enter Number of Elements : "))

    for i in range(Limit):
        val = int(input(f"Enter Element {i+1} : "))
        Data.append(val)
    print(f"Input Data : {Data}")

    FData = list(filter(Prime , Data))
    print("List after filter : ",FData)

    MData = list(map(Multiply , FData))
    print("List after map : ",MData)

    RData = reduce(Max , MData)
    print("List after reduce : ",RData)

if __name__ == "__main__":
    main()