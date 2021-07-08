import sqlite3

base = sqlite3.connect('library_many to many.db')
cursor = base.cursor()

base.execute('''CREATE TABLE books(
             id INTEGER PRIMARY KEY,
             title TEXT, 
             pages_count INTEGER)''')
base.commit()
base.execute('''CREATE TABLE authors(
             id INTEGER PRIMARY KEY,
             name TEXT)''')
base.commit()
base.execute('''CREATE TABLE authors_books(
             author_id INTEGER,
             book_id INTEGER,
             FOREIGN KEY (author_id) REFERENCES authors(id),
             FOREIGN KEY (book_id) REFERENCES books(id))''')
base.commit()

cursor.execute('INSERT INTO authors VALUES(?, ?)', ('1', 'Dj. London'))
base.commit()
cursor.execute('INSERT INTO authors VALUES(?, ?)', ('2', 'Dik Svaab'))
base.commit()
cursor.execute('INSERT INTO authors VALUES(?, ?)', ('3', 'Author the White Fang'))
base.commit()

cursor.execute('INSERT INTO books VALUES(?, ?, ?)', ('1', 'The call of the wild', '100'))
base.commit()
cursor.execute('INSERT INTO books VALUES(?, ?, ?)', ('2', 'White fang', '200'))
base.commit()
cursor.execute('INSERT INTO books VALUES(?, ?, ?)', ('3', 'The sea-wolf', '300'))
base.commit()
cursor.execute('INSERT INTO books VALUES(?, ?, ?)', ('4', 'We are our brains', '400'))
base.commit()
cursor.execute('INSERT INTO books VALUES(?, ?, ?)', ('5', 'Our cultural brain', '500'))
base.commit()
cursor.execute('INSERT INTO books VALUES(?, ?, ?)', ('6', 'Human hypothalamus', '600'))

cursor.execute('INSERT INTO authors_books VALUES(?, ?)', ('1', '1'))
base.commit()
cursor.execute('INSERT INTO authors_books VALUES(?, ?)', ('1', '2'))
base.commit()
cursor.execute('INSERT INTO authors_books VALUES(?, ?)', ('1', '3'))
base.commit()
cursor.execute('INSERT INTO authors_books VALUES(?, ?)', ('2', '4'))
base.commit()
cursor.execute('INSERT INTO authors_books VALUES(?, ?)', ('2', '5'))
base.commit()
cursor.execute('INSERT INTO authors_books VALUES(?, ?)', ('2', '6'))
base.commit()
cursor.execute('INSERT INTO authors_books VALUES(?, ?)', ('3', '2'))
base.commit()
cursor.execute('INSERT INTO authors_books VALUES(?, ?)', ('3', '1'))
base.commit()

'''
- выбрать все книги автора с именем таким то

SELECT books.*
FROM books, authors
JOIN authors_books on authors_books.author_id = authors.id 
AND authors_books.book_id = books.id
WHERE authors.name = 'Dik Svaab'
'''

'''
- выбрать последние 2 книги (найбільше сторінок) автора такого то

SELECT books.*
FROM books, authors
JOIN authors_books on authors_books.author_id = authors.id
AND authors_books.book_id = books.id
WHERE authors.name = 'Dj. London'
ORDER by books.pages_count DESC LIMIT 2
'''

'''
не працює
- выбрать книги у которых два автора -  петя и автор влад

SELECT books.*
FROM books, authors
JOIN author_book on author_book.authors_id = authors.id
AND author_book.books_id = books.id
WHERE authors.name = 'Dj. London' AND authors.name = 'Author the White Fang'
'''

'''
- выбрать книги у которых два автора

SELECT books.*
FROM authors
JOIN books on authors_books.book_id = books.id
JOIN authors_books on authors_books.author_id = authors.id
GROUP by books.id 'завжди по id'
HAVING COUNT(authors.id) = 2
'''