class Book:
    """Represents a book in the library."""

    def __init__(self, title, author, isbn):
        """Initializes a Book object."""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        """Returns a string representation of the book."""
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.is_available}"

    def mark_as_checked_out(self):
        """Marks the book as checked out."""
        self.is_available = False

    def mark_as_returned(self):
        """Marks the book as returned."""
        self.is_available = True 