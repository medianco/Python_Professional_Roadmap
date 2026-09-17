"""
Lesson 28.7 - Exception Hierarchy

This example demonstrates Python's exception hierarchy
and how specific and general exceptions work together.

Network Engineering Context:
Understanding exception hierarchy helps us design
precise and maintainable error-handling logic.
"""


def convert_value(value: str) -> None:
    """
    Convert a string into an integer.

    Args:
        value: Value to convert.
    """

    try:
        # Attempt to convert the value to an integer.
        number = int(value)

        print(f"Converted value: {number}")

    except ValueError:
        # ValueError is more specific than Exception.
        print("ValueError: Invalid integer value")

    except Exception:
        # General fallback for unexpected exceptions.
        print("Exception: An unexpected error occurred")


def access_device(
    devices: dict[str, str],
    device_id: str,
) -> None:
    """
    Retrieve a device from a dictionary.

    Args:
        devices: Dictionary containing devices.
        device_id: Device identifier.
    """

    try:
        # Attempt to retrieve the device.
        device = devices[device_id]

        print(f"Device: {device}")

    except KeyError:
        # Handle a missing dictionary key specifically.
        print(f"KeyError: Device '{device_id}' was not found")

    except Exception:
        # General fallback.
        print("Exception: An unexpected error occurred")


def demonstrate_hierarchy() -> None:
    """Demonstrate the relationship between exceptions."""

    print("=== Exception Hierarchy ===")

    print(
        f"ValueError is subclass of Exception: "
        f"{issubclass(ValueError, Exception)}"
    )

    print(
        f"KeyError is subclass of Exception: "
        f"{issubclass(KeyError, Exception)}"
    )

    print(
        f"ConnectionError is subclass of OSError: "
        f"{issubclass(ConnectionError, OSError)}"
    )


def main() -> None:
    """Run the exception hierarchy examples."""

    print("=== ValueError Example ===")
    convert_value("100")
    convert_value("Cisco")

    print("\n=== KeyError Example ===")

    devices = {
        "R1": "Cisco Router",
        "SW1": "Cisco Switch",
    }

    access_device(devices, "R1")
    access_device(devices, "R2")

    print("\n=== Hierarchy Information ===")
    demonstrate_hierarchy()


if __name__ == "__main__":
    main()
