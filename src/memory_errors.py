"""Module demonstrating MemoryError, resource leaks, and dangerous patterns."""


def infinite_list_growth():
    """Build an ever-growing list until memory runs out."""
    data = []
    while True:
        data.append("x" * 10_000_000)  # Bug: MemoryError eventually


def leaky_file_handles(directory):
    """Open files without closing them."""
    handles = []
    for i in range(100_000):
        # Bug: resource leak - files never closed
        f = open(f"{directory}/file_{i}.txt", "w")
        handles.append(f)
        f.write("data")
    # Bug: handles list grows unbounded, files never flushed/closed


def circular_reference():
    """Create objects that reference each other - potential memory leak."""
    class Node:
        def __init__(self, name):
            self.name = name
            self.parent = None
            self.children = []

    nodes = []
    for i in range(100_000):
        parent = Node(f"parent_{i}")
        child = Node(f"child_{i}")
        parent.children.append(child)
        child.parent = parent  # Bug: circular reference prevents garbage collection
        nodes.append(parent)
    return nodes


def huge_string_concatenation(n):
    """Build a string via concatenation in a loop - O(n²) memory usage."""
    result = ""
    for i in range(n):
        result += str(i) + ","  # Bug: quadratic time/memory due to string immutability
    return result


if __name__ == "__main__":
    huge_string_concatenation(1_000_000)
    infinite_list_growth()
