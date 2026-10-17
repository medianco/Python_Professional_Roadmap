
"""
Lesson 36.1 — Introduction to Collections

Explore Python's built-in collection types and the collections module
using practical network automation examples.
"""

from collections import Counter, defaultdict, deque


def main() -> None:
    """Demonstrate collection types with network device data."""

    # Store device hostnames in a list.
    device_list = ["R1", "R2", "SW1", "R1", "FW1"]

    # Map device hostnames to their management IP addresses.
    device_ips = {
        "R1": "192.168.1.1",
        "R2": "192.168.1.2",
        "SW1": "192.168.1.10",
        "FW1": "192.168.1.254",
    }

    # Store unique vendor names in a set.
    device_vendors = {"Cisco", "Juniper", "Cisco", "Fortinet"}

    # Represent a fixed management endpoint.
    management_endpoint = ("192.168.1.1", 22)

    print("1. Built-in Collections")
    print("-" * 40)

    print(f"Device list: {device_list}")
    print(f"R1 management IP: {device_ips['R1']}")
    print(f"Unique vendors: {device_vendors}")
    print(f"Management endpoint: {management_endpoint}")

    # Count repeated device names in the inventory list.
    device_counts = Counter(device_list)

    print("\n2. Counter — Device Frequency")
    print("-" * 40)

    for hostname, count in device_counts.items():
        print(f"{hostname}: {count}")

    # Group device hostnames by vendor.
    devices_by_vendor = defaultdict(list)

    vendor_inventory = [
        {"hostname": "R1", "vendor": "Cisco"},
        {"hostname": "R2", "vendor": "Cisco"},
        {"hostname": "SW1", "vendor": "Cisco"},
        {"hostname": "FW1", "vendor": "Fortinet"},
    ]

    for device in vendor_inventory:
        devices_by_vendor[device["vendor"]].append(device["hostname"])

    print("\n3. defaultdict — Devices by Vendor")
    print("-" * 40)

    for vendor, hostnames in sorted(devices_by_vendor.items()):
        print(f"{vendor}: {hostnames}")

    # Keep only the three most recent monitoring events.
    recent_events = deque(maxlen=3)

    recent_events.append("R1: SSH_CONNECTED")
    recent_events.append("R2: SSH_CONNECTED")
    recent_events.append("SW1: INTERFACE_DOWN")
    recent_events.append("FW1: LOGIN_FAILURE")

    print("\n4. deque — Recent Events")
    print("-" * 40)

    for event in recent_events:
        print(event)


# Run the demonstration when this file is executed directly.
if __name__ == "__main__":
    main()
