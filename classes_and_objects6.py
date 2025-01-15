import json

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

customer_data = '{"name": "John Doe", "email": "john.doe@example.com"}' #json : key-value pairs
customer_info = json.loads(customer_data)
customer = Customer(customer_info['name'], customer_info['email'])

print("Customer name:", customer.name, "\n","Customer email:", customer.email)
