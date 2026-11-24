
# Parent class
class Animal:

    def eat(self):
        print("Animals are eating")


# First child class
class Dog(Animal):

    def bark(self):
        print("Dog is barking")


# Second child class
class Cat(Animal):

    def meow(self):
        print("Cat is meowing")


# Third child class
class Cow(Animal):

    def moo(self):
        print("Cow is mooing")


# Creating objects
d1 = Dog()
c1 = Cat()
co1 = Cow()


# Calling Dog methods
d1.eat()
d1.bark()

print()

# Calling Cat methods
c1.eat()
c1.meow()

print()

# Calling Cow methods
co1.eat()
co1.moo()
