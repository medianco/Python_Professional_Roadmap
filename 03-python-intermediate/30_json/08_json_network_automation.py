"""
Lesson 30.8 - JSON in Network Automation

This lesson demonstrates how JSON can be used as a
network inventory source for automation.

Network Engineering Context:
JSON can store device information such as hostname,
management IP, device type, vendor, and automation status.

The Python program reads this inventory and prepares
the devices for future automation tasks.

## Automation Workflow
    
    inventory.json
          ↓
       json.load()
          ↓
       Validate / Filter
          ↓
    Enabled Devices
          ↓
    Automation Target List
          ↓
    Future: Netmiko / APIs / Nornir
"""

import json


def load_inventory(filename: str) -> dict:
    """
    Load network inventory from a JSON file.

    Args:
        filename: Path to the JSON inventory file.

    Returns:
        A dictionary containing the network inventory.

    Raises:
        FileNotFoundError: If the inventory file does not exist.
        json.JSONDecodeError: If the JSON file is invalid.
    """

    with open(filename, "r") as file:
        return json.load(file)


def get_enabled_devices(inventory: dict) -> list[dict]:
    """
    Return only devices that are enabled for automation.

    Args:
        inventory: Network inventory dictionary.

    Returns:
        List of enabled network devices.
    """

    devices = inventory["devices"]

    return [
        device
        for device in devices
        if device["enabled"]
    ]


def display_devices(devices: list[dict]) -> None:
    """
    Display devices prepared for automation.

    Args:
        devices: List of network devices.
    """

    print("=== Devices Ready for Automation ===")

    for device in devices:
        print(
            f"Hostname      : {device['hostname']}\n"
            f"Management IP : {device['management_ip']}\n"
            f"Device Type   : {device['device_type']}\n"
            f"Vendor        : {device['vendor']}\n"
            f"Location      : {device['location']}\n"
            f"Status        : Enabled\n"
        )


def prepare_automation_targets(devices: list[dict]) -> list[dict]:
    """
    Prepare a simplified target list for future automation.

    Args:
        devices: List of enabled network devices.

    Returns:
        List containing automation target information.
    """

    targets = []

    for device in devices:
        target = {
            "hostname": device["hostname"],
            "ip": device["management_ip"],
            "device_type": device["device_type"],
            "vendor": device["vendor"],
        }

        targets.append(target)

    return targets


def main() -> None:
    """
    Main program workflow.
    """

    inventory_file = "inventory.json"

    # ---------------------------------------------------------
    # Step 1: Load inventory
    # ---------------------------------------------------------

    try:
        inventory = load_inventory(inventory_file)

    except FileNotFoundError:
        print(f"Error: {inventory_file} was not found.")
        return

    except json.JSONDecodeError:
        print(f"Error: {inventory_file} contains invalid JSON.")
        return

    # ---------------------------------------------------------
    # Step 2: Select enabled devices
    # ---------------------------------------------------------

    enabled_devices = get_enabled_devices(inventory)

    # ---------------------------------------------------------
    # Step 3: Display selected devices
    # ---------------------------------------------------------

    display_devices(enabled_devices)

    # ---------------------------------------------------------
    # Step 4: Prepare automation targets
    # ---------------------------------------------------------

    automation_targets = prepare_automation_targets(
        enabled_devices
    )

    # ---------------------------------------------------------
    # Step 5: Display automation targets
    # ---------------------------------------------------------

    print("=== Automation Targets ===")

    for target in automation_targets:
        print(
            f"{target['hostname']} "
            f"→ {target['ip']} "
            f"→ {target['vendor']} "
            f"→ {target['device_type']}"
        )

    # ---------------------------------------------------------
    # Step 6: Display summary
    # ---------------------------------------------------------

    print("\n=== Automation Summary ===")
    print(f"Total devices in inventory : {len(inventory['devices'])}")
    print(f"Enabled devices            : {len(enabled_devices)}")
    print(f"Automation targets         : {len(automation_targets)}")


# -------------------------------------------------------------
# Program Entry Point
# -------------------------------------------------------------

if __name__ == "__main__":
    main()
