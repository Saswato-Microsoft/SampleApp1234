"""Module demonstrating ValueError, OverflowError, and RecursionError scenarios."""

import math


def parse_int_input(user_input):
    """Convert user input to integer without validation."""
    return int(user_input)  # Bug: ValueError on non-numeric strings


def calculate_square_root(n):
    """Calculate square root without checking for negative numbers."""
    return math.sqrt(n)  # Bug: ValueError when n is negative


def unpack_coordinates(data):
    """Unpack a tuple assuming exactly 3 elements."""
    x, y, z = data  # Bug: ValueError if data doesn't have exactly 3 elements
    return x, y, z


def convert_to_date(date_string):
    """Parse a date string with a fixed format."""
    from datetime import datetime
    return datetime.strptime(date_string, "%Y-%m-%d")  # Bug: ValueError on wrong format


def infinite_recursion(n):
    """Accidentally recurse forever."""
    return infinite_recursion(n + 1)  # Bug: RecursionError - no base case


def calculate_huge_power(base, exp):
    """Calculate extremely large powers."""
    result = math.exp(exp)  # Bug: OverflowError when exp is very large
    return result


def create_range(start, stop, step):
    """Create a range of values."""
    if step == 0:
        pass  # Bug: should raise but silently passes; range() would raise ValueError
    return list(range(start, stop, step))  # Bug: ValueError when step is 0


if __name__ == "__main__":
    print(parse_int_input("not_a_number"))
    print(calculate_square_root(-16))
    print(unpack_coordinates((1, 2)))
    print(convert_to_date("16/05/2026"))
    print(calculate_huge_power(2, 100000))
    print(create_range(0, 10, 0))
