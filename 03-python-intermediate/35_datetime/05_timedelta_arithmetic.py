
"""
Lesson 35.5 — Date Arithmetic with timedelta

Learn how to calculate time differences and manipulate dates.
"""

import logging
from datetime import datetime, timedelta


def main() -> None:
    """Demonstrate timedelta operations using network examples."""

    # Configure logging to display informational messages.
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(message)s",
    )
    logger = logging.getLogger("network_timing")

    # Define the timestamps of a simulated network outage.
    device_down = datetime(2026, 10, 15, 10, 0, 0)
    device_up = datetime(2026, 10, 15, 10, 15, 30)

    # Calculate the duration between the down and up events.
    downtime = device_up - device_down

    print("Network outage analysis:")
    print(f"Device down at: {device_down}")
    print(f"Device up at:   {device_up}")
    print(f"Downtime:       {downtime}")
    print(f"Total seconds:  {downtime.total_seconds()}")

    logger.info("Device outage duration calculated.")

    # Calculate a future time by adding a duration.
    current_time = datetime.now()
    next_check = current_time + timedelta(minutes=15)

    print("\nScheduled monitoring:")
    print(f"Current time: {current_time}")
    print(f"Next check:   {next_check}")

    # Calculate an earlier time by subtracting a duration.
    previous_check = current_time - timedelta(hours=1)

    print(f"Previous check: {previous_check}")

    # Calculate a future date using a duration of several days.
    maintenance_date = datetime(2026, 10, 20, 22, 0, 0)
    reminder_date = maintenance_date - timedelta(days=3)

    print("\nMaintenance planning:")
    print(f"Maintenance: {maintenance_date}")
    print(f"Reminder:    {reminder_date}")


# Execute main() only when this file is run directly.
if __name__ == "__main__":
    main()
