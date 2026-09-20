"""
Lesson 29.6 - match(), search(), findall(), and fullmatch()

This example demonstrates the difference between
the main Regex matching functions in Python.

Network Engineering Context:
These functions are useful when processing:

- Cisco CLI output
- Router configurations
- Interface information
- IP addresses
- VLAN information
- Network logs

        re.match()
            ↓
        Beginning only
        
        re.search()
            ↓
        First match anywhere
        
        re.findall()
            ↓
        All matches
        
        re.fullmatch()
            ↓
        Entire string
"""

import re


def demonstrate_match(text: str) -> None:
    """
    Demonstrate re.match().

    re.match() checks only the beginning of the text.

    Args:
        text: Text to search.
    """

    # re.match() starts matching from the beginning
    # of the string.
    result = re.match(r"Router", text)

    if result:
        print(f"match(): {result.group()}")
    else:
        print("match(): No match found")


def demonstrate_search(text: str) -> None:
    """
    Demonstrate re.search().

    re.search() searches for the first occurrence
    anywhere in the text.

    Args:
        text: Text to search.
    """

    # Unlike match(), search() does not require
    # the pattern to appear at the beginning.
    result = re.search(r"Router", text)

    if result:
        print(f"search(): {result.group()}")
    else:
        print("search(): No match found")


def demonstrate_findall(text: str) -> None:
    """
    Demonstrate re.findall().

    findall() returns all matches found in the text.

    Args:
        text: Text to search.
    """

    # findall() returns a list containing
    # every matching occurrence.
    matches = re.findall(r"Router", text)

    print(f"findall(): {matches}")


def demonstrate_fullmatch(text: str) -> None:
    """
    Demonstrate re.fullmatch().

    fullmatch() requires the entire string
    to match the pattern.

    Args:
        text: Text to validate.
    """

    # The complete string must match "Router".
    result = re.fullmatch(r"Router", text)

    if result:
        print("fullmatch(): Complete match")
    else:
        print("fullmatch(): No complete match")


def extract_ip_addresses(text: str) -> None:
    """
    Extract all IPv4-looking values from text.

    Args:
        text: Network CLI output.
    """

    # This pattern finds values that look like
    # IPv4 addresses.
    #
    # Important:
    # This is a Regex format check only.
    # It does NOT guarantee that the IP address
    # is semantically valid.
    pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"

    matches = re.findall(pattern, text)

    print("IP addresses found:")

    for ip_address in matches:
        print(ip_address)


def main() -> None:
    """Run all Regex matching examples."""

    print("=== match() ===")

    # "Router" appears at the beginning.
    demonstrate_match(
        "Router R1 is operational"
    )

    # "Router" does not appear at the beginning.
    demonstrate_match(
        "Cisco Router R1 is operational"
    )

    print("\n=== search() ===")

    # search() can find Router anywhere in the text.
    demonstrate_search(
        "Cisco Router R1 is operational"
    )

    print("\n=== findall() ===")

    # findall() returns every occurrence.
    demonstrate_findall(
        "Router R1 connected to Router R2"
    )

    print("\n=== fullmatch() ===")

    # The complete text matches the pattern.
    demonstrate_fullmatch("Router")

    # The complete text does not match.
    demonstrate_fullmatch("Router R1")

    print("\n=== Network CLI Example ===")

    # Simulated Cisco CLI output.
    cli_output = """
Interface GigabitEthernet0/0
IP Address: 192.168.1.1

Interface GigabitEthernet0/1
IP Address: 10.10.10.1

Interface Loopback0
IP Address: 172.16.1.1
"""

    extract_ip_addresses(cli_output)


# Run the program only when this file
# is executed directly.
if __name__ == "__main__":
    main()
