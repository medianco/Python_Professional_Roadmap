"""
Lesson 29.2 - Character Classes

This example demonstrates Regex character classes
in Python.

Network Engineering Context:
Character classes are useful when processing
network device output such as:

- Device IDs
- Interface numbers
- VLAN IDs
- Hostnames
- IP-related data
"""

import re


def find_digits(text: str) -> None:
    """Find all digits in the provided text."""

    matches = re.findall("\\d", text)

    print(f"Text: {text}")
    print(f"Digits: {matches}")


def find_word_characters(text: str) -> None:
    """Find all word characters in the provided text."""

    matches = re.findall(r"\w", text)

    print(f"Text: {text}")
    print(f"Word characters: {matches}")


def find_uppercase_letters(text: str) -> None:
    """Find all uppercase letters in the provided text."""

    matches = re.findall(r"[A-Z]", text)

    print(f"Text: {text}")
    print(f"Uppercase letters: {matches}")


def find_lowercase_letters(text: str) -> None:
    """Find all lowercase letters in the provided text."""

    matches = re.findall(r"[a-z]", text)

    print(f"Text: {text}")
    print(f"Lowercase letters: {matches}")


def main() -> None:
    """Run the Character Classes examples."""

    print("=== Digits ===")
    find_digits("R1 Interface 10")

    print("\n=== Word Characters ===")
    find_word_characters("R1_SW1")

    print("\n=== Uppercase Letters ===")
    find_uppercase_letters("Cisco Router")

    print("\n=== Lowercase Letters ===")
    find_lowercase_letters("Cisco Router")


if __name__ == "__main__":
    main()
