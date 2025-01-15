class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def discount(self, discount_rate):
        self.price -= self.price * discount_rate

book = Book("Python 101", "John Doe", 29.99)
book.discount(0.1)
print(f"title: {book.title}, author: {book.author}, price: {book.price}")