def Count(n):
    return (len(n))


def main():
    no = input("Enter Number :")
    Ret = Count(no)
    print(f"Toatl no of elements in {no} is {Ret}")

if __name__ == "__main__":
    main()