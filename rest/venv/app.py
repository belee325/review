from flask import Flask, request
from flask_jwt import JWT, jwt_required
from flask_restful import Resource, Api, reqparse
from security import *

app = Flask(__name__)
app.secret_key = 'secret_key'
api = Api(app)
jwt = JWT(app, authenticate, identify)  # /auth

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be blank'
                        )
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return item, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': 'an item with name {} already exists'.format(name)}, 400
        data = Item.parser.parse_args()
        item = {'name': data['name'], 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'item deleted'}, 200

    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item:
            item['price'] = data['price']
            return {'message': 'updated price for {}'.format(name)}
        else:
            items.append({'name': name, 'price': data['price']})


class ItemList(Resource):
    def get(self):
        return {'Items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
app.run(debug=True)
