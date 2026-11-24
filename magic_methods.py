# Class
class Mobile:

    # Constructor magic method
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # String magic method
    def __str__(self):
        return f"{self.brand} {self.model} - Rs.{self.price}"


# Creating object
m1 = Mobile("Samsung", "Galaxy S25", 75000)

# Printing object
print(m1)


# class Calculator:

#     def __init__(self, number):
#         self.number = number

#     def __add__(self, other):
#         return self.number + other.number


# c1 = Calculator(10)
# c2 = Calculator(20)

# print("Addition:", c1 + c2)


# class Team:

#     def __init__(self, members):
#         self.members = members

#     def __len__(self):
#         return len(self.members)


# t1 = Team(["Akash", "Rahul", "John"])

# print("Total Members:", len(t1))