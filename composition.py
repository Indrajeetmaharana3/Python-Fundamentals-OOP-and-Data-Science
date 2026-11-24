# Engine class
class Engine:

    def start_engine(self):
        print("Car Engine Started")


# Car class
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        # Composition
        self.engine = Engine()

    def car_details(self):
        print("Car Brand:", self.brand)
        print("Car Model:", self.model)

    def start_car(self):
        self.engine.start_engine()


# Creating object
c1 = Car("Toyota", "Fortuner")

# Calling methods
c1.car_details()
c1.start_car()