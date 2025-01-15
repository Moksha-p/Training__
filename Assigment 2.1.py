# Class Definition and Object Instantiation 

# 1 Create a class Library with attributes like name, address, and a list of books. Implement methods to add and remove books.
class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def __str__(self):
        return f"name: {self.name}, address: {self.address}, books: {self.books}"

# Example Test Case
library = Library("City Library", "123 Main St")
library.add_book("Book1")
library.add_book("Book2")
library.remove_book("Book1")
print(library)

#2 Create a class House with attributes like address, num_rooms, and price. Implement a method to display the house details.
class House:
    def __init__(self, address, num_rooms, price):
        self.address = address
        self.num_rooms = num_rooms
        self.price = price

    def display_details(self):
        return f"address: {self.address}, num_rooms: {self.num_rooms}, price: {self.price}"

# Example Test Case
house = House("456 Elm St", 4, 350000)
print(house.display_details())


# Class Variables
# 5  Create a class School with a class variable total_students andinstance variables name and students. Implement a method to enroll students and update the total count.
class School:
    total_students = 0  # Class variable to keep track of total students across all schools

    def __init__(self, name, students):
        self.name = name
        self.students = students
        School.total_students += students

    def enroll_students(self, new_students):
        self.students += new_students
        School.total_students += new_students

    def __str__(self):
        return f"name: {self.name}, students: {self.students}, total_students: {School.total_students}"

# Example Test Case
school = School("Greenwood High", 300)
school.enroll_students(50)
print(school)

# 6. Create a class Company with a class variable industry an instance variables name and num_employees. Implement a method to update the number of employees.
class Company:
    industry = "Technology"  # Class variable representing the industry for all companies

    def __init__(self, name, num_employees):
        self.name = name
        self.num_employees = num_employees

    def update_employees(self, new_count):
        self.num_employees = new_count

    def __str__(self):
        return f"name: {self.name}, num_employees: {self.num_employees}, industry: {Company.industry}"

# Example Test Case
company = Company("TechCorp", 200)
company.update_employees(220)
print(company)

