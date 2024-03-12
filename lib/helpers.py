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
    brand = brand_instance()
    brand.delete()    

# get brand instance
def brand_instance():
    while True:
        try:
            number = int(input(f'enter brand number: '))
            if number > len(Brand.get_all()) or number <1: 
                print("incorrect number, please try again")
            else:
                number = number
                index = number -1
                brand = Brand.get_all()[index]
                # breakpoint()
                return brand
        except ValueError:
            print("Invalid input, please input valid integer")

#get product instance
def product_instance(brand):
       while True:
            try:
                number = int(input(f'enter product number: '))
                if number > len(brand.products()) or number < 1:
                    print("Incorrect number, please try again")
                else:
                    number= number
                    index = number - 1
                    product = brand.products()[index]
                    return product
            except ValueError:
                print("Invalid input, please enter a valid integer")
         

# view brand number
def item_query(item):
    if item == "brand":
        while True:
            try:
                number = int(input(f'enter {item} number: '))
                if number > len(Brand.get_all()) or number <1 or not isinstance(number, int): 
                    print("incorrect number, please try again")
                else:
                    return number
            except ValueError:
                print("Invalid input, please enter a valid integer")

    elif item == "product":
        while True:
            try:
                number = int(input(f'Enter {item} number: '))
                if number > len(Product.get_all()) or number < 1:
                    print("Incorrect number, please try again")
                else:
                    return number
            except ValueError:
                print("Invalid input, please enter a valid integer")
# show brand products
def brand_products(brand):
    # breakpoint()
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
    product = product_instance(brand)
    # breakpoint()
    product.delete()
    print("product successfully deleted")

def update_product(brand):
    product = product_instance(brand)
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
    product = product_instance(brand)
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

