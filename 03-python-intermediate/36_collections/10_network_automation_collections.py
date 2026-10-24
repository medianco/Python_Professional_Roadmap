
"""
Lesson 36.10 — Network Automation Collections

Analyze a network inventory and network events using collections.
Save a consolidated report to the output directory.
"""

import json
import logging
from collections import Counter, defaultdict, deque, namedtuple
from pathlib import Path
from typing import Any


# Define a lightweight record for network devices.
NetworkDevice = namedtuple(
    "NetworkDevice",
    ["hostname", "management_ip", "vendor", "device_type", "location"],
)

HIGH_SEVERITY_LEVELS = {"CRITICAL", "HIGH"}
RECENT_EVENT_LIMIT = 5


def configure_logging() -> None:
    """Configure application logging."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(message)s",
    )


def load_json_file(file_path: Path) -> Any:
    """Load JSON data from a file."""

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_devices(file_path: Path) -> list[NetworkDevice]:
    """Load and validate network device records."""

    data = load_json_file(file_path)

    if not isinstance(data, list):
        raise ValueError("Device inventory must contain a JSON list.")

    required_fields = {
        "hostname",
        "management_ip",
        "vendor",
        "device_type",
        "location",
    }

    devices = []

    for index, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            logging.warning("Skipping device record %d: not an object.", index)
            continue

        if not required_fields.issubset(item):
            logging.warning("Skipping device record %d: missing fields.", index)
            continue

        if not all(
            isinstance(item[field], str) and item[field].strip()
            for field in required_fields
        ):
            logging.warning("Skipping device record %d: invalid values.", index)
            continue

        devices.append(
            NetworkDevice(
                hostname=item["hostname"].strip(),
                management_ip=item["management_ip"].strip(),
                vendor=item["vendor"].strip(),
                device_type=item["device_type"].strip(),
                location=item["location"].strip(),
            )
        )

    return devices


def load_events(file_path: Path) -> list[dict[str, str]]:
    """Load and validate network event records."""

    data = load_json_file(file_path)

    if not isinstance(data, list):
        raise ValueError("Network logs must contain a JSON list.")

    required_fields = {"hostname", "event_type", "severity"}
    events = []

    for index, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            logging.warning("Skipping event record %d: not an object.", index)
            continue

        if not required_fields.issubset(item):
            logging.warning("Skipping event record %d: missing fields.", index)
            continue

        if not all(
            isinstance(item[field], str) and item[field].strip()
            for field in required_fields
        ):
            logging.warning("Skipping event record %d: invalid values.", index)
            continue

        events.append({
            "hostname": item["hostname"].strip(),
            "event_type": item["event_type"].strip(),
            "severity": item["severity"].strip().upper(),
        })

    return events


def analyze_devices(
    devices: list[NetworkDevice],
) -> tuple[dict[str, list[str]], dict[str, list[str]], Counter]:
    """Group devices by vendor and location and count device types."""

    devices_by_vendor = defaultdict(list)
    devices_by_location = defaultdict(list)
    device_type_counts = Counter()

    for device in devices:
        devices_by_vendor[device.vendor].append(device.hostname)
        devices_by_location[device.location].append(device.hostname)
        device_type_counts[device.device_type] += 1

    return (
        dict(devices_by_vendor),
        dict(devices_by_location),
        device_type_counts,
    )


def analyze_events(
    events: list[dict[str, str]],
) -> tuple[Counter, Counter, deque]:
    """Count event types and severity levels and retain recent events."""

    event_type_counts = Counter()
    severity_counts = Counter()
    recent_events = deque(maxlen=RECENT_EVENT_LIMIT)

    for event in events:
        event_type_counts[event["event_type"]] += 1
        severity_counts[event["severity"]] += 1
        recent_events.append(event)

    return event_type_counts, severity_counts, recent_events


def build_report(
    devices: list[NetworkDevice],
    events: list[dict[str, str]],
) -> str:
    """Build a consolidated text report."""

    vendor_groups, location_groups, device_type_counts = analyze_devices(devices)
    event_type_counts, severity_counts, recent_events = analyze_events(events)

    high_severity_count = sum(
        severity_counts[level] for level in HIGH_SEVERITY_LEVELS
    )

    lines = [
        "NETWORK AUTOMATION COLLECTIONS REPORT",
        "=" * 50,
        "",
        "1. INVENTORY SUMMARY",
        "-" * 50,
        f"Total valid devices: {len(devices)}",
        f"Total valid events: {len(events)}",
        "",
        "2. DEVICES BY VENDOR",
        "-" * 50,
    ]

    for vendor, hostnames in sorted(vendor_groups.items()):
        lines.append(f"{vendor}: {', '.join(hostnames)}")

    lines.extend([
        "",
        "3. DEVICES BY LOCATION",
        "-" * 50,
    ])

    for location, hostnames in sorted(location_groups.items()):
        lines.append(f"{location}: {', '.join(hostnames)}")

    lines.extend([
        "",
        "4. DEVICE TYPES",
        "-" * 50,
    ])

    for device_type, count in device_type_counts.most_common():
        lines.append(f"{device_type}: {count}")

    lines.extend([
        "",
        "5. EVENT COUNTS BY TYPE",
        "-" * 50,
    ])

    for event_type, count in event_type_counts.most_common():
        lines.append(f"{event_type}: {count}")

    lines.extend([
        "",
        "6. EVENT COUNTS BY SEVERITY",
        "-" * 50,
    ])

    for severity, count in sorted(severity_counts.items()):
        lines.append(f"{severity}: {count}")

    lines.extend([
        "",
        "7. HIGH-SEVERITY SUMMARY",
        "-" * 50,
        f"CRITICAL and HIGH events: {high_severity_count}",
        "",
        f"8. MOST RECENT {RECENT_EVENT_LIMIT} EVENTS",
        "-" * 50,
    ])

    for event in recent_events:
        lines.append(
            f"{event['hostname']} | "
            f"{event['event_type']} | "
            f"{event['severity']}"
        )

    lines.append("")
    lines.append("=" * 50)
    lines.append("End of report")

    return "\n".join(lines)


def main() -> None:
    """Load data, analyze it, and save the report."""

    configure_logging()

    project_dir = Path(__file__).resolve().parent
    data_dir = project_dir / "data"
    output_dir = project_dir / "output"

    devices_file = data_dir / "network_devices.json"
    events_file = data_dir / "network_logs.json"
    report_file = output_dir / "collections_analysis_report.txt"

    try:
        devices = load_devices(devices_file)
        events = load_events(events_file)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        logging.error("Unable to load input data: %s", error)
        return

    if not devices:
        logging.warning("No valid device records were loaded.")

    if not events:
        logging.warning("No valid event records were loaded.")

    report = build_report(devices, events)

    # Create the output directory if it does not already exist.
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        report_file.write_text(report + "\n", encoding="utf-8")
    except OSError as error:
        logging.error("Unable to save report: %s", error)
        return

    print(report)
    logging.info("Report saved to %s", report_file)


if __name__ == "__main__":
    main()
