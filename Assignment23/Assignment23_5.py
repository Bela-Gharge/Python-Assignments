import multiprocessing
import os

def Factorial(N):
    print("Process ID : " , os.getpid())
    Fact = 1
    for i in range(1,N+1):
        Fact = Fact *i
    return Fact

def main():
    Data = [10, 20, 30, 40]
    Result = []

    pobj = multiprocessing.Pool()
    Result = pobj.map(Factorial,Data)

    pobj.close()
    pobj.join()

    print("Result is : ", Result)
    
if __name__ == "__main__":
    main()