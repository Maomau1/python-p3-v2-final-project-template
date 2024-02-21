#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.brand import Brand
from models.product import Product
from prettytable import PrettyTable

def reset_database():
    Product.drop_table()
    Brand.drop_table()
    Product.create_table()
    Brand.create_table()

    # Create seed data
    sabi = Brand.create("sabi", "essentialsabi.com")
    l_occitane = Brand.create("L'occitane", "loccitane.com")
    # ------
    Product.create("naked", "body butter.",3, 13,sabi.id)
    Product.create("bum bum", "body cream", 4, 20, l_occitane.id)

reset_database()

ipdb.set_trace()
