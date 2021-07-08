from db_connector import base, cursor

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

cursor.execute('INSERT INTO categories VALUES(?, ?)', ('1', 'tires_discs_chains'))
base.commit()
cursor.execute('INSERT INTO categories VALUES(?, ?)', ('2', 'accessories'))
base.commit()