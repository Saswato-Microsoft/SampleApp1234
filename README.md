# SampleApp1234 - Buggy Python Code for Testing

A collection of intentionally buggy Python modules for testing error detection, exception handling, and debugging tools.

## Modules

| File | Exception Types |
|------|----------------|
| `divide_by_zero.py` | `ZeroDivisionError` |
| `index_errors.py` | `IndexError`, `KeyError` |
| `type_errors.py` | `TypeError`, `AttributeError` |
| `file_errors.py` | `FileNotFoundError`, `PermissionError`, `JSONDecodeError`, `UnicodeDecodeError` |
| `value_errors.py` | `ValueError`, `OverflowError`, `RecursionError` |
| `concurrency_errors.py` | Race conditions, deadlocks |
| `memory_errors.py` | `MemoryError`, resource leaks |
| `import_and_name_errors.py` | `ModuleNotFoundError`, `NameError`, `UnboundLocalError`, `ImportError` |

## Usage

Run any module directly to trigger its exceptions:

```bash
python src/divide_by_zero.py
python src/index_errors.py
```
