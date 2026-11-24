# Class
class Mobile:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # Instance method
    def display_details(self):
        print("Mobile Brand:", self.brand)
        print("Mobile Model:", self.model)
        print("Mobile Price:", self.price)


# Creating objects
m1 = Mobile("Samsung", "S25", 75000)
m2 = Mobile("Apple", "iPhone 17", 85000)


# Calling instance methods
m1.display_details()

print()

m2.display_details()