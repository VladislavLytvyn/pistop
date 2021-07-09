import json
import os
from db_connector import *
from get_products import categories

for category in categories:
    cursor.execute('INSERT INTO categories (category) VALUES(?)', [categories[category]])
    base.commit()
    category = json.load(open('resources' + os.sep + categories[category] + '.json', encoding='utf-8'))
    for product in category:
        cursor.execute('INSERT INTO products (name, cost) VALUES(?, ?)', (product['Name'], product['Price']))
        base.commit()