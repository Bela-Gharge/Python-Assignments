class Numbers : 

    def __init__(self):
        self.Value = int(input("Enter Number : "))

    def ChkPrime(self):
        count = 0
        for i in range(1,int(self.Value**0.5+1),1):
            if(self.Value%i==0):
                count = count+1
                if(self.Value//i != i):
                    count = count + 1

        if (count == 2):
            print("Prime Number")
        else :
            print("Not Prime")  
        

    def ChkPerfect(self):
        sum = 0
        for i in range(1,self.Value+1):
            if(self.Value %i == 0):
                sum = sum + i
        
        if(sum == self.Value):
            print("Perfect Number")
        else  :
            print("Not Perfect Number")

    def Factors(self):
        for i in range(1,self.Value+1):
            if(self.Value%i == 0):
                print(i)

    def SumFactors(self):
        count = 0
        for i in range(1,self.Value+1):
            if(self.Value%i == 0):
                count = count+i
        return(count)


obj1 = Numbers()
obj1.ChkPerfect()
obj1.ChkPrime()
obj1.Factors()
obj1.SumFactors()