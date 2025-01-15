import csv
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name = {self.name} , Price: {self.price} , Quantity: {self.quantity})"
    
def read_frm_csv(file_path):
    lst = []
    with open(file_path) as f:
        csv_reader = csv.DictReader(f)

        for row in csv_reader:
            prod = Product(
                name = row['name'],
                price = row['price'],
                quantity = row['quantity']
            )
            lst.append(prod)
    return lst



file_path = "prod_detail.csv"
prod_detail = read_frm_csv(file_path)
for prod in prod_detail:
    print(prod)

