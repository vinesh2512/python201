import view
from Python201_Final.itemclient import ItemRestClient

item_client = ItemRestClient()


# function to show all product
def list_all_items():
    list_of_items = item_client.get_all_items()
    view.print_all_items(list_of_items)
    view.return_to_menu()


# function to save new product
def new_item():
    print('\n-------- ADD NEW PRODUCT --------\n')
    i_id = str(view.input_not_int())
    item_client.check_id_exists(i_id)
    i_name = view.product_name_input()
    i_price = view.price_input()
    i_offer = bool(input('Is the product on offer? (True/False): '))
    item_client.post_new_item(i_id, i_name, i_price, i_offer)
    print('\nProduct added successfully.')
    add_again = input('\nType [Y] to add another product or\npress any key to return to main menu: ')
    view.test_menu(add_again)
    new_item()


# function to search product by ID
def search_item():
    try:
        search_item_id = input('\nEnter product ID to search: ')
        list_search_items = [item_client.search_item_by_id(search_item_id)]
        view.print_all_items(list_search_items)
    except (TypeError, KeyError):
        print('\nProduct not found!')
    search_again = input('\nType [Y] to search another product or\npress any key to return to main menu: ')
    view.test_menu(search_again)
    search_item()


# function to update product
def update_item():
    print('\n-------- UPDATE PRODUCT ---------\n')
    put_item_id = str(view.input_not_int())
    item_client.check_put_item_by_id(put_item_id)
    put_item_name = view.product_name_input()
    put_item_price = view.price_input()
    put_offer = bool(input('Is the product on offer? (True/False): '))
    item_client.put_item_by_id(put_item_id, put_item_name, put_item_price, put_offer)
    print('\nProduct updated successfully.')
    update_again = input('\nType [Y] to update another product or\npress any key to return to main menu: ')
    view.test_menu(update_again)
    update_item()


# function to delete product
def delete_item():
    print('\n-------- DELETE PRODUCT ---------\n')
    del_item_id = str(view.input_not_int())
    item_client.delete_item_by_id(del_item_id)
    delete_again = input('\nType [Y] to delete another product or\npress any key to return to main menu: ')
    view.test_menu(delete_again)
    delete_item()


# function to start main menu
def start_up():
    menu_selection = view.print_menu()
    if menu_selection == 'A' or menu_selection == 'a':
        list_all_items()
    elif menu_selection == 'B' or menu_selection == 'b':
        new_item()
    elif menu_selection == 'C' or menu_selection == 'c':
        search_item()
    elif menu_selection == 'D' or menu_selection == 'd':
        update_item()
    elif menu_selection == 'E' or menu_selection == 'e':
        delete_item()
    elif menu_selection == 'X' or menu_selection == 'x':
        print('\nShutting Down....')
        quit()

    else:
        print('\nInvalid selection! Please try again.')
