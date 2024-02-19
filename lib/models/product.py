# lib/models/product.py 
from models.__init__ import CONN, CURSOR
from models.brand import Brand

class Product:

    all=[]

    def __init__(self, name, description, quantity, price, brand_id, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
        self.brand_id = brand_id

    def __repr__(self) -> str:
        return (f'Product: {self.name}, quantity: {self.quantity}')
    
    @classmethod
    def create_table(cls):
        """create a products table"""
        sql = """
            CREATE TABLE IF NOT EXIST products(
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            quantity INTEGER,
            price INTEGER,
            brand_id INTEGER,
            FOREIGN KEY (brand_id) REFERENCES brands (id)) 
        """
        CURSOR.execute(sql,)
        CONN.commit()

    
