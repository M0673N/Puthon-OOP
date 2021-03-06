class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library):
        for user_name in library.rented_books:
            for book in library.rented_books[user_name]:
                if book == book_name:
                    return f'The book "{book_name}" is already rented' \
                           f' and will be available in {library.rented_books[user_name][book]} days!'
        if book_name in library.books_available[author]:
            library.books_available[author].remove(book_name)
            if self.username not in library.rented_books:
                library.rented_books[self.username] = {book_name: days_to_return}
            else:
                library.rented_books[self.username][book_name] = days_to_return
            self.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author, book_name, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"
        library.books_available[author].append(book_name)
        library.rented_books[self.username].pop(book_name)
        self.books.remove(book_name)

    def info(self):
        return ", ".join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
