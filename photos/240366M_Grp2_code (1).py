# Calcifer:    240456 X @mymail.nyp.edu.sg
# Caleb:       240345 B @mymail.nyp.edu.sg
# Gin Kiat:    240366 M @mymail.nyp.edu.sg

# Last updated on 3/8/24 00:30
# Last updated by: Cal

import math             # Comments: We import os to clear the screen
import os               # Comments: We import math to access the extended list of mathematical functions
from time import sleep  # Comments: We import sleep to add delays at key points in the program
import tkinter as tk    # Comments: We import tkinter to create a GUI

env_var = dict(os.environ)                                          # Comments: This creates a dictionary of the environment variables
check = "ACSVCPORT"                                                 # Comments: This sets the variable check
Pycharm = 0                                                         # Comments: We set variable Pycharm default value to 0
if env_var.get("PYCHARM_HOSTED") == "1":                            # Comments: This code checks if it is running in Pycharm
    Pycharm = 1
    print("You are running on Pycharm")
    if check == list(env_var.keys())[0]:                            # Comments: This code checks if the first key in env_var
        print("Your emulate terminal in output console is off")     # Comments:    matches the variable check, from this check,
    else:                                                           # Comments:    it prints whether emulate terminal settings
        print("Your emulate terminal in output console is on")      # Comments:    is on or off.
else:
    print("You are not running on Pycharm")                         # Comments: This code runs when the code is not being run on pycharm

# Comments: These are the Global Variables
global length_divider       # Comments: This is used when formatting, giving a standard length for the divider
global clear_name           # Comments: This is used in the clear code
global price                # Comments: This is used in the price in the GUI

# Comments: These are the initial values of the shared variables
length_divider = 80                 # Comments: This sets the standard length of the divider
default_number_item_cart = 0        # Comments: This sets the default number of items in the cart
quantity_upper_limit: int = 9999    # Comments: This sets the maximum number of items which can be added to the cart
default_pad_x = 20                  # Comments: This sets the default x spacing for each widget in the GUI
default_pad_y = 20                  # Comments: This sets the default y spacing for each widget in the GUI
font_name = "Calibri"               # Comments: This sets the font for the GUI
header_font_size = 14               # Comments: This sets the font size of headers in the GUI
content_font_size = 12              # Comments: This sets the font size of the other characters in the GUI
text = "A"                          # Comments: This resets the default variable text
width = 1700                        # Comments: This sets the ratio of the GUI window width
height = 1200                       # Comments: This sets the ratio of the GUI window height
pixel_multiplier = 1                # Comments: This multiplier multiplies to the width and height, allowing us to quickly change the size of the window
# Comments: This sets the Variable Width_height which is used in the GUI
Width_height = f"{width * pixel_multiplier}x{height * pixel_multiplier}"


# Comments: We need to find the operating system so that the clear function can work.
# Comments: This is needed as Linux and Windows having different commands to clear the console.
# Comments: Clear function won't work if the OS isn't found or the environment doesn't support it.
# Comments: Alternatively, we will semi clear screen by shifting all the previous text up
# Comments: This function finds the operating system, and set the clear name accordingly
def set_operating_system():
    global clear_name
    operating_system = os.name
    env_variable = os.environ
    if operating_system == "nt":
        clear_name = "cls"
    elif operating_system == "posix":
        clear_name = "clear"
    else:
        print("Unable to identify operating system.")
        clear_name = None
    if env_variable.get("PYCHARM_HOSTED") == "1":
        clear_name = None
        print("You are running on Pycharm.")
    if clear_name is None:
        print("Clear function will not work.")


# Comments: This function clears the screen
def clear_screen():
    if clear_name is not None:
        os.system(clear_name)
    else:
        print("\n" * 50)


# Comments: This list contains the shopping cart. Starting from index 0, Odd indexes are item quantity, Even indexes are item codes
shopping_cart = ["N32", default_number_item_cart, "M13", default_number_item_cart,
                 "V76", default_number_item_cart, "N14", default_number_item_cart,
                 "L11", default_number_item_cart, "P21", default_number_item_cart,
                 "A54", default_number_item_cart, "H91", default_number_item_cart,
                 "E11", default_number_item_cart, "F43", default_number_item_cart,
                 "CP31", default_number_item_cart, "D72", default_number_item_cart,
                 "FP76", default_number_item_cart, "FP32", default_number_item_cart,
                 "K22", default_number_item_cart, "D14", default_number_item_cart,
                 "SS93", default_number_item_cart, "MC14", default_number_item_cart,
                 "R35", default_number_item_cart, "HS11", default_number_item_cart]

# Comments: This list contain the item codes of the items in the store. This is used for the directory function.
list_item_code = ["N32", "M13", "V76", "N14",
                  "L11", "P21", "A54", "H91",
                  "E11", "F43", "CP31", "D72",
                  "FP76", "FP32", "K22", "D14",
                  "SS93", "MC14", "R35", "HS11"]

# Comments: This dictionary contain the item name, code and price respectively
products = {"Drinks (CD10)": [{"item": "Neo's Green Tea", "code": "N32", "price": 3.00},
                              {"item": "Melo Chocolate Malt Drink", "code": "M13", "price": 2.85},
                              {"item": "Very-Fair Full Cream Milk", "code": "V76", "price": 3.50},
                              {"item": "Nirigold UHT Milk", "code": "N14", "price": 4.15}, ],
            "Beer (CB20)": [{"item": "Lion (24 x 320 ml)", "code": "L11", "price": 52.00},
                            {"item": "Panda (24 x 320 ml)", "code": "P21", "price": 78.00},
                            {"item": "Axe (24 x 320 ml)", "code": "A54", "price": 58.00},
                            {"item": "Henekan (24 x 320 ml)", "code": "H91", "price": 68.00}, ],
            "Frozen (CF30)": [{"item": "Edker Ristorante Pizza 355g", "code": "E11", "price": 6.95},
                              {"item": "Fazzler Frozen Soup 500g", "code": "F43", "price": 5.15},
                              {"item": "CP Frozen Ready Meal 250g", "code": "CP31", "price": 4.12},
                              {"item": "Duitoni Cheese 270g", "code": "D72", "price": 5.60}, ],
            "Household (CH40)": [{"item": "FP Facial Tissues", "code": "FP76", "price": 9.50},
                                 {"item": "FP Premium Kitchen Towel", "code": "FP32", "price": 5.85},
                                 {"item": "Klinex Toilet Tissue Rolls", "code": "K22", "price": 7.50},
                                 {"item": "Danny Softener", "code": "D14", "price": 9.85}, ],
            "Snacks (CS50)": [{"item": "Singshort Seaweed", "code": "SS93", "price": 3.10},
                              {"item": "Mei Crab Cracker", "code": "MC14", "price": 2.05},
                              {"item": "Reo Pokemon Cookie", "code": "R35", "price": 4.80},
                              {"item": "Huat Seng Crackers", "code": "HS11", "price": 3.55}, ]}


# Comments: This function takes in the item code and returns the item name
def func_item_code_to_item_name(value):
    responses = {
        "N32": "Neo's Green Tea",
        "M13": "Melo Chocolate Malt Drink",
        "V76": "Very-Fair Full Cream Milk",
        "N14": "Nirigold UHT Milk",
        "L11": "Lion (24 x 320 ml)",
        "P21": "Panda (24 x 320 ml)",
        "A54": "Axe (24 x 320 ml)",
        "H91": "Henekan (24 x 320 ml)",
        "E11": "Edker Ristorante Pizza 355g",
        "F43": "Fazzler Frozen Soup 500g",
        "CP31": "CP Frozen Ready Meal 250g",
        "D72": "Duitoni Cheese 270g",
        "FP76": "FP Facial Tissues",
        "FP32": "FP Premium Kitchen Towel",
        "K22": "Klinex Toilet Tissue Rolls",
        "D14": "Danny Softener",
        "SS93": "Singshort Seaweed",
        "MC14": "Mei Crab Cracker",
        "R35": "Reo Pokemon Cookie",
        "HS11": "Huat Seng Crackers"}
    return responses.get(value)


# Comments: This function takes in the item name and returns the item code
def func_item_name_to_item_code(value):
    responses = {"Neo's Green Tea": "N32",
                 "Melo Chocolate Malt Drink": "M13",
                 "Very-Fair Full Cream Milk": "V76",
                 "Nirigold UHT Milk": "N14",
                 "Lion (24 x 320 ml)": "L11",
                 "Panda (24 x 320 ml)": "P21",
                 "Axe (24 x 320 ml)": "A54",
                 "Henekan (24 x 320 ml)": "H91",
                 "Edker Ristorante Pizza 355g": "E11",
                 "Fazzler Frozen Soup 500g": "F43",
                 "CP Frozen Ready Meal 250g": "CP31",
                 "Duitoni Cheese 270g": "D72",
                 "FP Facial Tissues": "FP76",
                 "FP Premium Kitchen Towel": "FP32",
                 "Klinex Toilet Tissue Rolls": "K22",
                 "Danny Softener": "D14",
                 "Singshort Seaweed": "SS93",
                 "Mei Crab Cracker": "MC14",
                 "Reo Pokemon Cookie": "R35",
                 "Huat Seng Crackers": "HS11"}
    return responses.get(value)


# Comments: This function takes in the item code and returns the item price
def func_item_code_to_item_price(value):
    responses = {
        "N32": 3.00, "M13": 2.85, "V76": 3.50, "N14": 4.15,
        "L11": 52.00, "P21": 78.00, "A54": 58.00, "H91": 68.00,
        "E11": 6.95, "F43": 5.15, "CP31": 4.12, "D72": 5.60,
        "FP76": 9.50, "FP32": 5.85, "K22": 7.50, "D14": 9.85,
        "SS93": 3.10, "MC14": 2.05, "R35": 4.80, "HS11": 3.55}
    return responses.get(value)


# Comments: This function takes in the user's input and returns the corresponding discount percentage
def func_discounts(value):
    responses = {
        1: 10,  # Senior 10% discount
        2: 8,  # Members 8% discount
        3: 5,  # NS Men 5% discount
        4: 0}  # No discount
    return responses.get(value)


# Comments: This function displays the catalogue
def func_display_catalogue():
    print("\nMenu:")
    for category, items in products.items():
        talk(f"\nCategory: {category}", 0.02, 0.14, 1)
        for item in items:
            print(f"        Code: {item['code']}", (4 - len(item['code'])) * ' ', f" - {item['item']}", (30 - len(item["item"])) * ' ', F" - ${item['price']:>6,.2f}")
    sleep(2)
    # Comments: We include a sleep here to pause the program and allow the user to read the catalogue before continuing


# Comments: This function takes a string input and displays it one letter at a time, creating a narator effect
def talk(string, interval=0, extra_wait=0, clear_amt=False):
    for i in string:
        print(i, end="", flush=True)
        sleep(interval)
    sleep(interval)
    sleep(extra_wait)
    if clear_amt is False:
        pass
    elif clear_amt == -1:
        clear_screen()
    else:
        print('\n' * clear_amt)


# Comments: This function generates the menu
def generate_menu(title, contents):
    print()
    divider = length_divider * '*'
    template = '{:2d} ----------- {:<20s}'
    print(divider)
    print('{:^75s}'.format(title))
    print(divider)
    for i in range(len(contents)):
        print(template.format(i + 1, contents[i]))
    print(divider)
    while True:
        try:
            input_value = input('Your choice ({} - {}):    '.format(1, len(contents))).replace(" ", "")
            scenario_list = ["What would you like to do?", "Which category would you like to shop at?", "Drinks (CD10)",
                             "Beer (CB20)", "Frozen (CF30)", "Household (CH40)", "Snacks (CS50)"]
            code_in_hand = str(input_value)
            if code_in_hand in list_item_code:
                if title in scenario_list:
                    func_shopping_item_code(code_in_hand)
                    break
                else:
                    continue
            input_value = int(input_value)
            if input_value <= 0 or input_value > len(contents):
                print("Oops! That doesn't seem to be a valid option. Please try again")
                continue
            clear_screen()
            return input_value
        except ValueError:
            print("Oops! That doesn't seem to be a valid option. Please try again")


# Comments: This function is the main menu
def main_menu():
    menu_title = 'What would you like to do?'
    choices = ["View catalogue", "Start shopping", "View cart", "Checkout", "Leave", "Run in GUI"]
    while True:
        choice = generate_menu(menu_title, choices)
        if choice == 5:
            func_leave()
        elif choice == 1:
            func_display_catalogue()
            main_menu()
        elif choice == 2:
            func_shopping_by_category()
        elif choice == 3:
            func_view_cart()
        elif choice == 4:
            func_checkout()
        elif choice == 6:
            start_gui()
        else:
            func_leave()


# Comments: This function is the first main menu
def first_menu():
    menu_title = 'What would you like to do?'
    choices = ["View catalogue", "Start shopping", "View cart", "Checkout", "Leave", "Run in GUI", "View introduction"]
    while True:
        choice = generate_menu(menu_title, choices)
        if choice == 5:
            func_leave()
        elif choice == 1:
            func_display_catalogue()
            main_menu()
        elif choice == 2:
            func_shopping_by_category()
        elif choice == 3:
            func_view_cart()
        elif choice == 4:
            func_checkout()
        elif choice == 6:
            start_gui()
        elif choice == 7:
            introduction()
        else:
            func_leave()


# Comments: This function displays the items in the category the user selected.
def categorised_menu(title, choices):
    while True:
        choice = generate_menu(title, choices)
        if choice == 5:
            print("Return to previous selection")
            func_shopping_by_category()
        else:
            func_shopping_item_code(products[title][choice - 1]["code"])


# Comments: This function asks the user to select the category they would like to shop
def func_shopping_by_category():
    menu_title = "Which category would you like to shop at?"
    choices = ["Drinks (CD10)", "Beer (CB20)", "Frozen (CF30)", "Household (CH40)", "Snacks (CS50)", "Flash Sale",
               "Clearance Sale", "Return to previous selection"]
    while True:
        choice = generate_menu(menu_title, choices)
        if choice == 6:
            print("There's nothing on sale right now")
            func_shopping_by_category()
        elif choice == 7:
            print("There's nothing on clearance right now")
            func_shopping_by_category()
        elif choice == 8:
            print("Return to previous selection")
            main_menu()
        else:
            choices_list = []
            for i in products[choices[choice - 1]]:
                choices_list.append(i["item"])
            choices_list.append("Return to previous selection")
            categorised_menu(choices[choice - 1], choices_list)


# Comments: This function handles the exiting of the program
def func_leave():
# Comments: This code checks if the shopping cart is empty
    read_cart = []
    read_cart = shopping_cart.copy()
    repeat_clear_cart = read_cart.count(0)
    while repeat_clear_cart > 0:
        repeat_clear_cart = repeat_clear_cart - 1
        clear_index_number = read_cart.index(0)
        read_cart.pop(clear_index_number - 1)
        read_cart.pop(clear_index_number - 1)
    repeat_clear_cart = len(read_cart) / 2
