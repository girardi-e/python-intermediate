# We use classes to define new types with their own methods and attributes
class Car:
    # class variable
    runs = True

    # Constructor: initializer method
    def __init__(self, name):
        # instance variable -> attributes
        self.name = name

    def start(self):

        if self.runs:
            print(f"{self.name} car is started =)")
        else:
            print(f"{self.name} car is broken =( ")
