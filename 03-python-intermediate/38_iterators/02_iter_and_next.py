"""
Lesson 38.2 — iter() and next()

Demonstrates manual iteration over network devices.
Shows how Iterator state changes after each next() call.
"""


# Network device inventory.
network_devices = [
    {"hostname": "R1", "vendor": "Cisco", "ip": "192.168.1.1"},
    {"hostname": "R2", "vendor": "Cisco", "ip": "192.168.1.2"},
    {"hostname": "SW1", "vendor": "Cisco", "ip": "192.168.1.10"},
    {"hostname": "J1", "vendor": "Juniper", "ip": "192.168.1.20"},
]


# Create an Iterator from the device inventory.
device_iterator = iter(network_devices)


print("NETWORK DEVICE PROCESSING")
print("=" * 55)


# Retrieve the first device.
device = next(device_iterator)

print(f"Hostname: {device['hostname']}")
print(f"Vendor: {device['vendor']}")
print(f"Management IP: {device['ip']}")


print("\nProcessing the remaining devices:")
print("=" * 55)


# Continue retrieving devices until the Iterator is exhausted.
while True:

    # Use next() with a default value to detect the end.
    device = next(device_iterator, None)

    # Stop processing when no more devices are available.
    if device is None:
        print("No more devices available.")
        break

    # Display the current device information.
    print(
        f"{device['hostname']:<5} | "
        f"{device['vendor']:<10} | "
        f"{device['ip']}"
    )


print("\nInventory processing completed.")
