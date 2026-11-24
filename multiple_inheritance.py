# First parent class
class Camera:
    def take_photo(self):
        print("Taking a photo")

# Second parent class
class MusicPlayer:
    def play_music(self):
        print("Playing music")
        
# child class
class Smartphone(Camera, MusicPlayer):
    def make_call(self):
        print("Making a call")
        
# creating an object
s1 = Smartphone()

# calling first parent method
s1.take_photo()

# calling second parent method
s1.play_music()

# calling child method
s1.make_call()
