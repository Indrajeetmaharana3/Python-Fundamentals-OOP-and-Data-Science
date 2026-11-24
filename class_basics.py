# Understanding Class in Python

class student:
    # Class Attribute
    name = "Jhon"
    age = 20
    course = "Python"
    #Instance method
    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student Course:", self.course)
        
# Creating object
s1 = student()

#calling method 
s1.display()