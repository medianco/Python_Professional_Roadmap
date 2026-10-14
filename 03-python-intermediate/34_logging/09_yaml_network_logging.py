"""
Lesson 34.9 — YAML Network Logging

This script reads a network device inventory from YAML,
performs basic validation, and logs processing events.

Log destinations:
    1. Terminal: INFO and higher
    2. Log file: DEBUG and higher

This is a simulated inventory-processing exercise.
It does not establish real network connections.
"""

import logging
from pathlib import Path

import yaml


# ---------------------------------------------------------
# 1. Define Project Paths
# ---------------------------------------------------------
# Keep inventory data separate from application logic.
# Path objects make file and directory handling clearer.

BASE_DIR = Path(__file__).resolve().parent

INVENTORY_FILE = BASE_DIR / "data" / "network_devices.yaml"
OUTPUT_DIR = BASE_DIR / "output"
LOG_FILE = OUTPUT_DIR / "network_automation.log"

# Create the output directory if it does not exist.
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------
# 2. Configure the Logger
# ---------------------------------------------------------
# Use a dedicated logger for YAML inventory processing.

logger = logging.getLogger("network_automation.yaml")
logger.setLevel(logging.DEBUG)

# Prevent duplicate handlers if this setup is reused
# in the same Python process.
if not logger.handlers:
    # Display INFO and higher messages in the terminal.
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Persist DEBUG and higher messages in the log file.
    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)

    # Keep terminal output concise.
    console_handler.setFormatter(
        logging.Formatter(
            "%(levelname)s | %(name)s | %(message)s"
        )
    )

    # Include timestamps in the persistent log.
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)s | "
            "%(name)s | %(message)s"
        )
    )

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


# ---------------------------------------------------------
# 3. Load the YAML Inventory
# ---------------------------------------------------------
def load_inventory(file_path: Path) -> dict:
    """Load YAML inventory and validate its basic structure.

    Raises:
        FileNotFoundError: If the inventory file is missing.
        yaml.YAMLError: If the YAML document is malformed.
        ValueError: If the document has an unexpected structure.
    """

    logger.info("Loading inventory from %s", file_path)

    # Open the YAML file using UTF-8 encoding.
    with file_path.open("r", encoding="utf-8") as file:
        # safe_load avoids constructing arbitrary Python objects.
        inventory = yaml.safe_load(file)

    # An empty YAML file produces None.
    if not isinstance(inventory, dict):
        raise ValueError(
            "Inventory root must be a YAML mapping."
        )

    # Verify that the expected devices collection exists.
    devices = inventory.get("devices")

    if not isinstance(devices, list):
        raise ValueError(
            "Inventory must contain a 'devices' list."
        )

    logger.info(
        "Inventory loaded successfully. Device records: %d",
        len(devices),
    )

    return inventory


# ---------------------------------------------------------
# 4. Process Each Device
# ---------------------------------------------------------
def process_device(device: object) -> bool:
    """Validate and simulate processing one device record.

    Returns:
        True if the record was processed, otherwise False.
    """

    # Each device record should be a mapping.
    if not isinstance(device, dict):
        logger.error(
            "Invalid device record: expected a mapping."
        )
        return False

    hostname = device.get("hostname", "UNKNOWN")

    logger.debug(
        "Starting inventory processing for %s",
        hostname,
    )

    # Check the required management information.
    management = device.get("management")

    if not isinstance(management, dict):
        logger.error(
            "%s: missing or invalid management section",
            hostname,
        )
        return False

    management_ip = management.get("ip")
    protocol = management.get("protocol")

    if not management_ip or not protocol:
        logger.error(
            "%s: management IP or protocol is missing",
            hostname,
        )
        return False

    # Skip devices that are not marked active.
    if device.get("status") != "active":
        logger.warning(
            "%s: device is not active; skipping",
            hostname,
        )
        return False

    # This exercise records inventory processing only.
    # No SSH, API, or other connection is attempted.
    logger.info(
        "%s: inventory record processed successfully "
        "(IP=%s, protocol=%s)",
        hostname,
        management_ip,
        protocol,
    )

    logger.debug(
        "%s: processing completed",
        hostname,
    )

    return True


# ---------------------------------------------------------
# 5. Run the Inventory Processing Job
# ---------------------------------------------------------
def main() -> None:
    """Load the inventory and process all device records."""

    logger.info("YAML Network Automation job started.")

    try:
        inventory = load_inventory(INVENTORY_FILE)

    except FileNotFoundError:
        # Log the exception and its traceback for diagnosis.
        logger.exception(
            "Inventory file was not found: %s",
            INVENTORY_FILE,
        )
        return

    except yaml.YAMLError:
        logger.exception(
            "Failed to parse the YAML inventory."
        )
        return

    except ValueError:
        logger.exception(
            "Inventory structure validation failed."
        )
        return

    successful = 0
    unsuccessful = 0

    for device in inventory["devices"]:
        if process_device(device):
            successful += 1
        else:
            unsuccessful += 1

    logger.info(
        "Job completed. Successful: %d | Unsuccessful: %d",
        successful,
        unsuccessful,
    )


# ---------------------------------------------------------
# 6. Program Entry Point
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
