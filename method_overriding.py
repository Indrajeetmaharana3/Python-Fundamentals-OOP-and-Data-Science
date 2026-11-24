# Parent class
class Animal:

    def sound(self):
        print("Animal makes a sound")


# Child class
class Dog(Animal):

    pass


# Creating objects
a = Dog()

# Calling the same method
a.sound()