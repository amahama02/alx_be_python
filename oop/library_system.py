class Book:
    """
    Base class for all types of books in the library system.
    """
    def __init__(self, title: str, author: str):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the basic Book.
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Represents an electronic book, inheriting from Book.
    """
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes a new EBook instance.

        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The size of the e-book file in KB.
        """
        super().__init__(title, author) # Call the constructor of the base class (Book)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the EBook, including file size.
        """
        # Leverage the base class's __str__ for common parts or build from scratch
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Represents a physical print book, inheriting from Book.
    """
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes a new PrintBook instance.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        super().__init__(title, author) # Call the constructor of the base class (Book)
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation of the PrintBook, including page count.
        """
        # Leverage the base class's __str__ for common parts or build from scratch
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Manages a collection of various book types using composition.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list to store books.
        """
        self._books = [] # Private list to hold Book, EBook, PrintBook instances

    def add_book(self, book):
        """
        Adds a Book (or its derived types like EBook, PrintBook) instance to the library.

        Args:
            book (Book): An instance of Book, EBook, or PrintBook.
        """
        # Optional: Add type checking if you only want to allow Book instances or its subclasses
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print(f"Cannot add non-Book object to library: {type(book)}")

    def list_books(self):
        """
        Prints the details of each book currently in the library.
        It uses the __str__ method of each book object, demonstrating polymorphism.
        """
        if not self._books:
            # print("The library is currently empty.") # Optional: for verbose output
            pass # Keep silent if no books as per expected output format
        for book in self._books:
            print(book) # This implicitly calls the __str__ method of each book object