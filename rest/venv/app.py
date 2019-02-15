from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from item import Item, ItemList
from user import UserRegister
from security import *

app = Flask(__name__)
app.secret_key = 'secret_key'
api = Api(app)
jwt = JWT(app, authenticate, identify)  # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

app.run(debug=True)
