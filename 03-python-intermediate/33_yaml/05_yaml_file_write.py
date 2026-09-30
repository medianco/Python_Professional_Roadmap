"""
05_yaml_file_write.py

Lesson 33.5 — YAML File Write

This file demonstrates how to write Python data
into a YAML file using PyYAML.

Main workflow:

    Python Dictionary
          ↓
    yaml.safe_dump()
          ↓
    YAML File

We will:

1. Create network device data.
2. Create the output directory if necessary.
3. Open a YAML file for writing.
4. Convert Python data into YAML.
5. Write the YAML data to the file.
6. Read the generated file again to verify it.

This is an important step toward configuration-driven
Network Automation.
"""

from pathlib import Path

import yaml


# ---------------------------------------------------------
# Step 1 — Define directories
# ---------------------------------------------------------

# Path(__file__) gives us the directory containing
# this Python script.
BASE_DIR = Path(__file__).resolve().parent

# Define the output directory.
OUTPUT_DIR = BASE_DIR / "output"

# Define the YAML output file.
OUTPUT_FILE = OUTPUT_DIR / "generated_devices.yaml"


# ---------------------------------------------------------
# Step 2 — Create the output directory
# ---------------------------------------------------------

# mkdir() creates the directory if it does not exist.
#
# parents=True:
#     Create parent directories when necessary.
#
# exist_ok=True:
#     Do not raise an error if the directory already exists.
OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


# ---------------------------------------------------------
# Step 3 — Create network device data
# ---------------------------------------------------------

# This is normal Python data.
#
# Later, this data could come from:
# - An API
# - A database
# - CSV
# - JSON
# - Network discovery
# - Another automation process

inventory = {
    "devices": [
        {
            "hostname": "R1",
            "management_ip": "192.168.1.1",
            "device_type": "router",
            "vendor": "Cisco",
            "location": "Data Center",
            "status": "active",
        },
        {
            "hostname": "R2",
            "management_ip": "192.168.1.2",
            "device_type": "router",
            "vendor": "Cisco",
            "location": "Branch 1",
            "status": "active",
        },
        {
            "hostname": "SW1",
            "management_ip": "192.168.1.10",
            "device_type": "switch",
            "vendor": "Cisco",
            "location": "Data Center",
            "status": "active",
        },
        {
            "hostname": "FW1",
            "management_ip": "192.168.1.254",
            "device_type": "firewall",
            "vendor": "Fortinet",
            "location": "Data Center",
            "status": "active",
        },
    ]
}


# ---------------------------------------------------------
# Step 4 — Write Python data to YAML
# ---------------------------------------------------------

print("=== YAML File Write ===")

print(f"Writing file: {OUTPUT_FILE}")


# Open the output file in write mode.
#
# "w" means:
#     Create a new file or overwrite an existing file.
#
# encoding="utf-8":
#     Use UTF-8 text encoding.
with OUTPUT_FILE.open("w", encoding="utf-8") as file:

    # Convert the Python dictionary into YAML
    # and write it directly into the file.
    yaml.safe_dump(
        inventory,
        file,
        sort_keys=False,
        default_flow_style=False,
    )


print("YAML file created successfully.")


# ---------------------------------------------------------
# Step 5 — Verify the file
# ---------------------------------------------------------

print("\n=== File Verification ===")

# Check whether the generated file exists.
if OUTPUT_FILE.exists():

    print("File exists: True")

    # Display the file size in bytes.
    file_size = OUTPUT_FILE.stat().st_size

    print(f"File size: {file_size} bytes")

else:

    print("File exists: False")

    raise SystemExit(1)


# ---------------------------------------------------------
# Step 6 — Read the generated YAML file
# ---------------------------------------------------------

print("\n=== Read Generated YAML ===")

# Open the file that we just created.
with OUTPUT_FILE.open("r", encoding="utf-8") as file:

    # Convert YAML back into Python.
    generated_inventory = yaml.safe_load(file)


# ---------------------------------------------------------
# Step 7 — Verify the generated data
# ---------------------------------------------------------

print("\n=== Generated Inventory ===")

# Access the devices list.
devices = generated_inventory["devices"]

# Display the total number of devices.
print(f"Total devices: {len(devices)}")


# Display each device.
for device in devices:

    print(
        f"{device['hostname']} | "
        f"{device['management_ip']} | "
        f"{device['device_type']} | "
        f"{device['vendor']}"
    )


# ---------------------------------------------------------
# Step 8 — Compare original and generated data
# ---------------------------------------------------------

print("\n=== Data Verification ===")

# The data read from the generated YAML file
# should be identical to the original Python data.
if inventory == generated_inventory:

    print("Data verification: PASSED")

else:

    print("Data verification: FAILED")
