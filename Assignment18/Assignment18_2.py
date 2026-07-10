def Max(Nums):
    max = Nums[0]
    for i in Nums:
        if(i>max):
            max = i
    return max


def main():
    Elements = []
    N = int(input("Enter the number of elements : "))

    for i in range(N):
        val = int(input(f"Enter element {i+1} : "))
        Elements.append(val)

    Ret = Max(Elements)
    print(f"Greatest number is {Ret}")

if __name__ == "__main__":
    main()