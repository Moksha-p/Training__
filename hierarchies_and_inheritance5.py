import json

class Product:
    def __init__(self, name, price, quantity):
        self._name = name  
        self._price = price  
        self._quantity = quantity  

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

product_data = '{"name": "Laptop", "price": 1000, "quantity": 5}'
product_info = json.loads(product_data)
product = Product(product_info['name'], product_info['price'], product_info['quantity'])

print(f"Product(name={product.name}, price={product.price}, quantity={product.quantity})")
