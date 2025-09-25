#!/usr/bin/env python3
"""
Basic Calculator Console Application

This module provides a simple calculator with basic arithmetic operations.
"""

import sys


class Calculator:
    """A simple calculator class with basic arithmetic operations."""
    
    @staticmethod
    def add(a, b):
        """Add two numbers."""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Subtract second number from first number."""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Divide first number by second number."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


def get_number_input(prompt):
    """Get a number from user input with validation."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def display_menu():
    """Display the calculator menu."""
    print("\n=== Basic Calculator ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("========================")


def main():
    """Main function to run the calculator application."""
    calculator = Calculator()
    
    print("Welcome to the Basic Calculator!")
    
    while True:
        display_menu()
        
        try:
            choice = input("Select an operation (1-5): ").strip()
            
            if choice == '5':
                print("Thank you for using the calculator. Goodbye!")
                sys.exit(0)
            
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice. Please select 1-5.")
                continue
            
            # Get numbers from user
            num1 = get_number_input("Enter first number: ")
            num2 = get_number_input("Enter second number: ")
            
            # Perform calculation based on choice
            if choice == '1':
                result = calculator.add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = calculator.subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = calculator.multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = calculator.divide(num1, num2)
                operation = "/"
            
            # Display result
            print(f"\nResult: {num1} {operation} {num2} = {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted by user. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()