class Employee:
    def __init__(self):
        self.name = "Rahul"
        self.emp_id = 101
        self.salary = 25000

    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Employee Salary:", self.salary)

# Creating Objects
e1 = Employee()
e2 = Employee()
# Calling method
e1.display()
e2.display()