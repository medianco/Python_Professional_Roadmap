"""
Lesson 29.9 - Regex Validation

This example demonstrates how Regular Expressions
can be used to validate network-related data.

Network Engineering Context:
Validation is important before sending data
to network devices or using it in automation tasks.

Examples:

- Hostnames
- IPv4 addresses
- VLAN IDs
- Interface names
- MAC addresses

Important:
Regex validates the FORMAT of data.
For semantic validation, specialized Python
modules may be required.

        Regex                   
          ↓
    Format Validation
    
        ipaddress
            ↓
    Semantic Validation
"""

import re
import ipaddress


def validate_hostname(hostname: str) -> None:
    """
    Validate a network device hostname.

    Expected format:
        R1
        SW1
        CORE-SW1
        EDGE-RTR01

    Args:
        hostname: Network device hostname.
    """

    # Hostname rules:
    #
    # ^       -> Start of string
    # [A-Za-z] -> First character must be a letter
    # [A-Za-z0-9-]* -> Remaining characters can contain
    #                  letters, numbers, or hyphens
    # $       -> End of string
    #
    # Example:
    # CORE-R1 -> Valid
    # 123-R1  -> Invalid
    pattern = r"^[A-Za-z][A-Za-z0-9-]*$"

    if re.fullmatch(pattern, hostname):
        print(f"Valid hostname: {hostname}")
    else:
        print(f"Invalid hostname: {hostname}")


def validate_ipv4(ip_address: str) -> None:
    """
    Validate an IPv4 address.

    Regex is first used to validate the format.
    ipaddress is then used for semantic validation.

    Args:
        ip_address: IPv4 address to validate.
    """

    # Basic IPv4 format.
    #
    # Example:
    # 192.168.1.1
    #
    # This pattern checks that there are
    # four numeric components.
    pattern = r"^\d{1,3}(?:\.\d{1,3}){3}$"

    # First check the basic format.
    if not re.fullmatch(pattern, ip_address):
        print(
            f"Invalid IPv4 format: {ip_address}"
        )
        return

    # Regex alone would accept values such as:
    #
    # 999.999.999.999
    #
    # Therefore, use ipaddress for semantic validation.
    try:
        address = ipaddress.ip_address(ip_address)

        # Make sure the address is actually IPv4.
        if address.version != 4:
            print(
                f"Not an IPv4 address: {ip_address}"
            )
            return

    except ValueError:
        print(
            f"Invalid IPv4 address: {ip_address}"
        )
        return

    print(f"Valid IPv4 address: {ip_address}")


def validate_vlan_id(vlan_id: str) -> None:
    """
    Validate a VLAN ID.

    Cisco VLAN IDs commonly range from 1 to 4094.

    Args:
        vlan_id: VLAN ID as a string.
    """

    # Regex checks that the input contains digits only.
    pattern = r"^\d+$"

    if not re.fullmatch(pattern, vlan_id):
        print(f"Invalid VLAN format: {vlan_id}")
        return

    # Convert the validated string to an integer.
    vlan_number = int(vlan_id)

    # Check the actual VLAN range.
    if 1 <= vlan_number <= 4094:
        print(f"Valid VLAN ID: {vlan_id}")
    else:
        print(f"Invalid VLAN ID: {vlan_id}")


def validate_interface(interface: str) -> None:
    """
    Validate a Cisco-style interface name.

    Examples:
        GigabitEthernet0/0
        GigabitEthernet0/1
        Loopback0

    Args:
        interface: Interface name.
    """

    # Match common Cisco interface names.
    #
    # (?:...) is a non-capturing group.
    pattern = (
        r"^(?:GigabitEthernet|"
        r"FastEthernet|Loopback)"
        r"\d+(?:/\d+)*$"
    )

    if re.fullmatch(pattern, interface):
        print(f"Valid interface: {interface}")
    else:
        print(f"Invalid interface: {interface}")


def validate_mac_address(mac_address: str) -> None:
    """
    Validate a Cisco-style MAC address.

    Expected format:
        aaaa.bbbb.cccc

    Args:
        mac_address: MAC address to validate.
    """

    # Cisco commonly displays MAC addresses
    # in the format:
    #
    # aaaa.bbbb.cccc
    #
    # Each hexadecimal group contains 4 characters.
    pattern = (
        r"^[0-9A-Fa-f]{4}"
        r"(?:\.[0-9A-Fa-f]{4}){2}$"
    )

    if re.fullmatch(pattern, mac_address):
        print(f"Valid MAC address: {mac_address}")
    else:
        print(
            f"Invalid MAC address: {mac_address}"
        )


def main() -> None:
    """Run all Regex validation examples."""

    print("=== Hostname Validation ===")

    validate_hostname("R1")
    validate_hostname("CORE-SW1")
    validate_hostname("123-R1")
    validate_hostname("SW@01")

    print("\n=== IPv4 Validation ===")

    validate_ipv4("192.168.1.1")
    validate_ipv4("10.10.10.1")
    validate_ipv4("192.168.1.999")
    validate_ipv4("Cisco")

    print("\n=== VLAN Validation ===")

    validate_vlan_id("10")
    validate_vlan_id("100")
    validate_vlan_id("4094")
    validate_vlan_id("4095")
    validate_vlan_id("VLAN10")

    print("\n=== Interface Validation ===")

    validate_interface("GigabitEthernet0/0")
    validate_interface("GigabitEthernet0/1")
    validate_interface("Loopback0")
    validate_interface("EthernetXYZ")

    print("\n=== MAC Address Validation ===")

    validate_mac_address("aaaa.bbbb.cccc")
    validate_mac_address("1122.3344.5566")
    validate_mac_address("aaaa.bbbb.zzzz")


if __name__ == "__main__":
    main()
