

# library_management.py

class Book:
    """A class representing a book with a title, an author, and checkout status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available (not checked out)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    """A library class to manage a collection of books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a Book instance to the library."""
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title. Returns a message indicating result."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"'{title}' has been checked out."
                else:
                    return f"'{title}' is already checked out."
        return f"Book titled '{title}' not found in the library."

    def return_book(self, title):
        """Returns a book by title. Returns a message indicating result."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f"'{title}' has been returned."
                else:
                    return f"'{title}' was not checked out."
        return f"Book titled '{title}' not found in the library."

    def list_available_books(self):
        """Returns a list of titles that are available for checkout."""
        available_books = [f"{book.title} by {book.author}" for book in self._books if book.is_available()]
        return available_books
