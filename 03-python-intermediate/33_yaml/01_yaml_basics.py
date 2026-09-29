"""
01_yaml_basics.py

Lesson 33.1 — YAML Basics

This file introduces the basic structure of YAML.

We are intentionally not using PyYAML yet.
The goal is to understand YAML syntax before
we start parsing YAML with Python.
"""


# ============================================================
# 1. Basic YAML Mapping
# ============================================================

# YAML uses the following structure:
#
# key: value
#
# Example:

basic_yaml = """
hostname: R1
management_ip: 192.168.1.1
vendor: Cisco
device_type: router
status: active
"""


print("=" * 60)
print("YAML BASICS")
print("=" * 60)

print("\n--- Basic YAML Mapping ---")
print(basic_yaml)


# ============================================================
# 2. YAML List
# ============================================================

# YAML lists use the "-" character.
#
# Example:
#
# vendors:
#   - Cisco
#   - Juniper
#   - Arista

list_yaml = """
vendors:
  - Cisco
  - Juniper
  - Arista
"""


print("--- YAML List ---")
print(list_yaml)


# ============================================================
# 3. Nested YAML
# ============================================================

# YAML supports nested structures using indentation.
#
# The "management" section contains:
# - ip
# - protocol

nested_yaml = """
device:
  hostname: R1

  management:
    ip: 192.168.1.1
    protocol: ssh
"""


print("--- Nested YAML ---")
print(nested_yaml)


# ============================================================
# 4. Network Device Example
# ============================================================

# This example represents a network device inventory record.

network_device_yaml = """
# Network device information

hostname: R1
management_ip: 192.168.1.1
device_type: router
vendor: Cisco
location: Data Center
status: active
"""


print("--- Network Device YAML ---")
print(network_device_yaml)


# ============================================================
# 5. Multiple Network Devices
# ============================================================

# The "devices" key contains a list of network devices.
#
# Each "-" represents one device.

devices_yaml = """
devices:

  - hostname: R1
    management_ip: 192.168.1.1
    device_type: router
    vendor: Cisco
    location: Data Center
    status: active

  - hostname: R2
    management_ip: 192.168.1.2
    device_type: router
    vendor: Cisco
    location: Branch 1
    status: active

  - hostname: SW1
    management_ip: 192.168.1.10
    device_type: switch
    vendor: Cisco
    location: Data Center
    status: active
"""


print("--- Network Device Inventory ---")
print(devices_yaml)


print("=" * 60)
print("YAML BASICS COMPLETED")
print("=" * 60)
