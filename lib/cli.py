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
    name_query,
    brand_products,
    delete_product,
    update_product,
    view_product_details,
    view_product_summary,
)


def main():
    initiate_brands()
    initiate_products()
    while True:
        home_page()
        choice = input("> ")
        if choice == "e":
            exit_program()
        elif choice == "b":
            brands_page()
        elif choice == "p":
            view_product_summary()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")

def home_page():
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
    print("      *******************        ")
    print("------    Brands Page    -------\n") 
    list_brands()
    print("\n--------------------------------")
    print("Please choose from the following:\n")
    print("     Type a to see the Add a brand")
    print("     Type v to see the View a brand details")
    print("     Type u to see the Update a brand")
    print("     Type d to see the Delete a brand")
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
        elif choice == "1":
            helper_1()
        else:
            print("brands page Invalid choice")

def brand_menu(name):
    print("      *******************        ")
    print(f'---------   {name}  -----------\n')
    brand_products(name)
    print("\n---------------**---------------")
    print("Please choose from the following:\n")
    print("     Type a to see the Add a product")
    print("     Type v to see the View a product details")
    print("     Type u to see the Update a product")
    print("     Type d to see the Delete a product")
    print("     Type b for Brands")
    print("     Type e to Exit")

def brand_page ():
    # print("      *******************        ")
    # print("-----------View Brand-----------\n")
    # list_brands()
    # print("\n--------------------------------\n")
    name = name_query("brand")
    product_page(name)
        
def product_page(name):
    while True:
        brand_menu(name)
        choice = input("> ")
        if choice == "e":
            exit_program()
        elif choice == "b":
            brands_page()
        elif choice == "a":
            add_product()
        elif choice == "d":
            delete_product()
        elif choice == "u":
            update_product()
        elif choice == "v":
            view_product_details()
        elif choice == "1":
            helper_1()
        else:
            print("Product Error:  Invalid choice")
    


if __name__ == "__main__":
    main()

# def main():
#     while True:
#         home_page()
#         choice = input("> ")
#         if choice == "e":
#             exit_program()
#         elif choice == "b":
#             brands_page()
#         elif choice == "1":
#             helper_1()
#         else:
#             print("Invalid choice")

# def brand_page ():
#     print("-----------View Brand-----------\n")
#     list_brands()
#     print("--------------------------------\n")
#     name = name_query()
#     brand_menu(name)
#     product_page()

# product_menu():
#     print("--------------------------------")
#     print("Products Page")
#     print("--------------------------------")
#     print("")
#     print("---------------**---------------")
#     print("Please choose from the following:")
#     print("")
#     print("     Type a to see the Add a product")
#     print("     Type v to see the View a product details")
#     print("     Type u to see the Update a product")
#     print("     Type d to see the Delete a product")
#     print("     Type e to Exit")
