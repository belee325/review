import sqlite3

class ItemModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def json(self):
        return {'name':self.name, 'price':self.price}

    @classmethod
    def find_by_name(cls, name):
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            query = 'SELECT * FROM items where item_name = ?'
            res = cursor.execute(query, (self.name,))
            row = res.fetchone()
        if row:
            return cls(row[1], row[2])

    def insert_item(self):
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            query = "insert into items values (NULL, ?, ?)"
            cursor.execute(query, (self.name, self.price))

    def update_price(self, new_price):
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            query = "update items set price = ? where item_name = ?"
            cursor.execute(query, (new_price, self.name))