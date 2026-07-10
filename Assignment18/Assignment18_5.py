from MarvellousNum import Prime

def ListPrime(List):
    sum = 0

    for i in List:
        if(Prime(i)== True):
            sum = sum+1
    return sum

def main():
    List = []
    Nums  = int(input("Enter Number of elements : "))

    for i in range (Nums):
        val = int(input("Enter numbers : "))
        List.append(val)

    Ret = ListPrime(List)
    print(f"Total number of prime numbers are {Ret}")


if __name__ == "__main__" :
    main()