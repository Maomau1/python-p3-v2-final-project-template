# lib/cli.py

from helpers import (
    exit_program,
    helper_1,
    list_brands,
    initiate_brands,
    add_brand,
)


def main():
    while True:
        initiate_brands()
        home_page()
        choice = input("> ")
        if choice == "e":
            exit_program()
        elif choice == "b":
            brands_page()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


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


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")

def home_page():
    print("Welcome to MR Rose - Inventory App")
    print("")
    print("Please choose from the following:")
    print("")
    print("     Type b to see the Brands in store")
    print("     Type p to see the Products summary")
    print("     Type e to Exit")

def brands_menu():
    print("---------------**---------------")
    print("         Brands Page             ")
    print("--------------------------------\n")
    list_brands()
    print("\n--------------------------------")
    print("Please choose from the following:")
    print("")
    print("     Type a to see the Add a brand")
    print("     Type v to see the View a brand details")
    print("     Type u to see the Update a brand")
    print("     Type d to see the Delete a brand")
    print("     Type e to Exit")

def brands_page():
    while True:
        brands_menu()
        choice = input("> ")
        if choice == "e":
            exit_program()
        elif choice == "a":
            add_brand()
        elif choice == "v":
            product_page()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")
def product_menu():
    print("--------------------------------")
    print("Products Page")
    print("--------------------------------")
    print("")
    print("---------------**---------------")
    print("Please choose from the following:")
    print("")
    print("     Type a to see the Add a product")
    print("     Type v to see the View a product details")
    print("     Type u to see the Update a product")
    print("     Type d to see the Delete a product")
    print("     Type e to Exit")

def product_page():
    while True:
        product_menu()
        choice = input("> ")
        if choice == "e":
            exit_program()
        elif choice == "b":
            brands_page()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
