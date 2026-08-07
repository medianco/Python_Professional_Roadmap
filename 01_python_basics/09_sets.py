"""
===============================================================================
File        : 09_sets.py
Author      : Mohammed AL-Dubai
Course      : Python Basics
Lesson      : Sets

Description:
    This lesson explains Python sets, unique data storage,
    adding and removing elements, and practical usage.

Learning Objectives
-------------------
After completing this lesson, you will be able to:

✔ Understand Python sets.
✔ Create and modify sets.
✔ Remove duplicate values.
✔ Add and remove set elements.
✔ Understand set properties.
✔ Apply sets in networking and cybersecurity.

===============================================================================
"""


# =============================================================================
# SECTION 1 - Introduction to Sets
# =============================================================================


"""
A set is an unordered collection of unique elements.

Characteristics:

✔ Unordered
✔ Mutable
✔ No duplicate values
✔ No indexing
✔ Supports mathematical operations


Examples:

Network IP addresses

Security indicators

Unique ports
"""


def introduction_demo() -> None:
    """
    Demonstrates the concept of sets.
    """

    print("\nIntroduction to Sets")
    print("-" * 40)

    protocols: set[str] = {
        "HTTP",
        "HTTPS",
        "SSH"
    }

    print(
        "Protocols:",
        protocols
    )

    print(
        "Type:",
        type(protocols)
    )


# =============================================================================
# SECTION 2 - Creating Sets
# =============================================================================


def creating_sets_demo() -> None:
    """
    Demonstrates creating sets.
    """

    print("\nCreating Sets")
    print("-" * 40)

    ports: set[int] = {
        22,
        80,
        443
    }

    devices: set[str] = {
        "Router",
        "Switch",
        "Firewall"
    }

    mixed_data: set = {
        "Cisco",
        443,
        True
    }

    print(
        "Ports:",
        ports
    )

    print(
        "Devices:",
        devices
    )

    print(
        "Mixed:",
        mixed_data
    )


# =============================================================================
# SECTION 3 - Removing Duplicates
# =============================================================================


def remove_duplicates_demo() -> None:
    """
    Demonstrates how sets remove duplicates.
    """

    print("\nRemoving Duplicates")
    print("-" * 40)

    ip_addresses: list[str] = [
        "192.168.1.10",
        "192.168.1.20",
        "192.168.1.10",
        "192.168.1.30"
    ]

    unique_ips = set(ip_addresses)

    print(
        "Original:",
        ip_addresses
    )

    print(
        "Unique:",
        unique_ips
    )


# =============================================================================
# SECTION 4 - Set Length
# =============================================================================


def set_length_demo() -> None:
    """
    Demonstrates len() with sets.
    """

    print("\nSet Length")
    print("-" * 40)

    services: set[str] = {
        "SSH",
        "HTTP",
        "HTTPS",
        "DNS"
    }

    print(
        "Number of Services:",
        len(services)
    )


# =============================================================================
# SECTION 5 - Adding Elements
# =============================================================================


def add_demo() -> None:
    """
    Demonstrates add() method.
    """

    print("\nAdding Elements")
    print("-" * 40)

    protocols: set[str] = {
        "HTTP",
        "HTTPS"
    }

    print(
        "Before:",
        protocols
    )

    protocols.add("SSH")

    print(
        "After:",
        protocols
    )


# =============================================================================
# SECTION 6 - Updating Sets
# =============================================================================


def update_demo() -> None:
    """
    Demonstrates update() method.

    update() adds multiple elements.
    """

    print("\nupdate() Method")
    print("-" * 40)

    ports: set[int] = {
        22,
        80
    }

    new_ports: set[int] = {
        443,
        3389
    }

    ports.update(new_ports)

    print(
        ports
    )


# =============================================================================
# SECTION 7 - Removing Elements
# =============================================================================


def remove_demo() -> None:
    """
    Demonstrates remove() method.
    """

    print("\nremove() Method")
    print("-" * 40)

    services: set[str] = {
        "SSH",
        "FTP",
        "HTTP"
    }

    services.remove("FTP")

    print(
        services
    )


