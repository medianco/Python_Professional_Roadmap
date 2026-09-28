"""
06_xml_network_devices.py

Lesson 32.6 — XML & Network Devices

This module demonstrates how XML can be used as a
Network Device Inventory.

We will:
1. Read network devices from an XML file.
2. Extract device information.
3. Filter devices by vendor.
4. Filter devices by device type.
5. Filter devices by location.
6. Display network device statistics.

This is a simplified example of how XML can be
used as an inventory source in Network Automation.
"""

import xml.etree.ElementTree as ET
from pathlib import Path


# ============================================================
# 1. Define the XML file path
# ============================================================

# __file__ points to this Python file.
# parent.parent gives us the 32_xml directory.
BASE_DIR = Path(__file__).resolve().parent

XML_FILE = BASE_DIR / "data" / "devices.xml"


# ============================================================
# 2. Read the XML file
# ============================================================

tree = ET.parse(XML_FILE)

# Get the root element:
# <network_inventory>
root = tree.getroot()


print("=" * 60)
print("NETWORK DEVICE INVENTORY")
print("=" * 60)


# ============================================================
# 3. Extract all devices
# ============================================================

devices = root.findall("device")

print(f"\nTotal Devices: {len(devices)}")


# ============================================================
# 4. Display all devices
# ============================================================

print("\n--- All Network Devices ---")

for device in devices:

    # Read XML attribute
    device_id = device.get("id")

    # Read XML child elements
    hostname = device.find("hostname").text
    management_ip = device.find("management_ip").text
    device_type = device.find("device_type").text
    vendor = device.find("vendor").text
    location = device.find("location").text

    print(
        f"{device_id:<5} | "
        f"{hostname:<5} | "
        f"{management_ip:<15} | "
        f"{device_type:<8} | "
        f"{vendor:<8} | "
        f"{location}"
    )


# ============================================================
# 5. Find Cisco devices
# ============================================================

print("\n--- Cisco Devices ---")

for device in devices:

    vendor = device.find("vendor").text

    if vendor == "Cisco":

        hostname = device.find("hostname").text
        management_ip = device.find("management_ip").text
        device_type = device.find("device_type").text

        print(
            f"{hostname} | "
            f"{management_ip} | "
            f"{device_type}"
        )


# ============================================================
# 6. Find routers
# ============================================================

print("\n--- Routers ---")

for device in devices:

    device_type = device.find("device_type").text

    if device_type == "router":

        hostname = device.find("hostname").text
        management_ip = device.find("management_ip").text

        print(
            f"{hostname} | "
            f"{management_ip}"
        )


# ============================================================
# 7. Find devices in Data Center
# ============================================================

print("\n--- Data Center Devices ---")

for device in devices:

    location = device.find("location").text

    if location == "Data Center":

        hostname = device.find("hostname").text
        vendor = device.find("vendor").text
        device_type = device.find("device_type").text

        print(
            f"{hostname} | "
            f"{vendor} | "
            f"{device_type}"
        )


# ============================================================
# 8. Extract Management IPs
# ============================================================

print("\n--- Management IP Addresses ---")

for device in devices:

    hostname = device.find("hostname").text
    management_ip = device.find("management_ip").text

    print(f"{hostname:<5} -> {management_ip}")


# ============================================================
# 9. Network Device Statistics
# ============================================================

cisco_count = 0
router_count = 0
switch_count = 0
firewall_count = 0
data_center_count = 0


for device in devices:

    vendor = device.find("vendor").text
    device_type = device.find("device_type").text
    location = device.find("location").text

    # Count Cisco devices
    if vendor == "Cisco":
        cisco_count += 1

    # Count device types
    if device_type == "router":
        router_count += 1

    elif device_type == "switch":
        switch_count += 1

    elif device_type == "firewall":
        firewall_count += 1

    # Count Data Center devices
    if location == "Data Center":
        data_center_count += 1


# ============================================================
# 10. Display statistics
# ============================================================

print("\n--- Inventory Statistics ---")

print(f"Total Devices       : {len(devices)}")
print(f"Cisco Devices       : {cisco_count}")
print(f"Routers             : {router_count}")
print(f"Switches            : {switch_count}")
print(f"Firewalls           : {firewall_count}")
print(f"Data Center Devices : {data_center_count}")


print("\n" + "=" * 60)
print("Inventory Processing Completed")
print("=" * 60)
