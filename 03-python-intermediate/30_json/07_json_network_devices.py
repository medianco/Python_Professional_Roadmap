"""
Lesson 30.7 - JSON & Network Devices

This lesson demonstrates how JSON can be used to represent
a network device inventory stored in an external JSON file.

Network Engineering Context:
Separating data from code is a common practice in Network Automation.

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
    """
    Load network inventory from a JSON file
    and display useful information about network devices.
    """

    # Name of the external JSON inventory file
    inventory_file = "inventory.json"

    # ---------------------------------------------------------
    # Load inventory from JSON file
    # ---------------------------------------------------------

    try:
        with open(inventory_file, "r") as file:
            inventory = json.load(file)

    except FileNotFoundError:
        print(f"Error: {inventory_file} was not found.")
        return

    except json.JSONDecodeError:
        print(f"Error: {inventory_file} contains invalid JSON.")
        return

    # Get the list of devices from the JSON object
    devices = inventory["devices"]

    # ---------------------------------------------------------
    # Display total number of devices
    # ---------------------------------------------------------

    print("=== Network Inventory ===")
    print(f"Total Devices: {len(devices)}")

    # ---------------------------------------------------------
    # Display all network devices
    # ---------------------------------------------------------

    print("\n=== All Network Devices ===")

    for device in devices:
        print(
            f"{device['hostname']} | "
            f"{device['management_ip']} | "
            f"{device['device_type']} | "
            f"{device['vendor']} | "
            f"{device['location']}"
        )

    # ---------------------------------------------------------
    # Display enabled devices
    # ---------------------------------------------------------

    print("\n=== Enabled Devices ===")

    for device in devices:
        if device["enabled"]:
            print(
                f"{device['hostname']} "
                f"({device['management_ip']})"
            )

    # ---------------------------------------------------------
    # Display Cisco devices
    # ---------------------------------------------------------

    print("\n=== Cisco Devices ===")

    for device in devices:
        if device["vendor"] == "Cisco":
            print(
                f"{device['hostname']} | "
                f"{device['device_type']} | "
                f"{device['management_ip']}"
            )

    # ---------------------------------------------------------
    # Display routers
    # ---------------------------------------------------------

    print("\n=== Routers ===")

    for device in devices:
        if device["device_type"] == "router":
            print(
                f"{device['hostname']} | "
                f"{device['management_ip']}"
            )

    # ---------------------------------------------------------
    # Display enabled routers
    # ---------------------------------------------------------

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

    # ---------------------------------------------------------
    # Calculate device statistics
    # ---------------------------------------------------------

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

    # ---------------------------------------------------------
    # Display statistics
    # ---------------------------------------------------------

    print("\n=== Device Statistics ===")
    print("Routers  :", routers)
    print("Switches :", switches)
    print("Firewalls:", firewalls)


# -------------------------------------------------------------
# Program Entry Point
# -------------------------------------------------------------

if __name__ == "__main__":
    main()
