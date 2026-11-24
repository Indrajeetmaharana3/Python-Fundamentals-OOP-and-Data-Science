from abc import ABC, abstractmethod


# Abstract class
class Payment(ABC):

    @abstractmethod
    def payment(self, amount):
        pass


# Child class
class CreditCard(Payment):

    def payment(self, amount):
        print(f"Paid Rs.{amount} using Credit Card")


# Child class
class UPI(Payment):

    def payment(self, amount):
        print(f"Paid Rs.{amount} using UPI")


# Child class
class Cash(Payment):

    def payment(self, amount):
        print(f"Paid Rs.{amount} using Cash")


# Creating objects
p1 = CreditCard()
p2 = UPI()
p3 = Cash()


# Calling methods
p1.payment(500)
p2.payment(1000)
p3.payment(200)