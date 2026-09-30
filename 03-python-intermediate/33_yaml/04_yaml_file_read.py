"""
04_yaml_file_read.py

Lesson 33.4 — YAML File Read

This file demonstrates how to read a YAML file
and convert its contents into Python objects.

Workflow:

    devices.yaml
         ↓
       open()
         ↓
    yaml.safe_load()
         ↓
    Python Dictionary
         ↓
    Process Network Devices

This approach separates:
- Data
- Python logic

This is an important design principle in
Network Automation.
"""

from pathlib import Path

import yaml


# ---------------------------------------------------------
# Step 1 — Define the YAML file path
# ---------------------------------------------------------

# Path(__file__) represents the directory
# containing this Python script.
#
# We use it to build a reliable path to:
#
# data/devices.yaml
#
# This is better than depending on the directory
# from which the user happens to run the script.
BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "data" / "devices.yaml"


# ---------------------------------------------------------
# Step 2 — Check that the file exists
# ---------------------------------------------------------

print("=== YAML File Read ===")

if not DATA_FILE.exists():

    print(f"ERROR: File not found: {DATA_FILE}")

    raise SystemExit(1)


print(f"Reading file: {DATA_FILE}")


# ---------------------------------------------------------
# Step 3 — Open the YAML file
# ---------------------------------------------------------

# The "with" statement automatically closes
# the file after we finish reading it.
#
# encoding="utf-8" ensures proper text handling.
with DATA_FILE.open("r", encoding="utf-8") as file:

    # -----------------------------------------------------
    # Step 4 — Convert YAML into Python
    # -----------------------------------------------------

    # safe_load() reads the YAML content and converts it
    # into standard Python objects.
    inventory = yaml.safe_load(file)


# ---------------------------------------------------------
# Step 5 — Validate the basic structure
# ---------------------------------------------------------

print("\n=== Inventory Information ===")

# Our YAML should contain a top-level "devices" key.
if not isinstance(inventory, dict):

    print("ERROR: YAML root must be a dictionary.")

    raise SystemExit(1)


if "devices" not in inventory:

    print("ERROR: 'devices' key was not found.")

    raise SystemExit(1)


# Retrieve the devices list.
devices = inventory["devices"]


# Make sure "devices" is actually a list.
if not isinstance(devices, list):

    print("ERROR: 'devices' must be a list.")

    raise SystemExit(1)


print(f"Total devices: {len(devices)}")


# ---------------------------------------------------------
# Step 6 — Display network devices
# ---------------------------------------------------------

print("\n=== Network Devices ===")

for device in devices:

    print(
        f"{device['hostname']} | "
        f"{device['management_ip']} | "
        f"{device['device_type']} | "
        f"{device['vendor']} | "
        f"{device['location']} | "
        f"{device['status']}"
    )


# ---------------------------------------------------------
# Step 7 — Display Python data type
# ---------------------------------------------------------

print("\n=== Python Data Type ===")

print(f"Inventory type: {type(inventory).__name__}")
print(f"Devices type: {type(devices).__name__}")
print(f"First device type: {type(devices[0]).__name__}")


# ---------------------------------------------------------
# Step 8 — Access individual device information
# ---------------------------------------------------------

print("\n=== First Device ===")

first_device = devices[0]

print(f"Hostname: {first_device['hostname']}")
print(f"Management IP: {first_device['management_ip']}")
print(f"Vendor: {first_device['vendor']}")
print(f"Device Type: {first_device['device_type']}")
print(f"Location: {first_device['location']}")
print(f"Status: {first_device['status']}")
