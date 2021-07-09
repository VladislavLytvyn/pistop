import sqlite3

base = sqlite3.connect('products.db')
cursor = base.cursor()