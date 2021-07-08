import urllib.request
import sqlite3
import os
import json

categories = {
    'https://pitstop.rv.ua/s/catalog?Parent=(1d6f5bec-d49c-11e4-8586-002590aa75d3)': 'tires_discs_chains',
    'https://pitstop.rv.ua/s/catalog?Parent=(a5aa1e6f-d49b-11e4-8586-002590aa75d3)': 'accessories'
}

for category in categories:
    with urllib.request.urlopen(category) as response:
        file_name = categories[category] + '.json'
        file = open('resources' + os.sep + file_name, 'w', encoding='utf-8')
        file.write(response.read().decode())

base = sqlite3.connect('products.db')
cursor = base.cursor()

base.execute('''CREATE TABLE categories(
             category_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
             category TEXT)''')
base.commit()
base.execute('''CREATE TABLE products(
             product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,  
             name TEXT,
             cost FLOAT,
             FOREIGN KEY (product_id) REFERENCES categories(category_id))''')
base.commit()

cursor.execute('INSERT INTO categories VALUES(?, ?)', ('1', 'tires_discs_chains'))
base.commit()
cursor.execute('INSERT INTO categories VALUES(?, ?)', ('2', 'accessories'))
base.commit()

category1 = json.load(open('tires_discs_chains.json', encoding='utf-8'))
category2 = json.load(open('accessories.json', encoding='utf-8'))

for i in range(len(category1)):
    product_i = category1[i]
    name = product_i['Name']
    price = product_i['Price']
    cursor.execute('INSERT INTO products VALUES(?, ?, ?)', (i, name, price))
    base.commit()
    i += 1

for i in range(len(category2)):
    product_i = category2[i]
    name = product_i['Name']
    price = product_i['Price']
    cursor.execute('INSERT INTO products VALUES(?, ?, ?)', (i + len(category1), name, price))
    base.commit()
    i += 1

'''
def add_to_db():
'''