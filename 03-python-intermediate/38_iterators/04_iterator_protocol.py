
"""
Lesson 38.4 — Iterator Protocol

Demonstrates how to implement the Iterator Protocol
using a network device inventory.
"""

from collections.abc import Iterable, Iterator


class NetworkDeviceIterator:
    """
    Custom Iterator for processing network devices.

    Attributes:
        devices: Collection of network devices.
        index: Current position in the collection.
    """

    def __init__(self, devices):
        # Store the device collection.
        self.devices = devices

        # Initialize the current position.
        self.index = 0

    def __iter__(self):
        # An Iterator must return itself from __iter__().
        return self

    def __next__(self):
        # Check whether all devices have been processed.
        if self.index >= len(self.devices):
            raise StopIteration

        # Retrieve the device at the current position.
        device = self.devices[self.index]

        # Move to the next position.
        self.index += 1

        # Return the current device.
        return device


class NetworkDeviceInventory:
    """
    Iterable collection of network devices.

    Each call to __iter__() creates a new Iterator.
    """

    def __init__(self, devices):
        # Store the network device inventory.
        self.devices = devices

    def __iter__(self):
        # Return a new Iterator for this inventory.
        return NetworkDeviceIterator(self.devices)


def main():
    """Demonstrate the Iterator Protocol."""

    # Define the network device inventory.
    devices = [
        {"hostname": "R1", "vendor": "Cisco"},
        {"hostname": "R2", "vendor": "Cisco"},
        {"hostname": "SW1", "vendor": "Cisco"},
        {"hostname": "J1", "vendor": "Juniper"},
    ]

    # Create an Iterable inventory.
    inventory = NetworkDeviceInventory(devices)

    print("NETWORK DEVICE INVENTORY")
    print("=" * 55)

    # Check the Iterable and Iterator interfaces.
    print(f"Is Iterable: {isinstance(inventory, Iterable)}")
    print(f"Is Iterator: {isinstance(inventory, Iterator)}")

    # Obtain an Iterator from the inventory.
    device_iterator = iter(inventory)

    print(f"Iterator type: {type(device_iterator).__name__}")
    print(
        f"Iterator check: "
        f"{isinstance(device_iterator, Iterator)}"
    )

    print("\nPROCESSING DEVICES")
    print("=" * 55)

    # Process all devices using the Iterator Protocol.
    for device in inventory:
        print(
            f"Hostname: {device['hostname']:<5} | "
            f"Vendor: {device['vendor']}"
        )

    print("\nINDEPENDENT ITERATORS")
    print("=" * 55)

    # Create two independent Iterators.
    first_iterator = iter(inventory)
    second_iterator = iter(inventory)

    # Advance only the first Iterator.
    print(f"First Iterator: {next(first_iterator)['hostname']}")

    # The second Iterator starts from the beginning.
    print(f"Second Iterator: {next(second_iterator)['hostname']}")

    print("\nInventory processing completed.")


if __name__ == "__main__":
    main()

