# Important: do not change or remove any code function
# -- Made by Leffy --

import requests
import time

def get_item_price(item_id):
    url = f'https://economy.roblox.com/v1/assets/{item_id}/resellers'
    response = requests.get(url)
    data = response.json()
    lowest_price = None
    if 'data' in data and len(data['data']) > 0:
        for reseller in data['data']:
            price = reseller['price']
            if lowest_price is None or price < lowest_price:
                lowest_price = price
    return lowest_price

def check_item_price(item_id, target_price):
    print("The program checker is running")
    while True:
        price = get_item_price(item_id)
        if price is not None and int(price) < target_price:
            print(f"The item {item_id} is now available for {price} Robux!")
        time.sleep(60) 
        
# item u want to buy
# example here
item_id_1 = 12345678 # set the item id that you want to purchase
target_price_1 = 1000 # set the target price example: item resale price is 1500 and your target is 1000 then set it to 1000.
# note: Don't set the price too low, it might be no one will resale that much or mybe or take a long time
check_item_price(item_id_1, target_price_1)

# You can add more items as above like this
item_id_2 = 12345678
target_price_2 = 1000
check_item_price(item_id_2, target_price_2)
# and so on
# note: The variable "item_id" cannot be the same, nor can "target_price" just add "_3, _4, _5" at the end of the word