# =============================================================================
# SECTION 8 - discard()
# =============================================================================


def discard_demo() -> None:
    """
    Demonstrates discard() method.

    discard() does not raise an error
    if item does not exist.
    """

    print("\ndiscard() Method")
    print("-" * 40)

    protocols: set[str] = {
        "SSH",
        "HTTP"
    }

    protocols.discard("FTP")

    print(
        protocols
    )


# =============================================================================
# SECTION 9 - pop()
# =============================================================================


def pop_demo() -> None:
    """
    Demonstrates pop() method.

    Removes an arbitrary element.
    """

    print("\npop() Method")
    print("-" * 40)

    alerts: set[str] = {
        "ERROR",
        "WARNING",
        "INFO"
    }

    removed = alerts.pop()

    print(
        "Removed:",
        removed
    )

    print(
        "Remaining:",
        alerts
    )


# =============================================================================
# SECTION 10 - clear()
# =============================================================================


def clear_demo() -> None:
    """
    Demonstrates clear() method.
    """

    print("\nclear() Method")
    print("-" * 40)

    logs: set[str] = {
        "ERROR",
        "INFO"
    }

    logs.clear()

    print(
        logs
    )


# =============================================================================
# END OF PART 1
# =============================================================================

# =============================================================================
# SECTION 11 - Union Operation
# =============================================================================


def union_demo() -> None:
    """
    Demonstrates union operation.

    Union combines all unique elements
    from two sets.
    """

    print("\nUnion Operation")
    print("-" * 40)

    tcp_ports: set[int] = {
        22,
        80,
        443
    }

    udp_ports: set[int] = {
        53,
        161,
        443
    }

    all_ports = tcp_ports.union(udp_ports)

    print(
        "All Ports:",
        all_ports
    )


# =============================================================================
# SECTION 12 - Union Operator
# =============================================================================


def union_operator_demo() -> None:
    """
    Demonstrates union using | operator.
    """

    print("\nUnion Operator |")
    print("-" * 40)

    team_a: set[str] = {
        "Alice",
        "Bob",
        "John"
    }

    team_b: set[str] = {
        "Bob",
        "David",
        "Sara"
    }

    result = team_a | team_b

    print(
        result
    )


# =============================================================================
# SECTION 13 - Intersection Operation
# =============================================================================


def intersection_demo() -> None:
    """
    Demonstrates intersection.

    Returns common elements.
    """

    print("\nIntersection Operation")
    print("-" * 40)

    firewall_ports: set[int] = {
        22,
        80,
        443,
        3389
    }

    server_ports: set[int] = {
        22,
        443,
        8080
    }

    common_ports = firewall_ports.intersection(
        server_ports
    )

    print(
        "Common Ports:",
        common_ports
    )


# =============================================================================
# SECTION 14 - Intersection Operator
# =============================================================================


def intersection_operator_demo() -> None:
    """
    Demonstrates intersection using &.
    """

    print("\nIntersection Operator &")
    print("-" * 40)

    set_a: set[str] = {
        "SSH",
        "HTTP",
        "DNS"
    }

    set_b: set[str] = {
        "SSH",
        "FTP",
        "DNS"
    }

    print(
        set_a & set_b
    )


# =============================================================================
# SECTION 15 - Difference Operation
# =============================================================================


def difference_demo() -> None:
    """
    Demonstrates difference operation.

    Returns elements that exist
    only in the first set.
    """

    print("\nDifference Operation")
    print("-" * 40)

    allowed_ports: set[int] = {
        22,
        80,
        443
    }

    open_ports: set[int] = {
        22,
        443,
        3389
    }

    unexpected_ports = open_ports.difference(
        allowed_ports
    )

    print(
        "Unexpected Ports:",
        unexpected_ports
    )


# =============================================================================
# SECTION 16 - Difference Operator
# =============================================================================


