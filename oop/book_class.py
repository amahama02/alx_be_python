class Book:
    """
    A class to represent a book, demonstrating Python's magic methods
    for initialization, string representation, and object deletion.
    """
    def __init__(self, title: str, author: str, year: int):
        """
        Constructor method to initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        # print(f"Book '{self.title}' created.") # Optional: for creation tracking

    def __del__(self):
        """
        Destructor method, called when the object is about to be garbage-collected.
        Prints a message indicating the book being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book object.
        Used by str() and print().
        Format: "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation of the Book object
        that could be used to recreate the instance.
        Used by repr().
        Format: f"Book('{self.title}', '{self.author}', {self.year})"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"