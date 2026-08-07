"""
===============================================================================
File        : 13_for_loops.py
Author      : Mohammed AL-Dubai
Course      : Python Professional Roadmap
Lesson      : For Loops

Description:
    This lesson explains how to use for loops to iterate over
    sequences and automate repetitive tasks.

Learning Objectives
-------------------
After completing this lesson, you will be able to:

✔ Understand for loops.
✔ Use range().
✔ Iterate through strings, lists, tuples, sets and dictionaries.
✔ Apply loops in networking and cybersecurity scenarios.

===============================================================================
"""


# =============================================================================
# SECTION 1 - Introduction to For Loops
# =============================================================================


"""
A for loop executes a block of code once for each item
in an iterable object.

General Syntax

for item in iterable:
    statements
"""


def introduction_demo() -> None:
    """
    Demonstrates a basic for loop.
    """

    print("\nIntroduction to For Loops")
    print("-" * 40)

    for number in range(1, 6):
        print(number)


# =============================================================================
# SECTION 2 - Using range()
# =============================================================================


def range_demo() -> None:
    """
    Demonstrates the range() function.
    """

    print("\nUsing range()")
    print("-" * 40)

    print("range(5)")

    for number in range(5):
        print(number)

    print()

    print("range(1, 6)")

    for number in range(1, 6):
        print(number)

    print()

    print("range(0, 11, 2)")

    for number in range(0, 11, 2):
        print(number)


# =============================================================================
# SECTION 3 - Looping Through a String
# =============================================================================


def string_loop_demo() -> None:
    """
    Demonstrates iterating through a string.
    """

    print("\nLooping Through a String")
    print("-" * 40)

    protocol: str = "HTTPS"

    for character in protocol:
        print(character)


# =============================================================================
# SECTION 4 - Looping Through a List
# =============================================================================


def list_loop_demo() -> None:
    """
    Demonstrates iterating through a list.
    """

    print("\nLooping Through a List")
    print("-" * 40)

    devices: list[str] = [
        "Router",
        "Switch",
        "Firewall",
        "Access Point"
    ]

    for device in devices:
        print(device)


# =============================================================================
# SECTION 5 - Looping Through a Tuple
# =============================================================================


def tuple_loop_demo() -> None:
    """
    Demonstrates iterating through a tuple.
    """

    print("\nLooping Through a Tuple")
    print("-" * 40)

    ports: tuple[int, ...] = (
        22,
        80,
        443
    )

    for port in ports:
        print(port)


# =============================================================================
# SECTION 6 - Looping Through a Set
# =============================================================================


def set_loop_demo() -> None:
    """
    Demonstrates iterating through a set.
    """

    print("\nLooping Through a Set")
    print("-" * 40)

    protocols: set[str] = {
        "HTTP",
        "HTTPS",
        "SSH"
    }

    for protocol in protocols:
        print(protocol)


# =============================================================================
# SECTION 7 - Looping Through a Dictionary
# =============================================================================


def dictionary_loop_demo() -> None:
    """
    Demonstrates iterating through a dictionary.
    """

    print("\nLooping Through a Dictionary")
    print("-" * 40)

    services: dict[int, str] = {
        22: "SSH",
        80: "HTTP",
        443: "HTTPS"
    }

    print("Keys")

    for port in services:
        print(port)

    print()

    print("Values")

    for service in services.values():
        print(service)

    print()

    print("Key / Value")

    for port, service in services.items():
        print(f"{port} -> {service}")


# =============================================================================
# SECTION 8 - Run Part One
# =============================================================================


def run_part_one() -> None:
    """
    Runs all demonstrations
    from Part One.
    """

    introduction_demo()
    range_demo()
    string_loop_demo()
    list_loop_demo()
    tuple_loop_demo()
    set_loop_demo()
    dictionary_loop_demo()

# =============================================================================
# SECTION 9 - Using enumerate()
# =============================================================================


def enumerate_demo() -> None:
    """
    Demonstrates the enumerate() function.
    """

    print("\nUsing enumerate()")
    print("-" * 40)

    devices: list[str] = [
        "Router",
        "Switch",
        "Firewall",
        "Access Point"
    ]

    for index, device in enumerate(devices, start=1):
        print(f"{index}. {device}")


# =============================================================================
# SECTION 10 - Using zip()
# =============================================================================


