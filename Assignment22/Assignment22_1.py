import multiprocessing

def SumSquare(No):
    sum = 0
    for i in range(1,No+1):
        sum = sum + (i*i)
    return sum

def main():
    Data = [1000000, 2000000, 3000000, 4000000, 5000000,]
    Result = []

    pobj = multiprocessing.Pool()
    Result = pobj.map(SumSquare,Data)

    pobj.close()
    pobj.join()

    print("Result is : ",Result)


if __name__ == "__main__":
    main()