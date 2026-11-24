# Parent class
class Employee:
    def employee_details(self, name, id):
        self.name = name
        self.id = id
        print("Employee Name:", self.name)
        print("Employee ID:", self.id)

# Child class
class Developer(Employee):
    def developer_role(self):
        print("Developer Role: Machine Learning Engineer")
        
# creating object 
d = Developer()

#calling parent class method
d.employee_details("John", 123)

# calling child class method
d.developer_role()