class Calculator:

    def add(self, a, b, c=0):
        result = a + b + c
        print("Addition:", result)


# Creating object
cal = Calculator()

# Calling the same method with different arguments
cal.add(10, 20)
cal.add(10, 20, 30)