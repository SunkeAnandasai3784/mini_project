from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def credit(self, amount):
        pass

    @abstractmethod
    def debit(self, amount):
        pass

class CheckingAccount(Account):
    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount} to checking account. New balance: {self.balance}")

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Debited {amount} from checking account. New balance: {self.balance}")
        else:
            print("Insufficient funds in checking account")

class SavingsAccount(Account):
    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount} to savings account. New balance: {self.balance}")

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Debited {amount} from savings account. New balance: {self.balance}")
        else:
            print("Insufficient funds in savings account")

class BusinessAccount(Account):
    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount} to business account. New balance: {self.balance}")

    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Debited {amount} from business account. New balance: {self.balance}")
        else:
            print("Insufficient funds in business account")

# Create some accounts
checking = CheckingAccount(1000)
savings = SavingsAccount(2000)
business = BusinessAccount(5000)

# Credit and debit some amounts
checking.credit(500)
checking.debit(200)
savings.credit(1000)
savings.debit(500)
business.credit(2000)
business.debit(3000)
