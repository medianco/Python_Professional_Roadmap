
"""
Lesson 35.7 — Unix Timestamps

Learn how to convert between Unix timestamps and datetime objects.
"""

import logging
from datetime import datetime, timezone


def main() -> None:
    """Demonstrate Unix timestamp conversions."""

    # Configure logging for timestamp processing.
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(message)s",
    )
    logger = logging.getLogger("unix_timestamps")

    # Create a timezone-aware datetime in UTC.
    event_datetime = datetime(
        2026, 10, 15, 0, 0, 0,
        tzinfo=timezone.utc,
    )

    # Convert the datetime object into a Unix timestamp.
    unix_timestamp = event_datetime.timestamp()

    print("Datetime to Unix timestamp:")
    print(f"Datetime:  {event_datetime}")
    print(f"Timestamp: {unix_timestamp}")

    # Convert the Unix timestamp back into a UTC datetime object.
    converted_datetime = datetime.fromtimestamp(
        unix_timestamp,
        tz=timezone.utc,
    )

    print("\nUnix timestamp to UTC datetime:")
    print(converted_datetime)

    # Retrieve the current Unix timestamp.
    current_timestamp = datetime.now(timezone.utc).timestamp()

    print("\nCurrent Unix timestamp:")
    print(current_timestamp)

    # Simulate a timestamp received from a monitoring API.
    api_timestamp = 1792022400

    # Convert the API timestamp into a readable UTC datetime.
    api_datetime = datetime.fromtimestamp(
        api_timestamp,
        tz=timezone.utc,
    )

    print("\nMonitoring API event:")
    print(f"Unix timestamp: {api_timestamp}")
    print(f"UTC datetime:   {api_datetime.isoformat()}")

    logger.info("Unix timestamp conversion completed successfully.")


# Execute main() only when this file is run directly.
if __name__ == "__main__":
    main()
