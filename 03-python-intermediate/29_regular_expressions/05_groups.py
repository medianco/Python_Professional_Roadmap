"""
Lesson 29.5 - Regex Groups

This example demonstrates how to use capturing groups
to extract specific parts of text.

Network Engineering Context:
Groups are extremely useful when extracting structured
information from network device output, such as:

- Hostnames
- IP addresses
- Interface names
- VLAN IDs
- MAC addresses
"""

import re


def extract_hostname(text: str) -> None:
    """
    Extract a hostname from text.

    Args:
        text: Text containing hostname information.
    """
    pattern = r"Hostname: (\w+)"

    result = re.search(pattern, text)

    if result:
        print(f"Full match: {result.group()}")
        print(f"Hostname: {result.group(1)}")
    else:
        print("Hostname not found")


def extract_ip_address(text: str) -> None:
    """
    Extract an IP address from text.

    Args:
        text: Text containing IP information.
    """
    pattern = r"IP Address: ([0-9.]+)"

    result = re.search(pattern, text)

    if result:
        print(f"Full match: {result.group()}")
        print(f"IP address: {result.group(1)}")
    else:
        print("IP address not found")


def main() -> None:
    """Run the Regex Groups examples."""

    print("=== Hostname Group ===")

    hostname_text = "Hostname: R1"

    extract_hostname(hostname_text)

    print("\n=== IP Address Group ===")

    ip_text = "IP Address: 192.168.1.1"

    extract_ip_address(ip_text)


if __name__ == "__main__":
    main()
