# Private members with Getter and Setter methods
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            print("Balance Updated Successfully")
        else:
            print("Invalid Balance")


account = BankAccount(50000)

print("Current Balance:", account.get_balance())

account.set_balance(70000)

print("Updated Balance:", account.get_balance())
