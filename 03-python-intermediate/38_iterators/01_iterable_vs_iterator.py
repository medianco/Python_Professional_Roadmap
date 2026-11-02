"""
Lesson 38.1 — Iterable vs Iterator

Demonstrates the difference between an Iterable
and an Iterator using a network device inventory.
"""


# A list is an Iterable because it can provide an Iterator.
network_devices = ["R1", "R2", "SW1"]


print("NETWORK DEVICE INVENTORY")
print("=" * 45)


# Display the type of the original object.
print(f"Original object type: {type(network_devices)}")


# Check whether the list provides the Iterator Protocol.
print(f"Is Iterable: {hasattr(network_devices, '__iter__')}")
print(f"Is Iterator: {hasattr(network_devices, '__next__')}")


# Create an Iterator from the network device list.
device_iterator = iter(network_devices)


print("\nITERATOR INFORMATION")
print("=" * 45)


# Display the type of the Iterator.
print(f"Iterator object type: {type(device_iterator)}")


# Check the Iterator Protocol methods.
print(f"Has __iter__: {hasattr(device_iterator, '__iter__')}")
print(f"Has __next__: {hasattr(device_iterator, '__next__')}")


print("\nREADING NETWORK DEVICES")
print("=" * 45)


# Retrieve the first device from the Iterator.
first_device = next(device_iterator)
print(f"First device: {first_device}")


# Retrieve the second device from the Iterator.
second_device = next(device_iterator)
print(f"Second device: {second_device}")


# Retrieve the third device from the Iterator.
third_device = next(device_iterator)
print(f"Third device: {third_device}")
