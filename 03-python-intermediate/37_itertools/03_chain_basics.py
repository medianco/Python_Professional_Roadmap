
"""
Lesson 37.3 — Chain Basics

Combine network inventory collections using itertools.chain().
"""

from itertools import chain


def demonstrate_chain() -> None:
    """Combine separate device collections."""

    print("1. CHAIN MULTIPLE ITERABLES")
    print("-" * 45)

    routers = ["R1", "R2"]
    switches = ["SW1", "SW2"]
    firewalls = ["FW1"]

    # chain() processes each iterable in the order provided.
    all_devices = chain(routers, switches, firewalls)

    for device in all_devices:
        print(f"Device: {device}")


def demonstrate_chain_from_iterable() -> None:
    """Flatten a collection containing multiple device groups."""

    print("\n2. CHAIN FROM ITERABLE")
    print("-" * 45)

    device_groups = [
        ["R1", "R2"],
        ["SW1", "SW2"],
        ["FW1", "FW2"],
    ]

    # from_iterable() processes each inner iterable sequentially.
    all_devices = chain.from_iterable(device_groups)

    for device in all_devices:
        print(f"Processing: {device}")


def demonstrate_combined_inventory() -> None:
    """Process enabled devices from separate inventory sources."""

    print("\n3. COMBINED INVENTORY")
    print("-" * 45)

    branch_devices = ["BR-R1", "BR-SW1"]
    datacenter_devices = ["DC-R1", "DC-R2"]
    lab_devices = ["LAB-R1"]

    # chain() allows one loop to process all inventory sources.
    inventory = chain(
        branch_devices,
        datacenter_devices,
        lab_devices,
    )

    device_count = 0

    for device in inventory:
        device_count += 1
        print(f"{device_count}. Ready to process {device}")

    print(f"Total devices: {device_count}")


def main() -> None:
    """Run all demonstrations."""

    demonstrate_chain()
    demonstrate_chain_from_iterable()
    demonstrate_combined_inventory()


if __name__ == "__main__":
    main()

