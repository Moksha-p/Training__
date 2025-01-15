class Vehicle:
  def vehicleSpeed(self , max_speed ):
    print("Max speed is: " , max_speed)
  def vehicleMileage(self ,  mileage):
    print("Mileage is: " , mileage)

class Car(Vehicle):
  def carModel(self , Model):
    print("Model is: " , Model)
  def carColor(self , color):
    print("Color is: " , color)

class Bike:
  def bikeModel(self , Model):
    print("Model is: " , Model)
  def bikeColor(self , color):
    print("Color is: " , color)

veh = Vehicle()
veh.vehicleSpeed(100)
veh.vehicleMileage(20)
car = Car()
car.carModel("BMW")
car.carColor("Blue")
