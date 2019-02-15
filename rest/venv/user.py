import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM users WHERE username=?'
        res = cursor.execute(query, (username,))
        row = res.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM users WHERE id=?'
        res = cursor.execute(query, (id,))
        row = res.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

class UserRegister(Resource):
    user_parser = reqparse.RequestParser()
    reqparse.Argument
    user_parser.add_argument('username',type = str, required = True)
    user_parser.add_argument('password', type=str, required=True)
    def post(self):
        data = UserRegister.user_parser.parse_args()
        if not User.find_by_username(data['username']):
            return {'message':'the username already exists!'}, 400
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            query = 'INSERT INTO users VALUES (NULL, ?, ?)'
            cursor.execute(query, (data['username'], data['password']))

        return {'message':'user has been created successfully'}, 201