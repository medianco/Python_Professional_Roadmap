
"""
Lesson 36.3 — Counter for Network Log Analysis

Load network logs from an external JSON file and analyze
event frequencies by type, hostname, and severity.
"""

import json
import logging
from collections import Counter
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

    # Read and deserialize the external JSON data.
    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    # Ensure the top-level JSON structure is a list.
    if not isinstance(data, list):
        raise ValueError("The JSON file must contain a list of log records.")

    # Validate that each record is a dictionary.
    if not all(isinstance(record, dict) for record in data):
        raise ValueError("Every log record must be a JSON object.")

    logging.info("Loaded %d log records from %s", len(data), file_path)
    return data


def analyze_network_logs(logs: list[dict[str, Any]]) -> None:
    """Analyze network log frequencies using Counter."""

    required_fields = {"hostname", "event_type", "severity"}
    valid_logs: list[dict[str, str]] = []

    # Validate each record before accessing its fields.
    for index, log in enumerate(logs, start=1):
        if not required_fields.issubset(log):
            logging.warning("Record %d is missing required fields.", index)
            continue

        if not all(
            isinstance(log[field], str) and log[field].strip()
            for field in required_fields
        ):
            logging.warning("Record %d contains invalid field values.", index)
            continue

        valid_logs.append({
            "hostname": log["hostname"].strip(),
            "event_type": log["event_type"].strip(),
            "severity": log["severity"].strip().upper(),
        })

    if not valid_logs:
        logging.warning("No valid log records were available for analysis.")
        return

    # Count events by type, hostname, and severity.
    event_type_counts = Counter(
        log["event_type"] for log in valid_logs
    )
    hostname_counts = Counter(
        log["hostname"] for log in valid_logs
    )
    severity_counts = Counter(
        log["severity"] for log in valid_logs
    )

    print("\n1. Event Counts by Type")
    print("-" * 45)

    for event_type, count in event_type_counts.most_common():
        print(f"{event_type}: {count}")

    print("\n2. Event Counts by Device")
    print("-" * 45)

    for hostname, count in hostname_counts.most_common():
        print(f"{hostname}: {count}")

    print("\n3. Event Counts by Severity")
    print("-" * 45)

    for severity, count in severity_counts.most_common():
        print(f"{severity}: {count}")

    # Report all event types tied for the highest frequency.
    highest_count = max(event_type_counts.values())

    print("\n4. Most Frequent Event Types")
    print("-" * 45)

    for event_type, count in sorted(event_type_counts.items()):
        if count == highest_count:
            print(f"{event_type}: {count}")

    # Count events classified as high severity.
    high_severity_levels = {"CRITICAL", "HIGH"}
    high_severity_count = sum(
        severity_counts[level] for level in high_severity_levels
    )

    print("\n5. Analysis Summary")
    print("-" * 45)
    print(f"Total records: {len(logs)}")
    print(f"Valid records: {len(valid_logs)}")
    print(f"Invalid records: {len(logs) - len(valid_logs)}")
    print(f"High-severity events: {high_severity_count}")


def main() -> None:
    """Load and analyze network logs."""

    configure_logging()

    # Resolve the data file relative to this Python script.
    project_dir = Path(__file__).resolve().parent
    data_file = project_dir / "data" / "network_logs.json"

    try:
        network_logs = load_network_logs(data_file)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        logging.error("Unable to load network logs: %s", error)
        return

    analyze_network_logs(network_logs)


# Run the analysis when this file is executed directly.
if __name__ == "__main__":
    main()
