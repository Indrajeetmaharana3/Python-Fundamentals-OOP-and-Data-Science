# without oops
car1_name = "Toyota"
car1_year = 2020

car2_name = "Honda"
car2_year = 2021

print("Without OOPS:")
print(car1_name, car1_year)
print(car2_name, car2_year)

#With OOPS
class car:
    def display(self):
        print("Car Name:", self.name)
        print("Car Year:", self.year)
# Creating objects of the class car
c1 = car()
c1.name = "Toyota"
c1.year = 2020

# Creating another object of the class car
c2 = car()
c2.name = "Honda"
c2.year = 2021

print("\nWith OOPS:")
c1.display()
c2.display()