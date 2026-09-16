"""
Lesson 28.3 - Multiple Exceptions

This example demonstrates how to handle multiple
exception types in Python.

Network Engineering Context:
Network automation scripts often process dictionaries,
lists, user input, IP addresses, and device information.
Each operation may generate a different exception.
"""

import ipaddress


def process_device(
    devices: dict[str, str],
    device_id: str,
) -> None:
    """
    Retrieve and validate a device IP address.

    Args:
        devices: Dictionary containing device IDs and IP addresses.
        device_id: Device ID to process.
    """

    try:
        # Retrieve the IP address using the device ID.
        ip = devices[device_id]

        # Validate the IP address.
        validated_ip = ipaddress.ip_address(ip)

        print(
            f"{device_id}: {validated_ip} "
            f"(IPv{validated_ip.version})"
        )

    except KeyError:
        # Handle a device ID that does not exist.
        print(f"{device_id}: Device ID was not found")

    except ValueError:
        # Handle an invalid IP address.
        print(f"{device_id}: Invalid IP address")


def convert_device_id(value: str) -> None:
    """
    Convert a device ID to an integer.

    This is intentionally used to demonstrate ValueError.

    Args:
        value: Value to convert.
    """

    try:
        device_id = int(value)
        print(f"Device ID: {device_id}")

    except ValueError:
        print(f"Invalid device ID: {value}")


def main() -> None:
    """Run the multiple exception examples."""

    devices = {
        "R1": "192.168.1.1",
        "R2": "10.10.10.999",
        "R3": "2001:db8::1",
    }

    print("=== Network Device Validation ===")

    process_device(devices, "R1")
    process_device(devices, "R2")
    process_device(devices, "R3")
    process_device(devices, "R4")

    print("\n=== Device ID Conversion ===")

    convert_device_id("100")
    convert_device_id("R1")


if __name__ == "__main__":
    main()
