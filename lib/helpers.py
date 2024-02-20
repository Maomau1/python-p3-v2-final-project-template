# lib/helpers.py
from models.brand import Brand

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

# implement brand functions

# create brands table
def initiate_brands():
    Brand.create_table()
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
    print(brand)

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
