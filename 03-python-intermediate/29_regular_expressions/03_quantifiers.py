"""
Lesson 29.3 - Regex Quantifiers

This example demonstrates Regex quantifiers
in Python.

Network Engineering Context:
Quantifiers are useful when processing values
such as:

- Device IDs
- Interface numbers
- VLAN IDs
- IP address components
- Port numbers
"""

import re


def find_one_or_more_digits(text: str) -> None:
    """
    Find one or more consecutive digits.

    Args:
        text: Text to search.
    """
    matches = re.findall(r"\d+", text)

    print(f"Text: {text}")
    print(f"Numbers: {matches}")


def find_exact_digits(text: str) -> None:
    """
    Find exactly two consecutive digits.

    Args:
        text: Text to search.
    """
    matches = re.findall(r"\d{2}", text)

    print(f"Text: {text}")
    print(f"Two-digit groups: {matches}")


def find_at_least_two_digits(text: str) -> None:
    """
    Find groups containing at least two digits.

    Args:
        text: Text to search.
    """
    matches = re.findall(r"\d{2,}", text)

    print(f"Text: {text}")
    print(f"Two or more digits: {matches}")


def find_two_to_four_digits(text: str) -> None:
    """
    Find groups containing two to four digits.

    Args:
        text: Text to search.
    """
    matches = re.findall(r"\d{2,4}", text)

    print(f"Text: {text}")
    print(f"Two to four digits: {matches}")


def main() -> None:
    """Run the Regex quantifier examples."""

    print("=== One or More Digits (+) ===")
    find_one_or_more_digits(
        "R1 VLAN10 VLAN100 SW24"
    )

    print("\n=== Exactly Two Digits ({2}) ===")
    find_exact_digits(
        "VLAN10 VLAN100 SW24"
    )

    print("\n=== At Least Two Digits ({2,}) ===")
    find_at_least_two_digits(
        "R1 VLAN10 VLAN100 SW24"
    )

    print("\n=== Two to Four Digits ({2,4}) ===")
    find_two_to_four_digits(
        "R1 VLAN10 VLAN100 SW24"
    )


if __name__ == "__main__":
    main()
