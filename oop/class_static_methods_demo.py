#!/usr/bin/python3
"""
Module for demonstrating Class Methods vs Static Methods in Python.
"""


class Calculator:
    """
    A simple calculator demonstrating the use of class methods and static methods.
    """

    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Adds two numbers together.

        Args:
            a (float or int): The first number.
            b (float or int): The second number.

        Returns:
            float or int: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Multiplies two numbers and prints the calculation type.

        Args:
            a (float or int): The first number.
            b (float or int): The second number.

        Returns:
            float or int: The product of a and b.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
