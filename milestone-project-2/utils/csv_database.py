import csv

BOOKS_FILE = "books.csv"


def add_book(name, author):
    with open(BOOKS_FILE, "a") as bookdb:
        bookdb.write(f"{name},{author},0\n")


def list_books():
    with open(BOOKS_FILE, "r") as bookdb:
        lines = [book.strip().split(",") for book in bookdb.readlines()]
    for line in lines:
        print(f"name: {line[0]}, author: {line[1]}, read: {line[2]}")


def read_book(name):
    with open(BOOKS_FILE, "r") as bookdb:
        lines = [book.strip().split(",") for book in bookdb.readlines()]
        for line in lines:
            if line[0] == name:
                line[2] = "1"
    _save_all_books(lines)


def delete_book(name):
    with open(BOOKS_FILE, "r") as bookdb:
        lines = [book.strip().split(",") for book in bookdb.readlines()]
        lines = [line for line in lines if line[0] != name]
    _save_all_books(lines)

def _save_all_books(lines):
    with open(BOOKS_FILE, "w") as bookdb:
        for line in lines:
            bookdb.write(f"{line[0]},{line[1]},{line[2]}\n")
