from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'  
    
    id = Column(Integer, primary_key=True, autoincrement=True) 
    name = Column(String, nullable=False)  
    category = Column(String, nullable=False)  
    price = Column(Float, nullable=False)  

DATABASE_URL = "postgresql://postgres:Shilpkar09@localhost:5432/Demo"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
products_data = [
    {'name': 'Laptop', 'category': 'Electronics', 'price': 1000},
    {'name': 'Smartphone', 'category': 'Electronics', 'price': 700},
    {'name': 'Table', 'category': 'Furniture', 'price': 150},
    {'name': 'Chair', 'category': 'Furniture', 'price': 85}
]
for data in products_data:
    product = Product(**data)
    session.add(product)

session.commit()  


def get_products_by_category(category):
    products = session.query(Product.name, Product.category, Product.price).filter(Product.category == category).all()
    return products

electronics_products = get_products_by_category('Electronics')
print("Electronics Products:", electronics_products)

def get_products_above_price(threshold):
    products = session.query(Product.name, Product.category, Product.price).filter(Product.price > threshold).all()
    return products

expensive_products = get_products_above_price(500)
print("Products with price > 500:", expensive_products)

from sqlalchemy import func

def get_average_price_by_category():
    avg_prices = session.query(Product.category, func.avg(Product.price)).group_by(Product.category).all()
    return avg_prices

avg_prices = get_average_price_by_category()
print("Average Prices by Category:", avg_prices)

