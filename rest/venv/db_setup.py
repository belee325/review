import sqlite3

user = (1,'bob','asdf')
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)')
cursor.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, item_name text, price real)')
cursor.execute('INSERT INTO users VALUES (NULL,?,?)', ('bob','asdf'))
cursor.execute('INSERT INTO users VALUES (NULL,?,?)', ('cob','asdfg'))
cursor.execute('INSERT INTO users VALUES (NULL,?,?)', ('dob','asdfgh'))
cursor.execute('INSERT INTO items VALUES (NULL,?,?)', ('test',1234))


rows = cursor.execute('select * from users')
print(rows.fetchall())
connection.commit()
connection.close()

