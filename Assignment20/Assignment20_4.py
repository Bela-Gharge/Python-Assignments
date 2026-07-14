import threading

def Small(str):
    count = 0
    for char in str:
        if(char >= 'a' and char <= 'z'):
            count = count +1
    print(f"Total lowercase letters are : {count}")
    print("Id is : ",threading.get_ident())

def Capital(str):
    count = 0
    for char in str:
        if(char >= 'A' and char <= 'Z'):
            count = count +1
    print(f"Total uppercase letters are : {count}")
    print("Id is : ",threading.get_ident())

    
def Digit(str):
    count = 0
    for char in str:
        if(char >= '0' and char <= '9'):
            count = count +1
    print(f"Total digits are : {count}")
    print("Id is : ",threading.get_ident())

def main():
    str = input("Enter : ")
    
    t1 = threading.Thread(target=Small,args=(str,))
    t1.start()
    t1.join()    

    t2 = threading.Thread(target=Capital,args=(str,))
    t2.start()
    t2.join()

    t3 = threading.Thread(target=Digit,args=(str,))
    t3.start()
    t3.join()

if __name__ == "__main__":
    main()