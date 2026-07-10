from Arithmetic import Add,Sub,Mult,Div

def main():
    No1= int(input("Enter No 1 : "))
    No2= int(input("Enter No 2 : "))

    ret = Add(No1,No2)
    print(f"Addition is {ret}")

    ret = Sub(No1,No2)
    print(f"Subtraction is {ret}")

    ret = Mult(No1,No2)
    print(f"Multiplication is {ret}")

    ret = Div(No1,No2)
    print(f"Division is {ret}")


if __name__ == "__main__":
    main()