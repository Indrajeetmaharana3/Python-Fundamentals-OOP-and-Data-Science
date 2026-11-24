
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Mobile Brand:", self.brand)
        print("Mobile Model:", self.model)
        print("Mobile Price:", self.price)

# Creating Objects
m1 = Mobile("Samsung", "Galaxy S24", 75999)
m2 = Mobile("Apple", "iPhone 16", 80000)
m3 = Mobile("OnePlus", "OnePlus 13R", 42000)

# Displaying information
print("Mobile 1 Details:\n")
m1.display()
print("Mobile 2 Details:\n")
m2.display()
print("Mobile 3 Details:\n")
m3.display()
