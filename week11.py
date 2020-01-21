import sqlite3
connection = sqlite3.connect('data.db')

cursor = connection.cursor()


create_table = ('''CREATE TABLE IF NOT EXISTS users (id INTEGER,name text NOT NULL,password text NOT NULL)''')
cursor.execute(create_table)

users = [
(1, 'girija', '1234'),
(2, 'oct', '4567'),
(3, 'rtu', '2019')
]

insert_query = ("INSERT INTO users VALUES (?, ?, ?)")

for i in users:
    cursor.execute(insert_query, (i))
connection.commit()

connection.close()

print(users)