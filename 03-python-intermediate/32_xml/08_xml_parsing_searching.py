"""
08_xml_parsing_searching.py

Lesson 32.8 — XML Parsing & Searching

This module demonstrates how to search and filter
network devices inside an XML inventory.

Topics:
- find()
- findall()
- iter()
- Searching by XML attributes
- Searching by element values
- Filtering network devices
"""

import xml.etree.ElementTree as ET
from pathlib import Path


# ============================================================
# 1. XML File Path
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

XML_FILE = BASE_DIR / "data" / "devices.xml"


# ============================================================
# 2. Parse XML
# ============================================================

tree = ET.parse(XML_FILE)

root = tree.getroot()


print("=" * 60)
print("XML PARSING & SEARCHING")
print("=" * 60)


# ============================================================
# 3. find() — Find the first matching element
# ============================================================

print("\n--- find() Example ---")

first_device = root.find("device")

if first_device is not None:

    hostname = first_device.find("hostname").text
    management_ip = first_device.find("management_ip").text

    print(f"First Device : {hostname}")
    print(f"Management IP: {management_ip}")


# ============================================================
# 4. findall() — Find all devices
# ============================================================

print("\n--- findall() Example ---")

devices = root.findall("device")

print(f"Total Devices Found: {len(devices)}")


# ============================================================
# 5. Search by Device ID
# ============================================================

print("\n--- Search by Device ID ---")

search_id = "R1"

for device in devices:

    device_id = device.get("id")

    if device_id == search_id:

        hostname = device.find("hostname").text
        management_ip = device.find("management_ip").text
        vendor = device.find("vendor").text

        print(f"Device ID     : {device_id}")
        print(f"Hostname      : {hostname}")
        print(f"Management IP : {management_ip}")
        print(f"Vendor        : {vendor}")


# ============================================================
# 6. Search by Vendor
# ============================================================

print("\n--- Cisco Devices ---")

for device in devices:

    vendor = device.find("vendor").text

    if vendor == "Cisco":

        hostname = device.find("hostname").text
        management_ip = device.find("management_ip").text

        print(
            f"{hostname} -> {management_ip}"
        )


# ============================================================
# 7. Search by Device Type
# ============================================================

print("\n--- Router Devices ---")

for device in devices:

    device_type = device.find("device_type").text

    if device_type == "router":

        hostname = device.find("hostname").text
        management_ip = device.find("management_ip").text

        print(
            f"{hostname} -> {management_ip}"
        )


# ============================================================
# 8. Search by Location
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
# 9. Search by Status Attribute
# ============================================================

print("\n--- Active Devices ---")

for device in devices:

    status = device.get("status")

    if status == "active":

        hostname = device.find("hostname").text

        print(
            f"{hostname} -> {status}"
        )


# ============================================================
# 10. Search by Management IP
# ============================================================

print("\n--- Search by Management IP ---")

search_ip = "192.168.1.10"

for device in devices:

    management_ip = device.find("management_ip").text

    if management_ip == search_ip:

        hostname = device.find("hostname").text
        vendor = device.find("vendor").text
        device_type = device.find("device_type").text

        print(f"Hostname      : {hostname}")
        print(f"Management IP : {management_ip}")
        print(f"Vendor        : {vendor}")
        print(f"Device Type   : {device_type}")


# ============================================================
# 11. iter() — Iterate through matching elements
# ============================================================

print("\n--- iter() Example ---")

print("All Hostnames:")

for hostname_element in root.iter("hostname"):

    print(
        f"- {hostname_element.text}"
    )


# ============================================================
# 12. Combined Filtering
# ============================================================

print("\n--- Cisco Routers in Data Center ---")

for device in devices:

    vendor = device.find("vendor").text
    device_type = device.find("device_type").text
    location = device.find("location").text

    if (
        vendor == "Cisco"
        and device_type == "router"
        and location == "Data Center"
    ):

        hostname = device.find("hostname").text
        management_ip = device.find("management_ip").text

        print(
            f"{hostname} -> {management_ip}"
        )


# ============================================================
# 13. Summary
# ============================================================

print("\n--- Search Summary ---")

print(f"Total Devices : {len(devices)}")

cisco_devices = [
    device
    for device in devices
    if device.find("vendor").text == "Cisco"
]

routers = [
    device
    for device in devices
    if device.find("device_type").text == "router"
]

active_devices = [
    device
    for device in devices
    if device.get("status") == "active"
]

print(f"Cisco Devices : {len(cisco_devices)}")
print(f"Routers       : {len(routers)}")
print(f"Active Devices: {len(active_devices)}")


print("\n" + "=" * 60)
print("XML SEARCHING COMPLETED")
print("=" * 60)
