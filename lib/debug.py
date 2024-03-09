#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.brand import Brand
from models.product import Product
from prettytable import PrettyTable

def reset_database():
    Product.drop_table()
    Brand.drop_table()
    Product.create_table()
    Brand.create_table()

# reset_database()

breakpoint()
