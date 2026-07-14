from functools import reduce

GreaterNo = lambda N:N<= 90 and N>= 70  

Increment = lambda N1 : N1+10

Product = lambda N1,N2 : N1*N2

def main():
    List = []

    limit = int(input("Enter number of elements : "))


    for i in range(limit):
        val = int(input(f"Enter Number {i+1} : "))
        List.append(val)
    print("Input List : " ,List)

    FData = list(filter(GreaterNo , List))
    print("List after Filter : " , FData)

    MData = list(map(Increment , FData))
    print("List after Map : ",MData)

    RData = reduce(Product,MData)
    print("Output of reduce : ",RData)


if __name__ == "__main__" :
    main()