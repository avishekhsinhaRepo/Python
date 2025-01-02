#import csv
import sqlite3

BOOKS_FILE = "books.csv"
DB_FILE = "data.db"
TABLE_NAME = "books"


def create_book_table():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} (name text primary key, author text, read integer)")
    connection.commit()
    connection.close()


def add_book(name, author):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    print(f"INSERT INTO {TABLE_NAME} (name, author, read) VALUES({name}, {author}, 0)")
    cursor.execute(f"INSERT INTO {TABLE_NAME}  (name, author, read) VALUES ('{name}', '{author}', 0)")
    connection.commit()
    connection.close()


def list_books():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    print(f"SELECT * FROM {TABLE_NAME}")
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    books = [{'name': row[0], 'author': row[1], "read": row[2]} for row in
             cursor.fetchall()]  ## fetchall() returns a list of tuples
    connection.close()
    print(books)
    return books


def read_book(name):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    print(f"UPDATE {TABLE_NAME} WHERE name = {name}")
    cursor.execute(f"UPDATE {TABLE_NAME} SET read= 1 WHERE name = ?", (name,))
    connection.commit()
    connection.close()


def delete_book(name):
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    print(f"DELETE FROM {TABLE_NAME} WHERE name = {name}")
    cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE name = ?",(name,))
    connection.commit()
    connection.close()
