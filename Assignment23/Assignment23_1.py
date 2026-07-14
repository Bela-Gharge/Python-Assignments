import multiprocessing
import os

def EvenCount(N):
    print("Process ID : " , os.getpid())
    count = 0
    for i in range(1,N+1):
        if(i%2 == 0):
            count = count+i
    return count

def main():
    Data = [1000000, 2000000, 3000000, 4000000]
    Result = []

    pobj = multiprocessing.Pool()
    Result = pobj.map(EvenCount,Data)

    pobj.close()
    pobj.join()

    print("Result is : ", Result)
    
if __name__ == "__main__":
    main()