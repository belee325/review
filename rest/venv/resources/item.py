from flask import request
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from resources.user_register import UserRegister
from models.item_model import ItemModel
import sqlite3


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be blank'
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        return item.json(), 200 if item else {'message': 'item not found'}, 404


    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': 'an item with name {} already exists'.format(name)}, 400
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])
        item.insert_item()
        return item.json(), 201

    def delete(self, name):
        if not ItemModel.find_by_name(name):
            return {'message': 'item does not exist'}, 400
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            query = "delete from items where item_name = ?"
            cursor.execute(query, (name,))
        return {'message': 'item deleted'}, 200

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item:
            item.update_price(data['price'])
            return {'message': 'updated price for {}'.format(name)}, 200
        updated_item = ItemModel(name, data[1])
        updated_item.insert_item()
        return updated_item.json(), 201


class ItemList(Resource):
    def get(self):
        ret = []
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            query = 'SELECT * FROM items'
            res = cursor.execute(query)
            rows = res.fetchall()
            for row in rows:
                ret.append({'item_name': row[1], 'price': row[2]})
        return {'items':ret}, 200
