# Method Resolution Order (MRO) in Python
class Father:

    def show(self):
        print("Father class")


class Mother:

    def show(self):
        print("Mother class")


class Child(Father, Mother):
    pass


c = Child()
c.show()