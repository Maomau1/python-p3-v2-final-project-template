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