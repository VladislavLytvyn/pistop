import json
import os
from db_connector import *
from get_products import categories
from create_logger import logger

for category in categories:
    cursor.execute('INSERT INTO categories (category) VALUES(?)', [categories[category]])
    base.commit()
    category_dict = json.load(open('resources' + os.sep + categories[category] + '.json', encoding='utf-8'))
    logger.write('Start import for database field ' + categories[category])
    for product in category_dict:
        cursor.execute('INSERT INTO products (name, cost) VALUES(?, ?)', (product['Name'], product['Price']))
        base.commit()
    logger.write('Finish import for database field ' + categories[category])