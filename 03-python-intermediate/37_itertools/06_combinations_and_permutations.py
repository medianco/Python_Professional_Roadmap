
"""
Lesson 37.6 — Combinations and Permutations

Explore combinations and permutations using network device examples.
"""

from itertools import (
    combinations,
    combinations_with_replacement,
    permutations,
)


def demonstrate_combinations() -> None:
    """Generate unique pairs of network devices."""

    print("1. COMBINATIONS")
    print("-" * 50)

    devices = ["R1", "R2", "R3"]

    # Select two different devices without considering their order.
    device_pairs = combinations(devices, 2)

    for device_a, device_b in device_pairs:
        print(f"Device pair: {device_a} - {device_b}")


def demonstrate_permutations() -> None:
    """Generate ordered pairs of network devices."""

    print("\n2. PERMUTATIONS")
    print("-" * 50)

    devices = ["R1", "R2", "R3"]

    # Generate ordered pairs without repeating a position.
    ordered_pairs = permutations(devices, 2)

    for source, destination in ordered_pairs:
        print(f"Source: {source} -> Destination: {destination}")


def demonstrate_combinations_with_replacement() -> None:
    """Generate pairs where selecting the same device twice is allowed."""

    print("\n3. COMBINATIONS WITH REPLACEMENT")
    print("-" * 50)

    interfaces = ["Gi0/0", "Gi0/1", "Gi0/2"]

    # The same interface label can appear twice in a combination.
    interface_pairs = combinations_with_replacement(interfaces, 2)

    for interface_a, interface_b in interface_pairs:
        print(f"Interface pair: {interface_a} - {interface_b}")


def compare_pair_counts() -> None:
    """Compare the number of combinations and permutations."""

    print("\n4. PAIR COUNT COMPARISON")
    print("-" * 50)

    devices = ["R1", "R2", "R3", "R4"]

    combination_count = sum(1 for _ in combinations(devices, 2))
    permutation_count = sum(1 for _ in permutations(devices, 2))

    print(f"Devices: {len(devices)}")
    print(f"Unique unordered pairs: {combination_count}")
    print(f"Ordered pairs: {permutation_count}")


def main() -> None:
    """Run all demonstrations."""

    demonstrate_combinations()
    demonstrate_permutations()
    demonstrate_combinations_with_replacement()
    compare_pair_counts()


if __name__ == "__main__":
    main()

