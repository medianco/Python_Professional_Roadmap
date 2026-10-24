
"""
Lesson 36.8 — namedtuple Basics

Represent network device records with named fields.
"""

from collections import namedtuple


# Define a reusable structure for network devices.
NetworkDevice = namedtuple(
    "NetworkDevice",
    ["hostname", "ip_address", "vendor", "device_type"],
)


def display_device(device: NetworkDevice) -> None:
    """Display the details of a network device."""

    print(f"Hostname:   {device.hostname}")
    print(f"IP Address: {device.ip_address}")
    print(f"Vendor:     {device.vendor}")
    print(f"Device Type:{device.device_type}")


def main() -> None:
    """Create and inspect namedtuple device records."""

    # Create device records using named fields.
    router = NetworkDevice(
        hostname="R1",
        ip_address="192.168.1.1",
        vendor="Cisco",
        device_type="Router",
    )

    switch = NetworkDevice(
        hostname="SW1",
        ip_address="192.168.1.2",
        vendor="Cisco",
        device_type="Switch",
    )

    print("Network Device Inventory")
    print("=" * 35)

    display_device(router)

    print("-" * 35)

    display_device(switch)

    # Access a field by name instead of using a numeric index.
    print("\nRouter hostname:", router.hostname)

    # namedtuple also supports normal tuple indexing.
    print("Router IP by index:", router[1])

    # namedtuple records are immutable.
    print("\nNumber of fields:", len(router))
    print("Router as tuple:", tuple(router))


if __name__ == "__main__":
    main()
