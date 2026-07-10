def Min(Nums):
    min = Nums[0]
    for i in Nums:
        if(i<min):
            min = i
    return min


def main():
    Elements = []
    N = int(input("Enter the number of elements : "))

    for i in range(N):
        val = int(input(f"Enter element : "))
        Elements.append(val)

    Ret = Min(Elements)
    print(f"Smallest number is {Ret}")


if __name__ == "__main__":
    main()