# lib/helpers.py
from models.brand import Brand
from models.product import Product
from prettytable import PrettyTable
import os

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def clear_input_area():
    # Clear the input area in the CLI
    os.system('cls' if os.name == 'nt' else 'clear')
    

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
            print(f'{brands.index(brand)+1}. {brand.name}')

# create brand
def add_brand():
    name = input("enter brand's name: ")
    description = input("enter brand's website: ")
    if brand := Brand.create(name, description):
        print(f'{brand.name} successfully added')
    else:
        print("brand does not exist")

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
    number = item_query("brand")
    brand = brand_instance(number)
    brand.delete()    

# get brand instance
def brand_instance(number):
    index = number -1
    brand = Brand.get_all()[index]
    # breakpoint()
    return brand

#get product instance
def product_instance(number,brand):
    index = number - 1
    product = brand.products()[index]
    return product

# view brand number
def item_query(item):
    if item == "brand":
            number = int(input(f'enter {item} number: '))
            while number > len(Brand.get_all()): 
                print("incorrect number, please try again")
                number = int(input(f'enter {item} number: '))
            return number
            

# show brand products
def brand_products(number):
    # breakpoint()
    brand = brand_instance(number)
    products = brand.products()
    # breakpoint()
    if products == []:
        print(f'No products to display!')
    else:
        for product in products:
            print(f'{products.index(product)+1}. {product.name}')

    
# add product
def add_product(brand):
    name = input("enter product name: ")
    description = input("enter product description: ")
    quantity = int(input("enter product quantity: "))
    price = int(input("enter product price: $"))
    brand_id = brand.id
    product = Product.create(name, description,quantity, price, brand_id)
    # breakpoint()
    print(f'product: {product.name} successfully added')

def delete_product(brand):
    number = item_query("product")
    product = product_instance(number, brand)
    # breakpoint()
    product.delete()
    print("product successfully deleted")

def update_product(brand):
    number = item_query("product")
    product = product_instance(number,brand)
    # breakpoint()
    try:
        product.name = input("updated name: ")
        product.description = input("updated description: ")
        product.quantity = int(input("updated quantity: "))
        product.price = int(input("updated price: $"))
        product.update()
        breakpoint()
        print("product updated")
    except:
        print("product not updated")
    

def view_product_details(brand):
    number = item_query("product")
    product = product_instance(number, brand)
    clear_input_area()
    print(f'**********{product.name}**********\n',
            f'- name: {product.name}\n',
            f'- description: {product.description}\n',
            f'- quantity: {product.quantity}\n',
            f'- price: ${product.price}\n',
            f'- brand: {Brand.find_by_id(product.brand_id).name}\n'
            "----------------------------------")

def view_product_summary():
    print("-----        product summary     -----")
    table = PrettyTable(['product', 'quantity', 'price', 'brand'])
    for product in Product.get_all():
        # breakpoint()
        table.add_row([product.name, product.quantity, f'${product.price}', Brand.find_by_id(product.brand_id).name])
    print(table)

