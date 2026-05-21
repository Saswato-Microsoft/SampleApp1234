"""Module demonstrating ZeroDivisionError scenarios."""


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    total = sum(numbers)
    return total / len(numbers)


def percentage_calculator(score, total):
    """Calculate percentage with a zero-denominator guard."""
    if total == 0:
        return 0
    return (score / total) * 100


def distribute_evenly(amount, groups):
    """Split an amount across groups."""
    if groups == 0:
        raise ValueError("groups must be greater than zero")
    share = amount // groups
    remainder = amount % groups
    return share, remainder


if __name__ == "__main__":
    print(calculate_average([]))
    print(percentage_calculator(85, 0))
    print(distribute_evenly(100, 1))
