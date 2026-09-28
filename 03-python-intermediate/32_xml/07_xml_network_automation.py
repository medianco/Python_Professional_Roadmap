"""
07_xml_network_automation.py

Lesson 32.7 — XML & Network Automation

This module demonstrates how XML can be used as an
input source for a Network Automation workflow.

Workflow:

XML Inventory
      ↓
ElementTree
      ↓
Parse Devices
      ↓
Validate Status
      ↓
Filter Devices
      ↓
Automation Targets
      ↓
Simulated Automation

The example does NOT connect to real network devices.
It only prepares and processes automation targets.
"""

import xml.etree.ElementTree as ET
from pathlib import Path


# ============================================================
# 1. Define XML file path
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

XML_FILE = BASE_DIR / "data" / "devices.xml"


# ============================================================
# 2. Read XML Inventory
# ============================================================

tree = ET.parse(XML_FILE)

root = tree.getroot()


print("=" * 60)
print("XML NETWORK AUTOMATION")
print("=" * 60)


# ============================================================
# 3. Extract Devices
# ============================================================

devices = root.findall("device")

print(f"\nInventory Devices: {len(devices)}")


# ============================================================
# 4. Build Automation Targets
# ============================================================

automation_targets = []


for device in devices:

    # --------------------------------------------------------
    # Read device attributes
    # --------------------------------------------------------

    device_id = device.get("id")
    status = device.get("status")

    # --------------------------------------------------------
    # Read device information
    # --------------------------------------------------------

    hostname = device.find("hostname").text
    management_ip = device.find("management_ip").text
    device_type = device.find("device_type").text
    vendor = device.find("vendor").text
    location = device.find("location").text

    # --------------------------------------------------------
    # Only process active devices
    # --------------------------------------------------------

    if status != "active":
        continue

    # --------------------------------------------------------
    # Select Cisco routers
    # --------------------------------------------------------

    if vendor == "Cisco" and device_type == "router":

        automation_targets.append(
            {
                "id": device_id,
                "hostname": hostname,
                "management_ip": management_ip,
                "vendor": vendor,
                "device_type": device_type,
                "location": location,
            }
        )


# ============================================================
# 5. Display Automation Targets
# ============================================================

print("\n--- Automation Targets ---")

for target in automation_targets:

    print(
        f"{target['hostname']} | "
        f"{target['management_ip']} | "
        f"{target['vendor']} | "
        f"{target['device_type']}"
    )


# ============================================================
# 6. Simulate Network Automation
# ============================================================

print("\n--- Automation Simulation ---")


for target in automation_targets:

    hostname = target["hostname"]
    management_ip = target["management_ip"]

    print(f"\nConnecting to {hostname} ({management_ip})...")

    # --------------------------------------------------------
    # In a real project, this is where a tool such as
    # Netmiko, Nornir, or an API client could be used.
    #
    # Example:
    #
    # connection = ConnectHandler(...)
    # output = connection.send_command(...)
    #
    # We are intentionally simulating this step.
    # --------------------------------------------------------

    print(f"Running automation task on {hostname}...")
    print(f"Automation completed successfully on {hostname}")


# ============================================================
# 7. Display Summary
# ============================================================

print("\n--- Automation Summary ---")

print(f"Total Inventory Devices : {len(devices)}")
print(f"Automation Targets      : {len(automation_targets)}")

print("\nAutomation workflow completed.")

print("=" * 60)
