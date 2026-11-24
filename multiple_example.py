# First parent class
class Father:
    def father_skills(self):
        print("Father Knows JAVA")

# Second parent class
class Mother:
    def mother_skills(self):
        print("Mother Knows PYTHON")
        
# child class
class Child(Father, Mother):
    def child_skills(self):
        print("Child Knows ML")
        
# creating an object
s1 = Child()

# calling first parent method
s1.father_skills()

# calling second parent method
s1.mother_skills()

# calling child method
s1.child_skills()
