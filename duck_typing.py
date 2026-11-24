# Mobile class
class Mobile:

    def start(self):
        print("Mobile is starting")


# Laptop class
class Laptop:

    def start(self):
        print("Laptop is starting")


# Tablet class
class Tablet:

    def start(self):
        print("Tablet is starting")


# Common function
def start_device(device):
    device.start()


# Creating objects
m = Mobile()
l = Laptop()
t = Tablet()


# Calling common function
start_device(m)
start_device(l)
start_device(t)