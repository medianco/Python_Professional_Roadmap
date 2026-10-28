
"""
Lesson 37.9 — Pairwise Monitoring

Compare consecutive network monitoring samples using itertools.pairwise().
"""

from itertools import pairwise


def demonstrate_pairwise() -> None:
    """Compare consecutive values in a sequence."""

    print("1. BASIC PAIRWISE")
    print("-" * 50)

    response_times = [12, 18, 15, 27, 22]

    # pairwise() returns consecutive pairs from the input iterable.
    for previous, current in pairwise(response_times):
        print(f"Previous: {previous} ms -> Current: {current} ms")


def analyze_latency_changes() -> None:
    """Calculate latency changes between consecutive samples."""

    print("\n2. LATENCY CHANGE ANALYSIS")
    print("-" * 50)

    latency_samples = [20, 24, 19, 35, 42, 30]

    for previous, current in pairwise(latency_samples):
        difference = current - previous

        if difference > 0:
            trend = "INCREASED"
        elif difference < 0:
            trend = "DECREASED"
        else:
            trend = "UNCHANGED"

        print(
            f"{previous} ms -> {current} ms | "
            f"Change: {difference:+} ms | Trend: {trend}"
        )


def analyze_interface_counters() -> None:
    """Calculate traffic-counter increments between samples."""

    print("\n3. INTERFACE COUNTER ANALYSIS")
    print("-" * 50)

    received_packets = [1000, 1250, 1600, 1750, 2100]

    for previous, current in pairwise(received_packets):
        packet_delta = current - previous

        print(
            f"Previous: {previous} | Current: {current} | "
            f"New packets: {packet_delta}"
        )


def analyze_device_status() -> None:
    """Detect changes between consecutive device status checks."""

    print("\n4. DEVICE STATUS CHANGES")
    print("-" * 50)

    status_samples = [
        "UP",
        "UP",
        "DOWN",
        "DOWN",
        "UP",
    ]

    for check_number, (previous, current) in enumerate(
        pairwise(status_samples),
        start=1,
    ):
        if previous != current:
            print(
                f"Check {check_number}: "
                f"Status changed from {previous} to {current}"
            )
        else:
            print(f"Check {check_number}: Status remained {current}")


def main() -> None:
    """Run all demonstrations."""

    demonstrate_pairwise()
    analyze_latency_changes()
    analyze_interface_counters()
    analyze_device_status()


if __name__ == "__main__":
    main()

