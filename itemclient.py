import requests
import json
import controller
import view


# class to call rest clients and get response


class RestClientResponse:
    url = 'http://localhost:8000/itemssss'

    def call_all_item(self):
        return requests.get(self.url)

    def call_delete_item(self, item_id):
        return requests.delete(self.url + '/' + item_id)

    def call_search_item(self, item_id):
        return requests.get(self.url + '/' + item_id)

    def call_post_item(self, item_id, item_name, item_price, item_offer):
        save_item = {
            "id": item_id,
            "name": item_name,
            "price": item_price,
            "is_offer": item_offer
        }
        return requests.post(self.url, json=save_item)


class ItemRestClient:
    url = 'http://localhost:8000/items'

    # get all items from server
    def get_all_items(self):

        return json.loads(requests.get(self.url).text)

    # post item to server, using put to get url to follow product ID
    def post_new_item(self, item_id, item_name, item_price, item_offer):

        save_item = {
            "id": item_id,
            "name": item_name,
            "price": item_price,
            "is_offer": item_offer
        }
        return requests.put(self.url + '/' + item_id, json=save_item)

    # function to search json item by ID
    def search_item_by_id(self, item_id):

        return json.loads(requests.get(self.url + '/' + item_id).text)

    # function to validate existing ID and update item
    def check_put_item_by_id(self, item_id):

        response = json.loads(requests.get(self.url + '/' + item_id).text)
        if response is not None:
            pass
        else:
            print('\nProduct not found! Enter valid product ID.')
            update_again = input('\n|Type [Y] to update another product | Press any key to return to main menu| ')
            view.do_again(update_again)
            controller.update_item()

    # function to validate if ID exists
    def check_id_exists(self, item_id):

        response = json.loads(requests.get(self.url + '/' + item_id).text)
        if response is None:
            pass
        else:
            print('\nProduct ID exists! Input a different product ID.')
            view.do_again(input('\n|Type [Y] to enter product ID again | Press any key to return to main menu| '))
            controller.new_item()

    # function to update item by ID
    def put_item_by_id(self, item_id, item_name, item_price, item_offer):

        put_item = {
            "id": item_id,
            "name": item_name,
            "price": item_price,
            "is_offer": item_offer
        }
        return requests.put(self.url + '/' + item_id, json=put_item)

    # function to delete item by ID
    def delete_item_by_id(self, item_id):

        response = json.loads(requests.get(self.url + '/' + item_id).text)
        if response is not None:
            requests.delete(self.url + '/' + item_id)
            print("\nProduct deleted successfully.")
        else:
            print('\nProduct not found! Enter valid product ID.')
