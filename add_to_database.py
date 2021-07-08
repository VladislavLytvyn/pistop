import json
from db_connector import *
import os

category1 = json.load(open('resources' + os.sep + 'tires_discs_chains.json', encoding='utf-8'))
category2 = json.load(open('resources' + os.sep + 'accessories.json', encoding='utf-8'))

for product in category1:
    cursor.execute('INSERT INTO products (name, cost) VALUES(?, ?)', (product['Name'], product['Price']))
    base.commit()

for i in range(len(category2)):
    product_i = category2[i]
    name = product_i['Name']
    price = product_i['Price']
    cursor.execute('INSERT INTO products (name, cost) VALUES(?, ?)', (name, price))
    base.commit()
    i += 1

'''
def add_to_db():
'''
