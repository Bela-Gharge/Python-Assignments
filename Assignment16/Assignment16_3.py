def Add(N1,N2):
    return N1+N2

def main () : 
    No1 = int(input("Enter Number 1 : "))
    No2 = int(input("Enter Number 2 : "))
    Ret = Add(No1,No2)
    print(f"Addition of {No1} and {No2} is {Ret}")

if __name__ == "__main__" : 
    main()