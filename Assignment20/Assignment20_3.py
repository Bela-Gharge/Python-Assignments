import threading

def EvenList(List):
    sum = 0
    for i in List:
        if(i%2 == 0 ):
            sum = sum +i
    print(sum)

def OddList(List):
    sum = 0
    for i in List:
        if(i%2 != 0 ):
            sum = sum +i
    print(sum)


def main():
    Elements = []
    N = int(input("Enter the number of elements : "))

    for i in range(N):
        val = int(input(f"Enter element {i+1} : "))
        Elements.append(val)
    print("Input List : " , Elements)

    t1 = threading.Thread(target=EvenList,args = (Elements,))
    t1.start()

    t2 = threading.Thread(target=OddList,args = (Elements,))
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()