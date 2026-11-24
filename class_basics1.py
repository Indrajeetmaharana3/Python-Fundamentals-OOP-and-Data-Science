class Mobile:
    # Class Attribute
    brand = "Samsung"
    model = "Galaxy S24"
    price = 75000
    
    #Instance method
    def display(self):
        print("Mobile Brand:", self.brand)
        print("Mobile Model:", self.model)
        print("Mobile Price:", self.price)
        
# Creating object
m1 = Mobile()

#calling method 
m1.display()