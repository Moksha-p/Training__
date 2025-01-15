# Inheritance

# 9. Create a base class Employee with attributes name and salary.
# Create a subclass Developer that adds an attribute programming_language.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

# 10. Create a base class Appliance with a method turn_on. 
# Create a subclass WashingMachine that overrides the turn_on method. 
class Appliance:
    def turn_on(self):
        return "Appliance is turned on"

class WashingMachine(Appliance):
    def __init__(self, model):
        self.model = model

    def turn_on(self):
        return f"Washing Machine {self.model} is turned on"


# Encapsulation

# 11. Create a class PrivateData with private attributes username
# and password. Implement methods to get and set these attributes.
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

# 12. Create a class Account with private attributes account_number
# and balance. Implement methods to deposit and withdraw money.
class Account:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


# Polymorphism

# 13. Create a function operate_vehicle that takes a vehicle object and calls its move method. 
# Create classes Car and Bike that implement move differently.
class Car:
    def __init__(self, model):
        self.model = model

    def move(self):
        return f"{self.model} is driving"

class Bike:
    def __init__(self, model):
        self.model = model

    def move(self):
        return f"{self.model} is riding"

# 14. Create a function operate_device that takes a device object and calls its operate method. 
# Create classes Laptop and Smartphone that implement operate differently.
class Laptop:
    def __init__(self, model):
        self.model = model

    def operate(self):
        return f"{self.model} is operating"

class Smartphone:
    def __init__(self, model):
        self.model = model

    def operate(self):
        return f"{self.model} is operating"


# Abstraction

# 15. Define an abstract class Transport with an abstract method travel. 
# Create subclasses Bus and Train that implement the travel method.
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
    
# 16. Define an abstract class Payment with an abstract methodprocess. 
# Create subclasses CreditCard and PayPal that implement the process method.
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