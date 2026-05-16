"""Module demonstrating ZeroDivisionError scenarios."""


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = sum(numbers)
    average = total / len(numbers)  # Bug: crashes when list is empty
    return average


def percentage_calculator(score, total):
    """Calculate percentage without checking for zero denominator."""
    return (score / total) * 100  # Bug: ZeroDivisionError when total is 0


def distribute_evenly(amount, groups):
    """Split an amount across groups."""
    share = amount // groups  # Bug: no guard against groups=0
    remainder = amount % groups
    return share, remainder


if __name__ == "__main__":
    print(calculate_average([]))
    print(percentage_calculator(85, 0))
    print(distribute_evenly(100, 0))
