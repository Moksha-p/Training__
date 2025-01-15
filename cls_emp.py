class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

developer = Developer("Alice", 70000, "Python")
print(f"name: {developer.name}, salary: {developer.salary}, programming_language: {developer.programming_language}")