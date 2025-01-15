class House:
    def __init__(self, address, num_rooms, price):
        self.address = address
        self.num_rooms = num_rooms
        self.price = price

    def display_details(self):
        print(f"address: {self.address}, num_rooms: {self.num_rooms}, price: {self.price}")

house = House("456 Elm St", 4, 350000)
house.display_details()