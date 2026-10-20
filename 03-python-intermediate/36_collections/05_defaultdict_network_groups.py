
"""
Lesson 36.5 — defaultdict for Network Log Grouping

Load network logs from JSON and group events by severity.
"""

import json
import logging
from collections import defaultdict
from pathlib import Path
from typing import Any


def configure_logging() -> None:
    """Configure application logging."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(message)s",
    )


def load_network_logs(file_path: Path) -> list[dict[str, Any]]:
    """Load network log records from a JSON file."""

    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("The JSON file must contain a list.")

    if not all(isinstance(record, dict) for record in data):
        raise ValueError("Every log record must be a JSON object.")

    return data


def group_logs_by_severity(
    logs: list[dict[str, Any]],
) -> dict[str, list[dict[str, str]]]:
    """Group valid log records by severity."""

    # Create a list automatically for each severity level.
    severity_groups = defaultdict(list)

    required_fields = {"hostname", "event_type", "severity"}

    for index, log in enumerate(logs, start=1):
        # Skip records that do not contain all required fields.
        if not required_fields.issubset(log):
            logging.warning("Skipping record %d: missing fields.", index)
            continue

        # Validate that required values are non-empty strings.
        if not all(
            isinstance(log[field], str) and log[field].strip()
            for field in required_fields
        ):
            logging.warning("Skipping record %d: invalid values.", index)
            continue

        severity = log["severity"].strip().upper()

        # Add the normalized record to its severity group.
        severity_groups[severity].append({
            "hostname": log["hostname"].strip(),
            "event_type": log["event_type"].strip(),
            "severity": severity,
        })

    # Convert the result to a regular dictionary.
    return dict(severity_groups)


def display_severity_groups(
    groups: dict[str, list[dict[str, str]]],
) -> None:
    """Display grouped network events."""

    print("\nNetwork Events Grouped by Severity")
    print("=" * 50)

    # Display critical events first, followed by other severity levels.
    severity_order = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"]

    for severity in severity_order:
        events = groups.get(severity, [])

        if not events:
            continue

        print(f"\n{severity} — {len(events)} event(s)")
        print("-" * 50)

        for event in events:
            print(
                f"{event['hostname']} | "
                f"{event['event_type']}"
            )

    # Display any severity levels not included in the preferred order.
    for severity, events in sorted(groups.items()):
        if severity not in severity_order:
            print(f"\n{severity} — {len(events)} event(s)")
            print("-" * 50)

            for event in events:
                print(
                    f"{event['hostname']} | "
                    f"{event['event_type']}"
                )


def main() -> None:
    """Load, group, and display network events."""

    configure_logging()

    project_dir = Path(__file__).resolve().parent
    data_file = project_dir / "data" / "network_logs.json"

    try:
        network_logs = load_network_logs(data_file)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        logging.error("Unable to load network logs: %s", error)
        return

    severity_groups = group_logs_by_severity(network_logs)
    display_severity_groups(severity_groups)

    total_grouped_events = sum(
        len(events) for events in severity_groups.values()
    )
    print(f"\nTotal grouped events: {total_grouped_events}")


if __name__ == "__main__":
    main()
