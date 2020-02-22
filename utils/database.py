"""
Concerned with storing and retrieving books from from a JSON file.

[
    {
        'name': 'Clean Code''
        'author': 'Robert',
        'read': TRUE
    }
]
"""
import json

books_file = 'books.json'


def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)


def list_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def prompt_add_book_to_the_list(name, author):
    books = list_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


def prompt_mark_book_as_read(name):
    books = list_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
        _save_all_books(books)


def prompt_to_delete_a_book(name):
    books = list_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)
