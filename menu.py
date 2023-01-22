from app import books

USER_CHOICE = '''Enter one of the following options:

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to look at next available book
- 'q' to exit

Enter your choice: '''



def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating)
    for book in best_books:
        print (book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)
    for book in cheapest_books:
        print (book)

books_generator = (x for x in books)

def print_next_book():
    print(next(books_generator))

user_choises = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n':print_next_book

}

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_choises[user_input]()

        else:
            print ('Choose the valid command')
        user_input = input(USER_CHOICE)

menu()