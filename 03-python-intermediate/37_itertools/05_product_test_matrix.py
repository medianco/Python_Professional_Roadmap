
"""
Lesson 37.5 — Product Test Matrix

Generate combinations for network automation testing.
"""

from itertools import product


def demonstrate_basic_product() -> None:
    """Generate every combination of devices and connection methods."""

    print("1. BASIC PRODUCT")
    print("-" * 50)

    devices = ["R1", "SW1"]
    connection_methods = ["SSH", "API"]

    # product() generates every possible pair.
    test_cases = product(devices, connection_methods)

    for device, method in test_cases:
        print(f"Device: {device:<5} | Connection: {method}")


def demonstrate_test_matrix() -> None:
    """Build a matrix using devices, protocols, and test types."""

    print("\n2. NETWORK TEST MATRIX")
    print("-" * 50)

    devices = ["R1", "FW1"]
    protocols = ["SSH", "API"]
    test_types = ["CONNECTIVITY", "AUTHENTICATION"]

    # product() generates the Cartesian product of all three iterables.
    test_matrix = product(devices, protocols, test_types)

    test_count = 0

    for device, protocol, test_type in test_matrix:
        test_count += 1
        print(
            f"Test {test_count:02}: "
            f"Device={device:<3} | "
            f"Protocol={protocol:<3} | "
            f"Test={test_type}"
        )

    print(f"Total test cases: {test_count}")


def demonstrate_limited_product() -> None:
    """Generate combinations from selected configuration options."""

    print("\n3. CONFIGURATION COMBINATIONS")
    print("-" * 50)

    vendors = ["Cisco", "Juniper"]
    environments = ["LAB", "PRODUCTION"]

    # Each combination represents a vendor and an environment.
    for vendor, environment in product(vendors, environments):
        print(f"Vendor: {vendor:<8} | Environment: {environment}")


def main() -> None:
    """Run all demonstrations."""

    demonstrate_basic_product()
    demonstrate_test_matrix()
    demonstrate_limited_product()


if __name__ == "__main__":
    main()

