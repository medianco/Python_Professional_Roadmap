"""
Lesson 28.6 - Custom Exceptions

This example demonstrates how to create and use
custom exceptions in Python.

Network Engineering Context:
Custom exceptions allow Network Automation systems
to provide clear and meaningful error types for
network-specific validation and operations.

########################################################
                 Network Automation
                         │
                         ▼
                   Validation Layer
                         │
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
   IP Validation    Hostname Check    Device Type
        │                │                │
        ↓                ↓                ↓
InvalidIPAddress   InvalidHostname   InvalidDeviceType
        │                │                │
        └────────────────┼────────────────┘
                         ↓
                  Exception Handler
                         │
                         ↓
                       Logger
########################################################                       
"""

import ipaddress


class InvalidIPAddressError(Exception):
    """Raised when an invalid IP address is provided."""


class InvalidHostnameError(Exception):
    """Raised when an invalid hostname is provided."""


class InvalidDeviceTypeError(Exception):
    """Raised when an unsupported device type is provided."""


def validate_ip_address(ip: str) -> None:
    """
    Validate an IP address.

    Args:
        ip: IP address to validate.

    Raises:
        InvalidIPAddressError: If the IP address is invalid.
    """

    try:
        # Validate the IPv4 or IPv6 address.
        validated_ip = ipaddress.ip_address(ip)

    except ValueError as error:
        # Convert the built-in ValueError into our
        # application-specific exception.
        raise InvalidIPAddressError(
            f"Invalid IP address: {ip}"
        ) from error

    print(
        f"Valid IP address: "
        f"{validated_ip} (IPv{validated_ip.version})"
    )


def validate_hostname(hostname: str) -> None:
    """
    Validate a network device hostname.

    Args:
        hostname: Network device hostname.

    Raises:
        InvalidHostnameError: If the hostname is invalid.
    """

    # Check whether the hostname is empty.
    if not hostname.strip():
        raise InvalidHostnameError(
            "Hostname cannot be empty"
        )

    print(f"Valid hostname: {hostname}")


def validate_device_type(device_type: str) -> None:
    """
    Validate a network device type.

    Args:
        device_type: Device type to validate.

    Raises:
        InvalidDeviceTypeError: If the device type is unsupported.
    """

    supported_devices = {
        "cisco_router",
        "cisco_switch",
        "juniper_router",
        "juniper_switch",
    }

    if device_type not in supported_devices:
        raise InvalidDeviceTypeError(
            f"Unsupported device type: {device_type}"
        )

    print(f"Valid device type: {device_type}")


def main() -> None:
    """Run the custom exception examples."""

    print("=== IP Address Validation ===")

    try:
        validate_ip_address("192.168.1.1")
        validate_ip_address("192.168.1.999")

    except InvalidIPAddressError as error:
        print(f"IP validation error: {error}")

    print("\n=== Hostname Validation ===")

    try:
        validate_hostname("R1")
        validate_hostname("")

    except InvalidHostnameError as error:
        print(f"Hostname validation error: {error}")

    print("\n=== Device Type Validation ===")

    try:
        validate_device_type("cisco_router")
        validate_device_type("fortinet_firewall")

    except InvalidDeviceTypeError as error:
        print(f"Device type validation error: {error}")


if __name__ == "__main__":
    main()
