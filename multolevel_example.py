
# Grandparent class
class Person:

    def person_details(self, name):
        self.name = name
        print(f"Person: {self.name}")


# Parent class
class Employee(Person):

    def employee_details(self, id):
        self.id = id
        print(f"Employee ID: {self.id}")


# Child class
class Developer(Employee):

    def developer_details(self, role):
        self.role = role
        print(f"Role: {self.role}")

# Creating object   q
s1 = Developer()

# Calling Grandfather method
s1.person_details("Akash")

# Calling Father method
s1.employee_details(101)

# Calling Son method
s1.developer_details("Machine Learning Engineer")
