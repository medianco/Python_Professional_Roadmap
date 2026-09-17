"""
Lesson 28.9 - Network Device Validation

This example demonstrates how to validate network
device information before starting automation tasks.

Network Engineering Context:
Before connecting to network devices, an automation
system should validate important information such as:

- Hostname
- IP address
- Device type
- Connection type

Custom exceptions are used to provide clear and
meaningful validation errors.

Device
  │
  ├── Hostname
  │
  ├── IP Address
  │
  ├── Device Type
  │
  └── Connection Type
          │
          ▼
      Validation
          │
     ┌────┴────┐
     │         │
   Valid     Invalid
     │         │
     ▼         ▼
 Success    Exception
"""

import ipaddress


class InvalidHostnameError(Exception):
    """Raised when a hostname is invalid."""


class InvalidIPAddressError(Exception):
    """Raised when an IP address is invalid."""


class InvalidDeviceTypeError(Exception):
    """Raised when a device type is unsupported."""


class InvalidConnectionTypeError(Exception):
    """Raised when a connection type is unsupported."""


def validate_hostname(hostname: str) -> None:
    """
    Validate a network device hostname.

    Args:
        hostname: Device hostname.

    Raises:
        InvalidHostnameError: If hostname is empty.
    """
    if not hostname.strip():
        raise InvalidHostnameError(
            "Hostname cannot be empty"
        )


def validate_ip_address(ip: str) -> None:
    """
    Validate an IPv4 or IPv6 address.

    Args:
        ip: IP address.

    Raises:
        InvalidIPAddressError: If the IP address is invalid.
    """
    try:
        ipaddress.ip_address(ip)
    except ValueError as error:
        raise InvalidIPAddressError(
            f"Invalid IP address: {ip}"
        ) from error


def validate_device_type(device_type: str) -> None:
    """
    Validate the network device type.

    Args:
        device_type: Network device type.

    Raises:
        InvalidDeviceTypeError:
            If the device type is unsupported.
    """
    supported_types = {
        "cisco_router",
        "cisco_switch",
        "juniper_router",
        "juniper_switch",
    }

    if device_type not in supported_types:
        raise InvalidDeviceTypeError(
            f"Unsupported device type: {device_type}"
        )


def validate_connection_type(
    connection_type: str,
) -> None:
    """
    Validate the connection type.

    Args:
        connection_type: Connection method.

    Raises:
        InvalidConnectionTypeError:
            If the connection type is unsupported.
    """
    supported_connections = {
        "ssh",
        "api",
        "netconf",
    }

    if connection_type not in supported_connections:
        raise InvalidConnectionTypeError(
            f"Unsupported connection type: "
            f"{connection_type}"
        )


def validate_device(device: dict[str, str]) -> None:
    """
    Validate all network device information.

    Args:
        device: Dictionary containing device information.
    """
    try:
        validate_hostname(device["hostname"])
        validate_ip_address(device["ip"])
        validate_device_type(device["device_type"])
        validate_connection_type(device["connection"])

    except KeyError as error:
        print(
            f"Validation error: Missing field {error}"
        )
        return

    except (
        InvalidHostnameError,
        InvalidIPAddressError,
        InvalidDeviceTypeError,
        InvalidConnectionTypeError,
    ) as error:
        print(f"Validation error: {error}")
        return

    print(
        f"{device['hostname']}: "
        "Validation successful"
    )


def main() -> None:
    """Run the network device validation example."""

    devices = [
        {
            "hostname": "R1",
            "ip": "192.168.1.1",
            "device_type": "cisco_router",
            "connection": "ssh",
        },
        {
            "hostname": "SW1",
            "ip": "192.168.1.999",
            "device_type": "cisco_switch",
            "connection": "ssh",
        },
        {
            "hostname": "R2",
            "ip": "10.10.10.2",
            "device_type": "juniper_router",
            "connection": "telnet",
        },
        {
            "hostname": "",
            "ip": "10.10.10.3",
            "device_type": "juniper_switch",
            "connection": "netconf",
        },
        {
            "hostname": "R3",
            "ip": "2001:db8::1",
            "device_type": "juniper_router",
            "connection": "netconf",
        },
    ]

    print("=== Network Device Validation ===")

    for device in devices:
        validate_device(device)
        print("-" * 50)


if __name__ == "__main__":
    main()
