class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

product_data = [["Laptop", 1000, 5], ["Phone", 500, 10]]
products = [Product(name, price, quantity) for name, price, quantity in product_data]

for product in products:
    print(f"Product(name={product.name}, price={product.price}, quantity={product.quantity})")
