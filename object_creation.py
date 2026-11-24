# Object Creation in Python

class Student:
    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student Course:", self.course)
        
# Creating first object
s1 = Student()
s1.name = "John"
s1.age = 20
s1.course = "Python"

# Creating second object
s2 = Student()
s2.name = "Alice"
s2.age = 22
s2.course = "Java"

# Display student details
print("Student 1 Details:")
s1.display()

print("\nStudent 2 Details:")
s2.display()