def difference_operator_demo() -> None:
    """
    Demonstrates difference using -.
    """

    print("\nDifference Operator -")
    print("-" * 40)

    production_services: set[str] = {
        "HTTP",
        "HTTPS",
        "SSH"
    }

    development_services: set[str] = {
        "HTTP",
        "FTP"
    }

    print(
        production_services - development_services
    )


# =============================================================================
# SECTION 17 - Symmetric Difference
# =============================================================================


def symmetric_difference_demo() -> None:
    """
    Demonstrates symmetric difference.

    Returns elements that exist
    in either set but not both.
    """

    print("\nSymmetric Difference")
    print("-" * 40)

    network_a: set[str] = {
        "R1",
        "R2",
        "R3"
    }

    network_b: set[str] = {
        "R2",
        "R3",
        "R4"
    }

    result = network_a.symmetric_difference(
        network_b
    )

    print(
        result
    )


# =============================================================================
# SECTION 18 - Subset Checking
# =============================================================================


def subset_demo() -> None:
    """
    Demonstrates issubset().
    """

    print("\nissubset()")
    print("-" * 40)

    security_ports: set[int] = {
        22,
        443
    }

    allowed_ports: set[int] = {
        22,
        80,
        443
    }

    print(
        security_ports.issubset(
            allowed_ports
        )
    )


# =============================================================================
# SECTION 19 - Superset Checking
# =============================================================================


def superset_demo() -> None:
    """
    Demonstrates issuperset().
    """

    print("\nissuperset()")
    print("-" * 40)

    firewall_rules: set[int] = {
        22,
        80,
        443,
        3389
    }

    required_rules: set[int] = {
        22,
        443
    }

    print(
        firewall_rules.issuperset(
            required_rules
        )
    )


# =============================================================================
# SECTION 20 - Disjoint Checking
# =============================================================================


def disjoint_demo() -> None:
    """
    Demonstrates isdisjoint().

    Checks if two sets have no
    common elements.
    """

    print("\nisdisjoint()")
    print("-" * 40)

    internal_ips: set[str] = {
        "10.0.0.1",
        "10.0.0.2"
    }

    external_ips: set[str] = {
        "8.8.8.8",
        "1.1.1.1"
    }

    print(
        internal_ips.isdisjoint(
            external_ips
        )
    )


# =============================================================================
# SECTION 21 - List vs Set Comparison
# =============================================================================


def list_vs_set_demo() -> None:
    """
    Demonstrates differences between
    lists and sets.
    """

    print("\nList vs Set")
    print("-" * 40)

    """
    List:

    ✔ Ordered

    ✔ Allows duplicates

    ✔ Supports indexing


    Set:

    ✔ Unordered

    ✔ Unique values only

    ✔ Faster membership checking
    """

    ip_list: list[str] = [
        "10.0.0.1",
        "10.0.0.1",
        "10.0.0.2"
    ]

    ip_set: set[str] = set(
        ip_list
    )

    print(
        "List:",
        ip_list
    )

    print(
        "Set:",
        ip_set
    )


# =============================================================================
# SECTION 22 - Network Port Analysis
# =============================================================================


def network_port_analysis_demo() -> None:
    """
    Demonstrates port analysis using sets.
    """

    print("\nNetwork Port Analysis")
    print("-" * 40)

    scanned_ports: set[int] = {
        21,
        22,
        80,
        443,
        3389
    }

    secure_ports: set[int] = {
        22,
        443
    }

    insecure_ports = (
        scanned_ports - secure_ports
    )

    print(
        "Other Ports:",
        insecure_ports
    )


# =============================================================================
# SECTION 23 - IOC Comparison
# =============================================================================


def ioc_comparison_demo() -> None:
    """
    Demonstrates comparing indicators
    of compromise.
    """

    print("\nIOC Comparison")
    print("-" * 40)

    threat_feed_a: set[str] = {
        "bad.com",
        "malware.exe",
        "10.0.0.5"
    }

    threat_feed_b: set[str] = {
        "bad.com",
        "evil.com",
        "192.168.1.5"
    }

    common_iocs = (
        threat_feed_a &
        threat_feed_b
    )

    print(
        "Common IOC:",
        common_iocs
    )


