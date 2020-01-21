import sqlite3 
from flask_restful import Resource, reqparse

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    
    #price is added as argument
    parser.add_argument('username', type=str,required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str,required=True, help='This field cannot be left blank')

    #post is defined to create users
    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['username']):
            return {"message":"A user with this username is already exists"}, 400
        connection = sqlite3.connect('data.db')
        cursor =   connection.cursor()
        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'],data['password']))

        connection.commit()
        connection.close()

        return {"message": "User Create Successfully!!!"}, 201

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    #username is verified and exists
    @classmethod
    def find_by_username(cls, username):
        connection  = sqlite3.connect('data.db')
        cursor =   connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        #every row is selected in the database and uses data which matches parameter
        result = cursor.execute(query, (username,))
        
        #since a single value tuple is necessary
        row = result.fetchone()
        #first row is selected
        if row:
        #user = cls(row[0], row[1], row[2]) those match an id, username and password
            user = cls(*row)
        else:
            user = None 
        
        connection.close()
        return user
    #verify the id exists in database
    @classmethod
    def find_by_id(cls, id):
        connection  = sqlite3.connect('data.db')
        cursor =   connection.cursor()

        query = "SELECT * FROM users WHERE id=?" #select every row in the database with given id
        result = cursor.execute(query, (id,)) #since a single value tuple is necessary
        row = result.fetchone() #selects the first row out of the results set
        if row:
            #user = cls(row[0], row[1], row[2]) those match an id,
        
            user = cls(*row)
        else:
            user = None # None is when object doesnt exist
        
        connection.close()
        return user
