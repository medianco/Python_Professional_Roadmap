"""
09_xml_validation.py

Lesson 32.9 — XML Validation

This module demonstrates how to validate a network
device XML inventory before using it for automation.

Validation includes:

1. XML file existence
2. XML parsing
3. Required device attributes
4. Required XML elements
5. Valid management IP addresses
6. Valid device status
7. Valid device types

The goal is to prevent invalid inventory data
from entering a Network Automation workflow.
"""

import xml.etree.ElementTree as ET
import ipaddress
from pathlib import Path


# ============================================================
# 1. Define XML File
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

XML_FILE = BASE_DIR / "data" / "devices.xml"


print("=" * 60)
print("XML NETWORK INVENTORY VALIDATION")
print("=" * 60)


# ============================================================
# 2. Validate File Existence
# ============================================================

print("\n--- File Validation ---")


if not XML_FILE.exists():

    print(f"ERROR: XML file not found: {XML_FILE}")
    raise SystemExit(1)


print("XML file exists.")


# ============================================================
# 3. Parse XML
# ============================================================

print("\n--- XML Parsing Validation ---")


try:

    tree = ET.parse(XML_FILE)
    root = tree.getroot()

    print("XML syntax is valid.")
    print(f"Root Element: <{root.tag}>")

except ET.ParseError as error:

    print("ERROR: Invalid XML syntax.")
    print(f"Details: {error}")

    raise SystemExit(1)


# ============================================================
# 4. Validate Root Element
# ============================================================

print("\n--- Root Validation ---")


if root.tag != "network_inventory":

    print(
        "ERROR: Unexpected root element."
    )

    raise SystemExit(1)


print("Root element is valid.")


# ============================================================
# 5. Get Devices
# ============================================================

devices = root.findall("device")

print(f"\nDevices Found: {len(devices)}")


# ============================================================
# 6. Define Validation Rules
# ============================================================

required_attributes = [
    "id",
    "status",
]

required_elements = [
    "hostname",
    "management_ip",
    "device_type",
    "vendor",
    "location",
]

allowed_statuses = {
    "active",
    "inactive",
}

allowed_device_types = {
    "router",
    "switch",
    "firewall",
}


# ============================================================
# 7. Validate Each Device
# ============================================================

print("\n--- Device Validation ---")


validation_errors = []


for device in devices:

    device_id = device.get("id")

    # --------------------------------------------------------
    # Validate required attributes
    # --------------------------------------------------------

    for attribute in required_attributes:

        value = device.get(attribute)

        if not value:

            validation_errors.append(
                f"{device_id}: Missing attribute '{attribute}'"
            )

    # --------------------------------------------------------
    # Validate required XML elements
    # --------------------------------------------------------

    for element_name in required_elements:

        element = device.find(element_name)

        if element is None or not element.text:

            validation_errors.append(
                f"{device_id}: Missing element "
                f"'{element_name}'"
            )

    # --------------------------------------------------------
    # Stop deeper validation if required data is missing
    # --------------------------------------------------------

    if not device_id:
        continue

    # --------------------------------------------------------
    # Validate status
    # --------------------------------------------------------

    status = device.get("status")

    if status and status not in allowed_statuses:

        validation_errors.append(
            f"{device_id}: Invalid status '{status}'"
        )

    # --------------------------------------------------------
    # Extract management IP
    # --------------------------------------------------------

    management_ip_element = device.find("management_ip")

    if (
        management_ip_element is not None
        and management_ip_element.text
    ):

        management_ip = management_ip_element.text.strip()

        # ----------------------------------------------------
        # Validate IP address semantically
        # ----------------------------------------------------

        try:

            ipaddress.ip_address(management_ip)

        except ValueError:

            validation_errors.append(
                f"{device_id}: Invalid management IP "
                f"'{management_ip}'"
            )

    # --------------------------------------------------------
    # Validate device type
    # --------------------------------------------------------

    device_type_element = device.find("device_type")

    if (
        device_type_element is not None
        and device_type_element.text
    ):

        device_type = device_type_element.text.strip()

        if device_type not in allowed_device_types:

            validation_errors.append(
                f"{device_id}: Invalid device type "
                f"'{device_type}'"
            )


# ============================================================
# 8. Display Validation Results
# ============================================================

print("\n--- Validation Results ---")


if validation_errors:

    print(
        f"Validation failed with "
        f"{len(validation_errors)} error(s):"
    )

    for error in validation_errors:

        print(f"- {error}")

else:

    print("All devices passed validation.")


# ============================================================
# 9. Display Validated Devices
# ============================================================

if not validation_errors:

    print("\n--- Validated Devices ---")

    for device in devices:

        hostname = device.find("hostname").text
        management_ip = device.find("management_ip").text
        device_type = device.find("device_type").text
        vendor = device.find("vendor").text
        status = device.get("status")

        print(
            f"{hostname:<5} | "
            f"{management_ip:<15} | "
            f"{device_type:<8} | "
            f"{vendor:<8} | "
            f"{status}"
        )


# ============================================================
# 10. Automation Readiness
# ============================================================

print("\n--- Automation Readiness ---")


if validation_errors:

    print(
        "Inventory is NOT ready for automation."
    )

else:

    print(
        "Inventory is READY for automation."
    )

    print(
        "Validated devices can now be passed "
        "to an automation system."
    )


print("\n" + "=" * 60)
print("XML VALIDATION COMPLETED")
print("=" * 60)
