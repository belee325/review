from flask import request
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from user import UserRegister
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
        item = Item.find_by_name(name)
        return item, 200 if item else {'message': 'item not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            query = 'SELECT * FROM items where item_name = ?'
            res = cursor.execute(query, (name,))
            row = res.fetchone()
        if row:
            return {'item': {'name': row[0], 'price': row[1]}}

    @classmethod
    def insert_item(cls, name, price):
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            query = "insert into items values (NULL, ?, ?)"
            cursor.execute(query, (name, price))

    @classmethod
    def update_price(cls, name, new_price):
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            query = "update items set price = ? where item_name = ?"
            cursor.execute(query, (new_price, name))

    def post(self, name):
        if Item.find_by_name(name):
            return {'message': 'an item with name {} already exists'.format(name)}, 400
        data = Item.parser.parse_args()
        Item.insert_item(name, data['price'])
        return {'name': name, 'price': data['price']}, 201

    def delete(self, name):
        if not Item.find_by_name(name):
            return {'message': 'item does not exist'}, 400
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            query = "delete from items where item_name = ?"
            cursor.execute(query, (name,))
        return {'message': 'item deleted'}, 200

    def put(self, name):
        data = Item.parser.parse_args()
        if Item.find_by_name(name):
            Item.update_price(name, data['price'])
            return {'message': 'updated price for {}'.format(name)}, 200
        Item.insert_item(name, data['price'])
        return {'name': name, 'price': data['price']}, 201


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
