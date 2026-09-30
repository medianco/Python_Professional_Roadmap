"""
03_yaml_dump.py

Lesson 33.3 — YAML Dump

This file demonstrates how to convert Python objects
into YAML using PyYAML.

Main concept:

    Python Object
          ↓
    yaml.safe_dump()
          ↓
        YAML

We will practice with:
- Python dictionaries
- Python lists
- Nested dictionaries
- Network device inventory

Important:
We use safe_dump() because our data consists of
standard Python data types such as dict, list, str,
int, bool, etc.
"""

# Import PyYAML.
# The package is installed as "pyyaml",
# but the Python module is imported as "yaml".
import yaml


# ---------------------------------------------------------
# Example 1 — Python Dictionary → YAML
# ---------------------------------------------------------

# Create a normal Python dictionary representing
# a network device.
device = {
    "hostname": "R1",
    "management_ip": "192.168.1.1",
    "device_type": "router",
    "vendor": "Cisco",
    "status": "active",
}

# Convert the Python dictionary into YAML.
#
# sort_keys=False keeps the dictionary key order
# instead of alphabetically sorting the keys.
yaml_output = yaml.safe_dump(
    device,
    sort_keys=False,
)

print("=== Example 1: Dictionary → YAML ===")
print(yaml_output)


# ---------------------------------------------------------
# Example 2 — Python List → YAML
# ---------------------------------------------------------

# Create a Python list containing network vendors.
vendors = [
    "Cisco",
    "Juniper",
    "Arista",
    "Nokia",
]

# Convert the Python list into YAML.
yaml_vendors = yaml.safe_dump(
    vendors,
    sort_keys=False,
)

print("=== Example 2: List → YAML ===")
print(yaml_vendors)


# ---------------------------------------------------------
# Example 3 — Nested Python Dictionary → YAML
# ---------------------------------------------------------

# Create a nested Python structure.
#
# This is common in real network automation because
# a device may contain management, platform, and
# connection information.
network_device = {
    "device": {
        "hostname": "R1",
        "management": {
            "ip": "192.168.1.1",
            "protocol": "ssh",
        },
        "platform": {
            "vendor": "Cisco",
            "device_type": "router",
        },
    }
}

# Convert the nested Python dictionary into YAML.
nested_yaml = yaml.safe_dump(
    network_device,
    sort_keys=False,
)

print("=== Example 3: Nested Dictionary → YAML ===")
print(nested_yaml)


# ---------------------------------------------------------
# Example 4 — Network Device Inventory
# ---------------------------------------------------------

# Create a Python dictionary containing
# multiple network devices.
#
# Notice that "devices" contains a list of dictionaries.
# This structure is very common in automation systems.
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

# Convert the complete inventory into YAML.
inventory_yaml = yaml.safe_dump(
    inventory,
    sort_keys=False,
)

print("=== Example 4: Network Device Inventory ===")
print(inventory_yaml)


# ---------------------------------------------------------
# Example 5 — YAML Round Trip
# ---------------------------------------------------------

# First, convert the Python inventory into YAML.
yaml_data = yaml.safe_dump(
    inventory,
    sort_keys=False,
)

# Now convert the YAML back into Python.
#
# This demonstrates the relationship between:
#
# Python → YAML → Python
#
# safe_dump() performs the first conversion.
# safe_load() performs the second conversion.
restored_inventory = yaml.safe_load(yaml_data)

print("=== Example 5: YAML Round Trip ===")

# Check whether the restored Python object
# is equal to the original inventory.
print(f"Original equals restored: {inventory == restored_inventory}")

# Display the restored data type.
print(f"Restored type: {type(restored_inventory).__name__}")


# ---------------------------------------------------------
# Example 6 — Access Data After Round Trip
# ---------------------------------------------------------

print("\n=== Example 6: Access Restored Data ===")

# Access the devices list from the restored dictionary.
devices = restored_inventory["devices"]

# Display the number of devices.
print(f"Total devices: {len(devices)}")

# Loop through every restored device.
for device in devices:

    print(
        f"{device['hostname']} | "
        f"{device['management_ip']} | "
        f"{device['device_type']} | "
        f"{device['vendor']}"
    )
