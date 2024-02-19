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
    
    