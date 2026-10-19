"""
Lesson 36.2 — Counter Basics

Learn how to count repeated values and analyze
network event frequencies using Counter.
"""

from collections import Counter


def main() -> None:
    """Demonstrate Counter operations with network events."""

    # Simulate event types collected from network devices.
    network_events = [
        "LINK_DOWN",
        "LOGIN_FAILURE",
        "LINK_DOWN",
        "CONFIG_CHANGE",
        "LINK_DOWN",
        "LOGIN_FAILURE",
        "LINK_UP",
        "BGP_NEIGHBOR_DOWN",
        "LOGIN_FAILURE",
        "LINK_UP",
    ]

    # Count the occurrences of each event type.
    event_counts = Counter(network_events)

    print("1. Event Frequency")
    print("-" * 40)

    for event_type, count in event_counts.items():
        print(f"{event_type}: {count}")

    # Identify the three most frequent event types.
    print("\n2. Top Three Events")
    print("-" * 40)

    for event_type, count in event_counts.most_common(3):
        print(f"{event_type}: {count}")

    # Query a specific event type.
    print("\n3. Specific Event Count")
    print("-" * 40)

    print(f"LINK_DOWN: {event_counts['LINK_DOWN']}")
    print(f"INTERFACE_ERROR: {event_counts['INTERFACE_ERROR']}")

    # Add a new batch of monitoring events.
    additional_events = [
        "LINK_DOWN",
        "INTERFACE_ERROR",
        "LOGIN_FAILURE",
    ]

    event_counts.update(additional_events)

    print("\n4. Updated Event Frequency")
    print("-" * 40)

    for event_type, count in event_counts.most_common():
        print(f"{event_type}: {count}")

    # Calculate the total number of counted events.
    print("\n5. Total Event Count")
    print("-" * 40)

    print(f"Total events: {event_counts.total()}")


# Run the demonstration when this file is executed directly.
if __name__ == "__main__":
    main()
