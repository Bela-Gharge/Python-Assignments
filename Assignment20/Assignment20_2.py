import time
import threading

def EvenFactors(N):
    sum = 0
    for i in range(1,N+1):
        if (N%i == 0 ):
            if(i%2 == 0):
                sum = sum + i
    print("Sum of even factors is : " , sum)

def OddFactors(N):
    sum = 0
    for i in range(1,N+1):
        if (N%i == 0 ):
            if(i%2 != 0):
                sum = sum + i
    print("Sum of odd factors is : " , sum)


def main():
    No = int(input("Enter number : "))
    
    start_time = time.perf_counter()
    
    t1 = threading.Thread(target=EvenFactors,args=(No,))
    t1.start()
    t1.join()    

    t2 = threading.Thread(target=OddFactors,args=(No,))
    t2.start()
    t2.join()

    end_time = time.perf_counter()

    print("Time required : " , end_time - start_time)

    print("Exit from main")

if __name__ == "__main__":
    main()