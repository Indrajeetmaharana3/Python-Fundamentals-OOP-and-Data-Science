class Employee:

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Employee Salary:", self.salary)


# Creating objects
e1 = Employee("Rahul", 101, 25000)
e2 = Employee("Akash", 102, 30000)

# Displaying details
e1.display()

print()

e2.display()