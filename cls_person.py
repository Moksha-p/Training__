class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self):
        return f"Name: {self.name} , Age: {self.age} , Address: {self.address}"
    


t1 =Person( name = "John Doe", age = 30, address = "123 Main St")
print(t1)