def zip_demo() -> None:
    """
    Demonstrates the zip() function.
    """

    print("\nUsing zip()")
    print("-" * 40)

    hostnames: list[str] = [
        "R1",
        "R2",
        "R3"
    ]

    addresses: list[str] = [
        "192.168.1.1",
        "192.168.1.2",
        "192.168.1.3"
    ]

    for hostname, address in zip(hostnames, addresses):
        print(f"{hostname} -> {address}")


# =============================================================================
# SECTION 11 - Nested Loops
# =============================================================================


def nested_loops_demo() -> None:
    """
    Demonstrates nested for loops.
    """

    print("\nNested Loops")
    print("-" * 40)

    devices: list[str] = [
        "R1",
        "R2"
    ]

    commands: list[str] = [
        "show version",
        "show ip interface brief"
    ]

    for device in devices:

        print(f"\n{device}")

        for command in commands:
            print(f"Executing: {command}")


# =============================================================================
# SECTION 12 - break Statement
# =============================================================================


def break_demo() -> None:
    """
    Demonstrates the break statement.
    """

    print("\nbreak Statement")
    print("-" * 40)

    ports: list[int] = [
        21,
        22,
        80,
        443
    ]

    for port in ports:

        if port == 22:
            print("SSH found.")
            break

        print(f"Checking port {port}")


# =============================================================================
# SECTION 13 - continue Statement
# =============================================================================


def continue_demo() -> None:
    """
    Demonstrates the continue statement.
    """

    print("\ncontinue Statement")
    print("-" * 40)

    ports: list[int] = [
        21,
        22,
        23,
        80,
        443
    ]

    for port in ports:

        if port == 23:
            continue

        print(f"Scanning port {port}")


# =============================================================================
# SECTION 14 - pass Statement
# =============================================================================


def pass_demo() -> None:
    """
    Demonstrates the pass statement.
    """

    print("\npass Statement")
    print("-" * 40)

    devices: list[str] = [
        "Router",
        "Switch",
        "Firewall"
    ]

    for device in devices:

        if device == "Switch":
            pass

        print(device)


# =============================================================================
# SECTION 15 - for...else
# =============================================================================


def for_else_demo() -> None:
    """
    Demonstrates the for...else statement.
    """

    print("\nfor...else Statement")
    print("-" * 40)

    services: list[str] = [
        "HTTP",
        "HTTPS",
        "DNS"
    ]

    target: str = "SSH"

    for service in services:

        if service == target:
            print("Service found.")
            break

    else:
        print("Service not found.")


# =============================================================================
# SECTION 16 - Combining enumerate() and zip()
# =============================================================================


def enumerate_zip_demo() -> None:
    """
    Demonstrates combining enumerate() with zip().
    """

    print("\nCombining enumerate() and zip()")
    print("-" * 40)

    devices: list[str] = [
        "R1",
        "R2",
        "R3"
    ]

    statuses: list[str] = [
        "UP",
        "DOWN",
        "UP"
    ]

    for index, (device, status) in enumerate(
        zip(devices, statuses),
        start=1
    ):
        print(f"{index}. {device} -> {status}")


# =============================================================================
# SECTION 17 - Run Part Two
# =============================================================================


def run_part_two() -> None:
    """
    Runs all demonstrations
    from Part Two.
    """

    enumerate_demo()
    zip_demo()
    nested_loops_demo()
    break_demo()
    continue_demo()
    pass_demo()
    for_else_demo()
    enumerate_zip_demo()

# =============================================================================
# SECTION 18 - Network Device Inventory
# =============================================================================


def network_inventory_demo() -> None:
    """
    Demonstrates iterating through
    network devices.
    """

    print("\nNetwork Device Inventory")
    print("-" * 40)

    devices: list[str] = [
        "R1",
        "R2",
        "SW1",
        "FW1"
    ]

    for device in devices:
        print(f"Inventory Device: {device}")


# =============================================================================
# SECTION 19 - Interface Monitoring
# =============================================================================


def interface_monitoring_demo() -> None:
    """
    Demonstrates monitoring interfaces.
    """

    print("\nInterface Monitoring")
    print("-" * 40)

    interfaces: dict[str, str] = {
        "Gig0/0": "UP",
        "Gig0/1": "DOWN",
        "Gig0/2": "UP"
    }

    for interface, status in interfaces.items():
        print(f"{interface:<10} {status}")


# =============================================================================
# SECTION 20 - Port Scanner Simulation
# =============================================================================


