# Parent class
class Animal:
    def eat(self):
        print("Animal is eating")
        
# Child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
        
# creating object 
d1 = Dog()

#calling parent class method
d1.eat()

# calling child class method
d1.bark()