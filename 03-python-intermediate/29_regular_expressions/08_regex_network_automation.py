"""
Lesson 29.8 - Regex in Network Automation

This example demonstrates how Regular Expressions
can be used in a Network Automation workflow.

Network Engineering Context:
Network Automation tools may receive raw CLI output
from network devices.

Regex can be used to extract structured information
from that output and convert it into Python data.

        Raw CLI
           ↓
        Regex
           ↓
        Captured Groups
           ↓
        Python Dictionary
           ↓
        Automation Logic
"""

import re


def parse_interface_output(
    cli_output: str,
) -> list[dict[str, str]]:
    """
    Parse interface information from CLI output.

    Args:
        cli_output: Raw CLI output from a network device.

    Returns:
        A list of dictionaries containing interface data.
    """

    # The expected CLI format is:
    #
    # GigabitEthernet0/0    192.168.1.1    up    up
    #
    # Group 1 -> Interface
    # Group 2 -> IP address
    # Group 3 -> Status
    # Group 4 -> Protocol
    #
    pattern = (
        r"^(\S+)\s+"
        r"(\d{1,3}(?:\.\d{1,3}){3})\s+"
        r"(up|down)\s+"
        r"(up|down)$"
    )

    # MULTILINE allows ^ and $ to work
    # with every line in the CLI output.
    matches = re.findall(
        pattern,
        cli_output,
        re.MULTILINE,
    )

    interfaces: list[dict[str, str]] = []

    # Convert every Regex match into
    # a structured Python dictionary.
    for interface, ip_address, status, protocol in matches:
        interface_data = {
            "interface": interface,
            "ip_address": ip_address,
            "status": status,
            "protocol": protocol,
        }

        interfaces.append(interface_data)

    return interfaces


def display_interfaces(
    interfaces: list[dict[str, str]],
) -> None:
    """
    Display parsed interface information.

    Args:
        interfaces: List of interface dictionaries.
    """

    for interface in interfaces:
        print(
            f"Interface: {interface['interface']}"
        )
        print(
            f"IP Address: {interface['ip_address']}"
        )
        print(
            f"Status: {interface['status']}"
        )
        print(
            f"Protocol: {interface['protocol']}"
        )
        print("-" * 40)


def main() -> None:
    """Run the Network Automation example."""

    # Simulated output returned by a network device.
    #
    # In a real project, this output could come from
    # Netmiko, Paramiko, NAPALM, or another automation tool.
    cli_output = """
GigabitEthernet0/0    192.168.1.1    up    up
GigabitEthernet0/1    10.10.10.1     down  down
Loopback0             172.16.1.1     up    up
"""

    print("=== Raw CLI Output ===")
    print(cli_output)

    # Parse the raw CLI output.
    interfaces = parse_interface_output(
        cli_output
    )

    print("=== Parsed Interface Data ===")

    # Display the structured information.
    display_interfaces(interfaces)


if __name__ == "__main__":
    main()
