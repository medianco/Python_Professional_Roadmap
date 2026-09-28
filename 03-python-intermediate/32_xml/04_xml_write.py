"""
Lesson 32.4 - Writing XML Files

This lesson demonstrates how to create an XML document
from data stored in a separate JSON file.

Data Flow:

    JSON
      ↓
    Python
      ↓
    ElementTree
      ↓
    XML
      ↓
    Output File

Network Engineering Context:
In real Network Automation environments, data may come
from APIs, JSON files, databases, or inventories.

Python can transform this data into XML when required
by another system or network platform.
"""

import json
import xml.etree.ElementTree as ET


# ---------------------------------------------------------
# 1. File Paths
# ---------------------------------------------------------

# Input data is stored separately from Python logic.

JSON_FILE = "data/devices.json"

# The generated XML file will be stored in output/.

XML_FILE = "output/generated_devices.xml"


# ---------------------------------------------------------
# 2. Read JSON Data
# ---------------------------------------------------------

# Open the JSON file and load its contents into Python.

with open(
    JSON_FILE,
    "r",
    encoding="utf-8",
) as file:

    inventory = json.load(file)


# ---------------------------------------------------------
# 3. Extract Devices
# ---------------------------------------------------------

# The JSON structure contains a "devices" list.

devices = inventory["devices"]

print("=== JSON Data Loaded ===")
print(f"Source: {JSON_FILE}")
print(f"Total Devices: {len(devices)}")


# ---------------------------------------------------------
# 4. Create XML Root
# ---------------------------------------------------------

# Create the root element:

# <network_inventory>

root = ET.Element(
    "network_inventory"
)


# ---------------------------------------------------------
# 5. Convert Devices to XML
# ---------------------------------------------------------

for device_data in devices:

    # Create:
    #
    # <device>
    #
    device = ET.SubElement(
        root,
        "device",
    )

    # -----------------------------------------------------
    # Add Device Attributes
    # -----------------------------------------------------

    # Store hostname as the device ID.

    device.set(
        "id",
        device_data["hostname"],
    )

    # Store device status as an attribute.

    device.set(
        "status",
        device_data["status"],
    )

    # -----------------------------------------------------
    # Hostname
    # -----------------------------------------------------

    hostname = ET.SubElement(
        device,
        "hostname",
    )

    hostname.text = device_data["hostname"]

    # -----------------------------------------------------
    # Management IP
    # -----------------------------------------------------

    management_ip = ET.SubElement(
        device,
        "management_ip",
    )

    management_ip.text = device_data["management_ip"]

    # -----------------------------------------------------
    # Device Type
    # -----------------------------------------------------

    device_type = ET.SubElement(
        device,
        "device_type",
    )

    device_type.text = device_data["device_type"]

    # -----------------------------------------------------
    # Vendor
    # -----------------------------------------------------

    vendor = ET.SubElement(
        device,
        "vendor",
    )

    vendor.text = device_data["vendor"]

    # -----------------------------------------------------
    # Location
    # -----------------------------------------------------

    location = ET.SubElement(
        device,
        "location",
    )

    location.text = device_data["location"]


# ---------------------------------------------------------
# 6. Create ElementTree
# ---------------------------------------------------------

tree = ET.ElementTree(root)


# ---------------------------------------------------------
# 7. Format XML
# ---------------------------------------------------------

# Add indentation so that the generated XML
# is easy for humans to read.

ET.indent(
    tree,
    space="    ",
)


# ---------------------------------------------------------
# 8. Write XML File
# ---------------------------------------------------------

tree.write(
    XML_FILE,
    encoding="utf-8",
    xml_declaration=True,
)


# ---------------------------------------------------------
# 9. Display Result
# ---------------------------------------------------------

print("\n=== XML Generation Successful ===")

print(f"Output: {XML_FILE}")
print(f"Total Devices: {len(devices)}")


# ---------------------------------------------------------
# 10. Display Generated XML
# ---------------------------------------------------------

print("\n=== Generated XML ===")

xml_string = ET.tostring(
    root,
    encoding="unicode",
)

print(xml_string)
