# Issue Documentation

| No. | Issue identified | Tool | Fix applied |
|---|---|---|---|
| 1 | Mutable default argument in `schedule_room()` | Pylint | Replaced the default list with `None` and initialized it inside the function. |
| 2 | Missing function and module docstrings | Pylint | Added docstrings to describe functions and the module. |
| 3 | Unused local variables | Pylint / Flake8 | Removed unnecessary variables from the demonstration. |
| 4 | Bare exception handling in cancellation | Flake8 | Replaced broad exception handling with explicit missing-reservation handling. |
| 5 | Unsafe shell command using `os.system()` | Bandit | Replaced shell execution with safe Python file operations. |
| 6 | File operations without explicit encoding and context managers | Pylint | Used `with open(...)` and UTF-8 encoding. |
| 7 | Room double-booking was accepted | Manual testing | Added validation to reject duplicate reservations. |
| 8 | Equipment inventory could become negative | Manual testing | Validated equipment names and availability before allocation. |
| 9 | Invalid time slots could cause errors | Manual testing | Added time-slot format and range validation. |

## Summary

Pylint improved from 5.60/10 to 9.38/10. Bandit reported zero issues after the fixes. Flake8 still reports a trailing blank-line warning (W391), which remains to be corrected.
