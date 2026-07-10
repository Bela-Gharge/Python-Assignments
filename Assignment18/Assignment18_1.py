def Sum(no):                                      
    sum = 0
    for i in no :
        sum = sum+int(i)
    return(sum)


def main():
    Elements = []
    N = int(input("Enter the number of elements : "))

    for i in range(N):
        val = int(input(f"Enter {i+1}th element : "))
        Elements.append(val)
    
    Ret = Sum(Elements)
    print("Sum of elements is : " , Ret)

if __name__ == "__main__":
    main()