"""
Lesson 30.5 - Reading JSON from a File

This lesson demonstrates how to read JSON data
from a file using json.load().

Network Engineering Context:
Network automation scripts often read device inventories,
configuration data, and automation variables from JSON files.
"""

import json


def main() -> None:
    # =========================================================
    # 1. READ JSON FILE
    # =========================================================
    # The file "device.json" was created in Lesson 30.4.
    #
    # "r" means:
    # read mode
    #
    # json.load() reads the JSON file and converts
    # its content into a Python object.

    with open("device.json", "r") as file:
        device = json.load(file)

    # =========================================================
    # 2. DISPLAY THE PYTHON OBJECT
    # =========================================================

    print("=== Loaded Device Data ===")
    print(device)

    print("\nData type:")
    print(type(device).__name__)

    # =========================================================
    # 3. ACCESS INDIVIDUAL VALUES
    # =========================================================
    # After json.load(), the JSON object becomes
    # a Python dictionary.
    #
    # Therefore, we can access values using dictionary keys.

    print("\n=== Device Information ===")

    print("Hostname      :", device["hostname"])
    print("Management IP :", device["management_ip"])
    print("Device Type   :", device["device_type"])
    print("Vendor        :", device["vendor"])
    print("Location      :", device["location"])
    print("Enabled       :", device["enabled"])

    # =========================================================
    # 4. NETWORK AUTOMATION EXAMPLE
    # =========================================================
    # Imagine that device.json is our network inventory.
    #
    # The automation script can load the inventory
    # and then use the information to perform tasks.

    print("\n=== Network Automation ===")

    hostname = device["hostname"]
    management_ip = device["management_ip"]

    print(f"Preparing connection to {hostname}...")
    print(f"Management IP: {management_ip}")


if __name__ == "__main__":
    main()
