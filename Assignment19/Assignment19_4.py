from functools import reduce

ChkEven = lambda N : N%2 == 0 

Square = lambda N : N*N

Add = lambda N1,N2 : N1+N2

def main():
    Data = []

    Limit = int(input("Enter Number of Elements : "))

    for i in range(Limit):
        val = int(input(f"Enter Element {i+1} : "))
        Data.append(val)
    print(f"Input Data : {Data}")

    FData = list(filter(ChkEven , Data))
    print("List after filter : ",FData)

    MData = list(map(Square , FData))
    print("List after map : ",MData)

    RData = reduce(Add , MData)
    print("List after reduce : ",RData)



if __name__ == "__main__":
    main()