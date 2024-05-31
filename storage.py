import json
import os
from book import Book
from user import User
from check import Checkout
import re

DATA_FILE = "library_data.json"

def load_data():
    """Loads data from the JSON file."""
    global books, users, checkouts
    books = []
    users = []
    checkouts = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            for book_data in data.get('books', []):
                books.append(Book(book_data['title'], book_data['author'], book_data['isbn']))
            for user_data in data.get('users', []):
                users.append(User(user_data['name'], user_data['user_id']))
            for checkout_data in data.get('checkouts', []):
                checkouts.append(Checkout(checkout_data['user_id'], checkout_data['book_isbn']))

def save_data():
    """Saves data to the JSON file."""
    data = {
        'books': [{"title": b.title, "author": b.author, "isbn": b.isbn} for b in books],
        'users': [{"name": u.name, "user_id": u.user_id} for u in users],
        'checkouts': [{"user_id": c.user_id, "book_isbn": c.book_isbn} for c in checkouts],
    }
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def add_book(book):
    """Adds a new book to the list."""
    books.append(book)

def add_user(user):
    """Adds a new user to the list."""
    users.append(user)

def add_checkout(checkout):
    """Adds a new checkout to the list."""
    checkouts.append(checkout)

def get_all_books():
    """Returns a list of all books."""
    return books

def get_all_users():
    """Returns a list of all users."""
    return users

def get_book_by_isbn(isbn):
    """Finds and returns a book by its ISBN."""
    for book in books:
        if book.isbn == isbn:
            return book
    return None

def get_checkout_by_user_id_and_isbn(user_id, isbn):
    """Finds a checkout record based on user ID and ISBN."""
    for checkout in checkouts:
        if checkout.user_id == user_id and checkout.book_isbn == isbn:
            return checkout
    return None

def remove_checkout(checkout):
    """Removes a checkout record from the list."""
    checkouts.remove(checkout)

def is_book_exists(isbn):
    """Checks if a book with the given ISBN already exists."""
    return any(book.isbn == isbn for book in books)

def is_user_exists(user_id):
    """Checks if a user with the given user ID already exists."""
    return any(user.user_id == user_id for user in users)

def delete_book_by_isbn(isbn):
    """Deletes a book from the list based on its ISBN."""
    for i, book in enumerate(books):
        if book.isbn == isbn:
            del books[i]
            return True
    return False

def get_user_by_id(user_id):
    """Finds and returns a user by their user ID."""
    for user in users:
        if user.user_id == user_id:
            return user
    return None


def delete_user_by_id(user_id):
    """Deletes a user from the list based on their user ID."""
    for i, user in enumerate(users):
        if user.user_id == user_id:
            del users[i]
            return True
    return False

def update_book(book):
    """Updates the book in the storage."""
    for i, b in enumerate(books):
        if b.isbn == book.isbn:
            books[i] = book
            break

def get_checked_out_books():
    """Returns a list of books that are currently checked out."""
    checked_out_books = []
    for book in books:
        if not book.is_available:
            checked_out_books.append(book)
    return checked_out_books