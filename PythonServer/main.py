from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    price: float
    is_offer: Optional[bool] = None


mock_item_list = {1: Item.parse_obj({'id': 1, 'name': 'Pickles', 'price': 3.99}),
                  2: Item.parse_obj({'id': 2, 'name': 'Spaghetti', 'price': 1.99}),
                  3: Item.parse_obj({'id': 3, 'name': 'Bread', 'price': 2.99, 'is_offer': True})}


@app.get('/')
def read_root():
    return 'Mock Item Database'


@app.post('/items')
def save_item(item: Item):
    mock_item_list[max(mock_item_list.keys()) + 1] = item


@app.get('/items', response_model=List[Item])
def get_all_items():
    return list(mock_item_list.values())


@app.get('/items/{item_id}')
def get_by_id(item_id: int):
    return mock_item_list.get(item_id)


@app.put('/items/{item_id}')
def update_an_item(item_id: int, item: Item):
    mock_item_list[item_id] = item


@app.delete('/items/{item_id}')
def delete_an_item(item_id: int):
    mock_item_list.pop(item_id)