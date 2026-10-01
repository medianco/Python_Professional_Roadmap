"""
Lesson 33.9 — YAML Validation

This script demonstrates how to validate network device
information loaded from a YAML inventory.

The validation process checks:

1. YAML root structure.
2. Device list structure.
3. Required device fields.
4. Management information.
5. IP address validity.
6. Management protocol.
7. Device status.

The goal is to prevent invalid inventory data from
reaching a Network Automation workflow.
"""

from ipaddress import ip_address
from pathlib import Path

import yaml


# ---------------------------------------------------------
# 1. Define the YAML inventory path
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "data" / "network_devices.yaml"


# ---------------------------------------------------------
# 2. Load YAML inventory
# ---------------------------------------------------------

def load_inventory(file_path: Path) -> dict:
    """
    Load and parse the YAML inventory.

    Args:
        file_path: Path to the YAML inventory.

    Returns:
        Parsed YAML data as a dictionary.

    Raises:
        FileNotFoundError:
            If the YAML file does not exist.

        ValueError:
            If the YAML root is not a dictionary.
    """

    # Make sure the inventory file exists.
    if not file_path.exists():
        raise FileNotFoundError(
            f"Inventory file not found: {file_path}"
        )

    # Open the YAML file safely.
    with file_path.open("r", encoding="utf-8") as file:

        # Convert YAML into Python objects.
        inventory = yaml.safe_load(file)

    # The root structure must be a dictionary.
    if not isinstance(inventory, dict):
        raise ValueError(
            "Invalid inventory: root must be a dictionary."
        )

    return inventory


# ---------------------------------------------------------
# 3. Validate a single device
# ---------------------------------------------------------

def validate_device(device: dict) -> list[str]:
    """
    Validate a single network device.

    Args:
        device: Network device dictionary.

    Returns:
        A list containing validation errors.
        An empty list means the device is valid.
    """

    errors = []

    # -----------------------------------------------------
    # Required top-level fields
    # -----------------------------------------------------

    required_fields = [
        "hostname",
        "management",
        "platform",
        "status",
    ]

    for field in required_fields:

        if field not in device:
            errors.append(
                f"Missing required field: {field}"
            )

    # If required structures are missing, stop deeper validation.
    if errors:
        return errors

    # -----------------------------------------------------
    # Validate hostname
    # -----------------------------------------------------

    hostname = device.get("hostname")

    if not isinstance(hostname, str) or not hostname.strip():
        errors.append(
            "Hostname must be a non-empty string."
        )

    # -----------------------------------------------------
    # Validate management section
    # -----------------------------------------------------

    management = device.get("management")

    if not isinstance(management, dict):
        errors.append(
            "Management information must be a dictionary."
        )
        return errors

    # Required management fields.
    management_required_fields = [
        "ip",
        "protocol",
        "port",
    ]

    for field in management_required_fields:

        if field not in management:
            errors.append(
                f"Missing management field: {field}"
            )

    # -----------------------------------------------------
    # Validate IP address
    # -----------------------------------------------------

    ip_value = management.get("ip")

    if ip_value:

        try:
            # ip_address() validates both IPv4 and IPv6.
            ip_address(ip_value)

        except ValueError:
            errors.append(
                f"Invalid IP address: {ip_value}"
            )

    else:
        errors.append(
            "Management IP address is required."
        )

    # -----------------------------------------------------
    # Validate protocol
    # -----------------------------------------------------

    protocol = management.get("protocol")

    allowed_protocols = {
        "ssh",
        "https",
    }

    if protocol not in allowed_protocols:
        errors.append(
            f"Unsupported management protocol: {protocol}"
        )

    # -----------------------------------------------------
    # Validate port
    # -----------------------------------------------------

    port = management.get("port")

    if not isinstance(port, int):
        errors.append(
            "Management port must be an integer."
        )

    elif not 1 <= port <= 65535:
        errors.append(
            f"Invalid port number: {port}"
        )

    # -----------------------------------------------------
    # Validate platform information
    # -----------------------------------------------------

    platform = device.get("platform")

    if not isinstance(platform, dict):
        errors.append(
            "Platform information must be a dictionary."
        )

    else:

        platform_required_fields = [
            "vendor",
            "device_type",
            "os",
        ]

        for field in platform_required_fields:

            if field not in platform:
                errors.append(
                    f"Missing platform field: {field}"
                )

    # -----------------------------------------------------
    # Validate device status
    # -----------------------------------------------------

    status = device.get("status")

    allowed_statuses = {
        "active",
        "inactive",
        "maintenance",
    }

    if status not in allowed_statuses:
        errors.append(
            f"Invalid device status: {status}"
        )

    return errors


