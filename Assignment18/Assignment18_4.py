def Frequency(List):
    Target = int(input("Enter target element : "))

    count = 0
    for i in List:
        if(i==Target):
            count = count+1
    return count

def main():
    Elements = []
    N = int(input("Enter the number of elements : "))

    for i in range(N):
        val = int(input(f"Enter element {i+1} : "))
        Elements.append(val)

    Ret = Frequency(Elements)
    print(f"Frequency of is {Ret}")


if __name__ == "__main__":
    main()