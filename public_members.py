# Encapsulation in Python with public members
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def display_info(self):
        print("Mobile Brand:", self.brand)
        print("Mobile Model:", self.model)
        print("Mobile Price:", self.price)
        
#ceating an object 
m1 = Mobile("Samsung", "Galaxy S25", 80000)
m2 = Mobile("Apple", "iPhone 15", 120000)

# Accessing public members
print(m1.brand)
print(m1.model)
print(m1.price)
print("\n")
print(m2.brand)
print(m2.model)
print(m2.price)
print("\n")

# Calling public method
m1.display_info()
print("\n")
m2.display_info()
print("\n")

# Direct modification
m1.price = 70000
print("Updated Price:", m1.price)