"""
Lesson 35.9 — Datetime Error Handling

Learn how to validate timestamp strings, handle invalid
datetime values, and log errors without stopping processing.
"""

import logging
from datetime import datetime


def configure_logging() -> None:
    """Configure logging for timestamp validation."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(message)s",
    )


def parse_timestamp(timestamp_value: object) -> datetime | None:
    """Parse a timestamp string and return a datetime object."""

    # Reject values that are not strings before parsing.
    if not isinstance(timestamp_value, str):
        logging.error(
            "Invalid timestamp type: expected str, received %s",
            type(timestamp_value).__name__,
        )
        return None

    # Define the expected timestamp format.
    timestamp_format = "%Y-%m-%d %H:%M:%S"

    try:
        # Parse the string into a datetime object.
        parsed_datetime = datetime.strptime(
            timestamp_value,
            timestamp_format,
        )

        logging.info("Timestamp parsed successfully: %s", timestamp_value)
        return parsed_datetime

    except ValueError:
        # Handle malformed timestamps and impossible calendar dates.
        logging.error(
            "Invalid timestamp value: %r",
            timestamp_value,
        )
        return None


def main() -> None:
    """Validate a collection of network event timestamps."""

    configure_logging()

    # Simulate timestamps received from a monitoring system.
    network_events: list[object] = [
        "2026-10-15 08:30:00",
        "2026-10-15 09:45:00",
        "2026-02-30 12:00:00",
        "invalid-timestamp",
        None,
        1792051200,
        "2026-10-15 11:15:00",
    ]

    valid_events: list[datetime] = []
    invalid_count = 0

    print("Timestamp Validation Results")
    print("=" * 40)

    # Process each event independently so one invalid record
    # does not prevent the remaining records from being checked.
    for event_timestamp in network_events:
        parsed_event = parse_timestamp(event_timestamp)

        if parsed_event is None:
            invalid_count += 1
            continue

        valid_events.append(parsed_event)

    # Sort valid events chronologically.
    valid_events.sort()

    print("\nValid timestamps:")
    for event in valid_events:
        print(event)

    print("\nSummary:")
    print(f"Total records:   {len(network_events)}")
    print(f"Valid records:   {len(valid_events)}")
    print(f"Invalid records: {invalid_count}")


# Execute main() only when this file is run directly.
if __name__ == "__main__":
    main()
