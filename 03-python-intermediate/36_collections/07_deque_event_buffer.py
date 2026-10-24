
"""
Lesson 36.7 — deque Event Buffer

Load network events from JSON and retain only the latest events.
"""

import json
import logging
from collections import Counter, deque
from pathlib import Path
from typing import Any


BUFFER_SIZE = 5


def configure_logging() -> None:
    """Configure application logging."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(message)s",
    )


def load_network_logs(file_path: Path) -> list[dict[str, Any]]:
    """Load network events from a JSON file."""

    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("The JSON file must contain a list.")

    if not all(isinstance(record, dict) for record in data):
        raise ValueError("Every log record must be a JSON object.")

    return data


def validate_event(event: dict[str, Any]) -> bool:
    """Check whether an event has the required fields."""

    required_fields = {"hostname", "event_type", "severity"}

    if not required_fields.issubset(event):
        return False

    return all(
        isinstance(event[field], str) and event[field].strip()
        for field in required_fields
    )


def build_event_buffer(
    logs: list[dict[str, Any]],
    max_events: int,
) -> deque[dict[str, str]]:
    """Keep only the most recent valid events."""

    if max_events < 1:
        raise ValueError("max_events must be greater than zero.")

    # Automatically discard the oldest event when the buffer is full.
    event_buffer: deque[dict[str, str]] = deque(maxlen=max_events)

    for index, event in enumerate(logs, start=1):
        if not validate_event(event):
            logging.warning("Skipping invalid event record %d.", index)
            continue

        event_buffer.append({
            "hostname": event["hostname"].strip(),
            "event_type": event["event_type"].strip(),
            "severity": event["severity"].strip().upper(),
        })

    return event_buffer


def display_event_buffer(
    event_buffer: deque[dict[str, str]],
) -> None:
    """Display the retained events from oldest to newest."""

    print(f"\nRecent Network Events (last {event_buffer.maxlen})")
    print("=" * 60)

    for index, event in enumerate(event_buffer, start=1):
        print(
            f"{index}. {event['hostname']} | "
            f"{event['event_type']} | "
            f"{event['severity']}"
        )

    print("-" * 60)
    print(f"Events currently retained: {len(event_buffer)}")


def display_severity_summary(
    event_buffer: deque[dict[str, str]],
) -> None:
    """Count severity levels in the retained events only."""

    severity_counts = Counter(
        event["severity"] for event in event_buffer
    )

    print("\nSeverity Summary for Retained Events")
    print("=" * 40)

    for severity, count in sorted(severity_counts.items()):
        print(f"{severity}: {count}")


def main() -> None:
    """Load network logs and analyze the bounded event buffer."""

    configure_logging()

    project_dir = Path(__file__).resolve().parent
    data_file = project_dir / "data" / "network_logs.json"

    try:
        network_logs = load_network_logs(data_file)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        logging.error("Unable to load network logs: %s", error)
        return

    event_buffer = build_event_buffer(network_logs, BUFFER_SIZE)

    print(f"Total records loaded: {len(network_logs)}")
    display_event_buffer(event_buffer)
    display_severity_summary(event_buffer)


if __name__ == "__main__":
    main()
