"""
Lesson 30.7 - JSON & Network Devices

This lesson demonstrates how JSON can be used to represent
a network device inventory.

Network Engineering Context:
Network automation systems often maintain inventories
containing multiple routers, switches, firewalls, and
other network devices.

    JSON
     │
     ▼
    Network Inventory
     │
     ▼
    Python Dictionary
     │
     ▼
    List of Devices
     │
     ├── Router
     ├── Router
     ├── Switch
     └── Firewall
"""

import json


def main() -> None:
    # =========================================================
    # 1. NETWORK DEVICE INVENTORY IN JSON
    # =========================================================
    # The JSON contains multiple network devices.
    #
    # "devices" is an array.
    # Each element inside the array is a JSON object
    # representing one network device.

    inventory_json = """
    {
        "devices": [
            {
                "hostname": "R1",
                "management_ip": "192.168.1.1",
                "device_type": "router",
                "vendor": "Cisco",
                "location": "Data Center",
                "enabled": true
            },
            {
                "hostname": "R2",
                "management_ip": "192.168.1.2",
                "device_type": "router",
                "vendor": "Cisco",
                "location": "Branch 1",
                "enabled": true
            },
            {
                "hostname": "SW1",
                "management_ip": "192.168.1.10",
                "device_type": "switch",
                "vendor": "Cisco",
                "location": "Data Center",
                "enabled": false
            },
            {
                "hostname": "FW1",
                "management_ip": "192.168.1.254",
                "device_type": "firewall",
                "vendor": "Fortinet",
                "location": "Data Center",
                "enabled": true
            }
        ]
    }
    """

    # =========================================================
    # 2. CONVERT JSON TO PYTHON
    # =========================================================

    inventory = json.loads(inventory_json)

    print("=== Network Inventory ===")
    print(inventory)

    # =========================================================
    # 3. ACCESS THE DEVICES ARRAY
    # =========================================================
    # The "devices" key contains a list of dictionaries.

    devices = inventory["devices"]

    print("\n=== Total Devices ===")
    print(len(devices))

    # =========================================================
    # 4. DISPLAY ALL DEVICES
    # =========================================================
    # We can loop through all devices.

    print("\n=== All Network Devices ===")

    for device in devices:
        print(
            f"{device['hostname']} | "
            f"{device['management_ip']} | "
            f"{device['device_type']} | "
            f"{device['vendor']} | "
            f"{device['location']}"
        )

    # =========================================================
    # 5. DISPLAY ENABLED DEVICES
    # =========================================================
    # We can filter devices using the "enabled" field.

    print("\n=== Enabled Devices ===")

    for device in devices:
        if device["enabled"]:
            print(
                f"{device['hostname']} "
                f"({device['management_ip']})"
            )

    # =========================================================
    # 6. DISPLAY CISCO DEVICES
    # =========================================================
    # We can filter the inventory by vendor.

    print("\n=== Cisco Devices ===")

    for device in devices:
        if device["vendor"] == "Cisco":
            print(
                f"{device['hostname']} | "
                f"{device['device_type']} | "
                f"{device['management_ip']}"
            )

    # =========================================================
    # 7. DISPLAY ROUTERS
    # =========================================================
    # We can also filter devices by device type.

    print("\n=== Routers ===")

    for device in devices:
        if device["device_type"] == "router":
            print(
                f"{device['hostname']} | "
                f"{device['management_ip']}"
            )

    # =========================================================
    # 8. NETWORK AUTOMATION SCENARIO
    # =========================================================
    # Imagine that our automation system needs to connect
    # only to enabled routers.
    #
    # We can filter the inventory using two conditions.

    print("\n=== Enabled Routers ===")

    for device in devices:
        if (
            device["device_type"] == "router"
            and device["enabled"]
        ):
            print(
                f"Ready for automation: "
                f"{device['hostname']} "
                f"({device['management_ip']})"
            )

    # =========================================================
    # 9. COUNT DEVICES BY TYPE
    # =========================================================
    # We can calculate how many routers, switches,
    # and firewalls exist in the inventory.

    routers = 0
    switches = 0
    firewalls = 0

    for device in devices:

        if device["device_type"] == "router":
            routers += 1

        elif device["device_type"] == "switch":
            switches += 1

        elif device["device_type"] == "firewall":
            firewalls += 1

    print("\n=== Device Statistics ===")
    print("Routers  :", routers)
    print("Switches :", switches)
    print("Firewalls:", firewalls)


if __name__ == "__main__":
    main()
