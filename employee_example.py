
# Employee Management Example using OOPs

class Employee:

    # Method to display employee details
    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Department:", self.department)
        print("Salary:", self.salary)


# Creating first employee object
e1 = Employee()
e1.name = "Rahul"
e1.emp_id = 101
e1.department = "Data Science"
e1.salary = 30000


# Creating second employee object
e2 = Employee()
e2.name = "Amit"
e2.emp_id = 102
e2.department = "Software Development"
e2.salary = 35000


# Creating third employee object
e3 = Employee()
e3.name = "Priya"
e3.emp_id = 103
e3.department = "Machine Learning"
e3.salary = 40000


# Displaying employee details
print("===== Employee 1 Details =====")
e1.display()

print("\n===== Employee 2 Details =====")
e2.display()

print("\n===== Employee 3 Details =====")
e3.display()
