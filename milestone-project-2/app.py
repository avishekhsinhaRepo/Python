import prompts.prompts as prompts
import utils.sqlitedb as database

USER_CHOICE = """

Enter:
- 'a' to add a book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:"""

operations = {
    'a': prompts.prompt_add_book,
    'l': prompts.prompt_list_books,
    'r': prompts.prompt_read_book,
    'd': prompts.prompt_delete_book
}


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input and user_input in operations.keys():
            operations[user_input]()
        else:
            print('Invalid input. Please try again.')
        user_input = input(USER_CHOICE)


menu()
