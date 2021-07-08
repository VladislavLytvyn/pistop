import sqlite3
base = sqlite3.connect('library.db')
cursor = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS authors(id integer PRIMARY KEY, name text)')
base.commit()
base.execute('CREATE TABLE IF NOT EXISTS books(id integer PRIMARY KEY, author_id integer, name text)')
base.commit()
cursor.execute('INSERT INTO authors VALUES(?, ?)', ('1', 'Dj. London'))
base.commit()
cursor.execute('INSERT INTO authors VALUES(?, ?)', ('2', 'Dik Svaab'))
base.commit()
cursor.execute('INSERT INTO books VALUES(?, ?, ?)', ('1', '1', 'The call of the wild'))
base.commit()
cursor.execute('INSERT INTO books VALUES(?, ?, ?)', ('2', '1', 'White fang'))
base.commit()
cursor.execute('INSERT INTO books VALUES(?, ?, ?)', ('3', '1', 'The sea-wolf'))
base.commit()
cursor.execute('INSERT INTO books VALUES(?, ?, ?)', ('4', '2', 'We are our brains'))
base.commit()
cursor.execute('INSERT INTO books VALUES(?, ?, ?)', ('5', '2', 'Our cultural brain'))
base.commit()
cursor.execute('INSERT INTO books VALUES(?, ?, ?)', ('6', '2', 'Human hypothalamus'))
base.commit()
cursor.execute('INSERT INTO books VALUES(?, ?, ?)', ('7', '2', 'For Konstantin'))
base.commit()

'''
- выбрать все книги автора с именем таким то

SELECT books.*
FROM authors
JOIN books on authors.id = books.author_id
WHERE authors.name = 'Dj. London'
'''

'''
- выбрать последние две книги автора такого то

SELECT books.*
FROM authors
JOIN books on authors.id = books.author_id
WHERE authors.name = 'Dj. London' ORDER BY books.id DESC LIMIT 2
'''

'''
- вывести кол-во всех книг

SELECT COUNT(*) as count FROM books
'''

'''
- вывести кол-во книг каждого автора (это сложно)

SELECT authors.name, count(*) as count
FROM books
JOIN authors on authors.id = books.author_id 
GROUP BY books.author_id
'''