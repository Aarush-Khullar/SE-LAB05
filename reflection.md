# Reflection

## 1. Why is static analysis important?

Static analysis helps identify potential programming errors, security vulnerabilities, and code-quality issues without executing every possible program path.

## 2. How do Pylint, Bandit, and Flake8 differ?

Pylint checks code quality, naming conventions, and maintainability. Bandit detects common security risks in Python code. Flake8 checks coding style and selected programming errors.

## 3. What issues were fixed?

The program was improved by removing a mutable default argument, handling missing reservations safely, validating time slots and equipment availability, preventing duplicate bookings, and replacing unsafe shell execution with Python file operations.

## 4. What did I learn?

I learned that different static-analysis tools serve different purposes. Fixing warnings can improve readability and security, but functional testing is also necessary to ensure that the application behaves correctly.
