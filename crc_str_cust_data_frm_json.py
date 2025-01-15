import json
class Customer:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Customer(Name = {self.name} , Email = {self.email})"
    

def read_cust_frm_json(file_path):
    cust = []
    with open (file_path) as file:
        data = json.load(file)
        cust_data = Customer(
            name = data['name'],
            email = data['email']
        )
        cust.append(cust_data)
    return cust


file_path = "sample1.json"
customers = read_cust_frm_json(file_path)
for customer in customers:
    print(customer)

