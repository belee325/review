#import sqlite3
from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80))
    price = db.Column(db.Float(2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        #still returing an item model
        return cls.query.filter_by(name=name).first()  # select * from items where name = name limit 1

    def save_to_db(self):
        #this handles both insert and update
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

