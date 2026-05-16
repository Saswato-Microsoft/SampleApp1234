"""Module demonstrating IndexError and KeyError scenarios."""


def get_last_element(items):
    """Return the last element of a list."""
    return items[-1]  # Bug: IndexError on empty list


def get_nth_element(items, n):
    """Return the nth element without bounds checking."""
    return items[n]  # Bug: IndexError when n >= len(items)


def swap_first_last(items):
    """Swap the first and last elements of a list."""
    first = items[0]  # Bug: IndexError on empty list
    last = items[-1]
    items[0] = last
    items[-1] = first
    return items


def lookup_user(user_db, user_id):
    """Retrieve user info from a dictionary."""
    return user_db[user_id]  # Bug: KeyError if user_id doesn't exist


def get_nested_config(config):
    """Access deeply nested config values without safety checks."""
    db_host = config["database"]["host"]  # Bug: KeyError on missing keys
    db_port = config["database"]["port"]
    cache_ttl = config["cache"]["ttl"]
    return db_host, db_port, cache_ttl


if __name__ == "__main__":
    print(get_last_element([]))
    print(get_nth_element([1, 2, 3], 10))
    print(swap_first_last([]))
    print(lookup_user({"alice": "admin"}, "bob"))
    print(get_nested_config({"database": {"host": "localhost"}}))
