"""
Lesson 30.4 - Writing JSON to a File

This lesson demonstrates how to write Python data
directly into a JSON file using json.dump().

Network Engineering Context:
JSON files are commonly used to store:
- Network Device Inventory
- IP Address Information
- Device Configurations
- Automation Variables
- API Data
"""

import json


def main() -> None:
    # =========================================================
    # 1. CREATE NETWORK DEVICE DATA
    # =========================================================
    # This Python dictionary represents a network device.

    device = {
        "hostname": "R1",
        "management_ip": "192.168.1.1",
        "device_type": "router",
        "vendor": "Cisco",
        "location": "Data Center",
        "enabled": True,
    }

    print("=== Python Device Data ===")
    print(device)

    # =========================================================
    # 2. WRITE DATA TO A JSON FILE
    # =========================================================
    # json.dump() writes a Python object directly
    # into a JSON file.
    #
    # Syntax:
    #
    # json.dump(data, file)
    #
    # We use:
    # "w" -> write mode
    #
    # If the file does not exist, Python creates it.
    # If it already exists, its content will be replaced.

    with open("device.json", "w") as file:
        json.dump(device, file, indent=4)

    print("\nJSON file created successfully.")

    # =========================================================
    # 3. EXPLAIN THE FILE CONTENT
    # =========================================================
    # The generated file will contain valid JSON.
    #
    # File:
    #
    # device.json
    #
    # Content:
    #
    # {
    #     "hostname": "R1",
    #     "management_ip": "192.168.1.1",
    #     "device_type": "router",
    #     "vendor": "Cisco",
    #     "location": "Data Center",
    #     "enabled": true
    # }

    print("\nFile name: device.json")
    print("JSON formatting: indent=4")


if __name__ == "__main__":
    main()
