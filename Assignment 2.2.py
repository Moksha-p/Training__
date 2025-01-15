# Inheritance

#  9. Create a base class Employee with attributes name and salary. Create a subclass Developer that adds an attribute
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def __str__(self):
        return f"name: {self.name}, salary: {self.salary}, programming_language: {self.programming_language}"

# Example Test Case
developer = Developer("Alice", 70000, "Python")
print(developer)

# 10. Create a base class Appliance with a method turn_on. Create a subclass WashingMachine that overrides the turn_on method.
class Appliance:
    def turn_on(self):
        return "Appliance is turned on"

class WashingMachine(Appliance):
    def __init__(self, model):
        self.model = model

    def turn_on(self):
        return f"Washing Machine {self.model} is turned on"

# Example Test Case
appliance = Appliance()
washing_machine = WashingMachine("LG")
print(appliance.turn_on())
print(washing_machine.turn_on())

# Encapsulation

# 11. Create a class PrivateData with private attributes username and password. Implement methods to get and set these attributes.
class PrivateData:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def set_password(self, new_password):
        self.__password = new_password

    def get_password(self):
        return self.__password

# Example Test Case
private_data = PrivateData("user1", "pass123")
print(f"Username: {private_data.get_username()}")
private_data.set_password("newpass123")
print(f"Password: {private_data.get_password()}")

#12. Create a class Account with private attributes account_number and balance. Implement methods to deposit and withdraw money.
class Account:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Example Test Case
account = Account("987654321", 5000)
account.deposit(1500)
account.withdraw(2000)
print(f"Balance: {account.get_balance()}")

# Polymorphism

#13. Create a function operate_vehicle that takes a vehicle object and calls its move method. Create classes Car and Bike that implement move differently.
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def __init__(self, model):
        self.model = model

    def move(self):
        return f"{self.model} is driving"

class Bike(Vehicle):
    def __init__(self, model):
        self.model = model

    def move(self):
        return f"{self.model} is riding"

def operate_vehicle(vehicle):
    print(vehicle.move())

# Example Test Case
car = Car("Toyota")
bike = Bike("Yamaha")
operate_vehicle(car)
operate_vehicle(bike)

#14. Create a function operate_device that takes a device object and calls its operate method. Create classes Laptop and Smartphone that implement operate differently.
class Device:
    def operate(self):
        pass

class Laptop(Device):
    def __init__(self, model):
        self.model = model

    def operate(self):
        return f"{self.model} is operating"

class Smartphone(Device):
    def __init__(self, model):
        self.model = model

    def operate(self):
        return f"{self.model} is operating"

def operate_device(device):
    print(device.operate())

# Example Test Case
laptop = Laptop("Dell")
smartphone = Smartphone("iPhone")
operate_device(laptop)
operate_device(smartphone)

# Abstraction
# 15. Define an abstract class Transport with an abstract methodtravel. Create subclasses Bus and Train that implement the travel method.
from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def travel(self):
        pass

class Bus(Transport):
    def __init__(self, route):
        self.route = route

    def travel(self):
        return f"Bus {self.route} is traveling"

class Train(Transport):
    def __init__(self, route):
        self.route = route

    def travel(self):
        return f"Train {self.route} is traveling"

# Example Test Case
bus = Bus("10A")
train = Train("Express")
print(bus.travel())
print(train.travel())

#16. Define an abstract class Payment with an abstract method process. Create subclasses CreditCard and PayPal that implement the process method.
class Payment(ABC):
    @abstractmethod
    def process(self):
        pass

class CreditCard(Payment):
    def __init__(self, number):
        self.number = number

    def process(self):
        return f"Processing credit card payment for {self.number}"

class PayPal(Payment):
    def __init__(self, account):
        self.account = account

    def process(self):
        return f"Processing PayPal payment for {self.account}"

# Example Test Case
credit_card = CreditCard("1234")
paypal = PayPal("user@example.com")
print(credit_card.process())
print(paypal.process())
