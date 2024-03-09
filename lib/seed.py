from models.brand import Brand
from models.product import Product

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

print("seeded")