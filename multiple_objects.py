# Multiple Objects in Python

class Laptop:

    def display(self):
        print("Laptop Brand:", self.brand)
        print("Laptop Ram:", self.ram)
        print("Laptop Price:", self.price)


# Creating first object
l1 = Laptop()
l1.brand = "Dell"
l1.ram = "8 GB"
l1.price = 45000


# What happens when you change:
# l1.brand = "Apple"
# l1.ram = "32 GB"
# l1.price = 100000

# Creating second object
l2 = Laptop()
l2.brand = "HP"
l2.ram = "16 GB"
l2.price = 60000


# Creating third object
l3 = Laptop()
l3.brand = "Lenovo"
l3.ram = "16 GB"
l3.price = 55000

# Displaying details
print("Laptop 1 Details:")
l1.display()

print("\nLaptop 2 Details:")
l2.display()

print("\nLaptop 3 Details:")
l3.display()
