# Encapsulation in Python with protected members

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self._balance = balance

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self._balance)


# Creating object
account = BankAccount("Akash", 50000)

# Accessing public member
print("Account Holder:", account.account_holder)
# Accessing protected member
print("Balance:", account._balance)

# Calling method
account.display()
