import multiprocessing
import os

def Factorial(N):
    print("Pid of this process is : " , os.getpid() )
    Fact = 1
    for i in range(1,N+1):
        Fact = Fact * i
    return Fact

def main():
    Data = []
    N = int(input("Enter no of elements : "))

    for i in range(N):
        val = int(input(f"Enter Element {i+1} : "))
        Data.append(val)
    print(f"Input is : {Data}")

    pobj = multiprocessing.Pool()
    Result = pobj.map(Factorial,Data)

    pobj.close()
    pobj.join()

    print("Result is : ",Result)
if __name__== "__main__":
    main()