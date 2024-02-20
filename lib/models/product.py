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
        """create a products table to persist the attributes of Product instances"""
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

    def save(self):
        """save the attribute of a product instance"""
        sql = """
            INSERT INTO products(name, description, quantity, price, brand_id)
            VALUES(?,?,?,?,?)
        """
        CURSOR.execute(sql,(self.name, self.description, self.quantity, self.price, self.brand_id))
        CONN.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, description, quantity, price, brand_id):
        """Initialize a product instance and saves it to the products table"""
        product = cls(name,description,quantity, price, brand_id)
        product.save()
        return product