# Comments: This code prompts the user when they want to leave, but the shopping cart is not empty
    if repeat_clear_cart != 0:
        menu_title = "There are items in your shopping cart. Are you sure you wanna leave?"
        choices = ["Yes", "No"]
        choice = generate_menu(menu_title, choices)
        if choice == 1:
            print("Leave")
            exit()
        else:
            talk("return to main menu")
            main_menu()
    else:
        print("Leave")
        exit()


# Comments: This function is used to check if the user is about to buy beer, and if they are old enough to buy beer
def func_check_beer(code_in_hand):
# Comments: This list contain the item codes of the beers in the store
# Comments: It is used to check if the user is about to buy beer
    beer_codes = ["L11", "P21", "A54", "H91"]
    while code_in_hand in beer_codes:
        talk("To buy beer items, you need to be older than 18 y/o.", 0.02, 0.14, 1)
        input_age = input("Are you older than 18 y/o? (y/n): ")
        input_age = input_age.lower()
        if input_age == "no" or input_age == "n":
            clear_screen()
            talk("Apologies!", 0.01, 0, 0)
            talk(" You need to be above 18y/o to purchase this item", 0.01, 0.1)
            main_menu()
        elif input_age == "yes" or input_age == "y":
            clear_screen()
            talk("You are old enough to purchase this item", 0.01, 1, 1)
            break
        else:
            sleep(0)


# Comments: This function allows shopping using the item code
def func_shopping_item_code(code_in_hand):
    clear_screen()
    func_check_beer(code_in_hand)
    item_in_hand = func_item_code_to_item_name(code_in_hand)
    question_how_many = ('How many ' + str(item_in_hand) + ' would you like?\t:\t')
    while True:
        print("You have", shopping_cart[shopping_cart.index(code_in_hand) + 1],
              str(item_in_hand), "in your cart")
        how_many = input(question_how_many)
        how_many = how_many.replace(" ", "")
        if how_many.isdigit():
            how_many = int(how_many)
            if 0 <= how_many < (quantity_upper_limit + 1):
                break
            else:
                print("Oops! Please enter a quantity more than 0 and less than", quantity_upper_limit)
                continue
        else:
            print("Oops! Please enter a quantity more than 0 and less than", quantity_upper_limit)
            continue
    clear_screen()
    print('You would like to buy', how_many, item_in_hand)
# Comments: Shopping by setting var value by...
    shopping_cart.insert(shopping_cart.index(code_in_hand) + 1, int(how_many))
# Comments: Shopping by adding var value by...
    # shopping_cart.insert(shopping_cart.index(code_in_hand) + 1, int(how_many) +int(shopping_cart[shopping_cart.index(code_in_hand) + 1]))
    shopping_cart.pop(shopping_cart.index(code_in_hand) + 2)
# Comments: This code here returns the user to the category the item they were shopping were in
    choices = ["Drinks (CD10)", "Beer (CB20)", "Frozen (CF30)", "Household (CH40)", "Snacks (CS50)"]
    choice = math.ceil((list_item_code.index(code_in_hand) + 1) / 4)
    choices_list = []
    for i in products[choices[choice - 1]]:
        choices_list.append(i["item"])
    choices_list.append("Return to previous selection")
    categorised_menu(choices[choice - 1], choices_list)


# Comments: This function allows the user to view cart
def func_view_cart():
    read_cart = shopping_cart.copy()
    repeat_clear_cart = read_cart.count(0)
    while repeat_clear_cart > 0:
        repeat_clear_cart = repeat_clear_cart - 1
        clear_index_number = read_cart.index(0)
        read_cart.pop(clear_index_number - 1)
        read_cart.pop(clear_index_number - 1)
    repeat_clear_cart = len(read_cart) / 2
# Comments: This code prompts the user when they want to view cart, but the shopping cart is empty
    if repeat_clear_cart == 0:
        print("The shopping cart is empty")
        main_menu()
    else:
        read_longest_item_cart = read_cart.copy()
        longest_item_name_length = 0
        longest_item_quantity_length = 8
        while repeat_clear_cart > 0:
            if len(str(func_item_code_to_item_name(read_longest_item_cart[0]))) > longest_item_name_length:
                longest_item_name_length = len(func_item_code_to_item_name(read_longest_item_cart[0]))
            if len(str((read_longest_item_cart[1]))) > longest_item_quantity_length:
                longest_item_quantity_length = len(str((read_longest_item_cart[1])))
            read_longest_item_cart.pop(0)
            read_longest_item_cart.pop(0)
            repeat_clear_cart = repeat_clear_cart - 1
        print('\n' * 1)
        divider = length_divider * '*'
        print(divider)
        print('{:^75s}'.format("View Cart"))
        print(divider)
        print("Item", (longest_item_name_length - 4) * ' ', "Quantity", (longest_item_quantity_length - 8) * ' ', "Price")
        repeat_clear_cart = len(read_cart) / 2
        while repeat_clear_cart > 0:
            repeat_clear_cart = repeat_clear_cart - 1
            item_in_hand = func_item_code_to_item_name(read_cart[0])
            print(item_in_hand, (longest_item_name_length - len(item_in_hand)) * ' ', read_cart[1], (longest_item_quantity_length - len(str(read_cart[1]))) * ' ', f"${(func_item_code_to_item_price(read_cart[0]) * int(read_cart[1])):>7,.2f}")
            read_cart.pop(0)
            read_cart.pop(0)
        read_cart.clear()
        menu_title = "Would you like to make any changes?"
        choices = ["Yes, edit items in cart", "Yes, remove items in cart", "No, return to menu", "No, proceed to checkout"]
        choice = generate_menu(menu_title, choices)
        if choice == 1:
            read_cart = shopping_cart.copy()
            repeat_clear_cart = read_cart.count(0)
            while repeat_clear_cart > 0:
                repeat_clear_cart = repeat_clear_cart - 1
                clear_index_number = read_cart.index(0)
                read_cart.pop(clear_index_number - 1)
                read_cart.pop(clear_index_number - 1)
            repeat_clear_cart = len(read_cart) / 2
            total_repeat_clear = repeat_clear_cart
            while repeat_clear_cart > 0:
                repeat_clear_cart = repeat_clear_cart - 1
                clear_index_number = int(total_repeat_clear) - int(repeat_clear_cart)
                read_cart.pop(clear_index_number)

            repeat_clear_cart = len(read_cart)
            read_cart_name = read_cart.copy()
            while repeat_clear_cart > 0:
                repeat_clear_cart = repeat_clear_cart - 1
                read_cart_name.insert(repeat_clear_cart, func_item_code_to_item_name(read_cart_name[repeat_clear_cart]))
                read_cart_name.pop(repeat_clear_cart + 1)

            menu_title = "Which item would you like to edit?"
            choices = read_cart_name.copy()
            choice = generate_menu(menu_title, choices)
            choice = choice - 1
            item_in_hand = func_item_code_to_item_name(read_cart[choice])
            question_how_many = ('How many ' + str(item_in_hand) + ' would you like?\t:\t')
            while True:
                how_many = input(question_how_many)
                how_many = how_many.replace(" ", "")
                if how_many.isdigit():
                    how_many = int(how_many)
                    if 0 <= how_many < (quantity_upper_limit + 1):
                        break
                    else:
                        print("Oops! Please enter a quantity more than 0 and less than", quantity_upper_limit)
                        continue
                else:
                    print("Oops! Please enter a quantity more than 0 and less than", quantity_upper_limit)
                    continue
            print('You would like to buy', how_many, item_in_hand)
            shopping_cart.insert(shopping_cart.index(read_cart[choice]) + 1, int(how_many))
            shopping_cart.pop(shopping_cart.index(read_cart[choice]) + 2)
            main_menu()
        elif choice == 2:
            read_cart = shopping_cart.copy()
            repeat_clear_cart = read_cart.count(0)
            while repeat_clear_cart > 0:
                repeat_clear_cart = repeat_clear_cart - 1
                clear_index_number = read_cart.index(0)
                read_cart.pop(clear_index_number - 1)
                read_cart.pop(clear_index_number - 1)
            repeat_clear_cart = len(read_cart) / 2
            total_repeat_clear = repeat_clear_cart

            while repeat_clear_cart > 0:
                repeat_clear_cart = repeat_clear_cart - 1
                clear_index_number = int(total_repeat_clear) - int(
                    repeat_clear_cart)
                read_cart.pop(clear_index_number)

            repeat_clear_cart = len(read_cart)
            read_cart_name = read_cart.copy()
            while repeat_clear_cart > 0:
                repeat_clear_cart = repeat_clear_cart - 1
                read_cart_name.insert(
                    repeat_clear_cart,
                    func_item_code_to_item_name(
                        read_cart_name[repeat_clear_cart]))
                read_cart_name.pop(repeat_clear_cart + 1)

            menu_title = "Which item would you like to remove?"
            choices = read_cart_name.copy()
            choice = generate_menu(menu_title, choices)
            choice = choice - 1
            shopping_cart.insert(shopping_cart.index(read_cart[choice]) + 1, 0)
            shopping_cart.pop(shopping_cart.index(read_cart[choice]) + 2)
            print("you remove all the",
                  func_item_code_to_item_name(read_cart[choice]),
                  "from your cart")
            main_menu()

        elif choice == 3:
            main_menu()

        elif choice == 4:
            func_checkout()

        else:
            main_menu()


# Comments: This function allows the user to checkout
def func_checkout():
    price_in_cart = 0
    read_cart = shopping_cart.copy()
    repeat_clear_cart = read_cart.count(0)
    while repeat_clear_cart > 0:
        repeat_clear_cart = repeat_clear_cart - 1
        clear_index_number = read_cart.index(0)
        read_cart.pop(clear_index_number - 1)
        read_cart.pop(clear_index_number - 1)
    repeat_clear_cart = len(read_cart) / 2
# Comments: This code prompts the user when they want to checkout, but the shopping cart is empty
    if repeat_clear_cart == 0:
        print("The shopping cart is empty")
        main_menu()
    else:
        read_longest_item_cart = read_cart.copy()
        longest_item_name_length = 24
        longest_item_quantity_length = 8
        while repeat_clear_cart > 0:
            if len(str(func_item_code_to_item_name(read_longest_item_cart[0]))) > longest_item_name_length:
                longest_item_name_length = len(func_item_code_to_item_name(read_longest_item_cart[0]))
            if len(str((read_longest_item_cart[1]))) > longest_item_quantity_length:
                longest_item_quantity_length = len(str((read_longest_item_cart[1])))
            read_longest_item_cart.pop(0)
            read_longest_item_cart.pop(0)
            repeat_clear_cart = repeat_clear_cart - 1
        repeat_clear_cart = len(read_cart) / 2
        print('\n' * 1)
        divider = length_divider * '*'
        print(divider)
        print('{:^75s}'.format("Checkout"))
        print(divider)
        print("Item", (longest_item_name_length - 4) * ' ', "Unit Price  Quantity", (longest_item_quantity_length - 8) * ' ', "Price")
        while repeat_clear_cart > 0:
            repeat_clear_cart = repeat_clear_cart - 1
            item_in_hand = func_item_code_to_item_name(read_cart[0])
            print(item_in_hand, (longest_item_name_length - len(item_in_hand)) * ' ', f"${func_item_code_to_item_price(read_cart[0]):>6,.2f}", 3 * ' ', read_cart[1], (longest_item_quantity_length - len(str(read_cart[1]))) * ' ', f"${(func_item_code_to_item_price(read_cart[0]) * int(read_cart[1])):>7,.2f}")
            price_in_cart = price_in_cart + int(func_item_code_to_item_price(read_cart[0])) * int(read_cart[1])
            read_cart.pop(0)
            read_cart.pop(0)
        gst_before_discount = price_in_cart * 0.09
        final_price_before_discount = price_in_cart + gst_before_discount
        print(length_divider * '-')
        print("Price before GST", (longest_item_name_length - 18) * ' ', f": ${price_in_cart:>15,.2f}")
        print("GST(9%)", (longest_item_name_length - 9) * ' ', f": ${gst_before_discount:>15,.2f}")
        print("Price after GST", (longest_item_name_length - 17) * ' ', f": ${final_price_before_discount:>15,.2f}")
        print(length_divider * '-')
        read_cart.clear()
        menu_title = "Which discount are you eligible for?"
        choices = ["Senior", "Members", "NS Men", "None"]
        choice = generate_menu(menu_title, choices)
        if choice == 1:
            percent = price_in_cart * 0.10
            final_price = price_in_cart * 0.90
            print("You are eligible for a 10% discount!")
        elif choice == 2:
            percent = price_in_cart * 0.08
            final_price = price_in_cart * 0.92
            print("You are eligible for a 8% discount!")
        elif choice == 3:
            percent = price_in_cart * 0.05
            final_price = price_in_cart * 0.95
            print("You are eligible for a 5% discount!")
        elif choice == 4:
            percent = price_in_cart * 0
            final_price = price_in_cart * 1
        else:
            percent = price_in_cart * 0
            final_price = price_in_cart * 1
        gst_after_discount = final_price * 0.09
        total_amount = final_price + gst_after_discount
        price_in_cart = 0
        read_cart = shopping_cart.copy()
        repeat_clear_cart = read_cart.count(0)
        while repeat_clear_cart > 0:
            repeat_clear_cart = repeat_clear_cart - 1
            clear_index_number = read_cart.index(0)
            read_cart.pop(clear_index_number - 1)
            read_cart.pop(clear_index_number - 1)
        repeat_clear_cart = len(read_cart) / 2
        print('\n' * 1)
        divider = length_divider * '*'
        print(divider)
        print('{:^75s}'.format("Checkout"))
        print(divider)
        print("Item", (longest_item_name_length - 4) * ' ', "Unit Price  Quantity", (longest_item_quantity_length - 8) * ' ', "Price")
        while repeat_clear_cart > 0:
            repeat_clear_cart = repeat_clear_cart - 1
            item_in_hand = func_item_code_to_item_name(read_cart[0])
            print(item_in_hand, (longest_item_name_length - len(item_in_hand)) * ' ', f"${func_item_code_to_item_price(read_cart[0]):>6,.2f}", 3 * ' ', read_cart[1], (longest_item_quantity_length - len(str(read_cart[1]))) * ' ', f"${(func_item_code_to_item_price(read_cart[0]) * int(read_cart[1])):>7,.2f}")
            price_in_cart = price_in_cart + int(func_item_code_to_item_price(read_cart[0])) * int(read_cart[1])
            read_cart.pop(0)
            read_cart.pop(0)

        print(length_divider * '-')
        print("Price before discount", (longest_item_name_length - 23) * ' ', f": ${price_in_cart:>15,.2f}")
        print(f"{func_discounts(choice)}% discount applied", (longest_item_name_length - len(str(func_discounts(choice))) - 20) * ' ', f": ${percent:>15,.2f}")
        print("GST (9%)", (longest_item_name_length - 10) * ' ', f": ${gst_after_discount:>15,.2f}")
        print("Total amount payable", (longest_item_name_length - 22) * ' ', f": ${total_amount:>15,.2f}")
        print(length_divider * '-')

        menu_title = "Would you like self pick-up or delivery?"
        choices = ["Self pick-up", "Delivery"]
        choice = generate_menu(menu_title, choices)
        if choice == 1:
            talk("Thank you for choosing self pick-up.", 0.01, 0, 1)
            talk("Your order will be ready for collection at our store.", 0.01, 0, 1)
        elif choice == 2:
            talk("Thank you for choosing delivery", 0.01, 0, 1)
            talk("We will contact you to arrange the delivery schedule.", 0.01, 0, 1)
        else:
            sleep(1)
        sleep(1)
        # Comments: This empties the shopping cart
        repeat_clear_cart = len(shopping_cart) / 2
        while repeat_clear_cart > 0:
            clear_index_number = int(repeat_clear_cart) * 2
            shopping_cart.insert(clear_index_number - 1, 0)
            shopping_cart.pop(clear_index_number)
            repeat_clear_cart = repeat_clear_cart - 1
        main_menu()


