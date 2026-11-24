# Understanding self keyword in Python

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        
# Creating first Objects
s1 = Student("Rahul", 22)

# Creating second Objects
s2 = Student("Priya", 20)

# Displaying information
print("Student 1 Details:")
s1.display()
print("Student 2 Details:")
s2.display()