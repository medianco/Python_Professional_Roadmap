"""
Lesson 29.4 - Regex Anchors

This example demonstrates Regex anchors
in Python.

Network Engineering Context:
Anchors are useful when analyzing:

- CLI output
- Configuration lines
- Hostnames
- Interface configuration
- Log entries

They allow us to control where a pattern
must appear inside the text.
"""

import re


def find_lines_starting_with_router(text: str) -> None:
    """
    Find lines that start with the word 'Router'.

    Args:
        text: Text containing multiple lines.
    """
    matches = re.findall(
        r"^Router.*",
        text,
        re.MULTILINE,
    )

    print("Lines starting with 'Router':")
    for match in matches:
        print(match)


def find_lines_ending_with_up(text: str) -> None:
    """
    Find lines that end with the word 'up'.

    Args:
        text: Text containing multiple lines.
    """
    matches = re.findall(
        r".*up$",
        text,
        re.MULTILINE,
    )

    print("\nLines ending with 'up':")
    for match in matches:
        print(match)


def find_word_boundary(text: str) -> None:
    """
    Find the word 'Router' as a complete word.

    Args:
        text: Text to search.
    """
    matches = re.findall(
        r"\bRouter\b",
        text,
    )

    print("\nComplete word matches:")
    print(matches)


def main() -> None:
    """Run the Regex anchor examples."""

    cli_output = """
Router R1
Switch SW1
Router R2
Firewall FW1
Interface Gi0/1 up
Interface Gi0/2 down
Loopback0 up
"""

    print("=== Start Anchor (^) ===")
    find_lines_starting_with_router(cli_output)

    print("\n=== End Anchor ($) ===")
    find_lines_ending_with_up(cli_output)

    print("\n=== Word Boundary (\\b) ===")
    text = "Router R1 is a router. RouterOS is different."
    find_word_boundary(text)


if __name__ == "__main__":
    main()
