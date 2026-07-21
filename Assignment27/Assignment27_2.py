class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = input("Enter Name : ")
        self.Amount = float(input("Enter Initial Amount : "))

    def Display(self):
        print(f"{self.Name} has {self.Amount} in account")

    def Deposit(self):
        
        deposit_amt = float(input("Enter Amount to be deposited : "))
        self.Amount = self.Amount+deposit_amt
        print(f"Amount Deposited . Current Balance is : {self.Amount}")

    def Withdraw(self):
        withdraw_amt = float(input("Enter Amount to be withdrawn : "))
        
        if(withdraw_amt>self.Amount):
            print("Insufficient Balance")
        else :         
            self.Amount = self.Amount-withdraw_amt
            print(f"Amount Withdrawn . Current Balance is : {self.Amount}")


    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(interest)
    

print("_"*40)
obj1 = BankAccount()
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()
print("_"*40)

print("_"*40)
obj2 = BankAccount()
obj2.Display()
obj2.Deposit()
obj2.Withdraw()
obj2.CalculateInterest()
print("_"*40)