"""
Lesson 30.3 - json.loads()

This lesson demonstrates how to convert a JSON string
into a Python object using json.loads().

Network Engineering Context:
Network automation scripts frequently receive JSON data
from REST APIs and need to convert that data into Python
objects for processing.
"""

import json


def main() -> None:
    # =========================================================
    # 1. JSON STRING
    # =========================================================
    # This is a JSON string representing a network device.
    #
    # Important:
    # At this point, the data is still a Python string.

    json_data = """
    {
        "hostname": "R1",
        "ip_address": "192.168.1.1",
        "device_type": "router",
        "vendor": "Cisco",
        "enabled": true
    }
    """

    print("=== JSON String ===")
    print(json_data)

    print("\nData type:")
    print(type(json_data).__name__)

    # =========================================================
    # 2. CONVERT JSON STRING TO PYTHON
    # =========================================================
    # json.loads() converts the JSON string
    # into a Python object.
    #
    # In this example:
    #
    # JSON Object
    #     ↓
    # Python Dictionary

    device = json.loads(json_data)

    print("\n=== Python Object ===")
    print(device)

    print("\nData type:")
    print(type(device).__name__)

    # =========================================================
    # 3. ACCESS JSON DATA AS A PYTHON DICTIONARY
    # =========================================================
    # After conversion, we can access the values
    # using normal Python dictionary syntax.

    print("\n=== Device Information ===")

    print("Hostname   :", device["hostname"])
    print("IP Address :", device["ip_address"])
    print("Device Type:", device["device_type"])
    print("Vendor     :", device["vendor"])
    print("Enabled    :", device["enabled"])

    # =========================================================
    # 4. CHECK INDIVIDUAL DATA TYPES
    # =========================================================
    # JSON data types are automatically converted
    # into their corresponding Python data types.

    print("\n=== Python Data Types ===")

    print("hostname :", type(device["hostname"]).__name__)
    print("ip       :", type(device["ip_address"]).__name__)
    print("enabled  :", type(device["enabled"]).__name__)

    # =========================================================
    # 5. NETWORK AUTOMATION EXAMPLE
    # =========================================================
    # Imagine that a REST API returns the following JSON.
    #
    # Our Python automation script receives the response
    # as JSON text.
    #
    # We use json.loads() to convert it into a Python
    # dictionary so that we can process the information.

    api_response = """
    {
        "hostname": "R2",
        "management_ip": "192.168.1.2",
        "status": "up",
        "interfaces": 24
    }
    """

    api_data = json.loads(api_response)

    print("\n=== API Response ===")
    print(api_data)

    print("\n=== API Device Information ===")
    print("Hostname   :", api_data["hostname"])
    print("Management IP:", api_data["management_ip"])
    print("Status     :", api_data["status"])
    print("Interfaces :", api_data["interfaces"])


if __name__ == "__main__":
    main()
