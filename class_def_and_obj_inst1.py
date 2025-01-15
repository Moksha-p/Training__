class Library:
    def __init__(self, name, address, books=None):
        self.name = name
        self.address = address
        self.books = books if books is not None else []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

library = Library("City Library", "123 Main St")
library.add_book("Book1")
library.add_book("Book2")
library.remove_book("Book1")

print(f"name: {library.name}, address: {library.address}, books: {library.books}")
