"""
Lesson 32.3 - Reading XML Files

This lesson demonstrates how to read an XML file
using Python's xml.etree.ElementTree module.

Network Engineering Context:
XML files can be used to store network device
inventories and other structured network data.

In this lesson we will:

1. Read an XML file.
2. Get the root element.
3. Access XML elements.
4. Read element text.
5. Read XML attributes.
6. Iterate through network devices.
7. Display device information.
"""

import xml.etree.ElementTree as ET


# ---------------------------------------------------------
# 1. XML File Path
# ---------------------------------------------------------

# The XML data is stored separately from the Python logic.

XML_FILE = "data/devices.xml"


# ---------------------------------------------------------
# 2. Parse the XML File
# ---------------------------------------------------------

# ET.parse() reads the XML file and creates
# an ElementTree object.

tree = ET.parse(XML_FILE)


# ---------------------------------------------------------
# 3. Get the Root Element
# ---------------------------------------------------------

# getroot() returns the top-level element.

root = tree.getroot()

print("=== XML Root ===")
print(root.tag)


# ---------------------------------------------------------
# 4. Display Root Attributes
# ---------------------------------------------------------

print("\n=== Root Attributes ===")

for key, value in root.attrib.items():
    print(f"{key}: {value}")


# ---------------------------------------------------------
# 5. Find All Devices
# ---------------------------------------------------------

# The root contains multiple <device> elements.

devices = root.findall("device")

print("\n=== Device Count ===")
print(f"Total Devices: {len(devices)}")


# ---------------------------------------------------------
# 6. Read Device Attributes
# ---------------------------------------------------------

print("\n=== Device Attributes ===")

for device in devices:

    device_id = device.get("id")
    status = device.get("status")

    print(
        f"ID: {device_id} | "
        f"Status: {status}"
    )


# ---------------------------------------------------------
# 7. Read Device Elements
# ---------------------------------------------------------

print("\n=== Network Devices ===")

for device in devices:

    hostname = device.find("hostname")
    management_ip = device.find("management_ip")
    device_type = device.find("device_type")
    vendor = device.find("vendor")
    location = device.find("location")

    print(
        f"Hostname: {hostname.text} | "
        f"IP: {management_ip.text} | "
        f"Type: {device_type.text} | "
        f"Vendor: {vendor.text} | "
        f"Location: {location.text}"
    )


# ---------------------------------------------------------
# 8. Display Individual Device Information
# ---------------------------------------------------------

print("\n=== First Device ===")

first_device = devices[0]

print(
    f"Hostname: "
    f"{first_device.find('hostname').text}"
)

print(
    f"Management IP: "
    f"{first_device.find('management_ip').text}"
)

print(
    f"Device Type: "
    f"{first_device.find('device_type').text}"
)

print(
    f"Vendor: "
    f"{first_device.find('vendor').text}"
)


# ---------------------------------------------------------
# 9. Search for Cisco Devices
# ---------------------------------------------------------

print("\n=== Cisco Devices ===")

for device in devices:

    vendor = device.find("vendor")

    if vendor.text == "Cisco":

        hostname = device.find("hostname")
        management_ip = device.find("management_ip")

        print(
            f"Hostname: {hostname.text} | "
            f"IP: {management_ip.text}"
        )


# ---------------------------------------------------------
# 10. Search for Routers
# ---------------------------------------------------------

print("\n=== Routers ===")

for device in devices:

    device_type = device.find("device_type")

    if device_type.text == "router":

        hostname = device.find("hostname")
        management_ip = device.find("management_ip")

        print(
            f"Hostname: {hostname.text} | "
            f"IP: {management_ip.text}"
        )


# ---------------------------------------------------------
# 11. Search for Data Center Devices
# ---------------------------------------------------------

print("\n=== Data Center Devices ===")

for device in devices:

    location = device.find("location")

    if location.text == "Data Center":

        hostname = device.find("hostname")
        device_type = device.find("device_type")

        print(
            f"Hostname: {hostname.text} | "
            f"Type: {device_type.text}"
        )


# ---------------------------------------------------------
# 12. Inventory Statistics
# ---------------------------------------------------------

router_count = 0
switch_count = 0
firewall_count = 0
cisco_count = 0

for device in devices:

    device_type = device.find("device_type").text
    vendor = device.find("vendor").text

    if device_type == "router":
        router_count += 1

    elif device_type == "switch":
        switch_count += 1

    elif device_type == "firewall":
        firewall_count += 1

    if vendor == "Cisco":
        cisco_count += 1


print("\n=== Inventory Statistics ===")

print(f"Total Devices: {len(devices)}")
print(f"Cisco Devices: {cisco_count}")
print(f"Routers: {router_count}")
print(f"Switches: {switch_count}")
print(f"Firewalls: {firewall_count}")
