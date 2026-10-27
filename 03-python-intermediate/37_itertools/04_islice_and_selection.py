
"""
Lesson 37.4 — Islice and Selection

Select and filter iterator values using itertools.
"""

from itertools import islice, takewhile, dropwhile


def demonstrate_islice() -> None:
    """Select a specific range of devices."""

    print("1. ISLICE")
    print("-" * 45)

    devices = ["R1", "R2", "R3", "SW1", "SW2", "FW1"]

    # Select the first three devices.
    first_three = islice(devices, 3)
    print("First three devices:", list(first_three))

    # Select devices at indexes 2, 3, and 4.
    middle_devices = islice(devices, 2, 5)
    print("Devices at indexes 2-4:", list(middle_devices))

    # Select every second device, starting at index 0.
    every_second = islice(devices, 0, len(devices), 2)
    print("Every second device:", list(every_second))


def demonstrate_takewhile() -> None:
    """Take consecutive values while a condition is true."""

    print("\n2. TAKEWHILE")
    print("-" * 45)

    response_times = [12, 18, 25, 35, 80, 20, 15]

    # Stop taking values when a response time reaches 50 ms or more.
    acceptable_times = takewhile(
        lambda response_time: response_time < 50,
        response_times,
    )

    print("Response times before threshold:", list(acceptable_times))


def demonstrate_dropwhile() -> None:
    """Skip consecutive values while a condition is true."""

    print("\n3. DROPWHILE")
    print("-" * 45)

    response_times = [12, 18, 25, 35, 80, 20, 15]

    # Skip values while the response time is below 30 ms.
    remaining_times = dropwhile(
        lambda response_time: response_time < 30,
        response_times,
    )

    print("Values after initial threshold:", list(remaining_times))


def demonstrate_network_log_selection() -> None:
    """Select a limited number of network events."""

    print("\n4. NETWORK LOG SELECTION")
    print("-" * 45)

    events = [
        "INFO: R1 reachable",
        "INFO: SW1 reachable",
        "WARNING: R2 packet loss",
        "CRITICAL: FW1 unavailable",
        "INFO: R3 reachable",
    ]

    # Retrieve only the first three events from the iterator.
    first_events = islice(iter(events), 3)

    for event in first_events:
        print(event)


def main() -> None:
    """Run all demonstrations."""

    demonstrate_islice()
    demonstrate_takewhile()
    demonstrate_dropwhile()
    demonstrate_network_log_selection()


if __name__ == "__main__":
    main()

