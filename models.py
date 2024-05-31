from book import Book
from user import User
from check import Checkout
import storage
import re

def search_books(search_term):
    """Searches for books by title, author, or ISBN."""
    search_results = []
    for book in storage.books:  # Access global 'books' from storage.py
        if search_term.lower() in book.title.lower() or \
           search_term.lower() in book.author.lower() or \
           search_term.lower() in book.isbn.lower():
            search_results.append(book)
    return search_results

def search_users(search_term):
    """Searches for users by name or user ID."""
    search_results = []
    for user in storage.users:  # Access global 'users' from storage.py
        if search_term.lower() in user.name.lower() or \
           search_term.lower() in user.user_id.lower():
            search_results.append(user)
    return search_results

def is_valid_isbn(isbn):
    """Checks if the ISBN is in a valid format."""
    isbn = isbn.replace("-", "")
    if len(isbn) == 10:
        return re.match(r"^\d{10}$", isbn) is not None
    elif len(isbn) == 13:
        return re.match(r"^\d{13}$", isbn) is not None
    else:
        return False