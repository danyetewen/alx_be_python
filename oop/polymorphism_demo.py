#!/usr/bin/python3
"""
Module for demonstrating Polymorphism and Method Overriding
"""

import math


class Shape:
    """
    Base class representing a geometric shape.
    """

    def area(self):
        """
        Calculates the area of the shape.

        Raises:
            NotImplementedError: This method should be overridden in subclasses.
        """
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """
    Represents a rectangle shape.
    """

    def __init__(self, length, width):
        """
        Initializes a Rectangle instance.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.length * self.width


class Circle(Shape):
    """
    Represents a circle shape.
    """

    def __init__(self, radius):
        """
        Initializes a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)
