"""
Lesson 29.1 - Regular Expressions Basics

This example demonstrates the basic usage of
Regular Expressions in Python.

Network Engineering Context:
Regex can be used to search for network-related
information inside CLI output, logs, and configuration files.
"""

import re


def main() -> None:
    """Demonstrate basic Regular Expression usage."""

    text = "Cisco Router R1 is operational"

    pattern = r"Router"

    result = re.search(pattern, text)

    if result:
        print("Pattern found")
        print(f"Matched text: {result.group()}")
    else:
        print("Pattern not found")


if __name__ == "__main__":
    main()
