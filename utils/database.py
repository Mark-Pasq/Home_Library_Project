
"""
Concerned with storing and retrieving books from from a csv file.
"""
import app
books_file = 'books.txt'


def add_book_to_the_list(name, author):
    with open('books.txt', 'a') as my_file:
        my_file.write(f'''{name}, {author},0''')


def get_all_books():
    with open(books_file,'r') as your_file:
        lines = [line.strip().split(',') for line in your_file.readlines()]

        return [{'name' : line[0], 'author': line[1], 'read': line[2]}
                for line in lines
        ]


def prompt_mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
        _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as her_file:
        for book in books:
            her_file.write(f'''{book['name']}, {book['author']}, {book['read']}''')


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)