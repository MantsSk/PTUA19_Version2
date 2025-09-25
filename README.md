# PTUA19_Version2

## Basic Python Calculator Console App

A simple console-based calculator application written in Python that supports basic arithmetic operations.

### Features

- Addition, subtraction, multiplication, and division
- Input validation and error handling
- Division by zero protection
- Support for floating-point numbers
- User-friendly interactive console interface

### Usage

Run the calculator:

```bash
python3 calculator.py
```

The calculator will present a menu with the following options:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit

Simply select an operation by entering the corresponding number, then enter two numbers when prompted.

### Example

```
=== Basic Calculator ===
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit
========================
Select an operation (1-5): 1
Enter first number: 10
Enter second number: 5

Result: 10.0 + 5.0 = 15.0
```

### Testing

Run the test suite to verify calculator functionality:

```bash
python3 test_calculator.py
```

### Files

- `calculator.py` - Main calculator application
- `test_calculator.py` - Simple test suite for the calculator operations
- `README.md` - This documentation
