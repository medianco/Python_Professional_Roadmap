"""
Lesson 33.8 — YAML & Network Automation

This script demonstrates how YAML can be used as an
external inventory source for Network Automation.

The YAML file contains device information, while this
Python script is responsible for:

1. Loading the YAML inventory.
2. Validating the basic inventory structure.
3. Filtering devices that can be automated.
4. Selecting active SSH devices.
5. Building automation targets.
6. Displaying the targets that would be used by
   a real automation framework.

Note:
This lesson does not establish real SSH connections.
It prepares the data that could later be passed to
Netmiko, Nornir, Paramiko, or another automation tool.
"""

from pathlib import Path

import yaml


# ---------------------------------------------------------
# 1. Define the location of the YAML inventory file
# ---------------------------------------------------------

# Path(__file__) gives us the location of this Python file.
# resolve() converts it into an absolute path.
BASE_DIR = Path(__file__).resolve().parent

# The inventory is stored separately from the Python logic.
DATA_FILE = BASE_DIR / "data" / "network_devices.yaml"


# ---------------------------------------------------------
# 2. Load the YAML inventory
# ---------------------------------------------------------

def load_inventory(file_path: Path) -> dict:
    """
    Load the network device inventory from a YAML file.

    Args:
        file_path: Path to the YAML inventory file.

    Returns:
        A Python dictionary containing the inventory.

    Raises:
        FileNotFoundError: If the YAML file does not exist.
        ValueError: If the YAML root structure is invalid.
    """

    # Check whether the inventory file exists before reading it.
    if not file_path.exists():
        raise FileNotFoundError(
            f"Inventory file not found: {file_path}"
        )

    # Open the YAML file using UTF-8 encoding.
    with file_path.open("r", encoding="utf-8") as file:

        # safe_load() converts YAML data into Python objects.
        inventory = yaml.safe_load(file)

    # The root of our inventory must be a dictionary.
    if not isinstance(inventory, dict):
        raise ValueError(
            "Invalid inventory format: root must be a dictionary."
        )

    return inventory


# ---------------------------------------------------------
# 3. Validate the device list
# ---------------------------------------------------------

def validate_devices(inventory: dict) -> list:
    """
    Validate that the inventory contains a device list.

    Args:
        inventory: Parsed YAML inventory.

    Returns:
        List of network devices.

    Raises:
        ValueError: If the devices section is missing or invalid.
    """

    # Extract the devices section from the inventory.
    devices = inventory.get("devices")

    # The devices section must be a list.
    if not isinstance(devices, list):
        raise ValueError(
            "Invalid inventory format: 'devices' must be a list."
        )

    return devices


# ---------------------------------------------------------
# 4. Build automation targets
# ---------------------------------------------------------

def build_automation_targets(devices: list) -> list:
    """
    Select devices that are ready for SSH-based automation.

    Conditions:

    - Device status must be active.
    - Management protocol must be SSH.
    - Management IP must exist.

    Args:
        devices: List of network devices.

    Returns:
        List of automation targets.
    """

    automation_targets = []

    # Process every device in the inventory.
    for device in devices:

        # Read the nested management information.
        management = device.get("management", {})

        # Read the device status.
        status = device.get("status")

        # Read the management protocol.
        protocol = management.get("protocol")

        # Read the management IP address.
        ip_address = management.get("ip")

        # Only active devices using SSH are selected.
        if (
            status == "active"
            and protocol == "ssh"
            and ip_address
        ):

            # Create a simplified target dictionary.
            # This is the information an automation framework
            # would need to begin a connection.
            target = {
                "hostname": device.get("hostname"),
                "ip": ip_address,
                "protocol": protocol,
                "port": management.get("port"),
                "vendor": device.get("platform", {}).get("vendor"),
                "device_type": device.get("platform", {}).get(
                    "device_type"
                ),
                "os": device.get("platform", {}).get("os"),
            }

            automation_targets.append(target)

    return automation_targets


# ---------------------------------------------------------
# 5. Display automation targets
# ---------------------------------------------------------

def display_targets(targets: list) -> None:
    """
    Display the devices selected for automation.

    Args:
        targets: List of automation targets.
    """

    print("\n=== Network Automation Targets ===")

    # Check whether any devices were selected.
    if not targets:
        print("No suitable automation targets found.")
        return

    # Display every selected target.
    for target in targets:

        print(
            f"{target['hostname']} | "
            f"{target['ip']} | "
            f"{target['protocol']} | "
            f"Port: {target['port']} | "
            f"{target['vendor']} | "
            f"{target['device_type']} | "
            f"{target['os']}"
        )

    print(f"\nTotal automation targets: {len(targets)}")


# ---------------------------------------------------------
# 6. Main program
# ---------------------------------------------------------

def main() -> None:
    """
    Main application workflow.
    """

    print("=== YAML Network Automation ===")
    print(f"Inventory file: {DATA_FILE}")

    # Load the YAML inventory.
    inventory = load_inventory(DATA_FILE)

    # Validate and retrieve the device list.
    devices = validate_devices(inventory)

    print(f"Total devices in inventory: {len(devices)}")

    # Convert the inventory into automation targets.
    automation_targets = build_automation_targets(devices)

    # Display the selected targets.
    display_targets(automation_targets)


# ---------------------------------------------------------
# 7. Python entry point
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
