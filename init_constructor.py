# Without constructor:
#class Student:
#   pass

#s1 = Student()

#s1.name = "John"
#s1.age = 22
#s1.course = "Python"

# With constructor:
#class student:
#    def __init__(self):
 #       print("Constructor is called automatically when object is created")

# Creating objects
#s1 = student()
#s2 = student()
#s3 = student()

#constructor with attributes
class Student:
    def __init__(self):
        self.name = "John"
        self.age = 22
        self.course = "Python"
        
    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student Course:", self.course)

# Creating Objects
s1 = Student()
# Calling method
s1.display()