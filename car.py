class Car:
    def __init__(self, make , model , year):
        self.make = make
        self.model = model
        self.year = year
c = Car("Toyota" , "Camry" , 2020)
print(f"make: {c.make} , model: {c.model} , year: {c.year}")