# =============================================================================
# END OF PART 2
# =============================================================================

# =============================================================================
# SECTION 24 - Iterating Through Sets
# =============================================================================


def set_iteration_demo() -> None:
    """
    Demonstrates iterating through sets.
    """

    print("\nSet Iteration")
    print("-" * 40)

    services: set[str] = {
        "SSH",
        "HTTP",
        "HTTPS",
        "DNS"
    }

    for service in services:
        print(service)


# =============================================================================
# SECTION 25 - Membership Testing
# =============================================================================


def membership_demo() -> None:
    """
    Demonstrates checking membership
    using 'in' operator.
    """

    print("\nMembership Testing")
    print("-" * 40)

    open_ports: set[int] = {
        22,
        80,
        443
    }

    print(
        "SSH Available:",
        22 in open_ports
    )

    print(
        "FTP Available:",
        21 in open_ports
    )


# =============================================================================
# SECTION 26 - Set Comprehension
# =============================================================================


def set_comprehension_demo() -> None:
    """
    Demonstrates set comprehension.
    """

    print("\nSet Comprehension")
    print("-" * 40)

    numbers: set[int] = {
        1,
        2,
        3,
        4,
        5
    }

    squared_numbers: set[int] = {
        number ** 2
        for number in numbers
    }

    print(
        "Squared:",
        squared_numbers
    )


# =============================================================================
# SECTION 27 - Filtering Using Set Comprehension
# =============================================================================


def filtering_set_demo() -> None:
    """
    Demonstrates filtering using
    set comprehension.
    """

    print("\nFiltering Set")
    print("-" * 40)

    ports: set[int] = {
        21,
        22,
        80,
        443,
        3389
    }

    secure_ports: set[int] = {
        port
        for port in ports
        if port in {
            22,
            443
        }
    }

    print(
        "Secure Ports:",
        secure_ports
    )


# =============================================================================
# SECTION 28 - Frozen Set
# =============================================================================


def frozenset_demo() -> None:
    """
    Demonstrates frozenset.

    frozenset is an immutable set.
    """

    print("\nfrozenset")
    print("-" * 40)

    protocols = frozenset(
        {
            "SSH",
            "HTTPS",
            "DNS"
        }
    )

    print(
        protocols
    )

    print(
        type(protocols)
    )


# =============================================================================
# SECTION 29 - Set Conversion
# =============================================================================


def set_conversion_demo() -> None:
    """
    Demonstrates converting between
    list and set.
    """

    print("\nSet Conversion")
    print("-" * 40)

    ip_list: list[str] = [
        "10.0.0.1",
        "10.0.0.2",
        "10.0.0.1"
    ]

    unique_ips: set[str] = set(
        ip_list
    )

    print(
        "List:",
        ip_list
    )

    print(
        "Set:",
        unique_ips
    )


# =============================================================================
# SECTION 30 - Sets With Functions
# =============================================================================


def analyze_ports(
    ports: set[int]
) -> int:
    """
    Returns number of open ports.
    """

    return len(ports)


def function_with_set_demo() -> None:
    """
    Demonstrates passing sets
    to functions.
    """

    print("\nSets With Functions")
    print("-" * 40)

    open_ports: set[int] = {
        22,
        80,
        443
    }

    result = analyze_ports(
        open_ports
    )

    print(
        "Open Ports:",
        result
    )


# =============================================================================
# SECTION 31 - Network Device Comparison
# =============================================================================