# ---------------------------------------------------------
# 4. Validate the complete inventory
# ---------------------------------------------------------

def validate_inventory(inventory: dict) -> tuple[list, list]:
    """
    Validate all devices in the inventory.

    Args:
        inventory: Parsed YAML inventory.

    Returns:
        A tuple containing:
        - valid devices
        - invalid devices
    """

    devices = inventory.get("devices")

    # The devices section must be a list.
    if not isinstance(devices, list):
        raise ValueError(
            "Invalid inventory: 'devices' must be a list."
        )

    valid_devices = []
    invalid_devices = []

    # Validate each device independently.
    for device in devices:

        # Each device must be a dictionary.
        if not isinstance(device, dict):

            invalid_devices.append(
                {
                    "device": device,
                    "errors": [
                        "Device entry must be a dictionary."
                    ],
                }
            )

            continue

        errors = validate_device(device)

        if errors:
            invalid_devices.append(
                {
                    "device": device,
                    "errors": errors,
                }
            )

        else:
            valid_devices.append(device)

    return valid_devices, invalid_devices


# ---------------------------------------------------------
# 5. Display validation results
# ---------------------------------------------------------

def display_results(
    valid_devices: list,
    invalid_devices: list,
) -> None:
    """
    Display validation results.

    Args:
        valid_devices: Devices that passed validation.
        invalid_devices: Devices that failed validation.
    """

    print("\n=== YAML Validation Results ===")

    # -----------------------------------------------------
    # Valid devices
    # -----------------------------------------------------

    print("\n=== Valid Devices ===")

    for device in valid_devices:

        hostname = device["hostname"]
        ip = device["management"]["ip"]

        print(
            f"{hostname} | {ip} | VALID"
        )

    # -----------------------------------------------------
    # Invalid devices
    # -----------------------------------------------------

    print("\n=== Invalid Devices ===")

    if not invalid_devices:

        print("No invalid devices found.")

    else:

        for item in invalid_devices:

            device = item["device"]
            errors = item["errors"]

            hostname = (
                device.get("hostname", "UNKNOWN")
                if isinstance(device, dict)
                else "UNKNOWN"
            )

            print(f"\nDevice: {hostname}")

            for error in errors:

                print(f"  - {error}")

    # -----------------------------------------------------
    # Summary
    # -----------------------------------------------------

    print("\n=== Validation Summary ===")

    print(
        f"Valid devices: {len(valid_devices)}"
    )

    print(
        f"Invalid devices: {len(invalid_devices)}"
    )

    print(
        f"Total devices: "
        f"{len(valid_devices) + len(invalid_devices)}"
    )


# ---------------------------------------------------------
# 6. Main application
# ---------------------------------------------------------

def main() -> None:
    """
    Main application workflow.
    """

    print("=== YAML Network Device Validation ===")

    print(
        f"Inventory file: {DATA_FILE}"
    )

    # Load the YAML inventory.
    inventory = load_inventory(DATA_FILE)

    # Validate all devices.
    valid_devices, invalid_devices = validate_inventory(
        inventory
    )

    # Display the validation results.
    display_results(
        valid_devices,
        invalid_devices,
    )


# ---------------------------------------------------------
# 7. Python entry point
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
