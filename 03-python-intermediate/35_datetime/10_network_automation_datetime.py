"""
Lesson 35.10 — Network Automation Datetime

Analyze network events using datetime, timedelta, UTC,
validation, and logging.
"""

import logging
from datetime import datetime, timedelta, timezone


def configure_logging() -> None:
    """Configure application logging."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(message)s",
    )


def parse_utc_timestamp(timestamp: str) -> datetime | None:
    """Parse an ISO 8601 timestamp and normalize it to UTC."""

    try:
        # Parse the ISO 8601 timestamp, including its timezone offset.
        parsed_datetime = datetime.fromisoformat(timestamp)

        # Reject naive timestamps because their timezone is unknown.
        if parsed_datetime.tzinfo is None:
            logging.error(
                "Timestamp has no timezone information: %s",
                timestamp,
            )
            return None

        # Normalize timestamps from different zones to UTC.
        return parsed_datetime.astimezone(timezone.utc)

    except (ValueError, TypeError) as error:
        # Log malformed timestamps without stopping event processing.
        logging.error(
            "Unable to parse timestamp %r: %s",
            timestamp,
            error,
        )
        return None


def analyze_events(events: list[dict[str, str]]) -> None:
    """Sort network events and calculate available outage durations."""

    valid_events: list[dict[str, str | datetime]] = []

    # Validate each event and retain its normalized UTC timestamp.
    for event in events:
        event_time = parse_utc_timestamp(event.get("timestamp", ""))

        if event_time is None:
            continue

        valid_events.append(
            {
                "device": event["device"],
                "event": event["event"],
                "timestamp": event["timestamp"],
                "utc_datetime": event_time,
            }
        )

    # Sort all valid events by their UTC datetime.
    valid_events.sort(key=lambda event: event["utc_datetime"])

    print("\nNETWORK EVENT TIMELINE")
    print("=" * 72)

    for event in valid_events:
        event_time = event["utc_datetime"]

        # Display a consistent timestamp format for every event.
        print(
            f"{event_time.isoformat()} | "
            f"{event['device']:5} | {event['event']}"
        )

    # Identify the oldest and newest valid events.
    if valid_events:
        oldest_event = valid_events[0]
        newest_event = valid_events[-1]

        oldest_time = oldest_event["utc_datetime"]
        newest_time = newest_event["utc_datetime"]

        print("\nEVENT SUMMARY")
        print("-" * 40)
        print(f"Valid events: {len(valid_events)}")
        print(f"Oldest event: {oldest_time.isoformat()}")
        print(f"Newest event: {newest_time.isoformat()}")
        print(f"Time span:    {newest_time - oldest_time}")

    # Track outages independently for each device.
    outage_started: dict[str, datetime] = {}

    print("\nOUTAGE ANALYSIS")
    print("-" * 40)

    for event in valid_events:
        device = str(event["device"])
        event_type = str(event["event"])
        event_time = event["utc_datetime"]

        if event_type == "DOWN":
            if device in outage_started:
                logging.warning(
                    "%s reported DOWN again before recovery; "
                    "keeping the original outage start.",
                    device,
                )
            else:
                outage_started[device] = event_time
                print(
                    f"{device}: outage started at "
                    f"{event_time.isoformat()}"
                )

        elif event_type == "UP":
            start_time = outage_started.pop(device, None)

            if start_time is None:
                logging.warning(
                    "%s reported UP without a matching DOWN event.",
                    device,
                )
                continue

            # Calculate downtime using timezone-aware datetime objects.
            downtime = event_time - start_time

            print(
                f"{device}: recovered at {event_time.isoformat()} "
                f"| Downtime: {downtime}"
            )

    # Report outages that do not yet have a recovery event.
    if outage_started:
        print("\nUNRESOLVED OUTAGES")
        print("-" * 40)

        for device, start_time in sorted(outage_started.items()):
            print(
                f"{device}: still awaiting recovery event; "
                f"started at {start_time.isoformat()}"
            )

    # Flag monitoring records older than the configured threshold.
    monitoring_time = datetime(
        2026, 10, 15, 12, 0, 0,
        tzinfo=timezone.utc,
    )
    stale_threshold = timedelta(minutes=15)

    print("\nMONITORING FRESHNESS")
    print("-" * 40)

    for event in valid_events:
        if event["event"] != "HEARTBEAT":
            continue

        event_time = event["utc_datetime"]
        age = monitoring_time - event_time

        if age < timedelta(0):
            logging.warning(
                "%s has a heartbeat later than the reference time.",
                event["device"],
            )
        elif age > stale_threshold:
            print(
                f"STALE: {event['device']} last heartbeat was "
                f"{age} ago."
            )
        else:
            print(
                f"OK: {event['device']} heartbeat age is {age}."
            )


def main() -> None:
    """Run the network event analysis."""

    configure_logging()

    # Use fixed, timezone-aware timestamps for a reproducible exercise.
    network_events: list[dict[str, str]] = [
        {
            "device": "R1",
            "event": "DOWN",
            "timestamp": "2026-10-15T09:00:00+00:00",
        },
        {
            "device": "R1",
            "event": "UP",
            "timestamp": "2026-10-15T09:12:30+00:00",
        },
        {
            "device": "SW1",
            "event": "DOWN",
            "timestamp": "2026-10-15T11:20:00+03:00",
        },
        {
            "device": "FW1",
            "event": "HEARTBEAT",
            "timestamp": "2026-10-15T11:40:00+03:00",
        },
        {
            "device": "R2",
            "event": "HEARTBEAT",
            "timestamp": "2026-10-15T11:55:00+03:00",
        },
        {
            "device": "R2",
            "event": "HEARTBEAT",
            "timestamp": "2026-10-15T12:05:00+03:00",
        },
        {
            "device": "R3",
            "event": "UP",
            "timestamp": "invalid-timestamp",
        },
    ]

    logging.info("Network event analysis started.")

    analyze_events(network_events)

    logging.info("Network event analysis completed.")


# Execute main() only when this file is run directly.
if __name__ == "__main__":
    main()
