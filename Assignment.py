#Student Class

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def __repr__(self):
        return f'name: "{self.name}", age: {self.age}, grades: {self.grades}'

# Test case
student = Student(name="Alice", age=20, grades=[90, 85, 88])
print(student)

#Employee Class (from CSV file)

import csv

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f'Employee(name="{self.name}", position="{self.position}", salary={self.salary})'

# Test case (CSV parsing)
employee_data = [["John Doe", "Manager", 75000], ["Jane Smith", "Engineer", 80000]]
employees = [Employee(name=row[0], position=row[1], salary=row[2]) for row in employee_data]
for emp in employees:
    print(emp)

#BankAccount Class
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def __repr__(self):
        return f'account_number: "{self.account_number}", balance: {self.balance}'

# Test case
account = BankAccount(account_number="12345678", balance=1000)
print(account)


#Rectangle Class

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Test case
rect = Rectangle(length=5, width=3)
print(f'area: {rect.area()}, perimeter: {rect.perimeter()}')

#Car Class

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self):
        return f'make: "{self.make}", model: "{self.model}", year: {self.year}'

# Test case
car = Car(make="Toyota", model="Camry", year=2020)
print(car)


#Customer Class (from JSON file)

import json

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'Customer(name="{self.name}", email="{self.email}")'

# Test case (JSON parsing)
customer_data = '{"name": "John Doe", "email": "john.doe@example.com"}'
customer_dict = json.loads(customer_data)
customer = Customer(name=customer_dict['name'], email=customer_dict['email'])
print(customer)


#Person Class
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self):
        return f'name: "{self.name}", age: {self.age}, address: "{self.address}"'

# Test case
person = Person(name="John Doe", age=30, address="123 Main St")
print(person)


#Circle Class

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

# Test case
circle = Circle(radius=4)
print(f'area: {circle.area():.2f}, circumference: {circle.circumference():.2f}')


#Product Class (from CSV file)
import csv

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'Product(name="{self.name}", price={self.price}, quantity={self.quantity})'

# Test case (CSV parsing)
product_data = [["Laptop", 1000, 5], ["Phone", 500, 10]]
products = [Product(name=row[0], price=row[1], quantity=row[2]) for row in product_data]
for prod in products:
    print(prod)


#Movie Class
class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def __repr__(self):
        return f'title: "{self.title}", director: "{self.director}", rating: {self.rating}'

# Test case
movie = Movie(title="Inception", director="Christopher Nolan", rating=8.8)
print(movie)


#Class Hierarchies and Inheritance

#Shape Class with Circle and Square
import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius



class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Test case
circle = Circle(radius=4)
square = Square(side=5)

print(f"Circle area: {circle.area():.2f}, Circle perimeter: {circle.perimeter():.2f}")
print(f"Square area: {square.area()}, Square perimeter: {square.perimeter()}")

#Employee Class Hierarchy


class Employee:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.name}'


class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def __repr__(self):
        return f'Manager: {self.name}, Department: {self.department}'


class Engineer(Employee):
    def __init__(self, name, field):
        super().__init__(name)
        self.field = field

    def __repr__(self):
        return f'Engineer: {self.name}, Field: {self.field}'

# Test case
manager = Manager(name="John Doe", department="Sales")
engineer = Engineer(name="Jane Smith", field="Software")

print(manager)
print(engineer)

#Inheritance for Shapes (Triangle, Rectangle)

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Test case
triangle = Triangle(base=5, height=3)
rectangle = Rectangle(length=4, width=2)

print(f"Triangle area: {triangle.area()}, Rectangle area: {rectangle.area()}")

#Animal Class Hierarchy (Bird, Fish)


class Animal:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.name}'


class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

    def __repr__(self):
        return f'Bird: {self.name}, Can Fly: {self.can_fly}'


class Fish(Animal):
    def __init__(self, name, can_swim):
        super().__init__(name)
        self.can_swim = can_swim

    def __repr__(self):
        return f'Fish: {self.name}, Can Swim: {self.can_swim}'

# Test case
bird = Bird(name="Parrot", can_fly=True)
fish = Fish(name="Goldfish", can_swim=True)

print(bird)
print(fish)

#Product Class with Encapsulation (from JSON)
import json

class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    def __repr__(self):
        return f'Product(name="{self.name}", price={self.price}, quantity={self.quantity})'

# Test case (JSON parsing)
product_data = '{"name": "Laptop", "price": 1000, "quantity": 5}'
product_dict = json.loads(product_data)
product = Product(name=product_dict['name'], price=product_dict['price'], quantity=product_dict['quantity'])
print(product)


#Vehicle Class Hierarchy (Car, Bike)

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.make} {self.model}'


class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)


