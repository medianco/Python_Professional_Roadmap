"""
Lesson 29.7 - Network Data Extraction

This example demonstrates how Regular Expressions
can be used to extract structured network information
from CLI output.

Network Engineering Context:
Network Engineers often need to extract information from
raw CLI output, such as:

- Interface names
- IPv4 addresses
- Interface status
- MAC addresses
- VLAN IDs

Regex can help convert raw CLI output into
structured Python data.

############################################################
  CLI Output → Structured Information
  
          Cisco CLI
           │
           ▼
        Raw Text
           │
           ▼
        Regex
           │
           ├── Interfaces
           ├── IP Addresses
           ├── MAC Addresses
           ├── VLAN IDs
           └── Interface Status
"""

import re


def extract_interfaces(text: str) -> None:
    """
    Extract interface names from CLI output.

    Args:
        text: Network device CLI output.
    """

    # This pattern looks for common Cisco interface names.
    #
    # Examples:
    # GigabitEthernet0/0
    # GigabitEthernet0/1
    # FastEthernet0/1
    # Loopback0
    #
    # (?:...) is a non-capturing group.
    # It groups alternatives without creating group numbers.
    pattern = (
        r"\b(?:GigabitEthernet|FastEthernet|"
        r"Loopback)\d+(?:/\d+)*\b"
    )

    # findall() returns all matching interfaces.
    matches = re.findall(pattern, text)

    print("Interfaces found:")

    for interface in matches:
        print(f"- {interface}")


def extract_ip_addresses(text: str) -> None:
    """
    Extract IPv4 addresses from CLI output.

    Args:
        text: Network device CLI output.
    """

    # This Regex finds values that look like IPv4 addresses.
    #
    # Example:
    # 192.168.1.1
    # 10.10.10.1
    # 172.16.1.1
    #
    # This checks the format only.
    # For semantic IP validation, use ipaddress.ip_address().
    pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"

    matches = re.findall(pattern, text)

    print("IP addresses found:")

    for ip_address in matches:
        print(f"- {ip_address}")


def extract_mac_addresses(text: str) -> None:
    """
    Extract MAC addresses from CLI output.

    Args:
        text: Network device CLI output.
    """

    # Cisco devices commonly display MAC addresses
    # using this format:
    #
    # aaaa.bbbb.cccc
    #
    # \b ensures that we match a complete value.
    pattern = r"\b[0-9a-fA-F]{4}(?:\.[0-9a-fA-F]{4}){2}\b"

    matches = re.findall(pattern, text)

    print("MAC addresses found:")

    for mac_address in matches:
        print(f"- {mac_address}")


def extract_vlans(text: str) -> None:
    """
    Extract VLAN IDs from CLI output.

    Args:
        text: Network device CLI output.
    """

    # This pattern looks for:
    #
    # VLAN 10
    # VLAN 20
    # VLAN 100
    #
    # (\d+) captures the VLAN number.
    pattern = r"\bVLAN\s+(\d+)\b"

    matches = re.findall(pattern, text)

    print("VLAN IDs found:")

    for vlan_id in matches:
        print(f"- {vlan_id}")


def extract_interface_status(text: str) -> None:
    """
    Extract interface name and operational status.

    Args:
        text: Network device CLI output.
    """

    # Example input:
    #
    # GigabitEthernet0/0    up    up
    #
    # Group 1 → Interface name
    # Group 2 → Interface status
    # Group 3 → Line protocol status
    #
    pattern = (
        r"^(\S+)\s+"
        r"(up|down)\s+"
        r"(up|down)$"
    )

    # MULTILINE allows ^ and $ to work with each line.
    matches = re.findall(
        pattern,
        text,
        re.MULTILINE,
    )

    print("Interface status:")

    for interface, status, protocol in matches:
        print(
            f"- {interface}: "
            f"Status={status}, "
            f"Protocol={protocol}"
        )


def main() -> None:
    """Run the Network Data Extraction examples."""

    # Simulated Cisco CLI output.
    #
    # In a real Network Automation project,
    # this could come from Netmiko, NAPALM,
    # Paramiko, or another automation library.
    cli_output = """
R1# show interfaces status

GigabitEthernet0/0    up    up
GigabitEthernet0/1    down  down
FastEthernet0/1       up    up
Loopback0             up    up

R1# show ip interface brief

GigabitEthernet0/0    192.168.1.1
GigabitEthernet0/1    10.10.10.1
Loopback0             172.16.1.1

R1# show mac address-table

aaaa.bbbb.cccc
1122.3344.5566

R1# show vlan brief

VLAN 10
VLAN 20
VLAN 100
"""

    print("=== Interface Extraction ===")
    extract_interfaces(cli_output)

    print("\n=== IP Address Extraction ===")
    extract_ip_addresses(cli_output)

    print("\n=== MAC Address Extraction ===")
    extract_mac_addresses(cli_output)

    print("\n=== VLAN Extraction ===")
    extract_vlans(cli_output)

    print("\n=== Interface Status Extraction ===")
    extract_interface_status(cli_output)


# Run main() only when this file
# is executed directly.
if __name__ == "__main__":
    main()
