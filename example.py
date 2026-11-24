class student:
    def __init__(self, name, _rollno, __marks):
        self.name = name            # public
        self._rollno = _rollno      # protected
        self.__marks = __marks      # private
    
    # Using Getter and Setter methods
    def get_marks(self):
         return self.__marks
        
    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
            print("Marks Updated Successfully")
        else:
            print("Invalid Marks")
            
    # Display method
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self._rollno)
        print("Marks:", self.__marks)
# creating object
s1 = student("Akash", 101, 85)
s1.display()
print("\n")
# Updating marks using setter
s1.set_marks(95)

# Display updated marks
print("Updated Marks:", s1.get_marks())
