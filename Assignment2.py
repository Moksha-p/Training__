# Class Definition and Object Instantiation

# 1. Create a class Library with attributes like name, address, and a list of books. Implement methods to add and remove books.
class Library:
    def __init__(self, name, address, books=None):
        self.name = name
        self.address = address
        self.books = books if books else []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

# 2. Create a class House with attributes like address, num_rooms, and price. Implement a method to display the house details.
class House:
    def __init__(self, address, num_rooms, price):
        self.address = address
        self.num_rooms = num_rooms
        self.price = price

    def display_details(self):
        return f"address: {self.address}, num_rooms: {self.num_rooms}, price: {self.price}"

# Class Variables

# 5. Create a class School with a class variable total_students and instance variables name and students. 
# Implement a method to enroll students and update the total count.
# Class Variables
class School:
    total_students = 0

    def __init__(self, name, students):
        self.name = name
        self.students = students
        School.total_students += students

    def enroll_students(self, count):
        self.students += count
        School.total_students += count

# 6. Create a class Company with a class variable industry and instance variables name and num_employees. 
# Implement a method to update the number of employees.
class Company:
    industry = "Technology"

    def __init__(self, name, num_employees):
        self.name = name
        self.num_employees = num_employees

    def update_employees(self, new_count):
        self.num_employees = new_count