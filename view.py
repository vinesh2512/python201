import controller


# function to display the main menu
def print_menu():
    print('\n----------- MAIN MENU -----------\n')
    print('Select a menu option:')
    print('[A]: Show all products.')
    print('[B]: Create a new product.')
    print('[C]: Search product by ID.')
    print('[D]: Update product by ID.')
    print('[E]: Delete product by ID.\n')
    print('[X]: Quit application.\n')
    main_menu_selection = input('Please Enter your selection: ')
    print('---------------------------------')
    return main_menu_selection


# function to list dict of items
def print_all_items(items):
    print('\n--------- PRODUCT LIST ----------')
    for item in items:
        print('---------------------------------')
        print('Product ID:', item['id'])
        print('Product Name:', item['name'])
        print('Product Price:', item['price'])
        if item['is_offer']:
            print('**** ITEM ON SALE! ****')
    print('---------------------------------')


# function to return to main menu and exit application
def return_to_menu():
    while True:
        return_menu = input('\nType [R] to return to main menu | [X] to exit application: ')
        if return_menu == 'r' or return_menu == 'R':
            controller.start_up()
        elif return_menu == 'x' or return_menu == 'X':
            print('\nShutting Down....')
            quit()
        else:
            print('\nInvalid selection! Please try again.')
            continue


# function to get product name and validate if field empty.
def product_name_input():
    while True:
        product_name = input('Enter new product name: ')
        if product_name != '':
            break
        else:
            print("\nPlease enter a product name to continue.\n")
            continue
    return product_name


# function to get price input and validate if no int or float is entered.
def price_input():
    while True:
        try:
            item_price = float(input('Enter product price: '))
            break
        except ValueError:
            print('\nInvalid price format! Enter correct value.\n')
    return item_price


# function to get product ID input and validate if not integer
def input_not_int():
    while True:
        try:
            item_id = int(input('Enter product ID: '))
            break
        except ValueError:
            print('\nInvalid ID format! Only integers allowed.\n')
    return item_id


# function to validate input to repeat action else will return to main menu
def test_menu(input1):
    if input1 == 'Y' or input1 == 'y':
        pass
    else:
        controller.start_up()
