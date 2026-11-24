# Encapsulation in Python with private members


class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Account Balance:", self.__balance)


# Creating object
account = BankAccount("Akash", 50000)

# Accessing public member
print(account.account_holder)

# Accessing private member through method
account.display_balance()

