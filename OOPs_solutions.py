class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name, "Manager", 0)
        self.department = department

class Engineer(Employee):
    def __init__(self, name, field):
        super().__init__(name, "Engineer", 0)
        self.field = field

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

class Bike(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def get_password(self):
        return "******"
