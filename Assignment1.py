#Class Definition and Object Instantiation

# 1. Create a class to represent a Student with attributes like name, age, and grades.

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

# Example Test Case
student = Student("Alice", 20, [90, 85, 88])
print(f"name: {student.name}, age: {student.age}, grades: {student.grades}")

# 2. Given a CSV file with employee details (name, position, salary), create a class to represent an Employee.

import csv

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

def read_employees_from_csv(file_name):
    employees = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            employee = Employee(row[0], row[1], int(row[2]))
            employees.append(employee)
    return employees

# Example Test Case
csv_content = [["John Doe", "Manager", 75000], ["Jane Smith", "Engineer", 80000]]

# 3. Implement a program that simulates a basic bank account using a BankAccount class.

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

# Example Test Case
account = BankAccount("12345678", 1000)
print(f"account_number: {account.account_number}, balance: {account.balance}")

# 4. Write a Python program that uses a Rectangle class to calculate the area and perimeter of a rectangle.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Example Test Case
rect = Rectangle(5, 3)
print(f"area: {rect.area()}, perimeter: {rect.perimeter()}")

# 5. Create a class to represent a Car with attributes like make, model, and year.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Example Test Case
car = Car("Toyota", "Camry", 2020)
print(f"make: {car.make}, model: {car.model}, year: {car.year}")

# 6. Given a JSON file with customer data, create a Customer class to store and manipulate the data.

import json

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

def read_customer_from_json(json_content):
    data = json.loads(json_content)
    return Customer(data["name"], data["email"])

# Example Test Case
json_content = '{"name": "John Doe", "email": "john.doe@example.com"}'
customer = read_customer_from_json(json_content)
print(f"name: {customer.name}, email: {customer.email}")

# 7. Write a program that uses a Person class to keep track of a person's name, age, and address.

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

# Example Test Case
person = Person("John Doe", 30, "123 Main St")
print(f"name: {person.name}, age: {person.age}, address: {person.address}")

# 8. Implement a program that uses a Circle class to calculate the area and circumference of multiple circles.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

# Example Test Case
circle = Circle(4)
print(f"area: {circle.area():.2f}, circumference: {circle.circumference():.2f}")

# 9. Given a CSV file with product details (name, price, quantity), create a Product class to manage the data.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

def read_products_from_csv(file_name):
    products = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            product = Product(row[0], float(row[1]), int(row[2]))
            products.append(product)
    return products

# Example Test Case
csv_content = [["Laptop", 1000, 5], ["Phone", 500, 10]]

# 10. Create a class to represent a Movie with attributes like title, director, and rating.

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

# Example Test Case
movie = Movie("Inception", "Christopher Nolan", 8.8)
print(f"title: {movie.title}, director: {movie.director}, rating: {movie.rating}")
