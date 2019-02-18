import sqlite3
from flask_restful import Resource, reqparse
from models.usermodel import UserModel

class UserRegister(Resource):
    user_parser = reqparse.RequestParser()
    reqparse.Argument
    user_parser.add_argument('username',type = str, required = True)
    user_parser.add_argument('password', type=str, required=True)
    def post(self):
        data = UserRegister.user_parser.parse_args()
        if not UserModel.find_by_username(data['username']):
            return {'message':'the username already exists!'}, 400
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            query = 'INSERT INTO users VALUES (NULL, ?, ?)'
            cursor.execute(query, (data['username'], data['password']))

        return {'message':'user has been created successfully'}, 201