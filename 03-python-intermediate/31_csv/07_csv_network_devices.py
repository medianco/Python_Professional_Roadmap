"""
Lesson 31.7 - CSV & Network Devices

This lesson demonstrates how to use a CSV file
as a Network Device Inventory.

Network Engineering Context:
CSV files are commonly used to maintain network
device inventories and provide input for automation.

In this lesson we will:

1. Read the CSV inventory.
2. Display all devices.
3. Filter Cisco devices.
4. Filter routers.
5. Filter switches.
6. Display inventory statistics.
"""

# Import Python's built-in CSV module.
import csv


# -------------------------------------------------------------
# File Path
# -------------------------------------------------------------

# Define the path to the network device inventory.
CSV_FILE = "data/network_devices.csv"


# -------------------------------------------------------------
# Load Network Devices
# -------------------------------------------------------------

# Create an empty list to store all network devices.
devices = []


# Open the CSV inventory file.
with open(CSV_FILE, "r", encoding="utf-8", newline="") as file:

    # Create a DictReader object.
    #
    # Each CSV row will be converted into a dictionary.
    reader = csv.DictReader(file)

    # Read every device from the CSV file.
    for device in reader:

        # Add the device dictionary to our devices list.
        devices.append(device)


# -------------------------------------------------------------
# Display All Devices
# -------------------------------------------------------------

print("=== All Network Devices ===")

# Loop through all devices.
for device in devices:

    print(
        f"{device['hostname']} | "
        f"{device['management_ip']} | "
        f"{device['device_type']} | "
        f"{device['vendor']}"
    )


# -------------------------------------------------------------
# Filter Cisco Devices
# -------------------------------------------------------------

print("\n=== Cisco Devices ===")

# Loop through all devices.
for device in devices:

    # Check whether the vendor is Cisco.
    if device["vendor"] == "Cisco":

        print(
            f"{device['hostname']} | "
            f"{device['management_ip']} | "
            f"{device['device_type']}"
        )


# -------------------------------------------------------------
# Filter Routers
# -------------------------------------------------------------

print("\n=== Routers ===")

# Loop through all devices.
for device in devices:

    # Check whether the device type is router.
    if device["device_type"] == "router":

        print(
            f"{device['hostname']} | "
            f"{device['management_ip']} | "
            f"{device['vendor']}"
        )


# -------------------------------------------------------------
# Filter Switches
# -------------------------------------------------------------

print("\n=== Switches ===")

# Loop through all devices.
for device in devices:

    # Check whether the device type is switch.
    if device["device_type"] == "switch":

        print(
            f"{device['hostname']} | "
            f"{device['management_ip']} | "
            f"{device['vendor']}"
        )


# -------------------------------------------------------------
# Inventory Statistics
# -------------------------------------------------------------

# Calculate the total number of devices.
total_devices = len(devices)


# Count Cisco devices.
cisco_devices = sum(
    1
    for device in devices
    if device["vendor"] == "Cisco"
)


# Count routers.
router_count = sum(
    1
    for device in devices
    if device["device_type"] == "router"
)


# Count switches.
switch_count = sum(
    1
    for device in devices
    if device["device_type"] == "switch"
)


# Count firewalls.
firewall_count = sum(
    1
    for device in devices
    if device["device_type"] == "firewall"
)


# -------------------------------------------------------------
# Display Statistics
# -------------------------------------------------------------

print("\n=== Inventory Statistics ===")

print(f"Total Devices: {total_devices}")
print(f"Cisco Devices: {cisco_devices}")
print(f"Routers: {router_count}")
print(f"Switches: {switch_count}")
print(f"Firewalls: {firewall_count}")
