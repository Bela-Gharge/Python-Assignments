def Pattern(N):
    for i in range(1,N+1,1):
        print(*range(1,i+1))

def main():
    no = int(input("Enter number : "))
    Pattern(no)


if __name__ == "__main__":
    main()