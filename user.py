class User:
    """Represents a library user."""

    def __init__(self, name, user_id):
        """Initializes a User object."""
        self.name = name
        self.user_id = user_id

    def __str__(self):
        """Returns a string representation of the user."""
        return f"Name: {self.name}, User ID: {self.user_id}"