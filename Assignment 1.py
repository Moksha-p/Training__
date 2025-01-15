# Class Definition and Object Instantiation

#1.Create a class to represent a Student with attributes like name, age, and grades.
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def __str__(self):
        return f"name: {self.name}, age: {self.age}, grades: {self.grades}"

# Example Test Case
student = Student("Alice", 20, [90, 85, 88])
print(student)

#2 Given a CSV file with employee details (name, position, salary), create a class to represent an Employee.
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"Employee(name={self.name}, position={self.position}, salary={self.salary})"

# Example Test Case
employees = [
    Employee("John Doe", "Manager", 75000),
    Employee("Jane Smith", "Engineer", 80000)
]
for emp in employees:
    print(emp)

#3 Implement a program that simulates a basic bank account using a BankAccount class.
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
    
    def __str__(self):
        return f"account_number: {self.account_number}, balance: {self.balance}"

# Example Test Case
account = BankAccount("12345678", 1000)
print(account)

#4 Write a Python program that uses a Rectangle class to calculate the area and perimeter of a rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Example Test Case
rectangle = Rectangle(5, 3)
print(f"area: {rectangle.area()}, perimeter: {rectangle.perimeter()}")

#5 Create a class to represent a Car with attributes like make, model, and year.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def __str__(self):
        return f"make: {self.make}, model: {self.model}, year: {self.year}"

# Example Test Case
car = Car("Toyota", "Camry", 2020)
print(car)

#6 Given a JSON file with customer data, create a Customer class to store and manipulate the data.
import json

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Customer(name={self.name}, email={self.email})"

# Example Test Case
json_data = '{"name": "John Doe", "email": "john.doe@example.com"}'
customer_dict = json.loads(json_data)
customer = Customer(customer_dict["name"], customer_dict["email"])
print(customer)

#7 Write a program that uses a Person class to keep track of a person's name, age, and address.
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def __str__(self):
        return f"name: {self.name}, age: {self.age}, address: {self.address}"

# Example Test Case
person = Person("John Doe", 30, "123 Main St")
print(person)

#8 Implement a program that uses a Circle class to calculate the area and circumference of multiple circles.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return round(math.pi * self.radius ** 2, 2)
    
    def circumference(self):
        return round(2 * math.pi * self.radius, 2)

# Example Test Case
circle = Circle(4)
print(f"area: {circle.area()}, circumference: {circle.circumference()}")

#9 Given a CSV file with product details (name, price, quantity), create a Product class to manage the data.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

# Example Test Case
products_data = [
    ["Laptop", 1000, 5],
    ["Phone", 500, 10]
]

products = [Product(name, price, quantity) for name, price, quantity in products_data]
for product in products:
    print(product)

#10 Create a class to represent a Movie with attributes like title, director, and rating.
class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating
    
    def __str__(self):
        return f"title: {self.title}, director: {self.director}, rating: {self.rating}"

# Example Test Case
movie = Movie("Inception", "Christopher Nolan", 8.8)
print(movie)

