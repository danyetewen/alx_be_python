#!/usr/bin/python3
"""
Module for Book class implementation
"""

class Book:
    """
    A class to represent a book
    """

    def __init__(self, title, author, year):
        """
        Initializes a Book instance

        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor method called when a Book instance is deleted
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Informal string representation of the book

        Returns:
            str: A user-friendly string representation
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official string representation of the book

        Returns:
            str: A string that can recreate the Book instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
