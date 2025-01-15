class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __repr__(self):
        return f"Car: {self.make} {self.model}"

class Bike(Vehicle):
    def __repr__(self):
        return f"Bike: {self.make} {self.model}"

car = Car("Toyota", "Camry")
bike = Bike("Yamaha", "MT-07")

print(car)
print(bike)