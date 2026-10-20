
"""
Lesson 36.6 — deque Basics

Demonstrate double-ended queue operations.
"""

from collections import deque


def main() -> None:
    """Demonstrate adding and removing elements at both ends."""

    # Create a deque with initial network events.
    events = deque([
        "INTERFACE_UP",
        "BGP_NEIGHBOR_UP",
        "CONFIG_CHANGE",
    ])

    print("Initial events:")
    print(events)

    # Add an event to the right end.
    events.append("LOGIN_FAILURE")
    print("\nAfter append():")
    print(events)

    # Add an event to the left end.
    events.appendleft("DEVICE_REACHABLE")
    print("\nAfter appendleft():")
    print(events)

    # Remove the event from the right end.
    latest_event = events.pop()
    print(f"\nRemoved from right: {latest_event}")
    print(events)

    # Remove the event from the left end.
    oldest_event = events.popleft()
    print(f"\nRemoved from left: {oldest_event}")
    print(events)

    # Create a bounded deque for recent events.
    recent_events = deque(maxlen=3)

    for event in [
        "LINK_DOWN",
        "LINK_UP",
        "BGP_DOWN",
        "BGP_UP",
    ]:
        recent_events.append(event)

    print("\nLast three events:")
    print(recent_events)


if __name__ == "__main__":
    main()
