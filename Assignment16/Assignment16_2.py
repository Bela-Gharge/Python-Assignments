def ChkNum(N):
    if(N%2==0):
        print("Even number")
    else : 
        print("Odd Number")

def main():
    no = int(input("Enter Number : "))
    ChkNum(no)

if __name__ == "__main__":
    main()