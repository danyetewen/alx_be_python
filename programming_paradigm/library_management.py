#!/usr/bin/env python3
"""
Module for a simple Library Management System using basic OOP principles.
"""

class Book:
    """Represents a book in the library."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out


class Library:
    """Represents a library containing books."""
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book by title.
        If the book is found and available, it is marked as checked out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        # Book not available or not found (no message needed as per spec)

    def return_book(self, title):
        """
        Returns a book by title.
        If the book is found and is checked out, it is marked as returned.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        # Book not checked out or not found (no message needed as per spec)

    def list_available_books(self):
        """Prints the list of books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
