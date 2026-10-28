
"""
Lesson 37.10 — Iterator Pipelines

Build iterator pipelines for network inventory and monitoring data.
"""

from itertools import accumulate, chain, islice


def demonstrate_device_pipeline() -> None:
    """Combine device sources, filter enabled devices, and transform names."""

    print("1. DEVICE INVENTORY PIPELINE")
    print("-" * 55)

    branch_devices = [
        {"hostname": "BR-R1", "enabled": True},
        {"hostname": "BR-SW1", "enabled": False},
    ]

    datacenter_devices = [
        {"hostname": "DC-R1", "enabled": True},
        {"hostname": "DC-R2", "enabled": True},
    ]

    # Combine the sources, keep enabled devices, then extract hostnames.
    all_devices = chain(branch_devices, datacenter_devices)
    enabled_devices = filter(
        lambda device: device["enabled"],
        all_devices,
    )
    hostnames = map(
        lambda device: device["hostname"],
        enabled_devices,
    )

    for hostname in hostnames:
        print(f"Enabled device: {hostname}")


def demonstrate_limited_event_pipeline() -> None:
    """Select critical events and process only the first two."""

    print("\n2. CRITICAL EVENT PIPELINE")
    print("-" * 55)

    event_sources = [
        [
            {"device": "R1", "severity": "INFO"},
            {"device": "R2", "severity": "CRITICAL"},
        ],
        [
            {"device": "SW1", "severity": "HIGH"},
            {"device": "FW1", "severity": "CRITICAL"},
            {"device": "R3", "severity": "CRITICAL"},
        ],
    ]

    # Flatten the sources, filter critical events, and limit the results.
    all_events = chain.from_iterable(event_sources)
    critical_events = filter(
        lambda event: event["severity"] == "CRITICAL",
        all_events,
    )
    first_two_critical = islice(critical_events, 2)

    for event in first_two_critical:
        print(
            f"Critical event on {event['device']} "
            f"({event['severity']})"
        )


def demonstrate_traffic_pipeline() -> None:
    """Calculate cumulative traffic from multiple monitoring intervals."""

    print("\n3. CUMULATIVE TRAFFIC PIPELINE")
    print("-" * 55)

    traffic_sources = [
        [100, 150],
        [80, 120],
        [200],
    ]

    # Combine traffic samples and calculate the running total.
    all_samples = chain.from_iterable(traffic_sources)
    cumulative_traffic = accumulate(all_samples)

    for interval, total_mb in enumerate(cumulative_traffic, start=1):
        print(f"Interval {interval}: {total_mb} MB")


def demonstrate_lazy_processing() -> None:
    """Process only the first three matching devices."""

    print("\n4. LAZY PROCESSING")
    print("-" * 55)

    devices = ["R1", "SW1", "R2", "FW1", "R3", "SW2"]

    # Select router names, transform them, and stop after three results.
    routers = filter(lambda name: name.startswith("R"), devices)
    router_labels = map(lambda name: f"Router: {name}", routers)
    first_three = islice(router_labels, 3)

    for label in first_three:
        print(label)


def main() -> None:
    """Run all demonstrations."""

    demonstrate_device_pipeline()
    demonstrate_limited_event_pipeline()
    demonstrate_traffic_pipeline()
    demonstrate_lazy_processing()


if __name__ == "__main__":
    main()

