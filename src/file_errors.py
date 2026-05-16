"""Module demonstrating FileNotFoundError, PermissionError, and IOError scenarios."""

import json
import os


def read_config(filepath):
    """Read a configuration file without existence check."""
    with open(filepath, "r") as f:  # Bug: FileNotFoundError if file doesn't exist
        return json.load(f)


def append_log(filepath, message):
    """Append a message to a log file in a non-existent directory."""
    # Bug: FileNotFoundError - directory may not exist
    with open(os.path.join("/nonexistent/path", filepath), "a") as f:
        f.write(message + "\n")


def read_binary_as_text(filepath):
    """Read a binary file as text."""
    with open(filepath, "r", encoding="utf-8") as f:  # Bug: UnicodeDecodeError on binary files
        return f.read()


def write_to_readonly(filepath):
    """Write to a file without checking permissions."""
    os.chmod(filepath, 0o444)  # Make read-only
    with open(filepath, "w") as f:  # Bug: PermissionError
        f.write("new content")


def parse_json_data(raw_data):
    """Parse JSON from a string."""
    return json.loads(raw_data)  # Bug: json.JSONDecodeError on invalid JSON


if __name__ == "__main__":
    print(read_config("/does/not/exist.json"))
    append_log("app.log", "started")
    print(parse_json_data("{invalid json!!!}"))
