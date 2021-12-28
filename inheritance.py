class Vehicle:

    def __init__(self, make, model, fuel="gas"):

        self.make = make
        self.model = model
        self.fuel = fuel

    def is_eco_friendly(self):
        if self.fuel == "gas":
            return False
        else:
            return True


# class Car inherits attributes from parent class Vehicle
class Car(Vehicle):

    def __init__(self, make, model, fuel="gas", num_wheels=4):
        super().__init__(make, model, fuel)
        self.num_wheels = num_wheels


# class Motorcycle inherits attributes from parent class Vehicle
class Motorcycle(Vehicle):

    def __init__(self, make, model, fuel="gas", num_wheels=2):
        super().__init__(make, model, fuel)
        self.num_wheels = num_wheels


subaru = Car("Subaru", "WRX Limited")
print(subaru.is_eco_friendly())

zero_fxe = Motorcycle("Zero", "FXE", "electric")
print(zero_fxe.is_eco_friendly())
