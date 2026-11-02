"""
Lesson 38.3 — StopIteration

Demonstrates how StopIteration works when processing
network monitoring events using a custom Iterator.
"""


class NetworkEventIterator:
    """
    Custom Iterator for sequential network event processing.

    Attributes:
        events: List of network monitoring events.
        index: Current position in the event collection.
    """

    def __init__(self, events):
        # Store the network monitoring events.
        self.events = events

        # Initialize the current iterator position.
        self.index = 0

    def __iter__(self):
        # Return the Iterator object itself.
        return self

    def __next__(self):
        # Check whether all events have been processed.
        if self.index >= len(self.events):

            # Signal that no more events are available.
            raise StopIteration

        # Retrieve the event at the current position.
        event = self.events[self.index]

        # Move the iterator to the next position.
        self.index += 1

        # Return the current network event.
        return event


def main():
    """Process network monitoring events sequentially."""

    # Sample network monitoring events.
    network_events = [
        {
            "device": "R1",
            "event": "BGP_NEIGHBOR_DOWN",
            "severity": "CRITICAL",
        },
        {
            "device": "SW1",
            "event": "INTERFACE_DOWN",
            "severity": "HIGH",
        },
        {
            "device": "FW1",
            "event": "LOGIN_FAILURE",
            "severity": "MEDIUM",
        },
    ]

    # Create a custom Iterator for network events.
    event_iterator = NetworkEventIterator(network_events)

    print("NETWORK MONITORING EVENT PROCESSOR")
    print("=" * 55)

    # Process events until StopIteration is raised.
    while True:

        try:
            # Retrieve the next available network event.
            event = next(event_iterator)

            # Display the event information.
            print(
                f"Device: {event['device']:<5} | "
                f"Event: {event['event']:<20} | "
                f"Severity: {event['severity']}"
            )

        except StopIteration:
            # Handle iterator exhaustion.
            print("\nAll network events have been processed.")
            break

    print("Monitoring process completed.")


if __name__ == "__main__":
    main()
