
"""
Lesson 37.7 — Groupby Network Events

Group network monitoring events by event type.
"""

from itertools import groupby
from operator import itemgetter


def demonstrate_groupby() -> None:
    """Group consecutive values with the same key."""

    print("1. BASIC GROUPBY")
    print("-" * 50)

    statuses = ["UP", "UP", "DOWN", "DOWN", "UP"]

    # groupby() groups consecutive values with the same key.
    for status, group in groupby(statuses):
        items = list(group)
        print(f"Status: {status} | Count: {len(items)}")


def analyze_network_events() -> None:
    """Group network events by their event type."""

    print("\n2. NETWORK EVENT ANALYSIS")
    print("-" * 50)

    events = [
        {"device": "R1", "event_type": "BGP_NEIGHBOR_DOWN", "severity": "CRITICAL"},
        {"device": "R2", "event_type": "BGP_NEIGHBOR_DOWN", "severity": "CRITICAL"},
        {"device": "SW1", "event_type": "INTERFACE_DOWN", "severity": "HIGH"},
        {"device": "SW2", "event_type": "INTERFACE_DOWN", "severity": "HIGH"},
        {"device": "FW1", "event_type": "LOGIN_FAILURE", "severity": "MEDIUM"},
        {"device": "R3", "event_type": "LOGIN_FAILURE", "severity": "MEDIUM"},
        {"device": "R4", "event_type": "BGP_NEIGHBOR_DOWN", "severity": "CRITICAL"},
    ]

    # Sort by event_type because groupby() groups consecutive matching keys.
    sorted_events = sorted(events, key=itemgetter("event_type"))

    total_events = 0

    for event_type, group in groupby(
        sorted_events,
        key=itemgetter("event_type"),
    ):
        grouped_events = list(group)
        total_events += len(grouped_events)

        print(f"\nEvent type: {event_type}")
        print(f"Count: {len(grouped_events)}")

        for event in grouped_events:
            print(
                f"  Device: {event['device']} | "
                f"Severity: {event['severity']}"
            )

    print(f"\nTotal events analyzed: {total_events}")


def demonstrate_grouping_without_sorting() -> None:
    """Show why sorting matters for global grouping."""

    print("\n3. GROUPBY WITHOUT SORTING")
    print("-" * 50)

    event_types = ["BGP_DOWN", "LOGIN_FAILURE", "BGP_DOWN"]

    # Non-consecutive matching values form separate groups.
    for event_type, group in groupby(event_types):
        print(f"{event_type}: {len(list(group))}")


def main() -> None:
    """Run all demonstrations."""

    demonstrate_groupby()
    analyze_network_events()
    demonstrate_grouping_without_sorting()


if __name__ == "__main__":
    main()

