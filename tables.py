import sqlite3

connection = sqlite3.connect('data.db') #data.db is created using connection

cursor = connection.cursor() #calling the execute() method and cursor object is created for SQL commands


#TABLE is created for users
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)
#TABLE is created for item
create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
cursor.execute(create_table)
#testitem is for inserting data
cursor.execute("INSERT INTO items VALUES ('hello', '123456789')")

connection.commit() # changes are saved and closed
connection.close()