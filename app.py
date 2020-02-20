from utils import database

USER_CHOICE = """
Enter:
- 'a' = to add a new book
- 'l' = to list all books in the library database
- 'r' = to mark a book as being read
- 'd' = to delete a book from the library database
- 'q' = to quit the program

Your choice: """


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_all_books()
        elif user_input == 'r':
            prompt_mark_book_as_read()
        elif user_input == 'd':
            prompt_to_delete_a_book()
        else:
            print('unknown command or input!  Try your selection')

        user_input - input(USER_CHOICE)

def prompt_add_book():
    name = input('Enter the name of your book to add.')
    author = 'Enter the name of the author of your book.')

    database.add_book_to_the_list(name, author)

def list_all_books()
        books = database.get_all_books()
        for books in books:
            read = 'YES' if book['read'] == '1' else 'None'
            print(f'''{book['name']} by {book['author']}, read: {book['read]}''')

def prompt_mark_book_as_read():
        name = input(f'Enter the name of the book from your library that you have read it!.''')

def prompt_to_delete_a_book():
    name = input(f'Enter the title of a book that you would like to delete from your library list.')

    database.delete_book(name)


menu()
