"""
Lesson 34.8 — Network Device Logging

This script demonstrates how to log events while
processing multiple network devices.

The example simulates device operations. It does not
connect to real network devices.

Logging destinations:
    1. Terminal
    2. output/network_automation.log
    
    Network Automation
        │
        ▼
   Device Manager
        │
        ├── R1 — 192.168.1.1
        ├── R2 — 192.168.1.2
        └── SW1 — 192.168.1.10
                │
                ▼
             Logging
                │
        ┌───────┴────────┐
        ▼                ▼
     Terminal       application.log
"""

import logging
from pathlib import Path


# ---------------------------------------------------------
# 1. Define the Output Directory and Log File
# ---------------------------------------------------------
# Path provides a convenient way to work with file paths.
# The directory is created automatically if it is missing.

OUTPUT_DIR = Path("output")
LOG_FILE = OUTPUT_DIR / "network_automation.log"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------
# 2. Create the Logger
# ---------------------------------------------------------
# Use a descriptive name for this application component.

logger = logging.getLogger("network_automation.devices")
logger.setLevel(logging.DEBUG)

# Avoid adding duplicate handlers if this setup function
# is reused in the same Python process.
if not logger.handlers:
    # Send INFO and higher messages to the terminal.
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Store DEBUG and higher messages in the log file.
    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)

    # Use a concise format for the terminal.
    console_handler.setFormatter(
        logging.Formatter(
            "%(levelname)s | %(name)s | %(message)s"
        )
    )

    # Include timestamps in the persistent log file.
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)s | "
            "%(name)s | %(message)s"
        )
    )

    # Attach both destinations to the logger.
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


# ---------------------------------------------------------
# 3. Define Sample Network Devices
# ---------------------------------------------------------
# These are sample inventory records, not live devices.

devices = [
    {"hostname": "R1", "management_ip": "192.168.1.1"},
    {"hostname": "R2", "management_ip": "192.168.1.2"},
    {"hostname": "SW1", "management_ip": "192.168.1.10"},
]


# ---------------------------------------------------------
# 4. Simulate Device Processing
# ---------------------------------------------------------
def process_device(device: dict[str, str]) -> None:
    """Simulate processing a network device and log its events."""

    hostname = device["hostname"]
    management_ip = device["management_ip"]

    logger.info(
        "Starting device processing: %s (%s)",
        hostname,
        management_ip,
    )

    # Simulate a diagnostic step.
    logger.debug(
        "Checking inventory data for %s",
        hostname,
    )

    # Simulate a successful operation.
    logger.info(
        "Device processing completed successfully: %s",
        hostname,
    )


# ---------------------------------------------------------
# 5. Process All Devices
# ---------------------------------------------------------
def main() -> None:
    """Process every device in the sample inventory."""

    logger.info(
        "Network Automation job started. Devices: %d",
        len(devices),
    )

    for device in devices:
        process_device(device)

    logger.info("Network Automation job completed.")


# ---------------------------------------------------------
# 6. Program Entry Point
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
