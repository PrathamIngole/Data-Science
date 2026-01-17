# create a class Account with 2 attribute - bank balance and Account No. 
# create a method for debit, credit and printing the balance.
import datetime

class Account:
    def __init__(self, Acc_No, Bank_Balance) :
        self.Acc_No = Acc_No
        self.Bank_Balance = Bank_Balance
    
    def credit(self, amount) :
        self.Bank_Balance += amount
        print(f"From Account No. {self.Acc_No}, on day {Account.get_date()}, Money credited rupees {amount}, and updated bank balance is {self.Bank_Balance}\n")

    def print_balance(self) :
        print(f"Account Number {self.Acc_No}, has rupees {self.Bank_Balance}/- On {Account.get_date()}\n")

    def debit(self, amount) :
        self.Bank_Balance -= amount
        print(f"From Account No. {self.Acc_No}, on day {Account.get_date()}, Money debited rupees {amount}, and updated bank balance is {self.Bank_Balance}\n")

    @staticmethod
    def get_date() :
        return datetime.date.today()
    


person1 = Account(1223545, 50000)

person1.print_balance()     
person1.credit(600)
person1.debit(24045)
person1.print_balance()     
