class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bike(Vehicle):
    def move(self):
        return "Bike is riding"

def operate_vehicle(vehicle):
    print(vehicle.move())

car = Car()
bike = Bike()
operate_vehicle(car)
operate_vehicle(bike)
