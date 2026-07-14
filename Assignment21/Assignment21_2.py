import threading

def Max(List):
    max = List[0] 
    for i in List:
        if(i>List[0]):
            max = i
    print("Maximum element is : ", max)    

def Min(List):
    min = List[0]  
    for i in List:
        if(i<List[0]):
            min = i
    print("Minimum element is : ",min)    


def main():
    List = []

    limit = int(input("Enter number of elements : "))


    for i in range(limit):
        val = int(input(f"Enter Number {i+1} : "))
        List.append(val)
    print("Input List : " ,List)

    
    t1=threading.Thread(target=Max, args=(List,))
    t1.start()
    t1.join()

    t2=threading.Thread(target=Min, args=(List,))
    t2.start()
    t2.join()


if __name__ == "__main__":
    main()