
# Grandparent class
class Grandfather:

    def grandfather_property(self):
        print("Grandfather owns a house")


# Parent class
class Father(Grandfather):

    def father_property(self):
        print("Father owns a car")


# Child class
class Son(Father):

    def son_property(self):
        print("Son owns a bike")


# Creating object
s1 = Son()

# Calling Grandfather method
s1.grandfather_property()

# Calling Father method
s1.father_property()

# Calling Son method
s1.son_property()
