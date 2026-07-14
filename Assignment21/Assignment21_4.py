import threading

def Sum(List):
    sum = 0 
    for i in List:
        sum = sum+i
    print("Sum is : ", sum)     

def Product(List):
    product = 1
    for i in List:
        product = product*i
    print("Product : ",product)    


def main():
    List = []

    limit = int(input("Enter number of elements : "))


    for i in range(limit):
        val = int(input(f"Enter Number {i+1} : "))
        List.append(val)
    print("Input List : " ,List)

    
    t1=threading.Thread(target=Sum, args=(List,))
    t1.start()
    t1.join()

    t2=threading.Thread(target=Product, args=(List,))
    t2.start()
    t2.join()


if __name__ == "__main__":
    main()