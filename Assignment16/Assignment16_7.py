def Divisiblity(N):
    if(N%5==0):
        return("Divisible by 5")
    else :
        return("Not Divisible by 5")

def main():
    no = int(input("Enter number : "))
    Ret = Divisiblity(no)
    print(Ret)

if __name__ == "__main__":
    main()