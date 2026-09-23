"""
Lesson 30.9 - JSON Validation

This lesson demonstrates how to validate JSON data
before using it in Network Automation.

Validation Levels:
1. JSON syntax validation
2. Data structure validation
3. Required fields validation
4. Network data validation

Network Engineering Context:
Before automating network devices, we should verify
that the inventory contains valid and complete data.

## Workflow
                inventory.json
                       │
                       ▼
                  json.load()
                       │
                       ▼
                Validate JSON
                       │
                       ▼
              Validate Structure
                       │
                       ▼
              Validate Device Data
                       │
                       ▼
                Filter Devices
                       │
                       ▼
               Automation Targets
                       │
                       ▼
               Network Automation
"""

import json
import ipaddress


# -------------------------------------------------------------
# Configuration
# -------------------------------------------------------------

INVENTORY_FILE = "inventory.json"

# Required fields for every network device
REQUIRED_FIELDS = {
    "hostname",
    "management_ip",
    "device_type",
    "vendor",
    "location",
    "enabled",
}


# -------------------------------------------------------------
# Load JSON Inventory
# -------------------------------------------------------------

def load_inventory(filename: str) -> dict:
    """
    Load and parse a JSON inventory file.

    Args:
        filename: Path to the JSON inventory file.

    Returns:
        Parsed JSON data as a Python dictionary.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the JSON syntax is invalid.
    """

    with open(filename, "r") as file:
        return json.load(file)


# -------------------------------------------------------------
# Validate Inventory Structure
# -------------------------------------------------------------

def validate_inventory_structure(inventory: dict) -> bool:
    """
    Validate the basic structure of the inventory.

    The inventory must contain a 'devices' key
    whose value must be a list.

    Args:
        inventory: Parsed inventory dictionary.

    Returns:
        True if the structure is valid, otherwise False.
    """

    if not isinstance(inventory, dict):
        print("ERROR: Inventory must be a JSON object.")
        return False

    if "devices" not in inventory:
        print("ERROR: 'devices' key is missing.")
        return False

    if not isinstance(inventory["devices"], list):
        print("ERROR: 'devices' must contain a list.")
        return False

    return True


# -------------------------------------------------------------
# Validate Required Fields
# -------------------------------------------------------------

def validate_required_fields(device: dict) -> bool:
    """
    Validate that a device contains all required fields.

    Args:
        device: Network device dictionary.

    Returns:
        True if all required fields exist.
    """

    missing_fields = REQUIRED_FIELDS - device.keys()

    if missing_fields:
        print(
            f"ERROR: {device.get('hostname', 'Unknown Device')} "
            f"is missing fields: {', '.join(missing_fields)}"
        )
        return False

    return True


# -------------------------------------------------------------
# Validate IP Address
# -------------------------------------------------------------

def validate_ip_address(device: dict) -> bool:
    """
    Validate the management IP address.

    Args:
        device: Network device dictionary.

    Returns:
        True if the IP address is valid.
    """

    hostname = device.get("hostname", "Unknown Device")
    ip_address = device.get("management_ip")

    try:
        ipaddress.ip_address(ip_address)
        return True

    except ValueError:
        print(
            f"ERROR: {hostname} has an invalid IP address: "
            f"{ip_address}"
        )
        return False


# -------------------------------------------------------------
# Validate Enabled Field
# -------------------------------------------------------------

def validate_enabled_field(device: dict) -> bool:
    """
    Validate that the 'enabled' field is a Boolean.

    Args:
        device: Network device dictionary.

    Returns:
        True if the field is valid.
    """

    hostname = device.get("hostname", "Unknown Device")

    if not isinstance(device["enabled"], bool):
        print(
            f"ERROR: {hostname} 'enabled' must be True or False."
        )
        return False

    return True


# -------------------------------------------------------------
# Validate Device
# -------------------------------------------------------------

def validate_device(device: dict) -> bool:
    """
    Perform all validation checks for one network device.

    Args:
        device: Network device dictionary.

    Returns:
        True if all validation checks pass.
    """

    if not isinstance(device, dict):
        print("ERROR: Device entry must be a JSON object.")
        return False

    if not validate_required_fields(device):
        return False

    if not validate_ip_address(device):
        return False

    if not validate_enabled_field(device):
        return False

    return True


# -------------------------------------------------------------
# Validate Complete Inventory
# -------------------------------------------------------------

def validate_inventory(inventory: dict) -> bool:
    """
    Validate the complete network inventory.

    Args:
        inventory: Parsed inventory dictionary.

    Returns:
        True if the complete inventory is valid.
    """

    if not validate_inventory_structure(inventory):
        return False

    devices = inventory["devices"]

    if not devices:
        print("ERROR: Inventory contains no devices.")
        return False

    print("=== Device Validation ===")

    inventory_is_valid = True

    for device in devices:

        hostname = device.get("hostname", "Unknown Device")

        if validate_device(device):
            print(f"[OK] {hostname}")
        else:
            print(f"[FAILED] {hostname}")
            inventory_is_valid = False

    return inventory_is_valid


# -------------------------------------------------------------
# Main Program
# -------------------------------------------------------------

def main() -> None:
    """
    Main program workflow.
    """

    print("=== JSON Network Inventory Validation ===\n")

    # ---------------------------------------------------------
    # Step 1: Load JSON
    # ---------------------------------------------------------

    try:
        inventory = load_inventory(INVENTORY_FILE)

    except FileNotFoundError:
        print(
            f"ERROR: {INVENTORY_FILE} was not found."
        )
        return

    except json.JSONDecodeError as error:
        print(
            f"ERROR: Invalid JSON syntax.\n"
            f"Details: {error}"
        )
        return

    # ---------------------------------------------------------
    # Step 2: Validate inventory
    # ---------------------------------------------------------

    is_valid = validate_inventory(inventory)

    # ---------------------------------------------------------
    # Step 3: Final result
    # ---------------------------------------------------------

    print("\n=== Validation Result ===")

    if is_valid:
        print("Inventory validation successful.")
        print("Inventory is ready for Network Automation.")

    else:
        print("Inventory validation failed.")
        print("Fix the inventory before starting automation.")


# -------------------------------------------------------------
# Program Entry Point
# -------------------------------------------------------------

if __name__ == "__main__":
    main()
