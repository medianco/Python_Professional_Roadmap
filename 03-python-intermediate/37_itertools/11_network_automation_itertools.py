"""
Lesson 37.11 — Network Automation with Itertools

Load external JSON data and analyze network inventory, events, and latency.
"""

import json
from itertools import accumulate, groupby, islice, pairwise
from operator import itemgetter
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DEVICES_FILE = DATA_DIR / "network_devices.json"
EVENTS_FILE = DATA_DIR / "network_events.json"


def load_json_data(file_path: Path) -> list[dict]:
    """Load a JSON file and validate that its top-level value is a list."""

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as error:
        raise FileNotFoundError(
            f"Required data file was not found: {file_path}"
        ) from error
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid JSON in data file: {file_path} "
            f"(line {error.lineno}, column {error.colno})"
        ) from error

    if not isinstance(data, list):
        raise ValueError(
            f"Expected a JSON list in data file: {file_path}"
        )

    if not all(isinstance(item, dict) for item in data):
        raise ValueError(
            f"Every item in the JSON list must be an object: {file_path}"
        )

    return data


def validate_devices(devices: list[dict]) -> None:
    """Validate required fields in each device record."""

    required_fields = {"hostname", "vendor", "enabled"}

    for index, device in enumerate(devices, start=1):
        missing_fields = required_fields - device.keys()

        if missing_fields:
            missing = ", ".join(sorted(missing_fields))
            raise ValueError(
                f"Device record {index} is missing required fields: {missing}"
            )

        if not isinstance(device["enabled"], bool):
            raise ValueError(
                f"Device record {index} has a non-boolean 'enabled' value"
            )


def validate_events(events: list[dict]) -> None:
    """Validate required fields in each network event record."""

    required_fields = {"device", "event_type", "severity"}

    for index, event in enumerate(events, start=1):
        missing_fields = required_fields - event.keys()

        if missing_fields:
            missing = ", ".join(sorted(missing_fields))
            raise ValueError(
                f"Event record {index} is missing required fields: {missing}"
            )


def analyze_inventory(devices: list[dict]) -> None:
    """Display enabled devices and vendor distribution."""

    print("1. NETWORK INVENTORY")
    print("=" * 60)

    enabled_devices = [
        device for device in devices if device["enabled"]
    ]

    for device in enabled_devices:
        print(f"{device['hostname']:<10} | {device['vendor']}")

    print(f"Total devices: {len(devices)}")
    print(f"Enabled devices: {len(enabled_devices)}")

    sorted_devices = sorted(enabled_devices, key=itemgetter("vendor"))

    print("\nEnabled devices by vendor:")

    for vendor, group in groupby(
        sorted_devices,
        key=itemgetter("vendor"),
    ):
        vendor_devices = list(group)
        hostnames = [device["hostname"] for device in vendor_devices]
        print(
            f"{vendor}: {len(hostnames)} device(s) "
            f"({', '.join(hostnames)})"
        )


def analyze_events(events: list[dict]) -> None:
    """Summarize events and identify critical incidents."""

    print("\n2. NETWORK EVENT ANALYSIS")
    print("=" * 60)

    critical_events = list(
        islice(
            (
                event
                for event in events
                if event["severity"] == "CRITICAL"
            ),
            10,
        )
    )

    print(f"Total events: {len(events)}")
    print(f"Critical events: {len(critical_events)}")

    for event in critical_events:
        print(
            f"CRITICAL | {event['device']} | "
            f"{event['event_type']}"
        )

    sorted_events = sorted(events, key=itemgetter("event_type"))

    print("\nEvents grouped by type:")

    for event_type, group in groupby(
        sorted_events,
        key=itemgetter("event_type"),
    ):
        grouped_events = list(group)
        affected_devices = [event["device"] for event in grouped_events]
        print(
            f"{event_type}: {len(grouped_events)} event(s) | "
            f"Devices: {', '.join(affected_devices)}"
        )


def analyze_latency() -> None:
    """Analyze latency changes and running maximum."""

    print("\n3. LATENCY ANALYSIS")
    print("=" * 60)

    latency_samples = [18, 22, 19, 45, 31, 28]
    print(f"Latency samples: {latency_samples}")

    print("\nConsecutive changes:")

    for previous, current in pairwise(latency_samples):
        difference = current - previous
        print(
            f"{previous} ms -> {current} ms | "
            f"Change: {difference:+} ms"
        )

    running_maximum = accumulate(latency_samples, max)

    print("\nRunning maximum latency:")

    for sample_number, maximum_latency in enumerate(running_maximum, start=1):
        print(f"Sample {sample_number}: {maximum_latency} ms")


def main() -> None:
    """Load external data and run the network analysis."""

    devices = load_json_data(DEVICES_FILE)
    events = load_json_data(EVENTS_FILE)

    validate_devices(devices)
    validate_events(events)

    analyze_inventory(devices)
    analyze_events(events)
    analyze_latency()

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, ValueError) as error:
        print(f"ERROR: {error}")
