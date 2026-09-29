"""
02_yaml_load.py

Lesson 33.2 — YAML Load

This file demonstrates how to convert YAML data
into Python objects using PyYAML.

Main concept:

    YAML
      ↓
    yaml.safe_load()
      ↓
    Python Object

We will work with:
- YAML mappings → Python dictionaries
- YAML sequences → Python lists
- Nested YAML → Nested Python dictionaries/lists

The focus is understanding the conversion process.
"""

# Import the PyYAML library.
# The package is installed as "pyyaml",
# but we import it in Python using "yaml".
import yaml


# ---------------------------------------------------------
# Example 1 — YAML Mapping → Python Dictionary
# ---------------------------------------------------------

# This string contains a simple YAML mapping.
yaml_data = """
hostname: R1
management_ip: 192.168.1.1
device_type: router
vendor: Cisco
status: active
"""

# safe_load() parses the YAML string
# and converts it into a Python object.
device = yaml.safe_load(yaml_data)

print("=== Example 1: YAML Mapping ===")

# The result is a Python dictionary.
print(device)

# We can access individual values using dictionary keys.
print(f"Hostname: {device['hostname']}")
print(f"Management IP: {device['management_ip']}")
print(f"Vendor: {device['vendor']}")


# ---------------------------------------------------------
# Example 2 — YAML List → Python List
# ---------------------------------------------------------

yaml_vendors = """
vendors:
  - Cisco
  - Juniper
  - Arista
"""

# Convert the YAML data into a Python dictionary.
vendor_data = yaml.safe_load(yaml_vendors)

print("\n=== Example 2: YAML List ===")

# Access the list stored under the "vendors" key.
vendors = vendor_data["vendors"]

print(f"Vendors: {vendors}")

# Loop through the Python list.
for vendor in vendors:
    print(f"- {vendor}")


# ---------------------------------------------------------
# Example 3 — Nested YAML → Nested Python Dictionary
# ---------------------------------------------------------

yaml_nested = """
device:
  hostname: R1

  management:
    ip: 192.168.1.1
    protocol: ssh

  platform:
    vendor: Cisco
    device_type: router
"""

# Convert the nested YAML structure into Python objects.
nested_data = yaml.safe_load(yaml_nested)

print("\n=== Example 3: Nested YAML ===")

# Access the top-level "device" dictionary.
device_data = nested_data["device"]

print(f"Hostname: {device_data['hostname']}")

# Access the nested "management" dictionary.
management = device_data["management"]

print(f"Management IP: {management['ip']}")
print(f"Protocol: {management['protocol']}")

# Access the nested "platform" dictionary.
platform = device_data["platform"]

print(f"Vendor: {platform['vendor']}")
print(f"Device Type: {platform['device_type']}")


# ---------------------------------------------------------
# Example 4 — Multiple Network Devices
# ---------------------------------------------------------

yaml_devices = """
devices:

  - hostname: R1
    management_ip: 192.168.1.1
    device_type: router
    vendor: Cisco
    status: active

  - hostname: R2
    management_ip: 192.168.1.2
    device_type: router
    vendor: Cisco
    status: active

  - hostname: SW1
    management_ip: 192.168.1.10
    device_type: switch
    vendor: Cisco
    status: active
"""

# Parse the YAML.
inventory = yaml.safe_load(yaml_devices)

print("\n=== Example 4: Network Device Inventory ===")

# "devices" is converted from a YAML sequence
# into a Python list of dictionaries.
devices = inventory["devices"]

# Display the total number of devices.
print(f"Total devices: {len(devices)}")

# Loop through every device.
for device in devices:

    print(
        f"{device['hostname']} | "
        f"{device['management_ip']} | "
        f"{device['device_type']} | "
        f"{device['vendor']} | "
        f"{device['status']}"
    )


# ---------------------------------------------------------
# Example 5 — Check Python Types
# ---------------------------------------------------------

print("\n=== Example 5: Python Types ===")

# The complete inventory is a Python dictionary.
print(f"Inventory type: {type(inventory).__name__}")

# The devices collection is a Python list.
print(f"Devices type: {type(devices).__name__}")

# Each individual device is a Python dictionary.
print(f"Device type: {type(devices[0]).__name__}")