# Comments: This is the introduction, where we introduce the group members
def introduction():
    app_icon()
    if Pycharm == 1:
        talk("     You are running this program on Pycharm", 0.02, 1, 2)
    talk("    Diploma in Electronics and Computer Engineering", 0.025, 1)
    talk("     24S1-EM151E Programming", 0.025, 1, 2)
    talk("\tA project by: Calcifer", 0.2, 0.5)
    face(1)
    talk("\tA project by: Calcifer", 0, 0)
    talk(", Caleb", 0.2, 0.5)
    face(2)
    talk("\tA project by: Calcifer, Caleb", 0, 0)
    talk(" and GinKiat", 0.2, 0.5, 1)
    face(3)
    talk("    Programming Group 2 presents", 0.02, 0.5)
    talk("...", 0.5, 0.2, -1)
# Comments: This is an inside joke, we were deciding what the max quantity limit should be.
# Comments: Calcifer told Caleb and Gin Kiat that our code has problems handling 5 digit quantities
# Comments: Then one of the reply from Gin Kiat was "we're not Costco, we are friendly neighbourhood store"
# Comments: It was later we changed neighbourhood store to online store, as it was indeed an inline store
    talk("    WELCOME TO YOUR FRIENDLY NEIGHBOURHOOD STORE", 0.01, 1, -1)
    talk("    WELCOME TO YOUR FRIENDLY NEIGHBOURHOOD ", 0, 1, -1)
    talk("    WELCOME TO YOUR FRIENDLY", 0, 1)
    talk(" ONLINE STORE", 0.05, 1.2)
    # talk("     (we're not Costco)", 0.11, 1, -1)
    clear_screen()
    main_menu()


