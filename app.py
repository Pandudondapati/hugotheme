from flask import Flask, request    #We get Flast class from flask module

from flask_restful import Resource, Api, abort, reqparse #Resource, Api, abort, reqparse is extracted from flask_restful to get rest api

from flask_jwt import JWT, jwt_required, current_identity #import JWT, jwt_required, current_identity from flask_jwt


from security import authenticate, identity #authenticate and identity is imported from security
from user import UserRegister
from item import Item


app = Flask(__name__) #Flask application is created

app.secret_key = 'Girija' #Secret line is added

api = Api(app) #this command id to create Api application instance

jwt = JWT(app, authenticate, identity) #JWT object is created and after that Flask_JWT registers has an endpoint

api.add_resource(Item, '/<name>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)
