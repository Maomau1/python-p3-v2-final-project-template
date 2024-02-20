# lib/helpers.py
from models.brand import Brand
from models.product import Product

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

# implement brand functions

# create brands table
def initiate_brands():
    Brand.create_table()

# create products table
def initiate_products():
    Product.create_table()
    
#list brands
def list_brands():
    brands = Brand.get_all()
    if brands == []:
        print("No brand entered yet. use menu below to register a brand")
    else :
        for brand in brands:
            print(brand)

# create brand
def add_brand():
    name = input("enter brand's name: ")
    description = input("enter brand's website: ")
    brand = Brand.create(name, description)
    print(f'{brand.name} successfully added')

# update brand
def update_brand():
    name = input("enter name of brand to updated: ")
    if brand := Brand.find_by_name(name):
        try:
           name = input("enter updated name: ")
           brand.name = name
           description = input("enter updated website: ")
           brand.description = description
           brand.update()
           print(f'Brand: {brand.name} succesfully updated')
        except Exception as exc:
            print("Error updating brand: ",exc) 
    else: 
        print(f'brand: {name} not found')

# delete brand
def delete_brand():
    name = input("enter name of brand to be deleted: ")
    if brand := Brand.find_by_name(name):
        brand.delete()
        print(f'brand: {brand.name} successfully deleted!')
    else: 
        print(f'brand: {brand.name} not found!')

# view brand
def name_query(item):
    name = input(f'enter {item} name: ')
    return name

# show brand products
def brand_products(name):
    brand = Brand.find_by_name(name)
    products = brand.products()
    # breakpoint()
    if products == []:
        print(f'No products to display!')
    else:
        for product in products:
            print(f'{product}')

    
# add product
def add_product():
    name = input("enter product name: ")
    description = input("enter product description: ")
    quantity = int(input("enter product quantity: "))
    price = int(input("enter product price: $"))
    brand = input("enter product brand: ")
    try:
        brand_id = Brand.find_by_name(brand).id
    except Exception as exc:
        print("error obtaining brand",exc)
    try:
        product = Product.create(name, description,quantity, price, brand_id)
        # breakpoint()
        print(f'product: {product.name} successfully added')
    except Exception as exc:
        print("error generating product",exc)

def delete_product():
    name = name_query("product")
    if product := Product.find_by_name(name):
        product.delete()
    else:
        print(f'product: {name} not found!') 

def update_product():
    name = name_query("product")
    if product := Product.find_by_name(name):
        name = input("enter updated product name: ")
        product.name = name
        description = input("enter updated product description: ")
        product.description = description
        quantity = input("enter updated product quantity: ")
        product.quantity = quantity
        price = input("enter updated product price: $")
        product.price = price
        brand_id = input("enter updated product brand: ")
        product.brand_id = Product.find_by_name(brand_id).id
        product.update()
        print(f'product {product.name} updated successfully')
    else:
        print(f'product {name} can\'t be found!')

def view_product_details():
    name = name_query("product")
    if product := Product.find_by_name(name):
        print(f'**********{product.name}**********\n',
                f'- name: {product.name}\n',
                f'- description: {product.description}\n',
                f'- quantity: {product.quantity}\n',
                f'- price: ${product.price}\n',
                f'- brand: {Brand.find_by_id(product.brand_id).name}\n'
                )
    else:
        print("product not found")

