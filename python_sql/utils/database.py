from typing import List, Tuple
import sqlite3
from utils.database_connection import DatabaseConnection

Book = Tuple[int, str, str, int]


def create_book_table() -> None:
    with DatabaseConnection('data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

def get_all_books() -> List[Book]:
    with DatabaseConnection('data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        books = [{'name':row[0], 'author':row[1], 'read':row[2]}
                 for row in cursor.fetchall()] #should give us [(name, author, read)....]
        return books

def insert_book(name: str, author: str) -> None:
    with DatabaseConnection('data.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO books VALUES(?,?,0)',(name, author))
        except sqlite3.IntegrityError as e:
            print("book already exists")

def mark_book_as_read(name: str) -> None:
    with DatabaseConnection('data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE books SET read = 1 WHERE name =?',(name,))

def delete_book(name: str) -> None:
    with DatabaseConnection('data.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM books WHERE name =?',(name,))
