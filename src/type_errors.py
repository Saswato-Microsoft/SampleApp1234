"""Module demonstrating TypeError and AttributeError scenarios."""


def add_values(a, b):
    """Add two values without type checking."""
    return a + b  # Bug: TypeError when mixing incompatible types (e.g., int + str)


def multiply_list(items, factor):
    """Multiply each element in the list by a factor."""
    return [item * factor for item in items]  # Bug: TypeError if items contain mixed types


def get_length(obj):
    """Get the length of an object."""
    return len(obj)  # Bug: TypeError when obj is int, None, etc.


def process_user(user):
    """Process user data assuming it's a dict."""
    name = user.get("name")  # Bug: AttributeError if user is None or not a dict
    email = user.get("email")
    age = user.upper()  # Bug: AttributeError - calling string method on dict
    return name, email, age


def call_function(func, *args):
    """Call a function with arguments."""
    return func(*args)  # Bug: TypeError if func is not callable


class Calculator:
    def add(self, x, y):
        return x + y

    def compute(self):
        result = self.add(10)  # Bug: TypeError - missing required argument 'y'
        return result


if __name__ == "__main__":
    print(add_values(10, "hello"))
    print(get_length(42))
    print(process_user(None))
    print(call_function("not_a_function", 1, 2))
    Calculator().compute()
