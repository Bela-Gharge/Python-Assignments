def nums(n):
    for i in range(1,n+1):
        print(*range(1,n+1))

def main():
    no = int(input("Enter a number"))
    nums(no)
                            
if __name__ == "__main__":
    main()