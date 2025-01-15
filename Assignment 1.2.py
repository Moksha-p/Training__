# Class Hierarchies and Inheritance

# 1. Create a base class Shape with methods to calculate area and perimeter, and derive classes Circle and Square.
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Example Test Case
circle = Circle(4)
square = Square(5)
print(f"Circle area: {circle.area()}, Circle perimeter: {circle.perimeter()}")
print(f"Square area: {square.area()}, Square perimeter: {square.perimeter()}")

# 2 Implement a class hierarchy to represent different types of employees (Manager, Engineer) with their attributes.
class Employee:
    def __init__(self, name):
        self.name = name

class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def __str__(self):
        return f"Manager: {self.name}, Department: {self.department}"

class Engineer(Employee):
    def __init__(self, name, field):
        super().__init__(name)
        self.field = field

    def __str__(self):
        return f"Engineer: {self.name}, Field: {self.field}"

# Example Test Case
manager = Manager("John Doe", "Sales")
engineer = Engineer("Jane Smith", "Software")
print(manager)
print(engineer)

# 3 Write a Python program that uses inheritance to represent a hierarchy of shapes (Triangle, Rectangle, etc.).
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

# Example Test Case
triangle = Triangle(5, 3)
rectangle = Rectangle(4, 2)
print(f"Triangle area: {triangle.area()}")
print(f"Rectangle area: {rectangle.area()}")

#4 Create a class hierarchy to represent different types of animals (Bird, Fish) with their own attributes and methods.
class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

    def __str__(self):
        return f"Bird: {self.name}, Can Fly: {self.can_fly}"

class Fish(Animal):
    def __init__(self, name, can_swim):
        super().__init__(name)
        self.can_swim = can_swim

    def __str__(self):
        return f"Fish: {self.name}, Can Swim: {self.can_swim}"

# Example Test Case
bird = Bird("Parrot", True)
fish = Fish("Goldfish", True)
print(bird)
print(fish)

#5 Given a JSON file with product details (name, price, quantity), create a Product class with encapsulated attributes.
class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def __str__(self):
        return f"Product(name={self.__name}, price={self.__price}, quantity={self.__quantity})"

# Example Test Case
product = Product("Laptop", 1000, 5)
print(product)

#6 Implement a program that uses inheritance to represent a hierarchy of vehicles (Car, Bike, Truck, etc.).
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

# Example Test Case
car = Car("Toyota", "Camry")
bike = Bike("Yamaha", "MT-07")
print(f"Car: {car}")
print(f"Bike: {bike}")

#7 Write a Python program that uses encapsulation to protect sensitive information in a User class.
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def set_password(self, new_password):
        self.__password = new_password

    def get_password(self):
        return "*" * len(self.__password)

# Example Test Case
user = User("john_doe", "secure123")
print(f"Username: {user.get_username()}")
print(f"Password: {user.get_password()}")  # Masked password
user.set_password("newsecure123")
print(f"Updated Password: {user.get_password()}")  # Updated and masked password
