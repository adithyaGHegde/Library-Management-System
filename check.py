class Checkout:
    """Represents a book checkout."""

    def __init__(self, user_id, book_isbn):
        """Initializes a Checkout object."""
        self.user_id = user_id
        self.book_isbn = book_isbn

    def __str__(self):
        """Returns a string representation of the checkout."""
        return f"User ID: {self.user_id}, Book ISBN: {self.book_isbn}"