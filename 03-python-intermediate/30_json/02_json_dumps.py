"""
Lesson 30.2 - json.dumps()

This lesson demonstrates how to convert Python objects
into JSON strings using json.dumps().

Network Engineering Context:
json.dumps() is commonly used when network automation
scripts need to prepare structured data for:
- REST APIs
- Network Management Systems
- Cloud APIs
- Logging
- Configuration Exchange
"""

import json


def main() -> None:
    # =========================================================
    # 1. CREATE A PYTHON DICTIONARY
    # =========================================================
    # This dictionary represents a network device.

    device = {
        "hostname": "R1",
        "ip_address": "192.168.1.1",
        "device_type": "router",
        "vendor": "Cisco",
        "enabled": True,
    }

    print("=== Python Dictionary ===")
    print(device)

    # Check the Python data type.
    print("\nData type:")
    print(type(device).__name__)

    # =========================================================
    # 2. CONVERT PYTHON DICTIONARY TO JSON
    # =========================================================
    # json.dumps() converts a Python object
    # into a JSON string.

    json_data = json.dumps(device)

    print("\n=== JSON String ===")
    print(json_data)

    # Check the resulting data type.
    print("\nData type:")
    print(type(json_data).__name__)

    # =========================================================
    # 3. FORMATTING JSON WITH indent
    # =========================================================
    # By default, json.dumps() produces compact JSON.
    #
    # We can make the JSON easier to read
    # by using indent=4.

    formatted_json = json.dumps(device, indent=4)

    print("\n=== Formatted JSON ===")
    print(formatted_json)

    # =========================================================
    # 4. SORT JSON KEYS
    # =========================================================
    # sort_keys=True sorts dictionary keys alphabetically.

    sorted_json = json.dumps(
        device,
        indent=4,
        sort_keys=True
    )

    print("\n=== Sorted JSON ===")
    print(sorted_json)

    # =========================================================
    # 5. NETWORK AUTOMATION EXAMPLE
    # =========================================================
    # Imagine that we want to prepare device information
    # before sending it to a REST API.
    #
    # The API expects JSON data.
    #
    # Therefore:
    #
    # Python Dictionary
    #       ↓
    #   json.dumps()
    #       ↓
    # JSON String
    #       ↓
    # REST API

    api_payload = {
        "hostname": "R1",
        "management_ip": "192.168.1.1",
        "status": "active",
    }

    api_data = json.dumps(api_payload)

    print("\n=== API Payload ===")
    print(api_data)


if __name__ == "__main__":
    main()
