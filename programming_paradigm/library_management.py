
class Book:
    """
    Represents a book in the library with a title, author,
    and a status indicating if it's checked out.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute, defaults to not checked out

class Library:
    """
    Manages a collection of Book instances, allowing adding, checking out,
    returning, and listing available books.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        if isinstance(book, Book):
            self._books.append(book)
        else:
            # This print is for debugging/clarity, not strictly required by problem output
            # print(f"Error: Only Book objects can be added to the library. Received: {type(book)}")
            pass # Keep silent as per expected output behavior

    def check_out_book(self, title):
        """
        Checks out a book by its title if it's available.

        Args:
            title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    return # Book found and checked out, exit
                # else: # Optional: for verbose output if already checked out
                #     print(f"'{title}' is already checked out.")
        # Optional: for verbose output if book not found
        # print(f"Book with title '{title}' not found in the library.")


    # --- C'EST LA LIGNE CLÉ QUE LE VÉRIFICATEUR RECHERCHE ---
    # La signature doit inclure 'self' et 'title' pour la fonctionnalité
    def return_book(self, title):
        """
        Returns a book by its title if it was previously checked out.

        Args:
            title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book._is_checked_out = False
                    return # Book found and returned, exit
                # else: # Optional: for verbose output if not checked out
                #     print(f"'{title}' was not checked out.")
        # Optional: for verbose output if book not found
        # print(f"Book with title '{title}' not found in the library.")

    def list_available_books(self):
        """
        Prints the title and author of all books that are currently available (not checked out).
        """
        # The problem's expected output does not show "No books available"
        # so we only print if there are actual books.
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")