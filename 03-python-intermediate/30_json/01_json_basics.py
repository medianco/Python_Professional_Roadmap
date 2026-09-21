"""
Lesson 30.1 - JSON Basics

This lesson introduces the basics of JSON and explains
the relationship between JSON data types and Python data types.

Network Engineering Context:
JSON is widely used in:
- Network Automation
- REST APIs
- Network Device Inventory
- Cloud Platforms
- Configuration Management
- Monitoring Systems

        JSON String
             ↕
         Conversion
             ↕
        Python Object
"""

import json


def main() -> None:
    # =========================================================
    # 1. JSON OBJECT
    # =========================================================
    # A JSON object is enclosed inside { }.
    #
    # JSON uses key-value pairs:
    #
    # "key": "value"
    #
    # This example represents a network device.

    device_json = """
    {
        "hostname": "R1",
        "ip_address": "192.168.1.1",
        "device_type": "router",
        "enabled": true,
        "interfaces": [
            "GigabitEthernet0/0",
            "GigabitEthernet0/1"
        ],
        "description": null
    }
    """

    print("=== JSON Data ===")
    print(device_json)

    # =========================================================
    # 2. JSON DATA TYPES
    # =========================================================
    # JSON supports several basic data types:
    #
    # String
    # Number
    # Boolean
    # Array
    # Object
    # Null

    print("\n=== JSON Data Types ===")

    print("hostname      -> String")
    print("ip_address    -> String")
    print("device_type   -> String")
    print("enabled       -> Boolean")
    print("interfaces    -> Array")
    print("description   -> Null")

    # =========================================================
    # 3. JSON vs PYTHON
    # =========================================================
    # JSON and Python have similar data types,
    # but some values are written differently.
    #
    # JSON          Python
    # ---------------------
    # true       -> True
    # false      -> False
    # null       -> None
    # Object     -> dict
    # Array      -> list
    # String     -> str
    # Number     -> int / float

    print("\n=== JSON vs Python ===")

    print("JSON true     -> Python True")
    print("JSON false    -> Python False")
    print("JSON null     -> Python None")
    print("JSON object   -> Python dict")
    print("JSON array    -> Python list")

    # =========================================================
    # 4. PYTHON DICTIONARY
    # =========================================================
    # The same network device can be represented
    # as a normal Python dictionary.

    device = {
        "hostname": "R1",
        "ip_address": "192.168.1.1",
        "device_type": "router",
        "enabled": True,
        "interfaces": [
            "GigabitEthernet0/0",
            "GigabitEthernet0/1"
        ],
        "description": None,
    }

    print("\n=== Python Dictionary ===")
    print(device)

    # =========================================================
    # 5. CHECK PYTHON DATA TYPES
    # =========================================================
    # Python automatically assigns a data type to each value.

    print("\n=== Python Data Types ===")

    print("hostname   :", type(device["hostname"]).__name__)
    print("ip_address :", type(device["ip_address"]).__name__)
    print("device_type:", type(device["device_type"]).__name__)
    print("enabled    :", type(device["enabled"]).__name__)
    print("interfaces :", type(device["interfaces"]).__name__)
    print("description:", type(device["description"]).__name__)

    # =========================================================
    # IMPORTANT
    # =========================================================
    # device_json is a JSON STRING.
    #
    # device is a Python DICTIONARY.
    #
    # They may represent the same information,
    # but they are NOT the same Python data type.
    #
    # In the next lessons, we will learn how to convert
    # between Python objects and JSON using:
    #
    # json.dumps()  -> Python -> JSON
    # json.loads()  -> JSON -> Python


if __name__ == "__main__":
    main()
