import json

class Product:
    def __init__(self, name, price, quantity):
        self._name = name  
        self._price = price  
        self._quantity = quantity  

    
    def name(self):
        return self._name

    
    def price(self):
        return self._price

    
    def quantity(self):
        return self._quantity
    
    def __repr__(self):
        return f"Product(name={self._name}, price={self._price}, quantity={self._quantity})"
    

def read_prod_frm_json(file_path):
    prod = []
    with open (file_path) as file:
        data = json.load(file)
        prod_data = Product(
            name = data['name'],
            price = data['price'],
            quantity = data['quantity']
        )
        prod.append(prod_data)
    return prod


file_path = "sample2.json"
products = read_prod_frm_json(file_path)
for product in products:
    print(product)

