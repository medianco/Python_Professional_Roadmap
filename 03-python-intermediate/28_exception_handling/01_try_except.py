"""
Lesson 28.1 - Basic Exception Handling

This example demonstrates the basic use of
try and except in Python.
"""


def divide_numbers(number1: int, number2: int) -> None:
    """Divide two numbers and handle division errors."""

    try:
        result = number1 / number2
        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")


def main() -> None:
    """Run the exception handling examples."""

    print("Example 1:")
    divide_numbers(10, 2)

    print("\nExample 2:")
    divide_numbers(10, 0)


if __name__ == "__main__":
    main()
