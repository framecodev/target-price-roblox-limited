import requests
import time
import json
from robloxapi import RobloxAPI

def get_item_price(item_id):
    url = f'https://economy.roblox.com/v1/assets/{item_id}/resellers'
    response = requests.get(url)
    data = response.json()
    if 'data' in data and len(data['data']) > 0:
        return data['data'][0]['price']
    return None

def check_item_price(item_id, target_price):
    rbx = RobloxAPI()
    with open('WARNING.json') as file:
        cookie_data = json.load(file)
    rbx.set_cookie(cookie_data['cookie'])

    while True:
        price = get_item_price(item_id)
        if price is not None and price < target_price:
            print(f"The item {item_id} is now available for {price} Robux!")
            if not rbx.owns_asset(item_id):
                rbx.buy_asset(item_id)
                print(f"Item {item_id} has been purchased!")
        time.sleep(60)

# item u want to buy

item_id_1 = 12345678 # set the item id taht you want to purchase
target_price_1 = 1000 # set the target price minimum is 5-10% example item price is 1500 and the target 1000 then set it to 1000

check_item_price(item_id_1, target_price_1)