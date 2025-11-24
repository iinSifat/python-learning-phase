class Bank_account:
    def __init__(self, acnt_no, balance):
        self.acnt_no= acnt_no
        self.balance = balance
    
    def deposit(self,amnt): #must always use self to refer the object itself like (this)    
        self.balance += amnt
    def withdraw(self,amnt):
        if(amnt<self.balance):
            self.balance-=amnt
        else:
            print("Insufficient balance")
    def print_det(self):
        print(self.balance)
        
B1 = Bank_account(1, 20000)
B1.print_det()
B1.withdraw(12000)
B1.print_det()
B1.deposit(13000)
B1.print_det()
