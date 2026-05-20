"""Utility module for statistical calculations."""


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = sum(numbers)
    average = total / len(numbers)  # Bug: ZeroDivisionError when list is empty
    return average


def calculate_pass_rate(passed, total):
    """Calculate the pass rate as a percentage."""
    return (passed / total) * 100  # Bug: ZeroDivisionError when total is 0
