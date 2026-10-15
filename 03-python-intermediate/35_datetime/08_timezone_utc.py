"""
Lesson 35.8 — Timezones and UTC

Learn how to work with timezone-aware datetime objects,
convert timestamps to UTC, and handle network events
from different time zones.
"""

import logging
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo


def main() -> None:
    """Demonstrate timezone handling for network automation."""

    # Configure logging for timezone conversion events.
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(message)s",
    )
    logger = logging.getLogger("timezone_utc")

    # Create a naive datetime without timezone information.
    naive_datetime = datetime(2026, 10, 15, 12, 0, 0)

    print("1. Naive datetime:")
    print(naive_datetime)
    print(f"Timezone information: {naive_datetime.tzinfo}")

    # Create a timezone-aware datetime using a fixed UTC+3 offset.
    utc_plus_three = timezone(timedelta(hours=3))
    local_datetime = datetime(
        2026, 10, 15, 12, 0, 0,
        tzinfo=utc_plus_three,
    )

    print("\n2. Timezone-aware datetime:")
    print(local_datetime)
    print(f"UTC offset: {local_datetime.utcoffset()}")

    # Convert the timezone-aware datetime to UTC.
    utc_datetime = local_datetime.astimezone(timezone.utc)

    print("\n3. Convert UTC+3 to UTC:")
    print(utc_datetime)

    # Use a named time zone for a location-based conversion.
    berlin_datetime = datetime(
        2026, 10, 15, 12, 0, 0,
        tzinfo=ZoneInfo("Europe/Berlin"),
    )

    berlin_utc = berlin_datetime.astimezone(timezone.utc)

    print("\n4. Named time zone — Europe/Berlin:")
    print(f"Berlin time: {berlin_datetime}")
    print(f"UTC time:    {berlin_utc}")

    # Convert a UTC event into another named time zone.
    utc_event = datetime(
        2026, 10, 15, 9, 0, 0,
        tzinfo=timezone.utc,
    )

    aden_event = utc_event.astimezone(ZoneInfo("Asia/Aden"))

    print("\n5. Convert a network event to Asia/Aden:")
    print(f"UTC event:  {utc_event}")
    print(f"Local event: {aden_event}")

    # Log a normalized timestamp for centralized monitoring.
    logger.info("Network event normalized to UTC: %s", utc_datetime.isoformat())
    logger.info("Named time zone conversion completed successfully.")


# Execute main() only when this file is run directly.
if __name__ == "__main__":
    main()
