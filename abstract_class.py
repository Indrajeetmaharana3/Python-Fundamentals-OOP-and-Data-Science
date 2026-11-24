from abc import ABC, abstractmethod


# Abstract class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


# Child class
class Dog(Animal):

    def sound(self):
        print("Dog barks")


# Another child class
class Cat(Animal):

    def sound(self):
        print("Cat meows")


# Creating objects
d = Dog()
c = Cat()


# Calling methods
d.sound()
c.sound()