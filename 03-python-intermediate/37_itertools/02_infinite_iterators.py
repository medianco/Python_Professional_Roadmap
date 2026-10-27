
"""
Lesson 37.2 — Infinite Iterators

Explore count(), cycle(), and repeat() using network automation examples.
"""

from itertools import count, cycle, repeat, islice


def demonstrate_count() -> None:
    """Generate sequential monitoring task IDs."""

    print("1. COUNT")
    print("-" * 40)

    # count() generates an increasing sequence starting from 1.
    task_ids = count(start=1, step=1)

    # islice() limits the number of generated values.
    for task_id in islice(task_ids, 5):
        print(f"Monitoring task ID: {task_id}")


def demonstrate_cycle() -> None:
    """Cycle through network device names."""

    print("\n2. CYCLE")
    print("-" * 40)

    devices = ["R1", "R2", "SW1"]

    # cycle() repeats the iterable indefinitely.
    device_cycle = cycle(devices)

    # Process only six values to avoid an infinite loop.
    for device in islice(device_cycle, 6):
        print(f"Checking device: {device}")


def demonstrate_repeat() -> None:
    """Repeat a monitoring status for a limited number of checks."""

    print("\n3. REPEAT")
    print("-" * 40)

    # repeat() returns the same value repeatedly.
    statuses = repeat("HEALTHY", 4)

    for check_number, status in enumerate(statuses, start=1):
        print(f"Check {check_number}: {status}")


def main() -> None:
    """Run all demonstrations."""

    demonstrate_count()
    demonstrate_cycle()
    demonstrate_repeat()


if __name__ == "__main__":
    main()

