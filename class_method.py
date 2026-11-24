# Class
class Employee:

    # Class variable
    company = "OpenAI"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method
    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", Employee.company)

    # Class method
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


# Creating objects
e1 = Employee("Akash", 30000)
e2 = Employee("Rahul", 40000)

# Display before changing company
e1.display()

print()

e2.display()

# Calling class method
Employee.change_company("Google")

print("\nAfter Changing Company:")

# Display after changing company
e1.display()

print()

e2.display()