"""
07_yaml_network_devices.py

Lesson 33.7 — YAML & Network Devices

This file demonstrates how YAML can be used
as a Network Device Inventory.

Data is stored separately in:

    data/network_devices.yaml

Python is responsible for:

    1. Reading the YAML file
    2. Parsing the inventory
    3. Displaying device information
    4. Filtering devices
    5. Generating basic inventory statistics

Architecture:

    YAML Inventory
          ↓
      safe_load()
          ↓
      Python Objects
          ↓
    Network Processing
          ↓
    Automation Targets
 #########################################################   
                network_devices.yaml
                         │
                         ▼
                      PyYAML
                         │
                         ▼
                  Python Objects
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
           Filter     Search     Statistics
              │
              ▼
      Automation Targets
              │
       ┌──────┼───────┐
       ▼      ▼       ▼
    Netmiko  Nornir   APIs
"""

from pathlib import Path

import yaml


# ---------------------------------------------------------
# Step 1 — Define the YAML file
# ---------------------------------------------------------

# Get the directory containing this Python file.
BASE_DIR = Path(__file__).resolve().parent

# Build the path to the YAML inventory.
DATA_FILE = BASE_DIR / "data" / "network_devices.yaml"


# ---------------------------------------------------------
# Step 2 — Check the YAML file
# ---------------------------------------------------------

print("=== YAML Network Device Inventory ===")

if not DATA_FILE.exists():

    print(f"ERROR: File not found: {DATA_FILE}")

    raise SystemExit(1)


print(f"Inventory file: {DATA_FILE}")


# ---------------------------------------------------------
# Step 3 — Read the YAML file
# ---------------------------------------------------------

with DATA_FILE.open("r", encoding="utf-8") as file:

    # Convert YAML into Python objects.
    inventory = yaml.safe_load(file)


# ---------------------------------------------------------
# Step 4 — Read inventory metadata
# ---------------------------------------------------------

print("\n=== Inventory Information ===")

inventory_info = inventory["inventory"]

print(f"Name: {inventory_info['name']}")
print(f"Environment: {inventory_info['environment']}")


# ---------------------------------------------------------
# Step 5 — Get the devices
# ---------------------------------------------------------

devices = inventory["devices"]

print(f"Total devices: {len(devices)}")


# ---------------------------------------------------------
# Step 6 — Display all devices
# ---------------------------------------------------------

print("\n=== Network Devices ===")

for device in devices:

    management = device["management"]
    platform = device["platform"]
    location = device["location"]

    print(
        f"{device['hostname']} | "
        f"{management['ip']} | "
        f"{platform['device_type']} | "
        f"{platform['vendor']} | "
        f"{location['site']} | "
        f"{device['status']}"
    )


# ---------------------------------------------------------
# Step 7 — Find Cisco devices
# ---------------------------------------------------------

print("\n=== Cisco Devices ===")

for device in devices:

    # Read the vendor from the nested platform dictionary.
    vendor = device["platform"]["vendor"]

    if vendor == "Cisco":

        print(
            f"{device['hostname']} | "
            f"{device['platform']['device_type']} | "
            f"{device['management']['ip']}"
        )


# ---------------------------------------------------------
# Step 8 — Find routers
# ---------------------------------------------------------

print("\n=== Routers ===")

for device in devices:

    device_type = device["platform"]["device_type"]

    if device_type == "router":

        print(
            f"{device['hostname']} | "
            f"{device['management']['ip']} | "
            f"{device['platform']['vendor']}"
        )


# ---------------------------------------------------------
# Step 9 — Find Data Center devices
# ---------------------------------------------------------

print("\n=== Data Center Devices ===")

for device in devices:

    site = device["location"]["site"]

    if site == "Data Center":

        print(
            f"{device['hostname']} | "
            f"{device['platform']['device_type']} | "
            f"{device['platform']['vendor']}"
        )


# ---------------------------------------------------------
# Step 10 — Find active devices
# ---------------------------------------------------------

print("\n=== Active Devices ===")

for device in devices:

    if device["status"] == "active":

        print(
            f"{device['hostname']} | "
            f"{device['management']['ip']}"
        )


# ---------------------------------------------------------
# Step 11 — Generate statistics
# ---------------------------------------------------------

print("\n=== Inventory Statistics ===")

cisco_count = 0
router_count = 0
switch_count = 0
firewall_count = 0
active_count = 0

for device in devices:

    vendor = device["platform"]["vendor"]
    device_type = device["platform"]["device_type"]
    status = device["status"]

    # Count Cisco devices.
    if vendor == "Cisco":
        cisco_count += 1

    # Count routers.
    if device_type == "router":
        router_count += 1

    # Count switches.
    if device_type == "switch":
        switch_count += 1

    # Count firewalls.
    if device_type == "firewall":
        firewall_count += 1

    # Count active devices.
    if status == "active":
        active_count += 1


print(f"Cisco devices: {cisco_count}")
print(f"Routers: {router_count}")
print(f"Switches: {switch_count}")
print(f"Firewalls: {firewall_count}")
print(f"Active devices: {active_count}")


# ---------------------------------------------------------
# Step 12 — Identify automation targets
# ---------------------------------------------------------

print("\n=== Automation Targets ===")

# For this example, we select active Cisco routers.
#
# In a real automation system, these devices could
# later be passed to Netmiko, Nornir, or an API client.

automation_targets = []

for device in devices:

    vendor = device["platform"]["vendor"]
    device_type = device["platform"]["device_type"]
    status = device["status"]

    if (
        vendor == "Cisco"
        and device_type == "router"
        and status == "active"
    ):

        automation_targets.append(device)


# Display the selected automation targets.
for device in automation_targets:

    print(
        f"{device['hostname']} | "
        f"{device['management']['ip']} | "
        f"{device['management']['protocol']}"
    )


print(
    f"Total automation targets: "
    f"{len(automation_targets)}"
)
