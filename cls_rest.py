class Restaurant:
    def __init__(self, name, cuisine_type, rating):
        self.name = name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def update_rating(self, new_rating):
        self.rating = new_rating

restaurant = Restaurant("Sushi Place", "Japanese", 4.5)
restaurant.update_rating(4.8)
print(f"name: {restaurant.name}, cuisine_type: {restaurant.cuisine_type}, rating: {restaurant.rating}")