def port_scanner_demo() -> None:
    """
    Demonstrates a simple port scanner.
    """

    print("\nPort Scanner Simulation")
    print("-" * 40)

    ports: list[int] = [
        22,
        80,
        443,
        3389
    ]

    for port in ports:
        print(f"Scanning TCP/{port}")


# =============================================================================
# SECTION 21 - Log Analysis
# =============================================================================


def log_analysis_demo() -> None:
    """
    Demonstrates log processing.
    """

    print("\nLog Analysis")
    print("-" * 40)

    logs: list[str] = [
        "INFO User login",
        "WARNING High CPU",
        "ERROR Disk Failure",
        "INFO Backup Completed"
    ]

    for log in logs:

        if "ERROR" in log:
            print(log)


# =============================================================================
# SECTION 22 - Failed Login Detection
# =============================================================================


def failed_login_demo() -> None:
    """
    Demonstrates detecting failed logins.
    """

    print("\nFailed Login Detection")
    print("-" * 40)

    events: list[str] = [
        "SUCCESS",
        "FAILED",
        "FAILED",
        "SUCCESS",
        "FAILED"
    ]

    failed_count: int = 0

    for event in events:

        if event == "FAILED":
            failed_count += 1

    print(f"Failed Logins: {failed_count}")


# =============================================================================
# SECTION 23 - Configuration Backup
# =============================================================================


def configuration_backup_demo() -> None:
    """
    Demonstrates configuration backup.
    """

    print("\nConfiguration Backup")
    print("-" * 40)

    devices: list[str] = [
        "R1",
        "R2",
        "SW1"
    ]

    for device in devices:
        print(f"Backing up configuration from {device}")


# =============================================================================
# SECTION 24 - API Response Processing
# =============================================================================


def api_processing_demo() -> None:
    """
    Demonstrates processing API data.
    """

    print("\nAPI Response Processing")
    print("-" * 40)

    responses: list[dict[str, str]] = [
        {"device": "R1", "status": "Online"},
        {"device": "R2", "status": "Offline"},
        {"device": "SW1", "status": "Online"}
    ]

    for response in responses:

        print(
            f"{response['device']} -> "
            f"{response['status']}"
        )


# =============================================================================
# SECTION 25 - Security Alert Processing
# =============================================================================


def security_alert_demo() -> None:
    """
    Demonstrates security alert processing.
    """

    print("\nSecurity Alert Processing")
    print("-" * 40)

    alerts: list[str] = [
        "Low",
        "Medium",
        "Critical",
        "High"
    ]

    for alert in alerts:

        print(f"Alert Level: {alert}")


# =============================================================================
# SECTION 26 - Automation Task Queue
# =============================================================================


def automation_queue_demo() -> None:
    """
    Demonstrates automation task execution.
    """

    print("\nAutomation Task Queue")
    print("-" * 40)

    tasks: list[str] = [
        "Backup",
        "Collect Logs",
        "Restart Service",
        "Generate Report"
    ]

    for task in tasks:
        print(f"Executing: {task}")


# =============================================================================
# SECTION 27 - Device Health Report
# =============================================================================


def health_report_demo() -> None:
    """
    Demonstrates generating a device report.
    """

    print("\nDevice Health Report")
    print("-" * 40)

    devices: dict[str, str] = {
        "R1": "Healthy",
        "R2": "Warning",
        "SW1": "Healthy",
        "FW1": "Critical"
    }

    for device, health in devices.items():
        print(f"{device:<5} {health}")


# =============================================================================
# SECTION 28 - Run Part Three
# =============================================================================


def run_part_three() -> None:
    """
    Runs all demonstrations
    from Part Three.
    """

    network_inventory_demo()
    interface_monitoring_demo()
    port_scanner_demo()
    log_analysis_demo()
    failed_login_demo()
    configuration_backup_demo()
    api_processing_demo()
    security_alert_demo()
    automation_queue_demo()
    health_report_demo()

# =============================================================================
# SECTION 29 - Professional Tips
# =============================================================================


def professional_tips_demo() -> None:
    """
    Demonstrates professional tips
    for writing for loops.
    """

    print("\nProfessional Tips")
    print("-" * 40)

    print("✔ Keep loops simple and readable.")
    print("✔ Choose meaningful variable names.")
    print("✔ Avoid unnecessary nested loops.")
    print("✔ Use enumerate() when an index is needed.")
    print("✔ Use zip() to iterate over related sequences.")


