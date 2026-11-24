# Parent class
class Employee:

    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)


# Child class
class Developer(Employee):

    def __init__(self, name, emp_id, language):

        # Calling parent constructor
        super().__init__(name, emp_id)

        self.language = language

    def display(self):

        # Calling parent method
        super().display()

        print("Programming Language:", self.language)


# Creating object
d1 = Developer("Akash", 101, "Python")

# Calling method
d1.display()