def network_device_comparison_demo() -> None:
    """
    Demonstrates comparing network devices.
    """

    print("\nNetwork Device Comparison")
    print("-" * 40)

    site_a_devices: set[str] = {
        "R1",
        "R2",
        "SW1"
    }

    site_b_devices: set[str] = {
        "R2",
        "SW1",
        "FW1"
    }

    common_devices = (
        site_a_devices &
        site_b_devices
    )

    new_devices = (
        site_b_devices -
        site_a_devices
    )

    print(
        "Common:",
        common_devices
    )

    print(
        "New:",
        new_devices
    )


# =============================================================================
# SECTION 32 - Firewall Rule Analysis
# =============================================================================


def firewall_rule_analysis_demo() -> None:
    """
    Demonstrates firewall rule analysis.
    """

    print("\nFirewall Rule Analysis")
    print("-" * 40)

    current_rules: set[int] = {
        22,
        80,
        443,
        3389
    }

    required_rules: set[int] = {
        22,
        443
    }

    missing_rules = (
        required_rules -
        current_rules
    )

    print(
        "Missing Rules:",
        missing_rules
    )


# =============================================================================
# SECTION 33 - Security Log Analysis
# =============================================================================


def security_log_analysis_demo() -> None:
    """
    Demonstrates extracting unique
    security events.
    """

    print("\nSecurity Log Analysis")
    print("-" * 40)

    logs: list[str] = [
        "FAILED LOGIN",
        "FAILED LOGIN",
        "PORT SCAN",
        "MALWARE DETECTED"
    ]

    unique_events: set[str] = set(
        logs
    )

    print(
        "Unique Events:"
    )

    for event in unique_events:
        print(event)


# =============================================================================
# END OF PART 3
# =============================================================================

# =============================================================================
# SECTION 34 - Professional Tips
# =============================================================================


def professional_tips_demo() -> None:
    """
    Demonstrates professional tips
    when working with sets.
    """

    print("\nProfessional Set Tips")
    print("-" * 40)

    """
    Professional Tips:

    ✔ Use sets when uniqueness is required.

    ✔ Use sets for fast membership checking.

    ✔ Use set operations instead of
      manual loops when possible.

    ✔ Use frozenset for constant sets.

    ✔ Use meaningful names.

    ✔ Convert lists to sets when
      removing duplicates.
    """

    print(
        "Use sets for unique and efficient data processing."
    )


# =============================================================================
# SECTION 35 - Best Practices
# =============================================================================


def best_practices_demo() -> None:
    """
    Demonstrates set best practices.
    """

    print("\nSet Best Practices")
    print("-" * 40)

    """
    Best Practices:

    ✔ Choose sets when order is not important.

    ✔ Avoid using sets when indexing is required.

    ✔ Validate data before adding it.

    ✔ Use set operations for comparisons.

    ✔ Keep data types consistent.
    """

    print(
        "Write clean and efficient set-based code."
    )


# =============================================================================
# SECTION 36 - Common Mistakes
# =============================================================================


def common_mistakes_demo() -> None:
    """
    Explains common mistakes with sets.
    """

    print("\nCommon Set Mistakes")
    print("-" * 40)

    """
    Mistake 1:

    Trying to access set elements
    using indexes.


    Mistake 2:

    Expecting a fixed order.


    Mistake 3:

    Adding mutable objects
    like lists into sets.


    Mistake 4:

    Using sets when duplicate
    values are important.


    Mistake 5:

    Confusing remove()
    with discard().
    """

    print(
        "Understand set limitations."
    )


# =============================================================================
# SECTION 37 - Performance Tips
# =============================================================================


def performance_tips_demo() -> None:
    """
    Demonstrates set performance tips.
    """

    print("\nSet Performance Tips")
    print("-" * 40)

    """
    Performance Tips:

    ✔ Membership testing with sets
      is usually faster than lists.

    ✔ Use sets for large searches.

    ✔ Avoid unnecessary conversions.

    ✔ Use set operations instead
      of nested loops.

    ✔ Prefer frozenset for
      read-only collections.
    """

    print(
        "Select the correct data structure."
    )


# =============================================================================
# SECTION 38 - Set Cheat Sheet
# =============================================================================


