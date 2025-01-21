from sqlalchemy import create_engine, Column, Integer, String, Float, func
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the database URL for PostgreSQL
DATABASE_URL = "postgresql+psycopg2://postgres:pawanjoshi123@localhost:5433/postgres"

# Create the engine and Base
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

# Define the Products table
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Float, nullable=False)

# Create the table in the PostgreSQL database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert sample data
products_data = [
    {"name": "Laptop", "category": "Electronics", "price": 1000},
    {"name": "Smartphone", "category": "Electronics", "price": 700},
    {"name": "Table", "category": "Furniture", "price": 150},
    {"name": "Chair", "category": "Furniture", "price": 85},
]

# Check if the table is empty, then insert sample data
if not session.query(Product).first():
    session.bulk_insert_mappings(Product, products_data)
    session.commit()

# Queries

# Query 1: Retrieve all products in 'Electronics' category
electronics_products = session.query(Product).filter(Product.category == "Electronics").all()
print("Query 1: Products in 'Electronics' category:")
for product in electronics_products:
    print((product.name, product.category, product.price))

# Query 2: Retrieve products with price > 500
expensive_products = session.query(Product).filter(Product.price > 500).all()
print("\nQuery 2: Products with price > 500:")
for product in expensive_products:
    print((product.name, product.category, product.price))

# Query 3: Retrieve average price of products in each category
average_prices = session.query(Product.category, func.avg(Product.price)).group_by(Product.category).all()
print("\nQuery 3: Average price of products in each category:")
for category, avg_price in average_prices:
    print((category, round(avg_price, 2)))

# Close the session
session.close()
