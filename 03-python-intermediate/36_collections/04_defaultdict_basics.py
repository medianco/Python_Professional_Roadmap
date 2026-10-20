
"""
Lesson 36.4 — defaultdict Basics

Group network devices by vendor using defaultdict.
"""

from collections import defaultdict


def group_devices_by_vendor(
    devices: list[dict[str, str]],
) -> dict[str, list[str]]:
    """Group device hostnames by vendor."""

    # Create an empty list automatically for each new vendor.
    vendor_devices = defaultdict(list)

    # Add each hostname to its vendor group.
    for device in devices:
        vendor = device["vendor"]
        hostname = device["hostname"]

        vendor_devices[vendor].append(hostname)

    # Return a regular dictionary for the caller.
    return dict(vendor_devices)


def main() -> None:
    """Demonstrate defaultdict with a network inventory."""

    # Define a small inventory for this focused example.
    devices = [
        {"hostname": "R1", "vendor": "Cisco"},
        {"hostname": "R2", "vendor": "Cisco"},
        {"hostname": "SW1", "vendor": "Cisco"},
        {"hostname": "J1", "vendor": "Juniper"},
        {"hostname": "J2", "vendor": "Juniper"},
        {"hostname": "FW1", "vendor": "Fortinet"},
    ]

    # Group devices by vendor.
    grouped_devices = group_devices_by_vendor(devices)

    print("Network Devices Grouped by Vendor")
    print("=" * 40)

    for vendor, hostnames in grouped_devices.items():
        print(f"{vendor}: {', '.join(hostnames)}")
        print(f"Device count: {len(hostnames)}")
        print("-" * 40)


if __name__ == "__main__":
    main()
