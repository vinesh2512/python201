import unittest
from unittest.mock import patch

from Python201_Final.itemclient import RestClientResponse, ItemRestClient


class RestClientTest(unittest.TestCase):

    @patch('requests.post')
    def test_call_post_item(self, mock_obj):
        mock_obj.return_value.status_code = 200
        mock_obj.return_value.text = {
            "id": 1,
            "name": "Spinach_Mock",
            "price": 2.22,
            "is_offer": False
        }
        post_item = RestClientResponse()
        response = post_item.call_post_item(item_id=1, item_name="Spinach_Mock", item_price=2.22, item_offer=False)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.text)

    @patch('requests.put')
    def test_call_put_item(self, mock_obj):
        mock_obj.return_value.status_code = 201
        mock_obj.return_value.text = {
            "id": 1,
            "name": "Spinach_Mock",
            "price": 2.22,
            "is_offer": False
        }
        put_item = ItemRestClient()
        response = put_item.put_item_by_id(item_id='1', item_name="spi", item_price=2.22, item_offer=False)
        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.text)

    @patch('requests.delete')
    def test_call_delete_item(self, mock_obj):
        mock_obj.return_value.status_code = 200
        mock_obj.return_value.text = {
            "id": 1,
            "name": "Spinach_Mock",
            "price": 2.22,
            "is_offer": False
        }
        delete_item = RestClientResponse()
        response = delete_item.call_delete_item(item_id='1')
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.text)

    @patch('requests.get')
    def test_call_search_item(self, mock_obj):
        mock_obj.return_value.status_code = 200
        mock_obj.return_value.text = {
            "id": 1,
            "name": "Spinach_Mock",
            "price": 2.22,
            "is_offer": False
        }
        search_item = RestClientResponse()
        response = search_item.call_search_item(item_id='1')
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.text)


if __name__ == '__main__':
    unittest.main()
