"""Module demonstrating ImportError, NameError, and UnboundLocalError scenarios."""


def use_nonexistent_module():
    """Import a module that doesn't exist."""
    import nonexistent_library  # Bug: ModuleNotFoundError
    return nonexistent_library.do_something()


def use_undefined_variable():
    """Reference a variable that was never defined."""
    result = x + 10  # Bug: NameError - 'x' is not defined
    return result


def shadowed_variable(flag):
    """Accidentally shadow a variable with conditional assignment."""
    value = 100
    if flag:
        value = value + 50
    else:
        print("Using default")
    return valeu  # Bug: NameError - typo in variable name


def unbound_local_example(items):
    """Trigger UnboundLocalError with premature reference."""
    total = 0
    for item in items:
        total += item
    if total > 100:
        bonus = total * 0.1
    return total + bonus  # Bug: UnboundLocalError if total <= 100 (bonus never assigned)


def wrong_import_path():
    """Import from a wrong submodule path."""
    from os.path import non_existent_function  # Bug: ImportError
    return non_existent_function("/some/path")


if __name__ == "__main__":
    use_nonexistent_module()
    use_undefined_variable()
    print(shadowed_variable(True))
    print(unbound_local_example([10, 20]))
    wrong_import_path()