"""
Set Cheat Sheet
===============


Creation:

items = {
    "A",
    "B"
}


Empty Set:

set()


Add:

add()


Add Multiple:

update()


Remove:

remove()

discard()

pop()


Clear:

clear()


Length:

len()


Operations:


Union:

A | B


Intersection:

A & B


Difference:

A - B


Symmetric Difference:

A ^ B


Checks:


Subset:

issubset()


Superset:

issuperset()


Disjoint:

isdisjoint()


Conversion:

set(list)

list(set)
"""


# =============================================================================
# SECTION 39 - Interview Questions
# =============================================================================


"""
Interview Questions
-------------------


1. What is a Python set?


2. Why do sets not allow duplicates?


3. Are sets ordered?


4. What is the difference between
   remove() and discard()?


5. When should you use a set
   instead of a list?


6. Explain union and intersection.


7. What is frozenset?


8. How can sets help in
   cybersecurity?


9. How can sets improve
   network analysis?


10. What happens when you add
    duplicate values to a set?
"""


# =============================================================================
# SECTION 40 - Coding Exercises
# =============================================================================


"""
Coding Exercises
----------------


Exercise 1:

Create a set of unique IP addresses.


Exercise 2:

Remove duplicated log events.


Exercise 3:

Compare two firewall rule sets.


Exercise 4:

Find common ports between
two servers.


Exercise 5:

Create a tool that detects
duplicate Indicators of Compromise.
"""


# =============================================================================
# SECTION 41 - Mini Project
# =============================================================================


def mini_project_description() -> None:
    """
    Mini Project:

    IOC Analyzer


    Scenario:

    A security analyst receives
    threat intelligence feeds from
    multiple sources.


    Requirements:


    Store:

    - Malicious IP addresses

    - Malicious domains

    - File hashes


    Tasks:


    1. Remove duplicates.

    2. Compare multiple feeds.

    3. Find common indicators.

    4. Detect new indicators.


    Example:


    Feed A:

    10.0.0.5
    malware.com


    Feed B:

    malware.com
    badfile.exe


    Common IOC:

    malware.com


    Skills Practiced:


    ✔ Sets

    ✔ Set Operations

    ✔ Data Analysis

    ✔ Cybersecurity Concepts
    """

    print(
        "\nMini Project: IOC Analyzer"
    )

    print(
        "See project requirements above."
    )


# =============================================================================
# SECTION 42 - What's Next?
# =============================================================================


"""
What's Next?

Next Lesson:

10_dictionaries.py


Topics:

✔ Creating Dictionaries

✔ Keys and Values

✔ Accessing Data

✔ Adding and Removing Items

✔ Dictionary Methods

✔ Nested Dictionaries

✔ Network Device Inventory

✔ Security Data Analysis
"""


# =============================================================================
# SECTION 43 - Main Function
# =============================================================================


def main() -> None:
    """
    Main function that runs all demonstrations.
    """

    # Part One

    introduction_demo()
    creating_sets_demo()
    remove_duplicates_demo()
    set_length_demo()
    add_demo()
    update_demo()
    remove_demo()
    discard_demo()
    pop_demo()
    clear_demo()


    # Part Two

    union_demo()
    union_operator_demo()
    intersection_demo()
    intersection_operator_demo()
    difference_demo()
    difference_operator_demo()
    symmetric_difference_demo()
    subset_demo()
    superset_demo()
    disjoint_demo()
    list_vs_set_demo()
    network_port_analysis_demo()
    ioc_comparison_demo()


    # Part Three

    set_iteration_demo()
    membership_demo()
    set_comprehension_demo()
    filtering_set_demo()
    frozenset_demo()
    set_conversion_demo()
    function_with_set_demo()
    network_device_comparison_demo()
    firewall_rule_analysis_demo()
    security_log_analysis_demo()


    # Part Four

    professional_tips_demo()
    best_practices_demo()
    common_mistakes_demo()
    performance_tips_demo()
    mini_project_description()


if __name__ == "__main__":
    main()
