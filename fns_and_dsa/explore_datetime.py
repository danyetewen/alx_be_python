#!/usr/bin/env python3
"""Script to explore Python datetime module by displaying current datetime
and calculating a future date based on user input."""

from datetime import datetime, timedelta


def display_current_datetime():
    """Displays the current date and time in YYYY-MM-DD HH:MM:SS format"""
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date():
    """Calculates and displays the future date based on user input"""
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


# Call the functions
display_current_datetime()
calculate_future_date()
