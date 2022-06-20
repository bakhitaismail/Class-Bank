from typing import Any
from datetime import datetime


class Account:    
    def __init__(self,name, account_number):
        self.name=name
        self.account_number=account_number
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        self.date=datetime.now()
        self.loan_balance=0
        self.instance=0

        
    def deposit(self, amount):
        if amount<=0:
           return f"Deposit must be more than zero"    
        else:
            self.balance+=amount 
            self.deposits.append({"date":self.date.strftime("%c"), "amount": amount, "narration":"deposit"})
            return f"Hello customer you have deposited {amount} and your new balance is {self.balance}"
            # self.deposits.append(amount)
            # return f"You have deposited {amount}. Your new balance is {self.balance}"
    
    def withdraw(self, amount):
        transaction=100
        if (amount+transaction)>self.balance:
           return f"Your balance is {self.balance}, you have withdrawn {amount}. Your transaction cost is {transaction}"
        elif (amount+transaction)<=0:
            return f"Amount must be greater than zero"
        else:
            self.balance-=(amount+transaction)
            self.withdrawals.append({"date":self.date.strftime("%c",), "amount":amount, "narration":"withdraw"})
            # return f"You have withdrawn {amount} a transaction fee of {transaction} has been deducted and your balance is {self.balance}"
        
    def deposits_statement(self):
        for message in self.deposits:
            print (message)
          
    def withdrawals_statement(self):
        for cash_out in self.withdrawals:
            print (cash_out)
            
    def current_balance(self):
        current = self.balance
        return f"Hello {self.name} your current balance is {current}"   
    
    def full_statement(self):
        statement=self.withdrawals+self.deposits
        for word in statement:
            print(word) 
            
    def borrow(self,amount):
        sum=0  
        for x in self.deposits:
            sum +=x[amount]
            if (len(self.deposits)) < 10:
                return f"Hello {self.name}, You can't borrow {amount} your account balnce is less"
            elif amount<100:
                return f"Hello {self.name}, You can't borrow less than Kshs 100"
            elif amount > sum//3:
                return f"Hello {self.name}, You can only borrow when you have 1/3 of your deposit"
            elif self.deposits==0:
                return f"Dear {self.name}, Your account balnce is zero"
            elif self.loan_balance>0:
                return f"Hello {self.name}, you have an outstanding loan of {self.loan_balance}"
            else:
                 self.loan_balance+=(amount(amount*3/100))
                 return f"Hello {self.name}, you have borrowed {amount} with an interest of {amount*3/100} as your total loan amount is {self.loan_balance}"
             
             
    def loan_repayment(self,amount):
        if amount < self.loan_balance:
            self.loan_balance-=amount
            return f"hello {self.name}, you have repaid {amount}.Outstanding balance is {self.loan_balance}"
        elif amount == self.loan_balance:
            self.loan_balance-=amount
            return f"Hello {self.name}, you have repaid {amount}. Your loan is fully paid "
        elif amount > self.loan_balance:
            over_pay = amount - self.loan_balance
            remainder = amount - over_pay 
            self.balance+=over_pay
            self.loan_balance-=remainder
            return f"Hello {self.name}, you have repaid {amount}.Your balance is {self.loan_balance}. Your account balance is {self.balance}"
        else:
            self.loan_balance-=amount
            return f"Hello {self.name}, you have paid a loan of {amount} and your current balance is {self.loan_balance}"
    
            
    def transfer(self,amount,instance):
        if amount<=0:
            return "Enter an amount"
        elif amount>=self.balance:
            return "Insufficient balance"
        else:
            self.balance-=amount
            instance.balance+=amount
            return f"You have transfered {amount} to {instance} account with the name of {instance.name}. Your new balance is {self.balance}"

                                                                                                                                  