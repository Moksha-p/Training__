import csv

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

employee_data = [["John Doe", "Manager", 75000], ["Jane Smith", "Engineer", 80000]]
employees = [Employee(name, position, salary) for name, position, salary in employee_data]

for employee in employees:
    print(f"Employee(name={employee.name}, position={employee.position}, salary={employee.salary})")
