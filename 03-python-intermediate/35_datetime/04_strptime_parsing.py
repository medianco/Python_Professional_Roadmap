
"""
Lesson 35.4 — Parsing Date Strings with strptime()

Learn how to convert date strings into datetime objects
and handle invalid date input safely.
"""

import logging
from datetime import datetime
from pathlib import Path


def configure_logger() -> logging.Logger:
    """Configure console logging for the parsing example."""

    # Create a named logger for this lesson.
    logger = logging.getLogger("datetime_parsing")
    logger.setLevel(logging.INFO)

    # Add a handler only if one has not already been configured.
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )
        )
        logger.addHandler(handler)

    return logger


def parse_timestamp(
    timestamp_text: str,
    timestamp_format: str,
) -> datetime:
    """Parse a timestamp string using the specified format."""

    # Convert the input string into a datetime object.
    return datetime.strptime(timestamp_text, timestamp_format)


def main() -> None:
    """Demonstrate timestamp parsing and error handling."""

    logger = configure_logger()

    # Define a timestamp received from a hypothetical monitoring system.
    timestamp_text = "2026-10-15 09:45:30"
    timestamp_format = "%Y-%m-%d %H:%M:%S"

    try:
        # Parse the timestamp using the matching format.
        parsed_datetime = parse_timestamp(
            timestamp_text,
            timestamp_format,
        )

        logger.info("Timestamp parsed successfully.")
        print(f"Original string: {timestamp_text}")
        print(f"Parsed datetime: {parsed_datetime}")
        print(f"Data type: {type(parsed_datetime).__name__}")

    except ValueError:
        # Log the failure without exposing unnecessary internal details.
        logger.exception("Failed to parse the timestamp.")

    # Demonstrate how invalid date input is handled.
    invalid_timestamp = "2026-02-30 12:00:00"

    try:
        parse_timestamp(invalid_timestamp, timestamp_format)
    except ValueError:
        logger.warning(
            "Rejected invalid timestamp: %s",
            invalid_timestamp,
        )


# Execute main() only when this file is run directly.
if __name__ == "__main__":
    main()
