
"""
Lesson 35.6 — Comparing Dates and Times

Learn how to compare, sort, and analyze network event timestamps.
"""

import logging
from datetime import datetime, timedelta


def main() -> None:
    """Demonstrate datetime comparisons with network monitoring data."""

    # Configure logging for monitoring results.
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(message)s",
    )
    logger = logging.getLogger("datetime_comparison")

    # Define sample timestamps for network events.
    events = [
        ("R1", datetime(2026, 10, 15, 10, 15, 0)),
        ("SW1", datetime(2026, 10, 15, 9, 45, 0)),
        ("FW1", datetime(2026, 10, 15, 10, 5, 0)),
        ("R2", datetime(2026, 10, 15, 9, 30, 0)),
    ]

    # Sort events by their datetime values, from oldest to newest.
    sorted_events = sorted(events, key=lambda event: event[1])

    print("Network events in chronological order:")

    for hostname, event_time in sorted_events:
        print(f"{event_time} | {hostname}")

    # Identify the oldest and newest events.
    oldest_event = min(events, key=lambda event: event[1])
    newest_event = max(events, key=lambda event: event[1])

    print("\nOldest event:")
    print(f"{oldest_event[0]} | {oldest_event[1]}")

    print("\nNewest event:")
    print(f"{newest_event[0]} | {newest_event[1]}")

    # Calculate the age of the latest monitoring record.
    reference_time = datetime(2026, 10, 15, 10, 20, 0)
    latest_event_time = newest_event[1]
    record_age = reference_time - latest_event_time

    print("\nLatest record age:")
    print(f"{record_age.total_seconds()} seconds")

    # Warn if the latest record is older than the allowed threshold.
    stale_threshold = timedelta(minutes=10)

    if record_age > stale_threshold:
        logger.warning("The latest monitoring record is stale.")
    else:
        logger.info("The latest monitoring record is within the threshold.")

    # Compare two timestamps directly.
    first_event = datetime(2026, 10, 15, 9, 30, 0)
    second_event = datetime(2026, 10, 15, 10, 30, 0)

    print("\nDirect comparison:")
    print(f"First event is earlier: {first_event < second_event}")


# Execute main() only when this file is run directly.
if __name__ == "__main__":
    main()
