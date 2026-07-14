import multiprocessing
import time

def Sum5(No):
    sum = 0
    for i in range(1,No+1):
        sum = sum + (i**5)
    return sum

def main():
    Data = []
    N = int(input("Enter no of elements : "))

    for i in range(N):
        val = int(input(f"Enter Element {i+1} : "))
        Data.append(val)
    print(f"Input is : {Data}")

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    Result = pobj.map(Sum5,Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Result is : ",Result)
    print(f"Time required is : {end_time - start_time:.4f} seconds ")

if __name__ == "__main__":
    main()