def face(value):
    if value == 1:
        print("....................................................................................................")
        print(".....................................................   ............................................")
        print("...........................................                     ....................................")
        print("................................  ....                              ................................")
        print("...............................                                        .............................")
        print(".........................                                                ...........................")
        print(".......................,. .                                                 ........................")
        print("....................                                                             ...................")
        print(".................                                                                  .................")
        print("................                                                                     ...............")
        print("...............                                                                       ..............")
        print("..............                                                                        ..............")
        print("..............               &@/             .%                                       ..............")
        print("..............            *@@@@@@@(           ,@@@&,                          *       ..............")
        print("..............       (&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#(            (%@@@@@@#      ..............")
        print("..............       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#      ..............")
        print("..............      /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&      ..............")
        print("..............     (@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@     ..............")
        print("..........%&&&./&@@@@@@@@@@@@@@@@@@@@@@@@..(@@@@@@@@@@@@@&..&@@@@@@@@@@@@@@@@@@@@@@@/.*&&%, ........")
        print("......&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    .@@&@@@@@@@@%    %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@......")
        print(".....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*       @@&@@@@@@       ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*....")
        print("....*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*       @@&@@@@@@       ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%....")
        print(".....&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.     %@@@@@@@@@%     .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.....")
        print("......,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@&@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@(......")
        print("..............(@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@&(#(&@@&@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@..............")
        print("..............#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..............")
        print("..............#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(#####(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..............")
        print("..............(@@@@@@@@@@@@@@@@@@@@@@((%@@@@@@@@#(((#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..............")
        print("..............(@@@@@@@@@@@@@@@@@@@@@@@(##(&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..............")
        print("..............#@@@@@@@@@@@@@@@@@@@@@@@@@@((########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..............")
        print("............../@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@..............")
        print(".............. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&..............")
        print("................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& ..............")
        print("................ #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*................")
        print("...................*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@...................")
        print("...................... ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%. .....................")
        print("...................................*////////////////////////////(...................................")
        print("...................................*/////////////////////////////...................................")
        print(".............................,#(/////////////////////////////////////((.............................")
        print("..........................(//////////////////////////////////////////////(/.........................")
        print("........................#///////////////////////////////////////////////////( ......................")
        print("......................///////////////////////////////////////////////////////(......................")
        print(".....................*////////////////////////////////////////////////////////( ....................")
        print("....................,(/////////////////////////////////////////////////////////(....................")
    if value == 2:
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%%%%%%%%%%%")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*               ./%%%%%%%%%%%%%%##%%%%%%%%%%%%%%%%%%%%")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%#                          .#%%%%%%%%%%##%%%%%%%%%%%%%%%%%%%")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%#%%##    #.                                ,%%%%%%%%%###%%%%%%%%%%%%%%%%%")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%*                                              %%%%%%%%###%%%%%%%%%%%%%%%%")
        print("%%%%%%%%%%%%%%%%%%%%%#%%%#                                               *#%%%%%%###%%%%%%%%%%%%%%%")
        print("%%%%%%%%%%%%%%%%%%%%%,                                                         #%%%##%%%%%%%%%%%%%%")
        print("%%%%%%%%%%%%%%%%%%                                                                /%%#%%%%%%%%%%%%%")
        print("%%%%%%%%%%%%%%%%                                                                    #%%%%%%%%%%%%%%")
        print("%%%%%%%%%%%%%%%                                                                      .%%%%%%%%%%%%%")
        print("%%%%%%%%%%%%%%                                                                        (%%%%%%%%%%%%")
        print("%%%%%%%%%%%%%#                                                                        .%%%%%%%%%%%%")
        print("%%%%%%%%%%%%%#              /////             */*                                      %%%%%%%%%%%%")
        print("%%%%%%%%%%%%%#           ,/////////(*         ./(///(.                      .((/       %%%%%%%%%%%%")
        print("%%%%%%%%%%%%%#       (((((((((////////(////////////////////////(////////////////       %%%%%%%%%%%%")
        print("%%%%%%%%%%%%%#       (((((((/.          *//////////////(/////*           *//(/(/       %%%%%%%%%%%%")
        print("%%%%%%%%%%%%%#      (((((.    /%%%%%%%%*    */////////////    .%%%%%%%%#     ///.      %%%%%%%%%%%%")
        print("%%%%%%%%%%%%%#    .((((   .%%%%%%%%%%   *%%   .((/////(/   (%%   ,%%%%%%%%%/   ///     %%%%%%%%%%%%")
        print("%%%%%%%#(/(((((/((((((   %%%%%%%%%%%%%     %%   /(((((,  *%%%%%     #%%%%%%%%,  ///////////(#%%%%%%")
        print("%%%#%((/((//((///       %%%%%%%%%%%%#      ,%#  ./////  *%%%%%       %%%%%%%%%.      ///////(/(%%%%")
        print("%%%%((((((((((/(       ,%%%%%%%%%          ,%%          %%,          %%%%%%%%%(       (////////(%%%")
        print("%%%%(((((((((/(/(.      %%%%%%%%%          ,%%     .    #%,          %%%%%%%%%/     .(//(///(//(%%%")
        print("%%%%#(/((((((((((((/(/  ,%%%%%%%%%,       *%%   ((((/(   #%#       .%%%%%%%%%/  ./(///////////(%%%%")
        print("%%%%%%#(((((((((((((((/   #%%%%%%%%%%%%%%%%/   ((/,,/((*  .%%%%%%%%%%%%%%%%%   ////(////////(%%%%%%")
        print("%%%%%%%%%%%#%%((((((((((/    #%%%%%%%%%%*    (((*,,,,,(((.   .%%%%%%%%%%#    ,((((////#%%%%%%%%%%%%")
        print("%%%%%%%%%%%%%%((((((((((((((             .//(//*,,,,,,,((((/*             /(((/((((((/#%%%%%%%%%%%%")
        print("%%%%%%%%%%%%%%(((((((((((((((((((((((((((/(((((/,,,,,,/((((//(//////(((///((((((((((((#%%%%%%%%%%%%")
        print("%%%%%%%%%%%%%%(((((((((((((((((((((((,,,,(/((((((////(((((((((((((((((((((((((((((((((#%%%%%%%%%%%%")
        print("%%%%%%%%%%%%%%(((((((((((((((((((((((((*,,,,,/////(((((((((/((((((((((((((((((((((((((#%%%%%%%%%%%%")
        print("%%%%%%%%%%%%%%(((((((((((((((((((((((((((((*,,,,,,,(((((((((((((((((((((((((((((((((((#%%%%%%%%%%%%")
        print("%%%%%%%%%###%#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((#%%%%%%%%%%%%")
        print("%%%%%%%%####%##(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((%%%%%%%%%%%%%")
        print("%%%%%%%%####%%##(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((/(((((%%%%%%%%%%%%%%")
        print("%%%%%%%#####%#####(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((%%%%%%%%%%%%%%%%")
        print("%%%%%%%#####%######%#(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((#%%%%%%%%%%%%%%%%%%")
        print("%%%%%#######%#%####%###%##(((((((((///////////////////////////////(((((((((#%%%%%%%%%%%%%%%%%%%%%%%")
        print("%%%#########%##################%%%%                              *%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("%#%###%#####%###%###%###%###%#%%%##                              *#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("############%#############%#                                            *%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("######%#####%############                                                  /%%%%%%%%%%%%%%%%%%%%%%%")
        print("############%##########                                                      *%%%%%%%%%%%%%%%%%%%%%")
        print("############%######%%#                                                        ,%%%%%%%%%%%%%%%%%%%%")
        print("############%########                                                          (%%%%%%%%%%%%%%%%%%%")
        print("######%#####%#######                                                            #%%%%%%%%%%%%%%%%%%")
        print("###################,                                                             %%%%%%%%%%%%%%%%%%")
    if value == 3:
        print("                                                                           .                        ")
        print("                   .(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(.   .                ")
        print("                ,%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%,                 ")
        print("              *%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.               ")
        print("            .%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(              ")
        print("            (%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*             ")
        print("           .%%%%%%%%%%%%%%%%%%%%%&@@@@@@@&%%%%%%%%%%%%%%%&@@@@@@@&%%%%%%%%%%%%%%%%%%%%#             ")
        print("           .%%%%%%%%%%%%%%%%%%&@@@@@@@@@@@@@@%%%%%%%%%@@@@@@@@@@@@@@&%%%%%%%%%%%%%%%%%%.            ")
        print("           .%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@&%%%%%%@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%.            ")
        print("   ..(%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@   ,@@@%%%%%@@@@@*   @@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%#.      ")
        print("  .%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@.    .@@%%%%%@@@@*     &@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%#    ")
        print(" ,%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@       .@@%%%%%@@.       &@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%(   ")
        print(" *%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@       .@@%%%%%@@,       &@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%   ")
        print("  #%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@     .@@@%%%%%@@@,     &@@@@@@@@&%%%%%%%%%%%%%%%%%%%%%%%%%.   ")
        print("    (%%%%%%%%%%%%%%%%%%%%%%%%&@@@@@@@@@@@@@@@&%%%(%%%&@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%.     ")
        print("        .. .%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@&%%%#((/(%%%&@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%....         ")
        print("           .%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%(//////%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%             ")
        print("           .%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%/((((((#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.            ")
        print("           .%%%%%%%%%%%%%%%%%%%%%%%#((%%%%%%%%%(///(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%             ")
        print("           .%%%%%%%%%%%%%%%%%%%%%%%%((//(%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%             ")
        print("           .%%%%%%%%%%%%%%%%%%%%%%%%%%%(/(//((/(/#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%             ")
        print("           .%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#             ")
        print("            (%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%/             ")
        print("            .%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#              ")
        print("              (%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*.              ")
        print("                /%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*.                ")
        print("                   *#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#,                    ")
        print("                        ..........,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.........                          ")
        print("                                  ,,,,,..,.,,,,,.,..,,,,.,,.,,..,                                   ")
        print("                               ...,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,...                                ")
        print("                         ...,,,,.,.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,,,,..                          ")
        print("                       ..,.,,,..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,.,,,,,,,,.                        ")
        print("                     .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,.                      ")
        print("                   .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.                     ")
        print("                   .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.                    ")
        print("                  .,.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,.                   ")
        print("                 .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..                   ")
        print("                .,,.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,                  ")
        print("               ..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.                 ")
        print("               .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.                ")
        print("              .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.               ")
        print("             ...,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..              ")
        print("            .,,.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,,.              ")
        print("           .,.,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.             ")
        print("           ..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,.,,.            ")
    else:
        print()


# Comments: This is the "app icon", which is an ASCII art of a shopping cart
def app_icon():
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣷⣤⣄⣉⠉⢻⣿ YOUR FRIENDLY ONLINE STORE")
    print("⣿⣿⣿⣿⣿⣷⡄⠹⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⡄⢰⣶⣶⣶⣶⡆⢰⣶⣶⣶⣶⠀⣶⣶⣶⣶⣶⠆⣸⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣷⠀⠿⠿⠿⠿⠇⠘⠿⠿⠿⠿⠀⠻⠿⠿⠿⠟⢀⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣇⠘⣿⣿⣿⡇⢸⣿⣿⣿⣿⠀⣾⣿⣿⣿⠀⣼⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠘⠛⠛⠃⠘⠛⠛⠛⠛⠀⠛⠛⠛⠃⢰⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⣿⣿⡇⢸⣿⣿⣿⣿⠀⣿⣿⡟⢀⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠈⣛⣃⣈⣛⣛⣛⣛⣀⣙⣛⣁⣼⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠈⡉⠉⣉⣉⣉⣉⣉⣉⠉⣉⠉⢉⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠘⠟⢀⣿⣿⣿⣿⣿⣿⡈⠻⠃⣸⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    sleep(2)
    clear_screen()


# Comments: This is the start of the code, we set operating system to see what system is running this code
def start():
    set_operating_system()
    first_menu()


# Comments: This is the GUI for the Main Menu
class MainMenuWindow:
    # Comments: We set this window under the variable 'master' as it is the main GUI
    def __init__(self, master):
        # Comments: We need to get the 'master' variable saved under self
        self.master = master
        # Comments: .Frame is used to group the group of widgets
        mainframe = tk.Frame(master)
        # Comments: This is setting the title of the window
        master.title("Python Group 2 - Welcome to your friendly online store")
        # Comments: This is the view catalogue button, it opens the view catalogue window
        view_catalogue_button = tk.Button(mainframe, text="View Catalogue", command=self.view_catalogue, font=(font_name, content_font_size))
        view_catalogue_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        # Comments: This is the view category button, it opens the view category shopping window
        view_category_button = tk.Button(mainframe, text="View Category", command=self.view_category, font=(font_name, content_font_size))
        view_category_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        # Comments: This is the view cart button, it opens the view cart window
        view_cart_button = tk.Button(mainframe, text="View Cart", command=self.view_cart, font=(font_name, content_font_size))
        view_cart_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        checkout_button = tk.Button(mainframe, text="Checkout", command=self.checkout, font=(font_name, content_font_size))
        checkout_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        leave_button = tk.Button(mainframe, text="Leave", command=self.leave, font=(font_name, content_font_size))
        leave_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        item_code_textbox_label = tk.Label(mainframe, text="Input item code if you would like to shop by item code:", anchor="w", font=(font_name, content_font_size))
        item_code_textbox_label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        self.textbox = tk.Text(mainframe, height=2)
        self.textbox.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        submit_item_code_button = tk.Button(mainframe, text="Submit item code", command=self.item_code, font=(font_name, content_font_size))
        submit_item_code_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        mainframe.pack(fill='both', padx=0, pady=0)

    def item_code(self):
        input_value = self.textbox.get('1.0', tk.END)
        input_value = str(input_value)
        input_value = input_value.replace("\n", "")
        if input_value in list_item_code:
            input_value = list_item_code.index(input_value)
            if input_value == 0:
                item("N32")
            if input_value == 1:
                item("M13")
            if input_value == 2:
                item("V76")
            if input_value == 3:
                item("N14")
            if input_value == 4:
                Lion24x320ml()
            if input_value == 5:
                Panda24x320ml()
            if input_value == 6:
                Axe24x320ml()
            if input_value == 7:
                Henekan24x320ml()
            if input_value == 8:
                item("E11")
            if input_value == 9:
                item("F43")
            if input_value == 10:
                item("CP31")
            if input_value == 11:
                item("D72")
            if input_value == 12:
                item("FP76")
            if input_value == 13:
                item("FP32")
            if input_value == 14:
                item("K22")
            if input_value == 15:
                item("D14")
            if input_value == 16:
                item("SS93")
            if input_value == 17:
                item("MC14")
            if input_value == 18:
                item("R35")
            if input_value == 19:
                item("HS11")

    @staticmethod
    def view_catalogue():
        ViewCatalogueWindow()

    @staticmethod
    def view_category():
        ViewCategoryWindow()

    @staticmethod
    def view_cart():
        ViewCartWindow()

    @staticmethod
    def checkout():
        CheckoutWindow()

    @staticmethod
    def leave():
        LeaveWindow()


class ViewCartWindow:  # Comments: handle view cart and sorting cart
    def __init__(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        read_cart = shopping_cart.copy()
        repeat_clear_cart = read_cart.count(0)
        while repeat_clear_cart > 0:
            repeat_clear_cart = repeat_clear_cart - 1
            clear_index_number = read_cart.index(0)
            read_cart.pop(clear_index_number - 1)
            read_cart.pop(clear_index_number - 1)
        repeat_clear_cart = len(read_cart) / 2
        # Comments: This code prompts the user when they want to view cart, but the shopping cart is empty
        if repeat_clear_cart == 0:
            label = tk.Label(top, text="There are no Items in the cart", font=(font_name, content_font_size))
            label.grid(sticky="w", row=0, column=0)
            button = tk.Button(top, text="Understood", command=top.destroy, font=(font_name, content_font_size))
            button.grid(sticky="w", row=1, column=0)
        else:
            read_longest_item_cart = read_cart.copy()
            longest_item_quantity_length = 9
            while repeat_clear_cart > 0:
                if len(str((read_longest_item_cart[1]))) > longest_item_quantity_length:
                    longest_item_quantity_length = len(str((read_longest_item_cart[1])))
                read_longest_item_cart.pop(0)
                read_longest_item_cart.pop(0)
                repeat_clear_cart = repeat_clear_cart - 1
            item_button = tk.Button(top, text="Item", font=(font_name, content_font_size), command=self.sort_az)
            item_button.grid(sticky="ew", row=0, column=0, padx=50, pady=10)
            unit_price_button = tk.Button(top, text="Unit Price", font=(font_name, content_font_size), command=self.sort_up_h)
            unit_price_button.grid(sticky="ew", row=0, column=1, padx=5, pady=10)
            quantity_button = tk.Button(top, text="Quantity", font=(font_name, content_font_size), command=self.sort_item_quantity_up)
            quantity_button.grid(sticky="ew", row=0, column=2, padx=5, pady=10)
            price_button = tk.Button(top, text="Price", font=(font_name, content_font_size), command=self.sort_cp_h)
            price_button.grid(sticky="ew", row=0, column=3, padx=5, pady=10)
            rows = 2
            data = [(func_item_code_to_item_name(read_cart[i]), func_item_code_to_item_price(read_cart[i]), read_cart[i + 1], (func_item_code_to_item_price(read_cart[i]) * int(read_cart[i + 1]))) for i in range(0, len(read_cart), 2)]
            self.data = data
            for row in data:
                rows += 1
                col1_width = max(len(str(row[0])) for row in data) + 2
                col2_width = max(len(str(row[1])) for row in data) + 2
                col3_width = max(len(str(row[2])) for row in data) + 2
                col4_width = max(len(str(row[3])) for row in data) + 2
                item_name = str(row[0]).ljust(col1_width)
                unit_price = f"${row[1]:,.2f}".rjust(col2_width)
                item_code = str(row[2]).rjust(col3_width)
                cart_price = f"${row[3]:,.2f}".rjust(col4_width)
                label = tk.Label(top, text=item_name, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=0)
                label = tk.Label(top, text=unit_price, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=1)
                label = tk.Label(top, text=item_code, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=2)
                label = tk.Label(top, text=cart_price, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=3)
            read_cart.clear()
            button = tk.Button(top, text="Edit items in cart", command=self.edit, font=(font_name, content_font_size))
            button.grid(sticky="w", row=0, column=7)
            button = tk.Button(top, text="Remove items in cart", command=self.remove, font=(font_name, content_font_size))
            button.grid(sticky="w", row=0, column=6, padx=5, pady=10)
            button = tk.Button(top, text="Return to main menu", command=top.destroy, font=(font_name, content_font_size))
            button.grid(sticky="w", row=0, column=5)

    def sort_az(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        data = self.data
        self.root = top
        button = tk.Button(top, text="Item  \u25BCA", font=(font_name, content_font_size), command=self.sort_az_za)
        button.grid(sticky="ew", row=0, column=0, padx=50, pady=10)
        label = tk.Label(top, text="Unit Price", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=1, padx=5, pady=10)
        label = tk.Label(top, text="Quantity", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=2, padx=5, pady=10)
        label = tk.Label(top, text="Price", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=3, padx=5, pady=10)
        data_sorted = sorted(data, key=lambda x: x[0])
        rows = 2
        for row in data_sorted:
            rows += 1
            col1_width = max(len(str(row[0])) for row in data_sorted) + 2
            col2_width = max(len(f"${row[1]:,.2f}") for row in data_sorted) + 2
            col3_width = max(len(str(row[2])) for row in data_sorted) + 2
            col4_width = max(len(f"${row[3]:,.2f}") for row in data_sorted) + 2
            item_name = str(row[0]).ljust(col1_width)
            unit_price = f"${row[1]:,.2f}".rjust(col2_width)
            item_code = str(row[2]).rjust(col3_width)
            cart_price = f"${row[3]:,.2f}".rjust(col4_width)

            label = tk.Label(top, text=item_name, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=0)
            label = tk.Label(top, text=unit_price, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=1)
            label = tk.Label(top, text=item_code, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=2)
            label = tk.Label(top, text=cart_price, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=3)
        button = tk.Button(top, text="Return to View Cart", command=top.destroy, font=(font_name, content_font_size))
        button.grid(row=0, column=4, padx=default_pad_x, pady=default_pad_y)

    def sort_az_za(self):
        self.root.destroy()
        self.sort_za()

    def sort_za_az(self):
        self.root.destroy()
        self.sort_az()

    def sort_za(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        data = self.data
        self.root = top
        button = tk.Button(top, text="Item  \u25BCZ", font=(font_name, content_font_size), command=self.sort_za_az)
        button.grid(sticky="ew", row=0, column=0, padx=50, pady=10)
        label = tk.Label(top, text="Unit Price", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=1, padx=5, pady=10)
        label = tk.Label(top, text="Quantity", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=2, padx=5, pady=10)
        label = tk.Label(top, text="Price", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=3, padx=5, pady=10)
        data_sorted = sorted(data, key=lambda x: x[0], reverse=True)
        rows = 2
        for row in data_sorted:
            rows += 1
            col1_width = max(len(str(row[0])) for row in data_sorted) + 2
            col2_width = max(len(f"${row[1]:,.2f}") for row in data_sorted) + 2
            col3_width = max(len(str(row[2])) for row in data_sorted) + 2
            col4_width = max(len(f"${row[3]:,.2f}") for row in data_sorted) + 2
            item_name = str(row[0]).ljust(col1_width)
            unit_price = f"${row[1]:,.2f}".rjust(col2_width)
            item_code = str(row[2]).rjust(col3_width)
            cart_price = f"${row[3]:,.2f}".rjust(col4_width)
            label = tk.Label(top, text=item_name, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=0)
            label = tk.Label(top, text=unit_price, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=1)
            label = tk.Label(top, text=item_code, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=2)
            label = tk.Label(top, text=cart_price, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=3)
        button = tk.Button(top, text="Return to View Cart", command=top.destroy, font=(font_name, content_font_size))
        button.grid(row=0, column=4, padx=default_pad_x, pady=default_pad_y)

    def sort_up_h(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        data = self.data
        label = tk.Label(top, text="Item", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=0, padx=50, pady=10)
        self.root = top
        button = tk.Button(top, text="Unit Price  \u25BClow", font=(font_name, content_font_size), command=self.sort_up_hl)
        button.grid(sticky="ew", row=0, column=1, padx=5, pady=10)
        label = tk.Label(top, text="Quantity", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=2, padx=5, pady=10)
        label = tk.Label(top, text="Price", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=3, padx=5, pady=10)
        data_sorted = sorted(data, key=lambda x: x[1])
        rows = 2
        for row in data_sorted:
            rows += 1
            col1_width = max(len(str(row[0])) for row in data_sorted) + 2
            col2_width = max(len(f"${row[1]:,.2f}") for row in data_sorted) + 2
            col3_width = max(len(str(row[2])) for row in data_sorted) + 2
            col4_width = max(len(f"${row[3]:,.2f}") for row in data_sorted) + 2
            item_name = str(row[0]).ljust(col1_width)
            unit_price = f"${row[1]:,.2f}".rjust(col2_width)
            item_code = str(row[2]).rjust(col3_width)
            cart_price = f"${row[3]:,.2f}".rjust(col4_width)

            label = tk.Label(top, text=item_name, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=0)
            label = tk.Label(top, text=unit_price, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=1)
            label = tk.Label(top, text=item_code, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=2)
            label = tk.Label(top, text=cart_price, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=3)
        button = tk.Button(top, text="Return to View Cart", command=top.destroy, font=(font_name, content_font_size))
        button.grid(row=0, column=4, padx=default_pad_x, pady=default_pad_y)

    def sort_up_hl(self):
        self.root.destroy()
        self.sort_up_l()

    def sort_up_lh(self):
        self.root.destroy()
        self.sort_up_h()

    def sort_up_l(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        data = self.data
        label = tk.Label(top, text="Item", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=0, padx=50, pady=10)
        self.root = top
        button = tk.Button(top, text="Unit Price  \u25BChigh", font=(font_name, content_font_size), command=self.sort_up_lh)
        button.grid(sticky="ew", row=0, column=1, padx=5, pady=10)
        label = tk.Label(top, text="Quantity", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=2, padx=5, pady=10)
        label = tk.Label(top, text="Price", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=3, padx=5, pady=10)
        data_sorted = sorted(data, key=lambda x: x[1], reverse=True)
        rows = 0
        for row in data_sorted:
            rows += 1
            col1_width = max(len(str(row[0])) for row in data_sorted) + 2
            col2_width = max(len(f"${row[1]:,.2f}") for row in data_sorted) + 2
            col3_width = max(len(str(row[2])) for row in data_sorted) + 2
            col4_width = max(len(f"${row[3]:,.2f}") for row in data_sorted) + 2
            item_name = str(row[0]).ljust(col1_width)
            unit_price = f"${row[1]:,.2f}".rjust(col2_width)
            item_code = str(row[2]).rjust(col3_width)
            cart_price = f"${row[3]:,.2f}".rjust(col4_width)

            label = tk.Label(top, text=item_name, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=0)
            label = tk.Label(top, text=unit_price, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=1)
            label = tk.Label(top, text=item_code, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=2)
            label = tk.Label(top, text=cart_price, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=3)
        button = tk.Button(top, text="Return to View Cart", command=top.destroy, font=(font_name, content_font_size))
        button.grid(row=0, column=4, padx=default_pad_x, pady=default_pad_y)

    def sort_item_quantity_up(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        data = self.data
        label = tk.Label(top, text="Item", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=0, padx=50, pady=10)
        label = tk.Label(top, text="Unit Price", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=1, padx=5, pady=10)
        self.root = top
        button = tk.Button(top, text="Quantity  \u25BClow", font=(font_name, content_font_size), command=self.sort_qud)
        button.grid(sticky="ew", row=0, column=2, padx=5, pady=10)
        label = tk.Label(top, text="Price", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=3, padx=5, pady=10)
        data_sorted = sorted(data, key=lambda x: x[2])
        rows = 0
        for row in data_sorted:
            rows += 1
            col1_width = max(len(str(row[0])) for row in data_sorted) + 2
            col2_width = max(len(f"${row[1]:,.2f}") for row in data_sorted) + 2
            col3_width = max(len(str(row[2])) for row in data_sorted) + 2
            col4_width = max(len(f"${row[3]:,.2f}") for row in data_sorted) + 2
            item_name = str(row[0]).ljust(col1_width)
            unit_price = f"${row[1]:,.2f}".rjust(col2_width)
            item_code = str(row[2]).rjust(col3_width)
            cart_price = f"${row[3]:,.2f}".rjust(col4_width)

            label = tk.Label(top, text=item_name, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=0)
            label = tk.Label(top, text=unit_price, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=1)
            label = tk.Label(top, text=item_code, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=2)
            label = tk.Label(top, text=cart_price, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=3)
        button = tk.Button(top, text="Return to View Cart", command=top.destroy, font=(font_name, content_font_size))
        button.grid(row=0, column=4, padx=default_pad_x, pady=default_pad_y)

    def sort_qud(self):
        self.root.destroy()
        self.sort_item_quantity_down()

    def sort_qdu(self):
        self.root.destroy()
        self.sort_item_quantity_up()

    def sort_item_quantity_down(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        data = self.data
        label = tk.Label(top, text="Item", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=0, padx=50, pady=10)
        label = tk.Label(top, text="Unit Price", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=1, padx=5, pady=10)
        self.root = top
        button = tk.Button(top, text="Quantity  \u25BChigh", font=(font_name, content_font_size), command=self.sort_qdu)
        button.grid(sticky="ew", row=0, column=2, padx=5, pady=10)
        label = tk.Label(top, text="Price", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=3, padx=5, pady=10)
        data_sorted = sorted(data, key=lambda x: x[2], reverse=True)
        rows = 0
        for row in data_sorted:
            rows += 1
            col1_width = max(len(str(row[0])) for row in data_sorted) + 2
            col2_width = max(len(f"${row[1]:,.2f}") for row in data_sorted) + 2
            col3_width = max(len(str(row[2])) for row in data_sorted) + 2
            col4_width = max(len(f"${row[3]:,.2f}") for row in data_sorted) + 2
            item_name = str(row[0]).ljust(col1_width)
            unit_price = f"${row[1]:,.2f}".rjust(col2_width)
            item_code = str(row[2]).rjust(col3_width)
            cart_price = f"${row[3]:,.2f}".rjust(col4_width)

            label = tk.Label(top, text=item_name, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=0)
            label = tk.Label(top, text=unit_price, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=1)
            label = tk.Label(top, text=item_code, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=2)
            label = tk.Label(top, text=cart_price, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=3)
        button = tk.Button(top, text="Return to View Cart", command=top.destroy, font=(font_name, content_font_size))
        button.grid(row=0, column=4, padx=default_pad_x, pady=default_pad_y)

    def sort_cp_h(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        data = self.data
        label = tk.Label(top, text="Item", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=0, padx=50, pady=10)
        label = tk.Label(top, text="Unit Price", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=1, padx=5, pady=10)
        label = tk.Label(top, text="Quantity", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=2, padx=5, pady=10)
        self.root = top
        button = tk.Button(top, text="Price  \u25BClow", font=(font_name, content_font_size), command=self.sort_cp_hl)
        button.grid(sticky="ew", row=0, column=3, padx=5, pady=10)
        data_sorted = sorted(data, key=lambda x: x[3])
        rows = 2
        for row in data_sorted:
            rows += 1
            col1_width = max(len(str(row[0])) for row in data_sorted) + 2
            col2_width = max(len(f"${row[1]:,.2f}") for row in data_sorted) + 2
            col3_width = max(len(str(row[2])) for row in data_sorted) + 2
            col4_width = max(len(f"${row[3]:,.2f}") for row in data_sorted) + 2
            item_name = str(row[0]).ljust(col1_width)
            unit_price = f"${row[1]:,.2f}".rjust(col2_width)
            item_code = str(row[2]).rjust(col3_width)
            cart_price = f"${row[3]:,.2f}".rjust(col4_width)

            label = tk.Label(top, text=item_name, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=0)
            label = tk.Label(top, text=unit_price, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=1)
            label = tk.Label(top, text=item_code, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=2)
            label = tk.Label(top, text=cart_price, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=3)
        button = tk.Button(top, text="Return to View Cart", command=top.destroy, font=(font_name, content_font_size))
        button.grid(row=0, column=4, padx=default_pad_x, pady=default_pad_y)

    def sort_cp_hl(self):
        self.root.destroy()
        self.sort_cp_l()

    def sort_cp_lh(self):
        self.root.destroy()
        self.sort_cp_h()

    def sort_cp_l(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        data = self.data
        label = tk.Label(top, text="Item", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=0, padx=50, pady=10)
        label = tk.Label(top, text="Unit Price", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=1, padx=5, pady=10)
        label = tk.Label(top, text="Quantity", font=(font_name, content_font_size))
        label.grid(sticky="ew", row=0, column=2, padx=5, pady=10)
        self.root = top
        button = tk.Button(top, text="Price  \u25BChigh", font=(font_name, content_font_size), command=self.sort_cp_lh)
        button.grid(sticky="ew", row=0, column=3, padx=5, pady=10)
        data_sorted = sorted(data, key=lambda x: x[3], reverse=True)
        rows = 0
        for row in data_sorted:
            rows += 1
            col1_width = max(len(str(row[0])) for row in data_sorted) + 2
            col2_width = max(len(f"${row[1]:,.2f}") for row in data_sorted) + 2
            col3_width = max(len(str(row[2])) for row in data_sorted) + 2
            col4_width = max(len(f"${row[3]:,.2f}") for row in data_sorted) + 2
            item_name = str(row[0]).ljust(col1_width)
            unit_price = f"${row[1]:,.2f}".rjust(col2_width)
            item_code = str(row[2]).rjust(col3_width)
            cart_price = f"${row[3]:,.2f}".rjust(col4_width)

            label = tk.Label(top, text=item_name, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=0)
            label = tk.Label(top, text=unit_price, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=1)
            label = tk.Label(top, text=item_code, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=2)
            label = tk.Label(top, text=cart_price, font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows, column=3)
        button = tk.Button(top, text="Return to View Cart", command=top.destroy, font=(font_name, content_font_size))
        button.grid(row=0, column=4, padx=default_pad_x, pady=default_pad_y)

    def remove(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        read_cart = shopping_cart.copy()
        repeat_clear_cart = read_cart.count(0)
        while repeat_clear_cart > 0:
            repeat_clear_cart = repeat_clear_cart - 1
            clear_index_number = read_cart.index(0)
            read_cart.pop(clear_index_number - 1)
            read_cart.pop(clear_index_number - 1)
        repeat_clear_cart = len(read_cart) / 2
        total_repeat_clear = repeat_clear_cart
        while repeat_clear_cart > 0:
            repeat_clear_cart = repeat_clear_cart - 1
            clear_index_number = int(total_repeat_clear) - int(repeat_clear_cart)
            read_cart.pop(clear_index_number)

        repeat_clear_cart = len(read_cart)
        read_cart_name = read_cart.copy()
        while repeat_clear_cart > 0:
            repeat_clear_cart = repeat_clear_cart - 1
            read_cart_name.insert(repeat_clear_cart, func_item_code_to_item_name(read_cart_name[repeat_clear_cart]))
            read_cart_name.pop(repeat_clear_cart + 1)
        label = tk.Label(top, text="What would you like to edit?", anchor="w", font=(font_name, content_font_size))
        label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        self.root = top
        self.read_cart_name = read_cart_name
        for item in self.read_cart_name:
            button = tk.Button(self.root, text=item, command=lambda text=item: self.do(text), anchor="w", font=(font_name, content_font_size))
            button.pack(fill='both', padx=default_pad_x, pady=0)

    @staticmethod
    def do(code):
        item_in_hand = func_item_name_to_item_code(code)
        top = tk.Toplevel()
        top.geometry(Width_height)
        shopping_cart.insert(shopping_cart.index(item_in_hand) + 1, 0)
        shopping_cart.pop(shopping_cart.index(item_in_hand) + 2)
        text = f"You have successfully removed {func_item_code_to_item_name(item_in_hand)} from your cart. Please close the window to refresh the quantity"
        label = tk.Label(top, text=text, anchor="w", font=(font_name, content_font_size))
        label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        button = tk.Button(top, text="Understood", command=top.destroy, font=(font_name, content_font_size))
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)

    def edit(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        read_cart = shopping_cart.copy()
        repeat_clear_cart = read_cart.count(0)
        while repeat_clear_cart > 0:
            repeat_clear_cart = repeat_clear_cart - 1
            clear_index_number = read_cart.index(0)
            read_cart.pop(clear_index_number - 1)
            read_cart.pop(clear_index_number - 1)
        repeat_clear_cart = len(read_cart) / 2
        total_repeat_clear = repeat_clear_cart
        while repeat_clear_cart > 0:
            repeat_clear_cart = repeat_clear_cart - 1
            clear_index_number = int(total_repeat_clear) - int(repeat_clear_cart)
            read_cart.pop(clear_index_number)

        repeat_clear_cart = len(read_cart)
        read_cart_name = read_cart.copy()
        while repeat_clear_cart > 0:
            repeat_clear_cart = repeat_clear_cart - 1
            read_cart_name.insert(
                repeat_clear_cart,
                func_item_code_to_item_name(
                    read_cart_name[repeat_clear_cart]))
            read_cart_name.pop(repeat_clear_cart + 1)
        label = tk.Label(top, text="What would you like to edit?", anchor="w", font=(font_name, content_font_size))
        label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        self.root = top
        self.read_cart_name = read_cart_name
        for item in self.read_cart_name:
            button = tk.Button(self.root, text=item, command=lambda text=item: self.run(text), anchor="w", font=(font_name, content_font_size))
            button.pack(fill='both', padx=default_pad_x, pady=0)

    @staticmethod
    def run(code):
        item(func_item_name_to_item_code(code))


class CheckoutWindow:  # Comments: Handles checkout
    def __init__(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        read_cart = shopping_cart.copy()
        repeat_clear_cart = read_cart.count(0)
        while repeat_clear_cart > 0:
            repeat_clear_cart = repeat_clear_cart - 1
            clear_index_number = read_cart.index(0)
            read_cart.pop(clear_index_number - 1)
            read_cart.pop(clear_index_number - 1)
        repeat_clear_cart = len(read_cart) / 2
        # Comments: This code prompts the user when they want to view cart, but the shopping cart is empty
        if repeat_clear_cart == 0:
            label = tk.Label(top, text="There are no Items in the cart", font=(font_name, content_font_size))
            label.grid(sticky="w", row=0, column=0)
            button = tk.Button(top, text="Understood", command=top.destroy, font=(font_name, content_font_size))
            button.grid(sticky="w", row=1, column=0)
        else:
            read_longest_item_cart = read_cart.copy()
            longest_item_quantity_length = 9
            while repeat_clear_cart > 0:
                if len(str((read_longest_item_cart[1]))) > longest_item_quantity_length:
                    longest_item_quantity_length = len(str((read_longest_item_cart[1])))
                read_longest_item_cart.pop(0)
                read_longest_item_cart.pop(0)
                repeat_clear_cart = repeat_clear_cart - 1
            item_label = tk.Label(top, text="Item", font=(font_name, content_font_size))
            item_label.grid(sticky="ew", row=0, column=0, padx=50, pady=10)
            unit_price_label = tk.Label(top, text="Unit Price", font=(font_name, content_font_size))
            unit_price_label.grid(sticky="ew", row=0, column=1, padx=5, pady=10)
            quantity_label = tk.Label(top, text="Quantity", font=(font_name, content_font_size))
            quantity_label.grid(sticky="ew", row=0, column=2, padx=5, pady=10)
            price_label = tk.Label(top, text="Price", font=(font_name, content_font_size))
            price_label.grid(sticky="ew", row=0, column=3, padx=5, pady=10)
            rows = 2
            data = [(func_item_code_to_item_name(read_cart[i]), func_item_code_to_item_price(read_cart[i]), read_cart[i + 1], (func_item_code_to_item_price(read_cart[i]) * int(read_cart[i + 1]))) for i in range(0, len(read_cart), 2)]
            self.data = data
            price = 0
            for row in data:
                rows += 1
                col1_width = max(len(str(row[0])) for row in data) + 2
                col2_width = max(len(str(row[1])) for row in data) + 2
                col3_width = max(len(str(row[2])) for row in data) + 2
                col4_width = max(len(str(row[3])) for row in data) + 2
                item_name = str(row[0]).ljust(col1_width)
                unit_price = f"${row[1]:,.2f}".rjust(col2_width)
                item_code = str(row[2]).rjust(col3_width)
                price = float(price) + row[3]
                cart_price = f"${row[3]:,.2f}".rjust(col4_width)
                label = tk.Label(top, text=item_name, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=0)
                label = tk.Label(top, text=unit_price, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=1)
                label = tk.Label(top, text=item_code, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=2)
                label = tk.Label(top, text=cart_price, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=3)
            read_cart.clear()
            button = tk.Button(top, text="Confirm checkout", command=self.discounts, font=(font_name, content_font_size))
            button.grid(sticky="w", row=0, column=6, padx=5, pady=10)
            button = tk.Button(top, text="Return to main menu", command=top.destroy, font=(font_name, content_font_size))
            button.grid(sticky="w", row=0, column=5)
            label = tk.Label(top, text="Total Price:", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+1, column=2)
            discount = price
            label = tk.Label(top, text=f"${discount:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+1, column=3)

    def discounts(self):  # Comments: Ask which discount the user is eligible for
        top = tk.Toplevel()
        top.geometry(Width_height)
        label = tk.Label(top, text="Are you eligible for any discounts?", anchor="w", font=(font_name, content_font_size))
        label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        button = tk.Button(top, text="Seniors", command=self.seniorsdiscount)
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        button = tk.Button(top, text="Members", command=self.membersdiscount)
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        button = tk.Button(top, text="NS Men", command=self.nsmendiscount)
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        button = tk.Button(top, text="None", command=self.nonediscount)
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)

    def seniorsdiscount(self):  # Comments: Senior discount checkout
        global price
        price = 0
        top = tk.Toplevel()
        top.geometry(Width_height)
        read_cart = shopping_cart.copy()
        repeat_clear_cart = read_cart.count(0)
        while repeat_clear_cart > 0:
            repeat_clear_cart = repeat_clear_cart - 1
            clear_index_number = read_cart.index(0)
            read_cart.pop(clear_index_number - 1)
            read_cart.pop(clear_index_number - 1)
        repeat_clear_cart = len(read_cart) / 2
        # Comments: This code prompts the user when they want to view cart, but the shopping cart is empty
        if repeat_clear_cart == 0:
            label = tk.Label(top, text="There are no Items in the cart", font=(font_name, content_font_size))
            label.grid(sticky="w", row=0, column=0)
            button = tk.Button(top, text="Understood", command=top.destroy, font=(font_name, content_font_size))
            button.grid(sticky="w", row=1, column=0)
        else:
            read_longest_item_cart = read_cart.copy()
            longest_item_quantity_length = 9
            while repeat_clear_cart > 0:
                if len(str((read_longest_item_cart[1]))) > longest_item_quantity_length:
                    longest_item_quantity_length = len(str((read_longest_item_cart[1])))
                read_longest_item_cart.pop(0)
                read_longest_item_cart.pop(0)
                repeat_clear_cart = repeat_clear_cart - 1
            item_label = tk.Label(top, text="Item", font=(font_name, content_font_size))
            item_label.grid(sticky="ew", row=0, column=0, padx=50, pady=10)
            unit_price_label = tk.Label(top, text="Unit Price", font=(font_name, content_font_size))
            unit_price_label.grid(sticky="ew", row=0, column=1, padx=5, pady=10)
            quantity_label = tk.Label(top, text="Quantity", font=(font_name, content_font_size))
            quantity_label.grid(sticky="ew", row=0, column=2, padx=5, pady=10)
            price_label = tk.Label(top, text="Price", font=(font_name, content_font_size))
            price_label.grid(sticky="ew", row=0, column=3, padx=5, pady=10)
            rows = 2
            data = [(func_item_code_to_item_name(read_cart[i]), func_item_code_to_item_price(read_cart[i]),
                     read_cart[i + 1], (func_item_code_to_item_price(read_cart[i]) * int(read_cart[i + 1]))) for i in
                    range(0, len(read_cart), 2)]
            self.data = data
            price = 0
            for row in data:
                rows += 1
                col1_width = max(len(str(row[0])) for row in data) + 2
                col2_width = max(len(str(row[1])) for row in data) + 2
                col3_width = max(len(str(row[2])) for row in data) + 2
                col4_width = max(len(str(row[3])) for row in data) + 2
                item_name = str(row[0]).ljust(col1_width)
                unit_price = f"${row[1]:,.2f}".rjust(col2_width)
                item_code = str(row[2]).rjust(col3_width)
                price = float(price) + row[3]
                cart_price = f"${row[3]:,.2f}".rjust(col4_width)
                label = tk.Label(top, text=item_name, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=0)
                label = tk.Label(top, text=unit_price, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=1)
                label = tk.Label(top, text=item_code, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=2)
                label = tk.Label(top, text=cart_price, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=3)
            read_cart.clear()
            label = tk.Label(top, text="Total Price:", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+1, column=2)
            discount = price
            label = tk.Label(top, text=f"${discount:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+1, column=3)
            label = tk.Label(top, text="Discount:", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+2, column=2)
            discount = price * 0.10
            label = tk.Label(top, text=f"${discount:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+2, column=3)
            label = tk.Label(top, text="Discounted Price:", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+3, column=2)
            discounted_price = price - discount
            label = tk.Label(top, text=f"${discounted_price:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+3, column=3)
            label = tk.Label(top, text="GST(9%):", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+4, column=2)
            gst_amount = discounted_price * 0.09
            label = tk.Label(top, text=f"${gst_amount:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+4, column=3)
            label = tk.Label(top, text="Final Price:", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+5, column=2)
            final_price = discounted_price + gst_amount
            label = tk.Label(top, text=f"${final_price:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+5, column=3)
            button = tk.Button(top, text="  Leave  ", command=self.exit)
            button.grid(sticky="e", row=0, column=4)

    def membersdiscount(self):  # Comments: Members discount checkout
        global price
        price = 0
        top = tk.Toplevel()
        top.geometry(Width_height)
        read_cart = shopping_cart.copy()
        repeat_clear_cart = read_cart.count(0)
        while repeat_clear_cart > 0:
            repeat_clear_cart = repeat_clear_cart - 1
            clear_index_number = read_cart.index(0)
            read_cart.pop(clear_index_number - 1)
            read_cart.pop(clear_index_number - 1)
        repeat_clear_cart = len(read_cart) / 2
        # Comments: This code prompts the user when they want to view cart, but the shopping cart is empty
        if repeat_clear_cart == 0:
            label = tk.Label(top, text="There are no Items in the cart", font=(font_name, content_font_size))
            label.grid(sticky="w", row=0, column=0)
            button = tk.Button(top, text="Understood", command=top.destroy, font=(font_name, content_font_size))
            button.grid(sticky="w", row=1, column=0)
        else:
            read_longest_item_cart = read_cart.copy()
            longest_item_quantity_length = 9
            while repeat_clear_cart > 0:
                if len(str((read_longest_item_cart[1]))) > longest_item_quantity_length:
                    longest_item_quantity_length = len(str((read_longest_item_cart[1])))
                read_longest_item_cart.pop(0)
                read_longest_item_cart.pop(0)
                repeat_clear_cart = repeat_clear_cart - 1
            item_label = tk.Label(top, text="Item", font=(font_name, content_font_size))
            item_label.grid(sticky="ew", row=0, column=0, padx=50, pady=10)
            unit_price_label = tk.Label(top, text="Unit Price", font=(font_name, content_font_size))
            unit_price_label.grid(sticky="ew", row=0, column=1, padx=5, pady=10)
            quantity_label = tk.Label(top, text="Quantity", font=(font_name, content_font_size))
            quantity_label.grid(sticky="ew", row=0, column=2, padx=5, pady=10)
            price_label = tk.Label(top, text="Price", font=(font_name, content_font_size))
            price_label.grid(sticky="ew", row=0, column=3, padx=5, pady=10)
            rows = 2
            data = [(func_item_code_to_item_name(read_cart[i]), func_item_code_to_item_price(read_cart[i]),
                     read_cart[i + 1], (func_item_code_to_item_price(read_cart[i]) * int(read_cart[i + 1]))) for i in
                    range(0, len(read_cart), 2)]
            self.data = data
            price = 0
            for row in data:
                rows += 1
                col1_width = max(len(str(row[0])) for row in data) + 2
                col2_width = max(len(str(row[1])) for row in data) + 2
                col3_width = max(len(str(row[2])) for row in data) + 2
                col4_width = max(len(str(row[3])) for row in data) + 2
                item_name = str(row[0]).ljust(col1_width)
                unit_price = f"${row[1]:,.2f}".rjust(col2_width)
                item_code = str(row[2]).rjust(col3_width)
                price = float(price) + row[3]
                cart_price = f"${row[3]:,.2f}".rjust(col4_width)
                label = tk.Label(top, text=item_name, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=0)
                label = tk.Label(top, text=unit_price, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=1)
                label = tk.Label(top, text=item_code, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=2)
                label = tk.Label(top, text=cart_price, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=3)
            read_cart.clear()
            label = tk.Label(top, text="Total Price:", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+1, column=2)
            discount = price
            label = tk.Label(top, text=f"${discount:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+1, column=3)
            label = tk.Label(top, text="Discount:", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+2, column=2)
            discount = price * 0.08
            label = tk.Label(top, text=f"${discount:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+2, column=3)
            label = tk.Label(top, text="Discounted Price:", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+3, column=2)
            discounted_price = price - discount
            label = tk.Label(top, text=f"${discounted_price:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+3, column=3)
            label = tk.Label(top, text="GST(9%):", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+4, column=2)
            gst_amount = discounted_price * 0.09
            label = tk.Label(top, text=f"${gst_amount:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+4, column=3)
            label = tk.Label(top, text="Final Price:", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+5, column=2)
            final_price = discounted_price + gst_amount
            label = tk.Label(top, text=f"${final_price:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+5, column=3)
            button = tk.Button(top, text="  Leave  ", command=self.exit)
            button.grid(sticky="e", row=0, column=4)

    def nsmendiscount(self):  # Comments: NS men discount checkout
        global price
        price = 0
        top = tk.Toplevel()
        top.geometry(Width_height)
        read_cart = shopping_cart.copy()
        repeat_clear_cart = read_cart.count(0)
        while repeat_clear_cart > 0:
            repeat_clear_cart = repeat_clear_cart - 1
            clear_index_number = read_cart.index(0)
            read_cart.pop(clear_index_number - 1)
            read_cart.pop(clear_index_number - 1)
        repeat_clear_cart = len(read_cart) / 2
        # Comments: This code prompts the user when they want to view cart, but the shopping cart is empty
        if repeat_clear_cart == 0:
            label = tk.Label(top, text="There are no Items in the cart", font=(font_name, content_font_size))
            label.grid(sticky="w", row=0, column=0)
            button = tk.Button(top, text="Understood", command=top.destroy, font=(font_name, content_font_size))
            button.grid(sticky="w", row=1, column=0)
        else:
            read_longest_item_cart = read_cart.copy()
            longest_item_quantity_length = 9
            while repeat_clear_cart > 0:
                if len(str((read_longest_item_cart[1]))) > longest_item_quantity_length:
                    longest_item_quantity_length = len(str((read_longest_item_cart[1])))
                read_longest_item_cart.pop(0)
                read_longest_item_cart.pop(0)
                repeat_clear_cart = repeat_clear_cart - 1
            item_label = tk.Label(top, text="Item", font=(font_name, content_font_size))
            item_label.grid(sticky="ew", row=0, column=0, padx=50, pady=10)
            unit_price_label = tk.Label(top, text="Unit Price", font=(font_name, content_font_size))
            unit_price_label.grid(sticky="ew", row=0, column=1, padx=5, pady=10)
            quantity_label = tk.Label(top, text="Quantity", font=(font_name, content_font_size))
            quantity_label.grid(sticky="ew", row=0, column=2, padx=5, pady=10)
            price_label = tk.Label(top, text="Price", font=(font_name, content_font_size))
            price_label.grid(sticky="ew", row=0, column=3, padx=5, pady=10)
            rows = 2
            data = [(func_item_code_to_item_name(read_cart[i]), func_item_code_to_item_price(read_cart[i]),
                     read_cart[i + 1], (func_item_code_to_item_price(read_cart[i]) * int(read_cart[i + 1]))) for i in
                    range(0, len(read_cart), 2)]
            self.data = data
            price = 0
            for row in data:
                rows += 1
                col1_width = max(len(str(row[0])) for row in data) + 2
                col2_width = max(len(str(row[1])) for row in data) + 2
                col3_width = max(len(str(row[2])) for row in data) + 2
                col4_width = max(len(str(row[3])) for row in data) + 2
                item_name = str(row[0]).ljust(col1_width)
                unit_price = f"${row[1]:,.2f}".rjust(col2_width)
                item_code = str(row[2]).rjust(col3_width)
                price = float(price) + row[3]
                cart_price = f"${row[3]:,.2f}".rjust(col4_width)
                label = tk.Label(top, text=item_name, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=0)
                label = tk.Label(top, text=unit_price, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=1)
                label = tk.Label(top, text=item_code, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=2)
                label = tk.Label(top, text=cart_price, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=3)
            read_cart.clear()
            label = tk.Label(top, text="Total Price:", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+1, column=2)
            discount = price
            label = tk.Label(top, text=f"${discount:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+1, column=3)
            label = tk.Label(top, text="Discount:", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+2, column=2)
            discount = price * 0.05
            label = tk.Label(top, text=f"${discount:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+2, column=3)
            label = tk.Label(top, text="Discounted Price:", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+3, column=2)
            discounted_price = price - discount
            label = tk.Label(top, text=f"${discounted_price:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+3, column=3)
            label = tk.Label(top, text="GST(9%):", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+4, column=2)
            gst_amount = discounted_price * 0.09
            label = tk.Label(top, text=f"${gst_amount:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+4, column=3)
            label = tk.Label(top, text="Final Price:", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+5, column=2)
            final_price = discounted_price + gst_amount
            label = tk.Label(top, text=f"${final_price:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+5, column=3)
            button = tk.Button(top, text="  Leave  ", command=self.exit)
            button.grid(sticky="e", row=0, column=4)

    def nonediscount(self):  # Comments: No discount checkout
        global price
        price = 0
        top = tk.Toplevel()
        top.geometry(Width_height)
        read_cart = shopping_cart.copy()
        repeat_clear_cart = read_cart.count(0)
        while repeat_clear_cart > 0:
            repeat_clear_cart = repeat_clear_cart - 1
            clear_index_number = read_cart.index(0)
            read_cart.pop(clear_index_number - 1)
            read_cart.pop(clear_index_number - 1)
        repeat_clear_cart = len(read_cart) / 2
        # Comments: This code prompts the user when they want to view cart, but the shopping cart is empty
        if repeat_clear_cart == 0:
            label = tk.Label(top, text="There are no Items in the cart", font=(font_name, content_font_size))
            label.grid(sticky="w", row=0, column=0)
            button = tk.Button(top, text="Understood", command=top.destroy, font=(font_name, content_font_size))
            button.grid(sticky="w", row=1, column=0)
        else:
            read_longest_item_cart = read_cart.copy()
            longest_item_quantity_length = 9
            while repeat_clear_cart > 0:
                if len(str((read_longest_item_cart[1]))) > longest_item_quantity_length:
                    longest_item_quantity_length = len(str((read_longest_item_cart[1])))
                read_longest_item_cart.pop(0)
                read_longest_item_cart.pop(0)
                repeat_clear_cart = repeat_clear_cart - 1
            item_label = tk.Label(top, text="Item", font=(font_name, content_font_size))
            item_label.grid(sticky="ew", row=0, column=0, padx=50, pady=10)
            unit_price_label = tk.Label(top, text="Unit Price", font=(font_name, content_font_size))
            unit_price_label.grid(sticky="ew", row=0, column=1, padx=5, pady=10)
            quantity_label = tk.Label(top, text="Quantity", font=(font_name, content_font_size))
            quantity_label.grid(sticky="ew", row=0, column=2, padx=5, pady=10)
            price_label = tk.Label(top, text="Price", font=(font_name, content_font_size))
            price_label.grid(sticky="ew", row=0, column=3, padx=5, pady=10)
            rows = 2
            data = [(func_item_code_to_item_name(read_cart[i]), func_item_code_to_item_price(read_cart[i]),
                     read_cart[i + 1], (func_item_code_to_item_price(read_cart[i]) * int(read_cart[i + 1]))) for i in
                    range(0, len(read_cart), 2)]
            self.data = data
            price = 0
            for row in data:
                rows += 1
                col1_width = max(len(str(row[0])) for row in data) + 2
                col2_width = max(len(str(row[1])) for row in data) + 2
                col3_width = max(len(str(row[2])) for row in data) + 2
                col4_width = max(len(str(row[3])) for row in data) + 2
                item_name = str(row[0]).ljust(col1_width)
                unit_price = f"${row[1]:,.2f}".rjust(col2_width)
                item_code = str(row[2]).rjust(col3_width)
                price = float(price) + row[3]
                cart_price = f"${row[3]:,.2f}".rjust(col4_width)
                label = tk.Label(top, text=item_name, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=0)
                label = tk.Label(top, text=unit_price, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=1)
                label = tk.Label(top, text=item_code, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=2)
                label = tk.Label(top, text=cart_price, font=(font_name, content_font_size))
                label.grid(sticky="e", row=rows, column=3)
            read_cart.clear()
            label = tk.Label(top, text="Total Price:", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+1, column=2)
            discount = price
            label = tk.Label(top, text=f"${discount:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+1, column=3)
            label = tk.Label(top, text="Discount:", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+2, column=2)
            discount = price * 0
            label = tk.Label(top, text=f"${discount:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+2, column=3)
            label = tk.Label(top, text="Discounted Price:", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+3, column=2)
            discounted_price = price - discount
            label = tk.Label(top, text=f"${discounted_price:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+3, column=3)
            label = tk.Label(top, text="GST(9%):", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+4, column=2)
            gst_amount = discounted_price * 0.09
            label = tk.Label(top, text=f"${gst_amount:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+4, column=3)
            label = tk.Label(top, text="Final Price:", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+5, column=2)
            final_price = discounted_price + gst_amount
            label = tk.Label(top, text=f"${final_price:.2f}", font=(font_name, content_font_size))
            label.grid(sticky="e", row=rows+5, column=3)
            button = tk.Button(top, text="  Leave  ", command=self.exit)
            button.grid(sticky="e", row=0, column=4)

    @staticmethod
    def exit():  # Comments: Leave after checkout
        exit()


class LeaveWindow: # Comments: Handling leaving
    def __init__(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        # Comments: This code checks if the shopping cart is empty
        read_cart = []
        read_cart = shopping_cart.copy()
        repeat_clear_cart = read_cart.count(0)
        while repeat_clear_cart > 0:
            repeat_clear_cart = repeat_clear_cart - 1
            clear_index_number = read_cart.index(0)
            read_cart.pop(clear_index_number - 1)
            read_cart.pop(clear_index_number - 1)
        repeat_clear_cart = len(read_cart) / 2
        # Comments: This code prompts the user when they want to leave, but the shopping cart is not empty
        if repeat_clear_cart != 0:
            item_code_textbox_label = tk.Label(top, text="There are items in your shopping cart. Are you sure you wanna leave?", anchor="w", font=(font_name, content_font_size))
            item_code_textbox_label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
            yes_button = tk.Button(top, text="Yes", command=self.exit_true)
            yes_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
            no_button = tk.Button(top, text="No", command=top.destroy)
            no_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)

        else:
            exit()

    @staticmethod
    def exit_true():  # Comments: Leave without items in cart
        exit()


class ViewCatalogueWindow:  # Comments: Displays Catalogue
    def __init__(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        label = tk.Label(top, anchor="w", text="Drinks (CD10)", font=(font_name, header_font_size))
        label.grid(row=0, column=0)
        label = tk.Label(top, anchor="w", text="Item:\tNeo's Green Tea\t\t\tCode: N32\tPrice: 3.00", font=(font_name, content_font_size - 0))
        label.grid(row=1, column=1)
        label = tk.Label(top, anchor="w", text="Item:\tMelo Chocolate Malt Drink\t\tCode: M13\tPrice: 2.85", font=(font_name, content_font_size - 0))
        label.grid(row=2, column=1)
        label = tk.Label(top, anchor="w", text="Item:\tVery-Fair Full Cream Milk\t\tCode: V76\tPrice: 3.50", font=(font_name, content_font_size - 0))
        label.grid(row=3, column=1)
        label = tk.Label(top, anchor="w", text="Item:\tNirigold UHT Milk\t\t\tCode: N14\tPrice: 4.15", font=(font_name, content_font_size - 0))
        label.grid(row=4, column=1)
        label = tk.Label(top, anchor="w", text="Beer (CB20)", font=(font_name, header_font_size))
        label.grid(row=5, column=0)
        label = tk.Label(top, anchor="w", text="Item:\tLion (24 x 320 ml)\t\t\tCode: L11\tPrice: 52.00", font=(font_name, content_font_size - 0))
        label.grid(row=6, column=1)
        label = tk.Label(top, anchor="w", text="Item:\tPanda (24 x 320 ml)\t\tCode: P21\tPrice: 78.00", font=(font_name, content_font_size - 0))
        label.grid(row=7, column=1)
        label = tk.Label(top, anchor="w", text="Item:\tAxe (24 x 320 ml)\t\t\tCode: A54\tPrice: 58.00", font=(font_name, content_font_size - 0))
        label.grid(row=8, column=1)
        label = tk.Label(top, anchor="w", text="Item:\tHenekan (24 x 320 ml)\t\tCode: H91\tPrice: 68.00", font=(font_name, content_font_size - 0))
        label.grid(row=9, column=1)
        label = tk.Label(top, anchor="w", text="Frozen (CF30)", font=(font_name, header_font_size))
        label.grid(row=10, column=0)
        label = tk.Label(top, anchor="w", text="Item:\tEdker Ristorante Pizza 355g\t\tCode: E11\tPrice: 6.95", font=(font_name, content_font_size - 0))
        label.grid(row=11, column=1)
        label = tk.Label(top, anchor="w", text="Item:\tFazzler Frozen Soup 500g\t\tCode: F43\tPrice: 5.15", font=(font_name, content_font_size - 0))
        label.grid(row=12, column=1)
        label = tk.Label(top, anchor="w", text="Item:\tCP Frozen Ready Meal 250g\t\tCode: CP31\tPrice: 4.12", font=(font_name, content_font_size - 0))
        label.grid(row=13, column=1)
        label = tk.Label(top, anchor="w", text="Item:\tDuitoni Cheese 270g\t\tCode: D72\tPrice: 5.60", font=(font_name, content_font_size - 0))
        label.grid(row=14, column=1)
        label = tk.Label(top, anchor="w", text="Household (CH40)", font=(font_name, header_font_size))
        label.grid(row=15, column=0)
        label = tk.Label(top, anchor="w", text="Item:\tFP Facial Tissues\t\t\tCode: FP76\tPrice: 9.50", font=(font_name, content_font_size - 0))
        label.grid(row=16, column=1)
        label = tk.Label(top, anchor="w", text="Item:\tFP Premium Kitchen Towel\t\tCode: FP32\tPrice: 5.85", font=(font_name, content_font_size - 0))
        label.grid(row=17, column=1)
        label = tk.Label(top, anchor="w", text="Item:\tKlinex Toilet Tissue Rolls\t\tCode: K22\tPrice: 7.50", font=(font_name, content_font_size - 0))
        label.grid(row=18, column=1)
        label = tk.Label(top, anchor="w", text="Item:\tDanny Softener\t\t\tCode: D14\tPrice: 9.85", font=(font_name, content_font_size - 0))
        label.grid(row=19, column=1)
        label = tk.Label(top, anchor="w", text="Snacks (CS50)", font=(font_name, header_font_size))
        label.grid(row=20, column=0)
        label = tk.Label(top, anchor="w", text="Item:\tSingshort Seaweed\t\t\tCode: SS93\tPrice: 3.10", font=(font_name, content_font_size - 0))
        label.grid(row=21, column=1)
        label = tk.Label(top, anchor="w", text="Item:\tMei Crab Cracker\t\t\tCode: MC14\tPrice: 2.05", font=(font_name, content_font_size - 0))
        label.grid(row=22, column=1)
        label = tk.Label(top, anchor="w", text="Item:\tReo Pokemon Cookie\t\tCode: R35\tPrice: 4.80", font=(font_name, content_font_size - 0))
        label.grid(row=23, column=1)
        label = tk.Label(top, anchor="w", text="Item:\tHuat Seng Crackers\t\t\tCode: HS11\tPrice: 3.55", font=(font_name, content_font_size - 0))
        label.grid(row=24, column=1)
        item_code_textbox_label = tk.Label(top, text="Input item code if you would like to shop by item code:", anchor="w", font=(font_name, content_font_size))
        item_code_textbox_label.grid(row=1, column=3)
        self.textbox = tk.Text(top, height=2)
        self.textbox.grid(row=2, column=3)
        submit_item_code_button = tk.Button(top, text="Submit item code", command=self.item_code, font=(font_name, content_font_size))
        submit_item_code_button.grid(row=3, column=3)
        main_menu_button = tk.Button(top, text="Return to main menu", command=top.destroy, font=(font_name, content_font_size))
        main_menu_button.grid(row=4, column=3)

    def item_code(self):    # Comments: Handles item code inputs
        input_value = self.textbox.get('1.0', tk.END)
        input_value = str(input_value)
        input_value = input_value.replace("\n", "")
        if input_value in list_item_code:
            input_value = list_item_code.index(input_value)
            if input_value == 0:
                item("N32")
            if input_value == 1:
                item("M13")
            if input_value == 2:
                item("V76")
            if input_value == 3:
                item("N14")
            if input_value == 4:
                Lion24x320ml()
            if input_value == 5:
                Panda24x320ml()
            if input_value == 6:
                Axe24x320ml()
            if input_value == 7:
                Henekan24x320ml()
            if input_value == 8:
                item("E11")
            if input_value == 9:
                item("F43")
            if input_value == 10:
                item("CP31")
            if input_value == 11:
                item("D72")
            if input_value == 12:
                item("FP76")
            if input_value == 13:
                item("FP32")
            if input_value == 14:
                item("K22")
            if input_value == 15:
                item("D14")
            if input_value == 16:
                item("SS93")
            if input_value == 17:
                item("MC14")
            if input_value == 18:
                item("R35")
            if input_value == 19:
                item("HS11")


class ViewCategoryWindow:   # Comments: View Category Window
    def __init__(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        drinks_cd10_button = tk.Button(top, text="Drinks (CD10)", command=self.category_drinks_cd10, font=(font_name, content_font_size))
        drinks_cd10_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        beer_cb20_button = tk.Button(top, text="Beer (CB20)", command=self.category_beer_cb20, font=(font_name, content_font_size))
        beer_cb20_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        frozen_cf30_button = tk.Button(top, text="Frozen (CF30)", command=self.category_frozen_cf30, font=(font_name, content_font_size))
        frozen_cf30_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        household_ch40_button = tk.Button(top, text="Household (CH40)", command=self.category_household_ch40, font=(font_name, content_font_size))
        household_ch40_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        snacks_cs50_button = tk.Button(top, text="Snacks (CS50)", command=self.category_snacks_cs50, font=(font_name, content_font_size))
        snacks_cs50_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        main_menu_button = tk.Button(top, text="Return to main menu", command=top.destroy, font=(font_name, content_font_size))
        main_menu_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        button = tk.Button(top, text="Flash Sale", command=self.notimplemented, font=(font_name, content_font_size))
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        button = tk.Button(top, text="Clearance Sale", command=self.notimplemented, font=(font_name, content_font_size))
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        item_code_textbox_label = tk.Label(top, text="Input item code if you would like to shop by item code:", anchor="w", font=(font_name, content_font_size))
        item_code_textbox_label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        self.textbox = tk.Text(top, height=2)
        self.textbox.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        submit_item_code_button = tk.Button(top, text="Submit item code", command=self.item_code, font=(font_name, content_font_size))
        submit_item_code_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)

    @staticmethod
    def notimplemented():
        top = tk.Toplevel()
        top.geometry('2900x2700')
        label = tk.Label(top, text="This function has not be implemented yet\nPlease come back in the future to check for more updates", anchor="w", font=(font_name, content_font_size))
        label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        button = tk.Button(top, text="Understood", command=top.destroy, font=(font_name, content_font_size))
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)

    def item_code(self):
        input_value = self.textbox.get('1.0', tk.END)
        input_value = str(input_value)
        input_value = input_value.replace("\n", "")
        if input_value in list_item_code:
            input_value = list_item_code.index(input_value)
            if input_value == 0:
                item("N32")
            if input_value == 1:
                item("M13")
            if input_value == 2:
                item("V76")
            if input_value == 3:
                item("N14")
            if input_value == 4:
                Lion24x320ml()
            if input_value == 5:
                Panda24x320ml()
            if input_value == 6:
                Axe24x320ml()
            if input_value == 7:
                Henekan24x320ml()
            if input_value == 8:
                item("E11")
            if input_value == 9:
                item("F43")
            if input_value == 10:
                item("CP31")
            if input_value == 11:
                item("D72")
            if input_value == 12:
                item("FP76")
            if input_value == 13:
                item("FP32")
            if input_value == 14:
                item("K22")
            if input_value == 15:
                item("D14")
            if input_value == 16:
                item("SS93")
            if input_value == 17:
                item("MC14")
            if input_value == 18:
                item("R35")
            if input_value == 19:
                item("HS11")

    @staticmethod
    def category_drinks_cd10():
        DrinksCD10window()

    @staticmethod
    def category_beer_cb20():
        BeerCB20window()

    @staticmethod
    def category_frozen_cf30():
        FrozenCF30window()

    @staticmethod
    def category_household_ch40():
        HouseholdCH40window()

    @staticmethod
    def category_snacks_cs50():
        SnacksCS50window()


class DrinksCD10window:  # Comments: This is the code for the drinks window
    def __init__(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        drinks_cd10_label = tk.Label(top, text="Drinks (CD10)", font=(font_name, header_font_size))
        drinks_cd10_label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        neo_s_green_tea_button = tk.Button(top, text="Neo's Green Tea", command=self.neosgreenteawindow, font=(font_name, content_font_size))
        neo_s_green_tea_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        melo_chocolate_malt_drink_button = tk.Button(top, text="Melo Chocolate Malt Drink", command=self.melochocolatemaltdrinkwindow, font=(font_name, content_font_size))
        melo_chocolate_malt_drink_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        very_fair_full_cream_milk_button = tk.Button(top, text="Very-Fair Full Cream Milk", command=self.veryfairfullcreammilkwindow, font=(font_name, content_font_size))
        very_fair_full_cream_milk_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        nirigold_uht_milk_button = tk.Button(top, text="Nirigold UHT Milk", command=self.nirigolduhtmilkwindow, font=(font_name, content_font_size))
        nirigold_uht_milk_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        view_category_button = tk.Button(top, text="Return to categories", command=top.destroy, font=(font_name, content_font_size))
        view_category_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
    @staticmethod
    def neosgreenteawindow():
        item("N32")     # Comments: Shopping for item function
    @staticmethod
    def melochocolatemaltdrinkwindow():
        item("M13")     # Comments: Shopping for item function
    @staticmethod
    def veryfairfullcreammilkwindow():
        item("V76")     # Comments: Shopping for item function
    @staticmethod
    def nirigolduhtmilkwindow():
        item("N14")     # Comments: Shopping for item function


class BeerCB20window:  # Comments: This is the code for the beer window
    def __init__(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        beer_cb20_label = tk.Label(top, text="Beer CB20", font=(font_name, header_font_size))
        beer_cb20_label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        lion_24_x_320_ml_button = tk.Button(top, text="Lion (24 x 320 ml)", command=self.lion24x320mlwindow, font=(font_name, content_font_size))
        lion_24_x_320_ml_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        panda_24_x_320_ml_button = tk.Button(top, text="Panda (24 x 320 ml)", command=self.panda24x320mlwindow, font=(font_name, content_font_size))
        panda_24_x_320_ml_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        axe_24_x_320_ml_button = tk.Button(top, text="Axe (24 x 320 ml)", command=self.axe24x320mlwindow, font=(font_name, content_font_size))
        axe_24_x_320_ml_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        henekan_24_x_320_ml_button = tk.Button(top, text="Henekan (24 x 320 ml)", command=self.henekan24x320mlwindow, font=(font_name, content_font_size))
        henekan_24_x_320_ml_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        view_category_button = tk.Button(top, text="Return to categories", command=top.destroy, font=(font_name, content_font_size))
        view_category_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
    @staticmethod
    def lion24x320mlwindow():
        Lion24x320ml()          # Comments: checking age before buying beer function
    @staticmethod
    def panda24x320mlwindow():
        Panda24x320ml()         # Comments: checking age before buying beer function
    @staticmethod
    def axe24x320mlwindow():
        Axe24x320ml()           # Comments: checking age before buying beer function
    @staticmethod
    def henekan24x320mlwindow():
        Henekan24x320ml()       # Comments: checking age before buying beer function


class FrozenCF30window:  # Comments: This is the code for the frozen window
    def __init__(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        frozen_cf30_label = tk.Label(top, text="Frozen CF30", font=(font_name, header_font_size))
        frozen_cf30_label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        edker_ristorante_pizza_355g_button = tk.Button(top, text="Edker Ristorante Pizza 355g", command=self.edkerristorantepizza355gwindow, font=(font_name, content_font_size))
        edker_ristorante_pizza_355g_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        fazzler_frozen_soup_500g_button = tk.Button(top, text="Fazzler Frozen Soup 500g", command=self.fazzlerfrozensoup500gwindow, font=(font_name, content_font_size))
        fazzler_frozen_soup_500g_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        cp_frozen_ready_meal_250g_button = tk.Button(top, text="CP Frozen Ready Meal 250g", command=self.cpfrozenreadymeal250gwindow, font=(font_name, content_font_size))
        cp_frozen_ready_meal_250g_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        duitoni_cheese_270g_button = tk.Button(top, text="Duitoni Cheese 270g", command=self.duitonicheese270gwindow, font=(font_name, content_font_size))
        duitoni_cheese_270g_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        view_category_button = tk.Button(top, text="Return to categories", command=top.destroy, font=(font_name, content_font_size))
        view_category_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
    @staticmethod
    def edkerristorantepizza355gwindow():
        item("E11")     # Comments: Shopping for item function
    @staticmethod
    def fazzlerfrozensoup500gwindow():
        item("F43")     # Comments: Shopping for item function
    @staticmethod
    def cpfrozenreadymeal250gwindow():
        item("CP31")    # Comments: Shopping for item function
    @staticmethod
    def duitonicheese270gwindow():
        item("D72")     # Comments: Shopping for item function


class HouseholdCH40window:  # Comments: This is the code for the household window
    def __init__(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        household_ch40_label = tk.Label(top, text="Household CH40", font=(font_name, header_font_size))
        household_ch40_label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        fp_facial_tissues_button = tk.Button(top, text="FP Facial Tissues", command=self.fpfacialtissueswindow, font=(font_name, content_font_size))
        fp_facial_tissues_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        fp_premium_kitchen_towel_button = tk.Button(top, text="FP Premium Kitchen Towel", command=self.fppremiumkitchentowelwindow, font=(font_name, content_font_size))
        fp_premium_kitchen_towel_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        klinex_toilet_tissue_rolls_button = tk.Button(top, text="Klinex Toilet Tissue Rolls", command=self.klinextoilettissuerollswindow, font=(font_name, content_font_size))
        klinex_toilet_tissue_rolls_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        danny_softener_button = tk.Button(top, text="Danny Softener", command=self.dannysoftenerwindow, font=(font_name, content_font_size))
        danny_softener_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        view_category_button = tk.Button(top, text="Return to categories", command=top.destroy, font=(font_name, content_font_size))
        view_category_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
    @staticmethod
    def fpfacialtissueswindow():
        item("FP76")    # Comments: Shopping for item function
    @staticmethod
    def fppremiumkitchentowelwindow():
        item("FP32")    # Comments: Shopping for item function
    @staticmethod
    def klinextoilettissuerollswindow():
        item("K22")     # Comments: Shopping for item function
    @staticmethod
    def dannysoftenerwindow():
        item("D14")     # Comments: Shopping for item function


class SnacksCS50window:  # Comments: This is the code for the snacks window
    def __init__(self):
        top = tk.Toplevel()
        top.geometry(Width_height)
        snacks_cs50_label = tk.Label(top, text="Snacks CS50", font=(font_name, header_font_size))
        snacks_cs50_label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        singshort_seaweed_button = tk.Button(top, text="Singshort Seaweed", command=self.singshortseaweedwindow, font=(font_name, content_font_size))
        singshort_seaweed_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        mei_crab_cracker_button = tk.Button(top, text="Mei Crab Cracker", command=self.meicrabcrackerwindow, font=(font_name, content_font_size))
        mei_crab_cracker_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        reo_pokemon_cookie_button = tk.Button(top, text="Reo Pokemon Cookie", command=self.reopokemoncookiewindow, font=(font_name, content_font_size))
        reo_pokemon_cookie_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        huat_seng_crackers_button = tk.Button(top, text="Huat Seng Crackers", command=self.huatsengcrackerswindow, font=(font_name, content_font_size))
        huat_seng_crackers_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        view_category_button = tk.Button(top, text="Return to categories", command=top.destroy, font=(font_name, content_font_size))
        view_category_button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
    @staticmethod
    def singshortseaweedwindow():
        item("SS93")    # Comments: Shopping for item function
    @staticmethod
    def meicrabcrackerwindow():
        item("MC14")    # Comments: Shopping for item function
    @staticmethod
    def reopokemoncookiewindow():
        item("R35")     # Comments: Shopping for item function
    @staticmethod
    def huatsengcrackerswindow():
        item("HS11")    # Comments: Shopping for item function


class Lion24x320ml:             # Comments: This is the code to check if you are above 18 y/o to buy beer
    def __init__(self):
        top = tk.Toplevel()
        top.geometry('2900x2700')
        label = tk.Label(top, text="To buy beer items, you need to be older than 18 y/o.\nAre you older than 18 y/o? (y/n): ", anchor="w", font=(font_name, content_font_size))
        label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        self.root = top
        button = tk.Button(top, text="No, I'm under 18 y/o", command=top.destroy, font=(font_name, content_font_size))
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        button = tk.Button(top, text="Yes, I'm above 18 y/o", command=self.confirm, font=(font_name, content_font_size))
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)

    def confirm(self):          # Comments: This closes the parent window before opening the shopping window
        self.root.destroy()
        item("L11")             # Comments: Shopping for item function


class Panda24x320ml:             # Comments: This is the code to check if you are above 18 y/o to buy beer
    def __init__(self):
        top = tk.Toplevel()
        top.geometry('2900x2700')
        label = tk.Label(top, text="To buy beer items, you need to be older than 18 y/o.\nAre you older than 18 y/o? (y/n): ", anchor="w", font=(font_name, content_font_size))
        label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        self.root = top
        button = tk.Button(top, text="No, I'm under 18 y/o", command=top.destroy, font=(font_name, content_font_size))
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        button = tk.Button(top, text="Yes, I'm above 18 y/o", command=self.confirm, font=(font_name, content_font_size))
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)

    def confirm(self):          # Comments: This closes the parent window before opening the shopping window
        self.root.destroy()
        item("P21")             # Comments: Shopping for item function


class Axe24x320ml:             # Comments: This is the code to check if you are above 18 y/o to buy beer
    def __init__(self):
        top = tk.Toplevel()
        top.geometry('2900x2700')
        label = tk.Label(top, text="To buy beer items, you need to be older than 18 y/o.\nAre you older than 18 y/o? (y/n): ", anchor="w", font=(font_name, content_font_size))
        label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        self.root = top
        button = tk.Button(top, text="No, I'm under 18 y/o", command=top.destroy, font=(font_name, content_font_size))
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        button = tk.Button(top, text="Yes, I'm above 18 y/o", command=self.confirm, font=(font_name, content_font_size))
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)

    def confirm(self):          # Comments: This closes the parent window before opening the shopping window
        self.root.destroy()
        item("A54")             # Comments: Shopping for item function


class Henekan24x320ml:          # Comments: This is the code to check if you are above 18 y/o to buy beer
    def __init__(self):
        top = tk.Toplevel()
        top.geometry('2900x2700')
        label = tk.Label(top, text="To buy beer items, you need to be older than 18 y/o.\nAre you older than 18 y/o? (y/n): ", anchor="w", font=(font_name, content_font_size))
        label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        self.root = top
        button = tk.Button(top, text="No, I'm under 18 y/o", command=top.destroy, font=(font_name, content_font_size))
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        button = tk.Button(top, text="Yes, I'm above 18 y/o", command=self.confirm, font=(font_name, content_font_size))
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)

    def confirm(self):          # Comments: This closes the parent window before opening the shopping window
        self.root.destroy()
        item("H91")             # Comments: Shopping for item function


class Keypad(tk.Frame):     # Comments: This is the keypad code
    def __init__(self, code, root, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = root
        top = root
        self.code_in_hand = code
        item_in_hand = func_item_code_to_item_name(self.code_in_hand).replace("\t", "")
        words = ("You have", shopping_cart[shopping_cart.index(self.code_in_hand) + 1], str(item_in_hand), "in your cart")
        words = str(words).replace(",", "").replace('"', "").replace("'", "").replace("(", "").replace(")", "")
        label = tk.Label(top, text=words, font=(font_name, content_font_size))
        label.grid(row=0, column=0, sticky='w')
        words = 'How many ' + str(item_in_hand) + ' would you like?'
        label = tk.Label(top, text=words, font=(font_name, content_font_size))  # Comments: Adding label to give the scenario some context
        label.grid(row=1, column=0, sticky='w')                                 # Comments: Adding the buttons to the keypad
        b = tk.Button(top, text=' 1 ', command=lambda btntext=item: self.append('1'), font=(font_name, content_font_size))
        b.grid(row=2, column=1, sticky='news')
        b = tk.Button(top, text=' 2 ', command=lambda btntext=item: self.append('2'), font=(font_name, content_font_size))
        b.grid(row=2, column=2, sticky='news')
        b = tk.Button(top, text=' 3 ', command=lambda btntext=item: self.append('3'), font=(font_name, content_font_size))
        b.grid(row=2, column=3, sticky='news')
        b = tk.Button(top, text=' 4 ', command=lambda btntext=item: self.append('4'), font=(font_name, content_font_size))
        b.grid(row=3, column=1, sticky='news')
        b = tk.Button(top, text=' 5 ', command=lambda btntext=item: self.append('5'), font=(font_name, content_font_size))
        b.grid(row=3, column=2, sticky='news')
        b = tk.Button(top, text=' 6 ', command=lambda btntext=item: self.append('6'), font=(font_name, content_font_size))
        b.grid(row=3, column=3, sticky='news')
        b = tk.Button(top, text=' 7 ', command=lambda btntext=item: self.append('7'), font=(font_name, content_font_size))
        b.grid(row=4, column=1, sticky='news')
        b = tk.Button(top, text=' 8 ', command=lambda btntext=item: self.append('8'), font=(font_name, content_font_size))
        b.grid(row=4, column=2, sticky='news')
        b = tk.Button(top, text=' 9 ', command=lambda btntext=item: self.append('9'), font=(font_name, content_font_size))
        b.grid(row=4, column=3, sticky='news')
        b = tk.Button(top, text=' 0 ', command=lambda btntext=item: self.append('0'), font=(font_name, content_font_size))
        b.grid(row=5, column=2, sticky='news')
        btn_backspace = tk.Button(top, text='Backspace', command=self.backspace, font=(font_name, content_font_size))
        btn_backspace.grid(row=2, column=10, sticky='news')
        btn_enter = tk.Button(top, text='Enter', command=self.enter, font=(font_name, content_font_size))
        btn_enter.grid(row=4, column=10, sticky='news')
        btn_clear = tk.Button(top, text='Clear', command=self.clear, font=(font_name, content_font_size))
        btn_clear.grid(row=3, column=10, sticky='news')
        btn_close = tk.Button(top, text='Close', command=self.close_window, font=(font_name, content_font_size))
        btn_close.grid(row=5, column=10, columnspan=11, sticky='news')

    def enter(self):                            # Comments: This code checks if the textbox value is valid
        if self.target:
            words = self.get().replace(" ", "")
            if words.isdigit():
                how_many = int(words)
                if 0 <= how_many < (quantity_upper_limit + 1):
                    shopping_cart[shopping_cart.index(self.code_in_hand) + 1] = how_many
                    self.event_success()
                else:
                    self.event_error_overflow()
            else:
                self.event_error_overflow()

    def get(self):                              # Comments: This code gets the character in the textbox
        if self.target:
            return self.target.get()

    def append(self, words):                    # Comments: This code add the word to the back of the textbox
        if self.target:
            self.target.insert('end', words)

    def clear(self):                            # Comments: This code clears all the characters in the textbox (clear button)
        if self.target:
            self.target.delete(0, 'end')

    def backspace(self):                        # Comments: This code deletes the last character in the textbox (backspace button)
        if self.target:
            words = self.get()[:-1]
            self.clear()
            self.append(words)

    def close_window(self):                     # Comments: This code closes the current window
        self.root.destroy()

    def show(self, entry):                      # Comments: This code displays the keypad
        self.target = entry
        self.place(relx=0.5, rely=0.5, anchor='c')

    def event_success(self):                    # Comments: This code runs when the user inputs a valid input
        top = tk.Toplevel(self.root)
        top.geometry('2900x2700')
        label = tk.Label(top, text="Item successfully added to cart, please close the window to refresh the quantity", anchor="w", font=(font_name, content_font_size))
        label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        button = tk.Button(top, text="Understood", command=top.destroy, font=(font_name, content_font_size))
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)

    def event_error_overflow(self):             # Comments: This code runs when the user inputs in an invalid input
        top = tk.Toplevel(self.root)
        top.geometry('2900x2700')
        oopstext = f"Oops! Please enter a quantity more than 0 and less than {quantity_upper_limit}."
        label = tk.Label(top, text=oopstext, anchor="w", font=(font_name, content_font_size))
        label.pack(fill='both', padx=default_pad_x, pady=default_pad_y)
        button = tk.Button(top, text="Understood", command=top.destroy, font=(font_name, content_font_size))
        button.pack(fill='both', padx=default_pad_x, pady=default_pad_y)


def item(code):                                 # Comments: This is the code which the user sees when shopping
    top = tk.Toplevel()                         # Comments: link the window to the variable top
    top.geometry('2900x2700')                   # Comments: set the window dimension
    keypad = Keypad(code, top)                  # Comments: Insert the keypad and other widgets
    keypad.pack()                               # Comments: Pack all the widgets together
    f = tk.Frame(top)                           # Comments: This code frames and add all the widgets together
    f.grid(padx=0, pady=0)                      # Comments: This code makes the frame go to 0, 0 relative
    e1 = tk.Entry(f)                            # Comments: This code adds the textbox
    e1.grid(row=0, column=0, sticky='news')     # Comments: This code sets the textbox to 0, 0
    keypad.show(e1)                             # Comments: This code displays the keypad

    top.mainloop()


def start_gui():                    # Comments: This is the start GUI code
    root = tk.Tk()                  # Comments: This code assigns the window to root
    root.geometry(Width_height)     # Comments: This code sets the dimension of the window
    MainMenuWindow(root)            # Comments: This code adds the respective widgets to the window
    root.mainloop()                 # Comments: This is the mainloop, which runs the GUI


start()                             # Comments: This is the start of the program