class Bike(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

# Test case
car = Car(make="Toyota", model="Camry")
bike = Bike(make="Yamaha", model="MT-07")

print(car)
print(bike)

#User Class with Encapsulation

class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password  # Encapsulated password

    @property
    def password(self):
        return "******"  # Hide the password

    def __repr__(self):
        return f'username: "{self.username}", password: "{self.password}"'

# Test case
user = User(username="john_doe", password="secure123")
print(user)


#Inheritance

#Employee Class with Developer Subclass

# Base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f'name: "{self.name}", salary: {self.salary}'

# Subclass Developer
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def __repr__(self):
        return f'name: "{self.name}", salary: {self.salary}, programming_language: "{self.programming_language}"'

# Test case
developer = Developer(name="Alice", salary=70000, programming_language="Python")
print(developer)

#Appliance Class with WashingMachine Subclass

# Base class
class Appliance:
    def turn_on(self):
        return "Appliance is turned on"

# Subclass WashingMachine
class WashingMachine(Appliance):
    def __init__(self, model):
        self.model = model

    def turn_on(self):
        return f"Washing Machine {self.model} is turned on"

# Test case
appliance = Appliance()
washing_machine = WashingMachine(model="LG")

print(appliance.turn_on())
print(washing_machine.turn_on())


#Encapsulation
#PrivateData Class with Getters and Setters
class PrivateData:
    def __init__(self, username, password):
        self.__username = username  # Private attribute
        self.__password = password  # Private attribute

    # Getter for username
    def get_username(self):
        return self.__username

    # Getter for password
    def get_password(self):
        return self.__password

    # Setter for password
    def set_password(self, new_password):
        self.__password = new_password

# Test case
private_data = PrivateData(username="user1", password="pass123")
print(f'username: "{private_data.get_username()}", password: "{private_data.get_password()}"')

# Updating the password using setter
private_data.set_password("newpass123")
print(f'username: "{private_data.get_username()}", password: "{private_data.get_password()}"')


#Account Class with Deposit and Withdraw Methods
class Account:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount.")

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Getter for account_number (optional, as account_number is typically sensitive)
    def get_account_number(self):
        return self.__account_number

# Test case
account = Account(account_number="987654321", balance=5000)

print(f'account_number: "{account.get_account_number()}", balance: {account.get_balance()}')

# Deposit and withdraw
account.deposit(1500)
account.withdraw(2000)

print(f'account_number: "{account.get_account_number()}", balance: {account.get_balance()}')


#Polymorphism

#operate_vehicle Function with Car and Bike Classes
# Base class for vehicles
class Vehicle:
    def __init__(self, model):
        self.model = model

    def move(self):
        raise NotImplementedError("Subclass must implement this method")

# Subclass Car
class Car(Vehicle):
    def move(self):
        return f"{self.model} is driving"

# Subclass Bike
class Bike(Vehicle):
    def move(self):
        return f"{self.model} is riding"

# Function to operate the vehicle
def operate_vehicle(vehicle):
    return vehicle.move()

# Test case
car = Car(model="Toyota")
bike = Bike(model="Yamaha")

print(operate_vehicle(car))  # Output: "Toyota is driving"
print(operate_vehicle(bike))  # Output: "Yamaha is riding"



#operate_device Function with Laptop and Smartphone Classes
# Base class for devices
class Device:
    def __init__(self, model):
        self.model = model

    def operate(self):
        raise NotImplementedError("Subclass must implement this method")

# Subclass Laptop
class Laptop(Device):
    def operate(self):
        return f"{self.model} is operating"

# Subclass Smartphone
class Smartphone(Device):
    def operate(self):
        return f"{self.model} is operating"

# Function to operate the device
def operate_device(device):
    return device.operate()

# Test case
laptop = Laptop(model="Dell")
smartphone = Smartphone(model="iPhone")

print(operate_device(laptop))  # Output: "Dell is operating"
print(operate_device(smartphone))  # Output: "iPhone is operating"


#Abstraction

#Abstract Class Transport with Bus and Train Subclasses
from abc import ABC, abstractmethod

# Abstract class Transport
class Transport(ABC):
    @abstractmethod
    def travel(self):
        pass

# Subclass Bus
class Bus(Transport):
    def __init__(self, route):
        self.route = route

    def travel(self):
        return f"Bus {self.route} is traveling"

# Subclass Train
class Train(Transport):
    def __init__(self, route):
        self.route = route

    def travel(self):
        return f"Train {self.route} is traveling"

# Test case
bus = Bus(route="10A")
train = Train(route="Express")

print(bus.travel())  # Output: "Bus 10A is traveling"
print(train.travel())  # Output: "Train Express is traveling"


#Abstract Class Payment with CreditCard and PayPal Subclasses
from abc import ABC, abstractmethod

# Abstract class Payment
class Payment(ABC):
    @abstractmethod
    def process(self):
        pass

# Subclass CreditCard
class CreditCard(Payment):
    def __init__(self, number):
        self.number = number

    def process(self):
        return f"Processing credit card payment for {self.number}"

# Subclass PayPal
class PayPal(Payment):
    def __init__(self, account):
        self.account = account

    def process(self):
        return f"Processing PayPal payment for {self.account}"

# Test case
credit_card = CreditCard(number="1234")
paypal = PayPal(account="user@example.com")

print(credit_card.process())  # Output: "Processing credit card payment for 1234"
print(paypal.process())  # Output: "Processing PayPal payment for user@example.com"












