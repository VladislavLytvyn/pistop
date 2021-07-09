from db_connector import base, cursor
from get_products import categories

base.execute('''CREATE TABLE categories(
             category_id INTEGER PRIMARY KEY AUTOINCREMENT, 
             category TEXT)''')
base.commit()
base.execute('''CREATE TABLE products(
             product_id INTEGER PRIMARY KEY AUTOINCREMENT,  
             name TEXT,
             cost FLOAT,
             FOREIGN KEY (product_id) REFERENCES categories(category_id))''')
base.commit()

for category in categories:
    cursor.execute('INSERT INTO categories (category) VALUES(?)', [categories[category]])
    base.commit()