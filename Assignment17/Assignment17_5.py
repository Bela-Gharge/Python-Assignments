def Prime(n):                                      
    count = 0
    for i in range(1,int(n**0.5+1),1):
        if(n%i==0):
            count = count+i
            if(n//i != i):
                count = count + 1

    if (count == 2):
        print("Prime Number")
    else :
        print("Not Prime Number")    
    

def main():
    no = int(input("Enter Number : "))
    Prime(no)

if __name__ == "__main__":
    main()