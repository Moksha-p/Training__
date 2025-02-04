class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

person = Person("John Doe", 30, "123 Main St")
print(f"name: {person.name}, age: {person.age}, address: {person.address}")
