"""
Lesson 28.5 - Raising Exceptions

This example demonstrates how to intentionally raise
exceptions using the raise statement.

Network Engineering Context:
We can use raise to validate network device information
and prevent invalid data from entering our application.
        
        IP Address
             │
             ▼
        Validation
             │
         ┌───┴────┐
         │        │
        Valid    Invalid
         │        │
         ▼        ▼
    Continue  raise ValueError
                  │
                  ▼
                except
"""

import ipaddress


def validate_ip_address(ip: str) -> None:
    """
    Validate an IP address.

    Args:
        ip: IP address to validate.

    Raises:
        ValueError: If the IP address is invalid.
    """

    try:
        # Validate the IP address.
        validated_ip = ipaddress.ip_address(ip)

    except ValueError:
        # Raise our own descriptive exception.
        raise ValueError(
            f"Invalid IP address: {ip}"
        )

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
        ValueError: If the hostname is empty.
    """

    if not hostname:
        raise ValueError(
            "Hostname cannot be empty"
        )

    print(f"Valid hostname: {hostname}")


def main() -> None:
    """Run the validation examples."""

    print("=== IP Address Validation ===")

    try:
        validate_ip_address("192.168.1.1")
        validate_ip_address("192.168.1.999")

    except ValueError as error:
        print(f"Validation error: {error}")

    print("\n=== Hostname Validation ===")

    try:
        validate_hostname("R1")
        validate_hostname("")

    except ValueError as error:
        print(f"Validation error: {error}")


if __name__ == "__main__":
    main()
