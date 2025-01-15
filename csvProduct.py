import csv
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
product_data = [["Laptop", 1000, 5], ["Phone", "500", 10]]
products = [Product(name, price, quantity) for name, price, quantity in product_data]
for p in products:
    print(f"Product(name={p.name}, price={p.price}, quantity={p.quantity})")