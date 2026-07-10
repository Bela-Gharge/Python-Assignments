def Factors (N):
    Count = 0
    for i in range(1,N+1):
        if(N%i == 0):
            Count = Count+1
    return Count
                                   ############    WRON
def main():
    no = int(input("Enter number : "))
    Ret = Factors(no)
    print(f"Total number of factors is {Ret}")

if __name__ == "__main__":
    main()