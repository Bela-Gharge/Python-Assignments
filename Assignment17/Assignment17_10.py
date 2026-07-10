def Sum(N):
    sum = 0 
    for i in str(N):
        sum = sum + int(i) 
    return sum

def main():
    no = int(input("Enter Number :"))
    Ret = Sum(no)
    print(f"Total of elements in {no} is {Ret}")

if __name__ == "__main__":
    main()