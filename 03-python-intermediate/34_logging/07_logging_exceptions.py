"""
Lesson 34.7 — Logging Exceptions

This script demonstrates how to handle exceptions
and record useful diagnostic information using logging.

Network Automation example:
A script attempts to retrieve information from a device.
If an error occurs, the exception is logged with its traceback.
"""

import logging


# ---------------------------------------------------------
# 1. Configure the Logger
# ---------------------------------------------------------
# basicConfig is sufficient for this introductory example.
# DEBUG allows all standard logging levels to be recorded.
# The format includes the timestamp, level, and message.

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

# Create a module-level logger for this script.
logger = logging.getLogger(__name__)


# ---------------------------------------------------------
# 2. Simulate a Network Device Operation
# ---------------------------------------------------------
def get_device_info(hostname: str) -> dict[str, str]:
    """Return simulated device information.

    Raises:
        ConnectionError: If the simulated device is unreachable.
    """

    logger.info("Attempting to retrieve information from %s", hostname)

    # Simulate a connection failure for this demonstration.
    raise ConnectionError(
        f"Unable to connect to device {hostname}"
    )


# ---------------------------------------------------------
# 3. Handle and Log the Exception
# ---------------------------------------------------------
def main() -> None:
    """Run the demonstration and handle the connection error."""

    hostname = "R1"

    try:
        # Attempt to retrieve information from the device.
        device_info = get_device_info(hostname)

        # This line executes only if the operation succeeds.
        logger.info("Device information: %s", device_info)

    except ConnectionError:
        # logger.exception records the message and traceback.
        # Use it inside an except block to capture the active
        # exception's diagnostic information.
        logger.exception(
            "Network operation failed for %s",
            hostname,
        )

    logger.info("Network Automation script finished.")


# ---------------------------------------------------------
# 4. Run the Program
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
