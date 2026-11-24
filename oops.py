# Introduction to object-oriented programming(OOPS)

# without oops
student1_name = "John"
student1_age = 20

student2_name = "Alice"
student2_age = 22

print("Without OOPS:")
print(student1_name, student1_age)
print(student2_name, student2_age)

#With OOPS
class student:
    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
# Creating objects of the class student
s1 = student()
s1.name = "John"
s1.age = 20

# Creating another object of the class student
s2 = student()
s2.name = "Alice"
s2.age = 22

print("\nWith OOPS:")
s1.display()
s2.display()