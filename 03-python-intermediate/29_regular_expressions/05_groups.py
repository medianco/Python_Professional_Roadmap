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

    # (\w+) is a capturing group.
    # \w matches word characters such as letters, digits, and "_".
    # + means one or more characters.
    #
    # Example:
    # "Hostname: R1"
    #             ↑
    #          group(1)
    pattern = r"Hostname: (\w+)"

    # re.search() looks for the pattern anywhere in the text.
    result = re.search(pattern, text)

    if result:
        # group() returns the complete matched text.
        print(f"Full match: {result.group()}")

        # group(1) returns the content captured
        # by the first parentheses.
        print(f"Hostname: {result.group(1)}")
    else:
        print("Hostname not found")


def extract_ip_address(text: str) -> None:
    """
    Extract an IP address from text.

    Args:
        text: Text containing IP information.
    """

    # ([0-9.]+) is a capturing group.
    #
    # [0-9.] means:
    # Match digits from 0 to 9 OR a dot (.).
    #
    # + means one or more characters.
    #
    # Example:
    # "IP Address: 192.168.1.1"
    #              ↑
    #           group(1)
    pattern = r"IP Address: ([0-9.]+)"

    # Search for the IP address pattern.
    result = re.search(pattern, text)

    if result:
        # Display the complete match.
        print(f"Full match: {result.group()}")

        # Extract only the captured IP address.
        print(f"IP address: {result.group(1)}")
    else:
        print("IP address not found")


def extract_device_information(text: str) -> None:
    """
    Extract hostname and IP address from network device output.

    Args:
        text: CLI output containing device information.
    """

    # First capturing group:
    # Hostname:\s*(\w+)
    #
    # \s* allows zero or more spaces after "Hostname:".
    #
    # (\w+) captures the hostname.
    #
    # Second capturing group:
    # IP Address:\s*([0-9.]+)
    #
    # ([0-9.]+) captures the IP address.
    #
    # .*? allows us to move from the hostname line
    # to the IP address line without consuming too much text.
    pattern = (
        r"Hostname:\s*(\w+)"
        r".*?"
        r"IP Address:\s*([0-9.]+)"
    )

    # re.DOTALL allows the "." character to match
    # newline characters as well.
    #
    # This is important because the hostname and IP address
    # are located on different lines in the CLI output.
    result = re.search(
        pattern,
        text,
        re.DOTALL,
    )

    if result:
        # group(1) contains the hostname.
        hostname = result.group(1)

        # group(2) contains the IP address.
        ip_address = result.group(2)

        print(f"Hostname: {hostname}")
        print(f"IP Address: {ip_address}")
    else:
        print("Device information not found")


def main() -> None:
    """Run the Regex Groups examples."""

    print("=== Hostname Group ===")

    # Example of extracting a hostname.
    hostname_text = "Hostname: R1"

    extract_hostname(hostname_text)

    print("\n=== IP Address Group ===")

    # Example of extracting an IP address.
    ip_text = "IP Address: 192.168.1.1"

    extract_ip_address(ip_text)

    print("\n=== Complete Device Information ===")

    # Simulated network device CLI output.
    #
    # This is similar to information that could be
    # returned by a router or switch.
    device_output = """
R1# show device information

Hostname: R1
IP Address: 192.168.1.1
"""

    # Extract both hostname and IP address.
    extract_device_information(device_output)


# This ensures that main() runs only when
# this file is executed directly.
if __name__ == "__main__":
    main()
