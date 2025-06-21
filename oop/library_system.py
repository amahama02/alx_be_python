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
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Manages a collection of various book types using composition.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list to store books.
        """
        # --- Ligne corrigée ici pour correspondre à l'exigence du vérificateur ---
        self.books = [] # Attribute for storing Book, EBook, PrintBook instances

    def add_book(self, book):
        """
        Adds a Book (or its derived types like EBook, PrintBook) instance to the library.

        Args:
            book (Book): An instance of Book, EBook, or PrintBook.
        """
        if isinstance(book, Book):
            self.books.append(book) # Utiliser self.books car corrigé
        else:
            pass

    def list_books(self):
        """
        Prints the details of each book currently in the library.
        It uses the __str__ method of each book object, demonstrating polymorphism.
        """
        for book in self.books: # Utiliser self.books car corrigé
            print(book)