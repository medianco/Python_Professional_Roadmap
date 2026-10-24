
"""
Lesson 36.9 — Collections Comparison

Compare Python collection types using network automation examples.
"""

from collections import Counter, defaultdict, deque, namedtuple


def main() -> None:
    """Demonstrate when to use different collection types."""

    # A list stores an ordered collection of devices.
    devices = ["R1", "R2", "SW1", "FW1", "R1"]
    print("1. List — Device Inventory")
    print(devices)

    # A tuple groups values that should remain unchanged.
    management_endpoint = ("R1", "192.168.1.1")
    print("\n2. Tuple — Management Endpoint")
    print(management_endpoint)

    # A dictionary maps device names to their IP addresses.
    device_ips = {
        "R1": "192.168.1.1",
        "R2": "192.168.1.2",
        "SW1": "192.168.1.3",
    }
    print("\n3. Dict — Device IP Lookup")
    print(device_ips["R1"])

    # A set removes duplicate device names.
    unique_devices = set(devices)
    print("\n4. Set — Unique Devices")
    print(sorted(unique_devices))

    # Counter counts repeated network events.
    event_types = [
        "BGP_DOWN",
        "INTERFACE_DOWN",
        "BGP_DOWN",
        "LOGIN_FAILURE",
        "BGP_DOWN",
    ]
    event_counts = Counter(event_types)
    print("\n5. Counter — Event Frequency")
    print(event_counts.most_common())

    # defaultdict groups devices without manual key initialization.
    vendor_devices = defaultdict(list)
    vendor_devices["Cisco"].append("R1")
    vendor_devices["Cisco"].append("SW1")
    vendor_devices["Juniper"].append("R2")
    print("\n6. defaultdict — Devices by Vendor")
    print(dict(vendor_devices))

    # deque keeps only the latest three monitoring events.
    recent_events = deque(maxlen=3)
    for event in ["LINK_UP", "BGP_DOWN", "LOGIN_FAILURE", "LINK_DOWN"]:
        recent_events.append(event)
    print("\n7. deque — Recent Events")
    print(list(recent_events))

    # namedtuple provides readable names for fixed record fields.
    NetworkDevice = namedtuple(
        "NetworkDevice",
        ["hostname", "ip_address"],
    )
    device = NetworkDevice("R1", "192.168.1.1")
    print("\n8. namedtuple — Device Record")
    print(f"{device.hostname}: {device.ip_address}")


if __name__ == "__main__":
    main()
