class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    
    def __repr__(self):
        return f"Make: {self.make} , Model: {self.model} , Year: {self.year}"
    
t1 = Car(make = "Toyota", model = "Camry", year = 2020)
print(t1)