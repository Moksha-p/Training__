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

manager = Manager("John Doe", "Sales")
engineer = Engineer("Jane Smith", "Software")

print(manager)
print(engineer)
