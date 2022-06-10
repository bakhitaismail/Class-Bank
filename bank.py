from typing import Any


class Account:    
    def __init__(self,name, account_number):
        self.name=name
        self.account_number=account_number
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        
    def deposit(self, amount):
        if amount<=0:
           return f"Hello your deposited amount {amount} this is your new balance {self.balance}"    
        else:
            self.balance+=amount 
            self.deposits.append(amount)
            return f"You have deposited {amount}. Your new balance is {self.balance}"
    
    def withdraw(self, amount):
        transaction=100
        if (amount+transaction)>self.balance:
           return f"Your balance is {self.balance}, you have withdrawn {amount}. Your transaction cost is {transaction}"
        elif (amount+transaction)<=0:
            return f"Amount must be greater than zero"
        else:
            self.balance-=(amount+transaction)
            self.withdrawals.append(amount)
            return f"You have withdrawn {amount} a transaction fee of {transaction} has been deducted and your balance is {self.balance}"
        
    def deposits_statement(self):
        for message in self.deposits:
            print (message)
          
    def withdrawals_statement(self):
        for cash_out in self.withdrawals:
            print (cash_out)
            
    def current_balance(self):
        current = self.balance
        print (current)      
