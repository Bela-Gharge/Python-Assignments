def Factorial(N):
    fact = 1
    for i in range(1,N+1):
        fact = fact*i
    return fact

def main():
    no = int(input("ENter number : "))
    Ret = Factorial(no)
    print(Ret)

if __name__ == "__main__":
    main()