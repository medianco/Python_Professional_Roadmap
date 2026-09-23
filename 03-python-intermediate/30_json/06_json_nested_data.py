"""
Lesson 30.6 - Nested JSON

This lesson demonstrates how to work with nested JSON data.

Network Engineering Context:
Real network APIs often return deeply nested JSON structures
containing devices, interfaces, IP addresses, VLANs, routing
information, and operational status.

    Device
    │
    ├── hostname
    ├── management
    │   ├── ip_address
    │   └── protocol
    │
    └── interfaces
        ├── Interface 1
        └── Interface 2
"""

import json


def main() -> None:
    # =========================================================
    # 1. NESTED JSON DATA
    # =========================================================
    # This JSON represents a network router.
    #
    # Notice that:
    #
    # "management" contains another JSON object.
    #
    # "interfaces" contains an array of JSON objects.

    json_data = """
    {
        "hostname": "R1",
        "device_type": "router",

        "management": {
            "ip_address": "192.168.1.1",
            "protocol": "SSH"
        },

        "interfaces": [
            {
                "name": "GigabitEthernet0/0",
                "ip_address": "10.0.0.1",
                "status": "up"
            },
            {
                "name": "GigabitEthernet0/1",
                "ip_address": "10.0.1.1",
                "status": "down"
            }
        ]
    }
    """

    # =========================================================
    # 2. CONVERT JSON STRING TO PYTHON
    # =========================================================

    device = json.loads(json_data)

    print("=== Complete Device Data ===")
    print(device)

    # =========================================================
    # 3. ACCESS TOP-LEVEL VALUES
    # =========================================================
    # These values are directly inside the main JSON object.

    print("\n=== Basic Device Information ===")

    print("Hostname   :", device["hostname"])
    print("Device Type:", device["device_type"])

    # =========================================================
    # 4. ACCESS NESTED OBJECT
    # =========================================================
    # "management" is another dictionary inside "device".
    #
    # We can access its values using:
    #
    # device["management"]["ip_address"]

    print("\n=== Management Information ===")

    print("Management IP :", device["management"]["ip_address"])
    print("Protocol      :", device["management"]["protocol"])

    # =========================================================
    # 5. ACCESS NESTED ARRAY
    # =========================================================
    # "interfaces" contains a list of dictionaries.
    #
    # We can access the first interface using index [0].

    print("\n=== First Interface ===")

    first_interface = device["interfaces"][0]

    print("Name      :", first_interface["name"])
    print("IP Address:", first_interface["ip_address"])
    print("Status    :", first_interface["status"])

    # =========================================================
    # 6. ACCESS SECOND INTERFACE
    # =========================================================

    print("\n=== Second Interface ===")

    second_interface = device["interfaces"][1]

    print("Name      :", second_interface["name"])
    print("IP Address:", second_interface["ip_address"])
    print("Status    :", second_interface["status"])

    # =========================================================
    # 7. LOOP THROUGH ALL INTERFACES
    # =========================================================
    # In real Network Automation, we usually do not know
    # how many interfaces exist.
    #
    # Therefore, we use a loop.

    print("\n=== All Interfaces ===")

    for interface in device["interfaces"]:
        print(
            f"{interface['name']} | "
            f"{interface['ip_address']} | "
            f"{interface['status']}"
        )

    # =========================================================
    # 8. FILTER INTERFACES
    # =========================================================
    # We can also use the information inside the nested
    # dictionaries to perform automation logic.
    #
    # Here we display only interfaces that are UP.

    print("\n=== Interfaces UP ===")

    for interface in device["interfaces"]:
        if interface["status"] == "up":
            print(
                f"{interface['name']} "
                f"({interface['ip_address']}) is UP"
            )

    # =========================================================
    # 9. COUNT INTERFACES
    # =========================================================

    interface_count = len(device["interfaces"])

    print("\n=== Interface Statistics ===")
    print("Total Interfaces:", interface_count)


if __name__ == "__main__":
    main()
