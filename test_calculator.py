#!/usr/bin/env python3
"""
Simple test script for the Calculator class.

This script tests the basic functionality of the calculator operations.
"""

from calculator import Calculator


def test_calculator():
    """Test all calculator operations."""
    calc = Calculator()
    
    print("Testing Calculator operations...")
    
    # Test addition
    result = calc.add(10, 5)
    expected = 15
    print(f"Addition test: 10 + 5 = {result} (expected: {expected}) - {'PASS' if result == expected else 'FAIL'}")
    
    # Test subtraction
    result = calc.subtract(10, 5)
    expected = 5
    print(f"Subtraction test: 10 - 5 = {result} (expected: {expected}) - {'PASS' if result == expected else 'FAIL'}")
    
    # Test multiplication
    result = calc.multiply(10, 5)
    expected = 50
    print(f"Multiplication test: 10 * 5 = {result} (expected: {expected}) - {'PASS' if result == expected else 'FAIL'}")
    
    # Test division
    result = calc.divide(10, 5)
    expected = 2.0
    print(f"Division test: 10 / 5 = {result} (expected: {expected}) - {'PASS' if result == expected else 'FAIL'}")
    
    # Test division by zero
    try:
        result = calc.divide(10, 0)
        print("Division by zero test: FAIL (should have raised ValueError)")
    except ValueError as e:
        print(f"Division by zero test: PASS (correctly raised ValueError: {e})")
    
    # Test with floating point numbers
    result = calc.add(3.14, 2.86)
    expected = 6.0
    print(f"Float addition test: 3.14 + 2.86 = {result} (expected: {expected}) - {'PASS' if abs(result - expected) < 0.001 else 'FAIL'}")
    
    print("\nAll tests completed!")


if __name__ == "__main__":
    test_calculator()