# =============================================================================
# SECTION 30 - Best Practices
# =============================================================================


def best_practices_demo() -> None:
    """
    Demonstrates best practices.
    """

    print("\nBest Practices")
    print("-" * 40)

    print("✔ Iterate directly over objects whenever possible.")
    print("✔ Use break only when necessary.")
    print("✔ Use continue carefully.")
    print("✔ Keep loop bodies focused on one task.")
    print("✔ Prefer clear code over clever code.")


# =============================================================================
# SECTION 31 - Common Mistakes
# =============================================================================


def common_mistakes_demo() -> None:
    """
    Demonstrates common mistakes.
    """

    print("\nCommon Mistakes")
    print("-" * 40)

    print("✘ Modifying a list while iterating over it.")
    print("✘ Creating deeply nested loops.")
    print("✘ Using range(len()) when not required.")
    print("✘ Forgetting break conditions.")
    print("✘ Writing duplicated loop logic.")


# =============================================================================
# SECTION 32 - Performance Tips
# =============================================================================


def performance_tips_demo() -> None:
    """
    Demonstrates performance tips.
    """

    print("\nPerformance Tips")
    print("-" * 40)

    print("✔ Minimize work inside loops.")
    print("✔ Move constant values outside the loop.")
    print("✔ Use generators for large datasets.")
    print("✔ Stop early using break when appropriate.")


# =============================================================================
# SECTION 33 - For Loop Cheat Sheet
# =============================================================================

"""
For Loop Cheat Sheet
====================

Basic Loop

for item in iterable:
    ...


Using range()

for number in range(5):
    ...


Using enumerate()

for index, value in enumerate(items):
    ...


Using zip()

for x, y in zip(list1, list2):
    ...


Loop Dictionary

for key, value in dictionary.items():
    ...


Loop Control

break

continue

pass

for...else
"""


# =============================================================================
# SECTION 34 - Interview Questions
# =============================================================================

"""
Interview Questions
-------------------

1. What is a for loop?

2. What is an iterable?

3. Explain range().

4. Difference between break and continue?

5. When should enumerate() be used?

6. What does zip() do?

7. Explain for...else.

8. Can a dictionary be iterated?

9. What is a nested loop?

10. Give a real-world automation example using for loops.
"""


# =============================================================================
# SECTION 35 - Coding Exercises
# =============================================================================

"""
Coding Exercises
----------------

Exercise 1

Print numbers from 1 to 100.


Exercise 2

Print all network devices.


Exercise 3

Display only active interfaces.


Exercise 4

Count failed login attempts.


Exercise 5

Print all HTTP services from a list of ports.
"""


# =============================================================================
# SECTION 36 - Challenge Exercises
# =============================================================================

"""
Challenge Exercises
-------------------

Challenge 1

Create a script that prints only even port numbers.


Challenge 2

Count how many devices are online.


Challenge 3

Read a list of log messages and print only ERROR entries.


Challenge 4

Generate a configuration backup message for each router.


Challenge 5

Display the hostname and IP address using zip().
"""


# =============================================================================
# SECTION 37 - Mini Project
# =============================================================================


def mini_project_description() -> None:
    """
    Mini Project

    Network Device Inventory Scanner

    Requirements

    - Store device names.
    - Display each device.
    - Count total devices.
    - Print a summary report.

    Skills

    ✔ for

    ✔ range()

    ✔ enumerate()

    ✔ Dictionary

    ✔ List
    """

    print("\nMini Project")
    print("-" * 40)

    devices: list[str] = [
        "R1",
        "R2",
        "SW1",
        "FW1"
    ]

    for index, device in enumerate(devices, start=1):
        print(f"{index}. {device}")

    print(f"\nTotal Devices: {len(devices)}")


# =============================================================================
# SECTION 38 - What's Next
# =============================================================================

"""
Next Lesson

14_while_loops.py

Topics

✔ while

✔ Infinite Loops

✔ break

✔ continue

✔ Sentinel Values

✔ Network Monitoring

✔ Automation Examples
"""


# =============================================================================
# SECTION 39 - Main Function
# =============================================================================


def main() -> None:
    """
    Runs the complete lesson.
    """

    run_part_one()

    run_part_two()

    run_part_three()

    professional_tips_demo()
    best_practices_demo()
    common_mistakes_demo()
    performance_tips_demo()
    mini_project_description()


if __name__ == "__main__":
    main()
