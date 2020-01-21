import sqlite3
import random
import string
#data.db database is created using connection(connect)
connection = sqlite3.connect('data.db')
#Cursor object is created and call its execute() method to perform SQL commands
cursor = connection.cursor()

#TABLE is created
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# ROW is inserted with static data with id as 1, username as naresh
user = (1, 'NARESH', 'NAresh1234')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

connection.commit()
 # Save (commit) the changes

# function is defined and called dynamic_user_entry is generating username and password
def dynamic_user_generate(num):
    name = ''.join([random.choice(string.ascii_uppercase) for n in range(6)]) 
 #random upper case letter with lenghth of 6
    pas = ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for n in range(10)])     #password includes uppercase, lowercase and number
    cursor.execute("INSERT INTO users (id, username, password) VALUES (?, ?, ?)", (num, name, pas)) # Inserting the values into table
    connection.commit() 
 # save the changes

for i in range(2,6):
    # calling dynamic_user_generate to generate random username and password
    dynamic_user_generate(i)

for row in cursor.execute('SELECT * FROM users ORDER BY id'):
    #all the numbers are printed with sorting id
    print(row)

# close the connection
connection.close()