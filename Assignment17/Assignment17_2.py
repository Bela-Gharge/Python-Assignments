def stars(n):
    for i in range(1,n+1):
        print('*'*n)

def main():
    no = int(input("Enter a number"))
    stars(no)
                            
if __name__ == "__main__":
    main()