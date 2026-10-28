
"""
Lesson 37.8 — Accumulate Network Metrics

Calculate cumulative network metrics using itertools.accumulate().
"""

from itertools import accumulate
from operator import add


def demonstrate_cumulative_traffic() -> None:
    """Calculate cumulative traffic volume."""

    print("1. CUMULATIVE NETWORK TRAFFIC")
    print("-" * 50)

    traffic_mb = [120, 180, 90, 210, 150]

    # accumulate() calculates a running total by default.
    cumulative_traffic = accumulate(traffic_mb)

    for interval, total_mb in enumerate(cumulative_traffic, start=1):
        print(f"Interval {interval}: Total traffic = {total_mb} MB")


def demonstrate_cumulative_packets() -> None:
    """Calculate the running total of transmitted packets."""

    print("\n2. CUMULATIVE PACKETS")
    print("-" * 50)

    packets = [1000, 1500, 800, 1700]

    # add explicitly defines the accumulation operation.
    cumulative_packets = accumulate(packets, add)

    for interval, total_packets in enumerate(cumulative_packets, start=1):
        print(f"Interval {interval}: Total packets = {total_packets}")


def demonstrate_running_maximum() -> None:
    """Track the highest observed latency."""

    print("\n3. RUNNING MAXIMUM LATENCY")
    print("-" * 50)

    latency_ms = [12, 18, 15, 42, 27, 55, 31]

    # max keeps the highest value seen so far.
    highest_latency = accumulate(latency_ms, max)

    for interval, max_latency in enumerate(highest_latency, start=1):
        print(f"Sample {interval}: Highest latency = {max_latency} ms")


def demonstrate_custom_accumulation() -> None:
    """Calculate a running total with a custom operation."""

    print("\n4. CUSTOM ACCUMULATION")
    print("-" * 50)

    error_counts = [2, 0, 3, 1, 4]

    # A lambda function can define a custom accumulation operation.
    cumulative_errors = accumulate(
        error_counts,
        lambda total, current: total + current,
    )

    for interval, total_errors in enumerate(cumulative_errors, start=1):
        print(f"Interval {interval}: Total errors = {total_errors}")


def main() -> None:
    """Run all demonstrations."""

    demonstrate_cumulative_traffic()
    demonstrate_cumulative_packets()
    demonstrate_running_maximum()
    demonstrate_custom_accumulation()


if __name__ == "__main__":
    main()

