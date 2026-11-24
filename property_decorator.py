# Class
class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    # Getter
    @property
    def balance(self):
        return self._balance

    # Setter
    @balance.setter
    def balance(self, new_balance):

        if new_balance >= 0:
            self._balance = new_balance
            print("Balance Updated Successfully")

        else:
            print("Invalid Balance! Cannot be negative.")


# Creating object
account = BankAccount(10000)

# Accessing property
print("Current Balance:", account.balance)

# Updating property
account.balance = 15000

print("Updated Balance:", account.balance)

# Trying invalid balance
account.balance = -500