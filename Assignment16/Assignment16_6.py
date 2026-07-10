def Check(N):
    if(N>0):
        return("Positive Number")
    elif(N<0):
        return("Negative Number")
    else:
        return("Zero")

def main():
    No = int(input("Enter number : "))
    Ret = Check(No)
    print(f"Number is {Ret}")

if __name__ == "__main__":
    main()