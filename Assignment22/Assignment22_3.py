import multiprocessing

def Prime(n):
    count = 0
    for i in range(1,int(n**0.5+1),1):
        if(n%i==0):
            count = count+1
            if(n//i != i):
                count = count + 1
    
    if (count == 2):
        return True
    else :
        return False
    

def PrimeCount(N):
    count = 0
    for i in range(1,N+1):
        if Prime(i):
            count=count+1
    return count

        
def main():
    Data = [1000, 2000, 3000, 4000, 5000]
    Result = []

    pobj = multiprocessing.Pool()
    Result = pobj.map(PrimeCount,Data)

    pobj.close()
    pobj.join()

    print("Result is : ",Result)


if __name__ == "__main__":
    main()