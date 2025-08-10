#!/usr/bin/python3
"""
Module for Library System demonstrating Inheritance and Composition
"""


class Book:
    """
    Base class to represent a book
    """

    def __init__(self, title, author):
        """
        Initializes a Book instance

        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the book

        Returns:
            str: String containing book title and author
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Represents an electronic book, inheriting from Book
    """

    def __init__(self, title, author, file_size):
        """
        Initializes an EBook instance

        Args:
            title (str): The title of the eBook
            author (str): The author of the eBook
            file_size (int): File size of the eBook in KB
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the eBook

        Returns:
            str: String containing eBook details
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Represents a printed book, inheriting from Book
    """

    def __init__(self, title, author, page_count):
        """
        Initializes a PrintBook instance

        Args:
            title (str): The title of the printed book
            author (str): The author of the printed book
            page_count (int): Number of pages in the book
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation of the printed book

        Returns:
            str: String containing printed book details
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Represents a library using composition to manage books
    """

    def __init__(self):
        """
        Initializes a Library instance with an empty list of books
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book to the library

        Args:
            book (Book): An instance of Book, EBook, or PrintBook
        """
        if isinstance(book, Book):
            self.books.append(book)

    def list_books(self):
        """
        Prints details of each book in the library
        """
        for book in self.books:
            print(book)
