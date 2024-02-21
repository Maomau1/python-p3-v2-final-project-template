# lib/cli.py

from helpers import (
    exit_program,
    helper_1,
    list_brands,
    initiate_brands,
    add_brand,
    update_brand,
    delete_brand,
    initiate_products,
    add_product,
    item_query,
    brand_products,
    delete_product,
    update_product,
    view_product_details,
    view_product_summary,
    clear_input_area,
    product_instance,
    brand_instance,
)


def main():
    # initiate_brands()
    # initiate_products()
    clear_input_area()
    while True:
        home_page()
        choice = input("> ")
        if choice == "e":
            exit_program()
        elif choice == "b":
            brands_page()
        elif choice == "p":
            product_summary_page()
        else:
            print("Invalid choice")

def home_page():
    clear_input_area()
    print("********************************************")
    print("*    Welcome to MR Rose - Inventory App    *")
    print("********************************************")
    print("     Please choose from the following:       \n")
    print("     Type b to see the Brands in store  ")
    print("     Type p to see the Products summary ")
    print("     Type e to Exit                     ")
    print("--------------------------------------------")
    
def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


def brands_menu():
    clear_input_area()
    print("      *******************        ")
    print("------    Brands Page    -------\n") 
    list_brands()
    print("\n--------------------------------")
    print("Please choose from the following:\n")
    print("     Type a to Add a brand")
    print("     Type v to View a brand details")
    print("     Type u to Update a brand")
    print("     Type d to Delete a brand")
    print("     Type m for Main Menu")
    print("     Type e to Exit")


def brands_page():
    while True:
        brands_menu()
        choice = input("> ")
        if choice == "e":
            exit_program()
        elif choice == "m":
            main()
        elif choice == "a":
            add_brand()
        elif choice == "v":
            brand_page()
        elif choice == "u":
            update_brand()
        elif choice == "d":
            delete_brand()
        else:
            print("brands page Invalid choice")

def brand_menu(brand_number, brand):
    clear_input_area()
    print("      *******************        ")
    print(f'---------   {brand.name}  -----------\n')
    brand_products(brand_number)
    print("\n---------------**---------------")
    print("Please choose from the following:\n")
    print("     Type a to Add a product")
    print("     Type v to View a product details")
    print("     Type u to Update a product")
    print("     Type d to Delete a product")
    print("     Type b for Brands")
    print("     Type e to Exit")

def brand_page ():
    brand_number = item_query("brand")
    brand = brand_instance(brand_number)
    product_page(brand_number, brand)


def product_page(brand_number, brand):
    brand_menu(brand_number, brand)
    while True:
        choice = input("> ")
        if choice == "e":
            exit_program()
        elif choice == "p":
            brand_menu(brand_number, brand)
        elif choice == "b":
            brands_page()
        elif choice == "a":
            add_product(brand)
            product_mini_menu(brand)
        elif choice == "d":
            delete_product(brand)
            product_mini_menu(brand)
        elif choice == "u":
            update_product(brand)
            product_mini_menu(brand)
        elif choice == "v":
            view_product_details(brand)
            product_mini_menu(brand)
        else:
            print("Product Error:  Invalid choice")
            product_mini_menu(brand)
        
def product_mini_menu(brand):
    print(f'     Type p to go back to {brand.name} products page')
    print("     Type e to Exit")
    
def product_summary_page():
    clear_input_area()
    while True:
        view_product_summary()
        print("Please choose from the following:\n")
        print("     Type m for Main Menu")
        print("     Type e to Exit")
        choice = input("> ")
        if choice == "m":
            main()
        elif choice == "e":
            exit()
        else:
            print("Product Error:  Invalid choice")

if __name__ == "__main__":
    main()
