"""
Lesson 28.2 - Specific Exceptions

This example demonstrates how to handle specific
exception types in Python.

Network Engineering Context:
Different failures may require different handling
strategies in Network Automation.

This example also uses the ipaddress module to
validate IPv4 and IPv6 addresses.
"""

import ipaddress


def convert_to_integer(value: str) -> None:
    """
    Convert a string value to an integer.

    Args:
        value: The value to convert.
    """

    try:
        # Attempt to convert the value to an integer.
        number = int(value)

        # Display the converted value.
        print(f"Converted value: {number}")

    except ValueError:
        # Handle values that cannot be converted to an integer.
        print(f"Error: '{value}' is not a valid integer")


def validate_ip_address(ip: str) -> None:
    """
    Validate an IPv4 or IPv6 address.

    Args:
        ip: IP address to validate.
    """

    try:
        # Validate the IP address.
        ip_address = ipaddress.ip_address(ip)

        # Display the valid IP address and its version.
        print(
            f"Valid IP address: {ip_address} "
            f"(IPv{ip_address.version})"
        )

    except ValueError:
        # Handle invalid IPv4 or IPv6 addresses.
        print(f"Error: '{ip}' is not a valid IP address")


def get_device_hostname(
    devices: dict[str, str],
    device_id: str,
) -> None:
    """
    Retrieve a device hostname from a dictionary.

    Args:
        devices: Dictionary containing device IDs and hostnames.
        device_id: Device ID to search for.
    """

    try:
        # Attempt to retrieve the hostname using the device ID.
        hostname = devices[device_id]

        # Display the hostname.
        print(f"Hostname: {hostname}")

    except KeyError:
        # Handle a device ID that does not exist.
        print(f"Error: Device ID '{device_id}' was not found")


def access_device(devices: list[str], index: int) -> None:
    """
    Access a device from a list using its index.

    Args:
        devices: List of network devices.
        index: Index of the device to access.
    """

    try:
        # Attempt to access the device at the specified index.
        device = devices[index]

        # Display the device.
        print(f"Device: {device}")

    except IndexError:
        # Handle an index that does not exist.
        print(f"Error: Index {index} is out of range")


def main() -> None:
    """Run the specific exception examples."""

    print("=== ValueError: Integer Conversion ===")

    convert_to_integer("100")
    convert_to_integer("Cisco")

    print("\n=== ValueError: IP Address Validation ===")

    validate_ip_address("192.168.1.1")
    validate_ip_address("10.10.10.0")
    validate_ip_address("2001:db8::1")
    validate_ip_address("192.168.1.999")
    validate_ip_address("Cisco")

    print("\n=== KeyError Example ===")

    devices = {
        "R1": "192.168.1.1",
        "R2": "192.168.1.2",
        "R3": "192.168.1.3",
    }

    get_device_hostname(devices, "R1")
    get_device_hostname(devices, "R4")

    print("\n=== IndexError Example ===")

    network_devices = [
        "R1",
        "R2",
        "R3",
    ]

    access_device(network_devices, 1)
    access_device(network_devices, 5)


if __name__ == "__main__":
    main()

