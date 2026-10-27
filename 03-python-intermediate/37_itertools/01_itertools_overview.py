
"""
Lesson 37.1 — Itertools Overview

Explore iterables, iterators, lazy evaluation, and itertools.chain().
"""

from itertools import chain


def demonstrate_iterable() -> None:
    """Demonstrate iterating over a list."""

    devices = ["R1", "R2", "SW1"]

    print("1. ITERABLE")
    print("-" * 40)

    # A list is an iterable because Python can obtain an iterator from it.
    for device in devices:
        print(f"Device: {device}")


def demonstrate_iterator() -> None:
    """Demonstrate retrieving values from an iterator."""

    devices = ["R1", "R2", "SW1"]
    device_iterator = iter(devices)

    print("\n2. ITERATOR")
    print("-" * 40)

    # Each next() call retrieves the next available value.
    print(next(device_iterator))
    print(next(device_iterator))
    print(next(device_iterator))

    # The iterator is exhausted after all three values are retrieved.


def demonstrate_lazy_evaluation() -> None:
    """Demonstrate processing values on demand."""

    devices = ["R1", "R2", "SW1"]
    device_iterator = iter(devices)

    print("\n3. LAZY EVALUATION")
    print("-" * 40)

    # The iterator provides one value only when requested.
    print("Requesting the first device...")
    print(next(device_iterator))

    print("Requesting the second device...")
    print(next(device_iterator))


def demonstrate_chain() -> None:
    """Combine multiple device inventories into one iterator."""

    routers = ["R1", "R2"]
    switches = ["SW1", "SW2"]

    # chain() iterates over both inventories without building a combined list.
    all_devices = chain(routers, switches)

    print("\n4. ITERTOOLS CHAIN")
    print("-" * 40)

    for device in all_devices:
        print(f"Processing: {device}")


def main() -> None:
    """Run all demonstrations."""

    demonstrate_iterable()
    demonstrate_iterator()
    demonstrate_lazy_evaluation()
    demonstrate_chain()


if __name__ == "__main__":
    main()

