"""
06_yaml_nested_data.py

Lesson 33.6 — YAML Nested Data

This file demonstrates how to read and process
nested YAML data from an external file.

Data is intentionally separated from Python logic.

Data:
    data/nested_devices.yaml

Logic:
    06_yaml_nested_data.py

Main structure:

    YAML File
        ↓
    yaml.safe_load()
        ↓
    Python Dictionary
        ↓
    Nested Dictionary/List
        ↓
    Network Device Processing
"""

from pathlib import Path

import yaml


# ---------------------------------------------------------
# Step 1 — Build the YAML file path
# ---------------------------------------------------------

# Get the directory where this Python file exists.
BASE_DIR = Path(__file__).resolve().parent

# Build the path to the nested YAML data file.
DATA_FILE = BASE_DIR / "data" / "nested_devices.yaml"


# ---------------------------------------------------------
# Step 2 — Check that the file exists
# ---------------------------------------------------------

print("=== YAML Nested Data ===")

if not DATA_FILE.exists():

    print(f"ERROR: File not found: {DATA_FILE}")

    raise SystemExit(1)


print(f"Reading file: {DATA_FILE}")


# ---------------------------------------------------------
# Step 3 — Read and parse the YAML file
# ---------------------------------------------------------

# Open the YAML file using UTF-8 encoding.
with DATA_FILE.open("r", encoding="utf-8") as file:

    # Convert YAML into Python objects.
    inventory = yaml.safe_load(file)


# ---------------------------------------------------------
# Step 4 — Validate the basic structure
# ---------------------------------------------------------

if not isinstance(inventory, dict):

    print("ERROR: YAML root must be a dictionary.")

    raise SystemExit(1)


if "devices" not in inventory:

    print("ERROR: 'devices' key was not found.")

    raise SystemExit(1)


# Retrieve the list of devices.
devices = inventory["devices"]


if not isinstance(devices, list):

    print("ERROR: 'devices' must be a list.")

    raise SystemExit(1)


print(f"Total devices: {len(devices)}")


# ---------------------------------------------------------
# Step 5 — Display device information
# ---------------------------------------------------------

print("\n=== Device Information ===")

for device in devices:

    # Basic device information.
    hostname = device["hostname"]

    # Access nested management information.
    management = device["management"]

    # Access nested platform information.
    platform = device["platform"]

    print(f"\nDevice: {hostname}")
    print(f"Management IP: {management['ip']}")
    print(f"Protocol: {management['protocol']}")
    print(f"Port: {management['port']}")
    print(f"Vendor: {platform['vendor']}")
    print(f"Device Type: {platform['device_type']}")
    print(f"OS: {platform['os']}")


# ---------------------------------------------------------
# Step 6 — Process interfaces
# ---------------------------------------------------------

print("\n=== Interface Information ===")

total_interfaces = 0
up_interfaces = 0
down_interfaces = 0

for device in devices:

    print(f"\nDevice: {device['hostname']}")

    # Interfaces are stored as a list
    # inside each device dictionary.
    interfaces = device["interfaces"]

    for interface in interfaces:

        total_interfaces += 1

        # Read the interface status.
        status = interface["status"]

        if status == "up":
            up_interfaces += 1

        elif status == "down":
            down_interfaces += 1

        print(
            f"  {interface['name']} | "
            f"{interface['ip_address']} | "
            f"{status}"
        )


# ---------------------------------------------------------
# Step 7 — Display interface statistics
# ---------------------------------------------------------

print("\n=== Interface Statistics ===")

print(f"Total interfaces: {total_interfaces}")
print(f"Interfaces up: {up_interfaces}")
print(f"Interfaces down: {down_interfaces}")


# ---------------------------------------------------------
# Step 8 — Find interfaces that are down
# ---------------------------------------------------------

print("\n=== Interfaces Down ===")

for device in devices:

    for interface in device["interfaces"]:

        if interface["status"] == "down":

            print(
                f"{device['hostname']} | "
                f"{interface['name']} | "
                f"{interface['status']}"
            )


# ---------------------------------------------------------
# Step 9 — Display Python data types
# ---------------------------------------------------------

print("\n=== Python Data Types ===")

print(f"Inventory type: {type(inventory).__name__}")
print(f"Devices type: {type(devices).__name__}")
print(f"Device type: {type(devices[0]).__name__}")
print(
    f"Interfaces type: "
    f"{type(devices[0]['interfaces']).__name__}"
)
print(
    f"Interface type: "
    f"{type(devices[0]['interfaces'][0]).__name__}"
)
