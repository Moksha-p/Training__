from sqlalchemy import create_engine, Column, Integer, String, Float, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
import time
from functools import lru_cache

# Define the database engine and session
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()

# Define the Base class
Base = declarative_base()

# Task 1: Define the Products table
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Float, nullable=False)

# Create the table
Base.metadata.create_all(engine)

# Insert sample data
products_data = [
    {'name': 'Laptop', 'category': 'Electronics', 'price': 1000},
    {'name': 'Smartphone', 'category': 'Electronics', 'price': 700},
    {'name': 'Table', 'category': 'Furniture', 'price': 150},
    {'name': 'Chair', 'category': 'Furniture', 'price': 85},
]

# Add data to the session
for product in products_data:
    session.add(Product(**product))
session.commit()

# Task 2: Caching with functools.lru_cache
@lru_cache(maxsize=128)
def get_product_by_id(product_id):
    time.sleep(2)  # Simulate a slow query
    product = session.query(Product).filter(Product.id == product_id).first()
    if product:
        return product.id, product.name, product.category, product.price
    return None

# Task 3: Define Authors and Books tables for one-to-many relationship
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    books = relationship('Book', backref=backref('author', lazy=True))

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)

# Create tables
Base.metadata.create_all(engine)

# Insert sample data for authors and books
authors_data = [{'name': 'J.K. Rowling'}, {'name': 'George R.R. Martin'}]
books_data = [
    {'title': "Harry Potter and the Philosopher's Stone", 'author_id': 1},
    {'title': "Harry Potter and the Chamber of Secrets", 'author_id': 1},
    {'title': "A Game of Thrones", 'author_id': 2},
    {'title': "A Clash of Kings", 'author_id': 2},
]

for author in authors_data:
    session.add(Author(**author))
for book in books_data:
    session.add(Book(**book))
session.commit()

# Task 4: Complex Query to Retrieve Top 3 Expensive Products Per Category
@lru_cache(maxsize=128)
def get_top_3_expensive_products_per_category():
    result = (
        session.query(Product.category, Product.name, Product.price)
        .order_by(Product.category, Product.price.desc())
        .all()
    )
    top_3_per_category = {}
    for category, name, price in result:
        if category not in top_3_per_category:
            top_3_per_category[category] = []
        if len(top_3_per_category[category]) < 3:
            top_3_per_category[category].append((name, price))
    return top_3_per_category

# Task 5: Implementing Soft Deletes for Users
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    is_deleted = Column(Integer, default=0)  # 0: Not Deleted, 1: Deleted

# Create Users table
Base.metadata.create_all(engine)

# Insert sample data for users
users_data = [
    {'name': 'Alice', 'age': 31, 'is_deleted': 0},
    {'name': 'Bob', 'age': 40, 'is_deleted': 0}
]

for user in users_data:
    session.add(User(**user))
session.commit()

# Soft delete a user
user_to_delete = session.query(User).filter(User.id == 2).first()
if user_to_delete:
    user_to_delete.is_deleted = 1
    session.commit()

@lru_cache(maxsize=128)
def get_user_by_id(user_id):
    user = session.query(User).filter(User.id == user_id, User.is_deleted == 0).first()
    if user:
        return user.id, user.name, user.age
    return None

# Test caching and functionalities
if __name__ == "__main__":
    # Task 2: Test caching for products
    start_time = time.time()
    print("First call:", get_product_by_id(1))
    print("Time taken for first call:", time.time() - start_time, "seconds")

    start_time = time.time()
    print("Second call:", get_product_by_id(1))
    print("Time taken for second call:", time.time() - start_time, "seconds")

    print("Cache Info for Products:", get_product_by_id.cache_info())

    # Task 3: Query authors and their books
    jk_rowling_books = session.query(Book.title).join(Author).filter(Author.name == 'J.K. Rowling').all()
    print("Books by J.K. Rowling:", jk_rowling_books)

    george_rr_martin_books = session.query(Author.name, Book.title).join(Book).filter(Author.name == 'George R.R. Martin').all()
    print("George R.R. Martin and their books:", george_rr_martin_books)

    # Task 4: Test top 3 expensive products per category
    print("Top 3 expensive products per category:", get_top_3_expensive_products_per_category())
    print("Cache Info for Expensive Products Query:", get_top_3_expensive_products_per_category.cache_info())

    # Task 5: Test soft delete for users
    print("Retrieve user by id 2 (should be None):", get_user_by_id(2))
    print("Retrieve user by id 1 (should return Alice):", get_user_by_id(1))
    print("Cache Info for Users:", get_user_by_id.cache_info())
