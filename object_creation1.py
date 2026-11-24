
class Employee:
    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.id)
        print("Employee Salary:", self.salary)

# Creating first object
e1 = Employee()
e1.name = "Rahul"
e1.id = 101
e1.salary = 25000

# Creating second object
e2 = Employee()
e2.name = "Amit"
e2.id = 102
e2.salary = 30000

# Creating third object
e3 = Employee()
e3.name = "Priya"
e3.id = 103
e3.salary = 35000

# Display employee details
print("Employee 1 Details:")
e1.display()

print("\nEmployee 2 Details:")
e2.display()

print("\nEmployee 3 Details:")
e3.display()