"""
===============================================================================
File        : 14_while_loops.py
Author      : Mohammed AL-Dubai
Course      : Python Professional Roadmap
Lesson      : While Loops

Description:
    This lesson explains how to use while loops to repeat
    code while a condition remains True.

Learning Objectives
-------------------
After completing this lesson, you will be able to:

✔ Understand while loops.
✔ Control loop execution with conditions.
✔ Prevent infinite loops.
✔ Apply while loops in networking and cybersecurity.

===============================================================================
"""


# =============================================================================
# SECTION 1 - Introduction to While Loops
# =============================================================================


"""
A while loop repeatedly executes a block of code
as long as its condition evaluates to True.

General Syntax

while condition:
    statements
"""


def introduction_demo() -> None:
    """
    Demonstrates a basic while loop.
    """

    print("\nIntroduction to While Loops")
    print("-" * 40)

    counter: int = 1

    while counter <= 5:
        print(counter)
        counter += 1


# =============================================================================
# SECTION 2 - Counter Loop
# =============================================================================


def counter_demo() -> None:
    """
    Demonstrates a counter loop.
    """

    print("\nCounter Loop")
    print("-" * 40)

    number: int = 0

    while number < 5:
        print(number)
        number += 1


# =============================================================================
# SECTION 3 - Condition-Based Loop
# =============================================================================


def condition_demo() -> None:
    """
    Demonstrates a condition-based loop.
    """

    print("\nCondition-Based Loop")
    print("-" * 40)

    service_running: bool = True
    checks: int = 0

    while service_running:

        print("Monitoring service...")

        checks += 1

        if checks == 3:
            service_running = False

    print("Monitoring stopped.")


# =============================================================================
# SECTION 4 - Infinite Loop Simulation
# =============================================================================


def infinite_loop_demo() -> None:
    """
    Demonstrates a controlled infinite loop.
    """

    print("\nInfinite Loop Simulation")
    print("-" * 40)

    attempts: int = 0

    while True:

        print(f"Attempt {attempts + 1}")

        attempts += 1

        if attempts == 3:
            print("Stopping loop.")
            break


# =============================================================================
# SECTION 5 - Countdown Timer
# =============================================================================


def countdown_demo() -> None:
    """
    Demonstrates a countdown.
    """

    print("\nCountdown")
    print("-" * 40)

    seconds: int = 5

    while seconds > 0:
        print(seconds)
        seconds -= 1

    print("Done!")


# =============================================================================
# SECTION 6 - Network Retry Simulation
# =============================================================================


def network_retry_demo() -> None:
    """
    Demonstrates retrying a network connection.
    """

    print("\nNetwork Retry Simulation")
    print("-" * 40)

    retries: int = 1
    max_retries: int = 3

    while retries <= max_retries:

        print(f"Connection attempt {retries}")

        retries += 1

    print("Maximum retries reached.")


# =============================================================================
# SECTION 7 - Device Availability Check
# =============================================================================


def device_availability_demo() -> None:
    """
    Demonstrates checking device availability.
    """

    print("\nDevice Availability Check")
    print("-" * 40)

    device_online: bool = False
    attempts: int = 0

    while not device_online:

        attempts += 1

        print(f"Checking device ({attempts})")

        if attempts == 3:
            device_online = True

    print("Device is reachable.")


# =============================================================================
# SECTION 8 - Run Part One
# =============================================================================


def run_part_one() -> None:
    """
    Runs all demonstrations
    from Part One.
    """

    introduction_demo()
    counter_demo()
    condition_demo()
    infinite_loop_demo()
    countdown_demo()
    network_retry_demo()
    device_availability_demo()

# =============================================================================
# SECTION 9 - break Statement
# =============================================================================


def break_demo() -> None:
    """
    Demonstrates the break statement.
    """

    print("\nbreak Statement")
    print("-" * 40)

    attempt: int = 1

    while attempt <= 5:

        print(f"Attempt {attempt}")

        if attempt == 3:
            print("Connection established.")
            break

        attempt += 1


# =============================================================================
# SECTION 10 - continue Statement
# =============================================================================


def continue_demo() -> None:
    """
    Demonstrates the continue statement.
    """

    print("\ncontinue Statement")
    print("-" * 40)

    number: int = 0

    while number < 6:

        number += 1

        if number == 3:
            continue

        print(number)


# =============================================================================
# SECTION 11 - pass Statement
# =============================================================================


def pass_demo() -> None:
    """
    Demonstrates the pass statement.
    """

    print("\npass Statement")
    print("-" * 40)

    counter: int = 1

    while counter <= 3:

        if counter == 2:
            pass

        print(counter)

        counter += 1


# =============================================================================
# SECTION 12 - Sentinel Value
# =============================================================================


def sentinel_demo() -> None:
    """
    Demonstrates using a sentinel value.
    """

    print("\nSentinel Value")
    print("-" * 40)

    commands: list[str] = [
        "show version",
        "show ip interface brief",
        "exit"
    ]

    index: int = 0

    while commands[index] != "exit":

        print(commands[index])

        index += 1

    print("Session closed.")


# =============================================================================
# SECTION 13 - Input Validation Simulation
# =============================================================================


def input_validation_demo() -> None:
    """
    Demonstrates input validation.
    """

    print("\nInput Validation Simulation")
    print("-" * 40)

    password: str = "admin123"

    entered_password: str = "guest"

    attempts: int = 1

    while entered_password != password:

        print(f"Invalid password (Attempt {attempts})")

        attempts += 1

        if attempts > 3:
            print("Access denied.")
            break

        entered_password = password

    else:
        print("Authentication successful.")


# =============================================================================
# SECTION 14 - while...else
# =============================================================================


def while_else_demo() -> None:
    """
    Demonstrates while...else.
    """

    print("\nwhile...else")
    print("-" * 40)

    value: int = 1

    while value <= 3:

        print(value)

        value += 1

    else:
        print("Loop completed successfully.")


# =============================================================================
# SECTION 15 - Retry Counter
# =============================================================================


def retry_counter_demo() -> None:
    """
    Demonstrates retry logic.
    """

    print("\nRetry Counter")
    print("-" * 40)

    retries: int = 0
    max_retries: int = 5

    while retries < max_retries:

        retries += 1

        print(f"Retry {retries}")

    print("Retry limit reached.")


# =============================================================================
# SECTION 16 - Connection Timeout Simulation
# =============================================================================


def timeout_demo() -> None:
    """
    Demonstrates a timeout simulation.
    """

    print("\nConnection Timeout Simulation")
    print("-" * 40)

    timeout: int = 5

    while timeout > 0:

        print(f"Waiting... {timeout}")

        timeout -= 1

    print("Connection timed out.")


# =============================================================================
# SECTION 17 - Run Part Two
# =============================================================================


def run_part_two() -> None:
    """
    Runs all demonstrations
    from Part Two.
    """

    break_demo()
    continue_demo()
    pass_demo()
    sentinel_demo()
    input_validation_demo()
    while_else_demo()
    retry_counter_demo()
    timeout_demo()

# =============================================================================
# SECTION 18 - Network Monitoring
# =============================================================================


def network_monitoring_demo() -> None:
    """
    Demonstrates network monitoring.
    """

    print("\nNetwork Monitoring")
    print("-" * 40)

    checks: int = 1
    max_checks: int = 5

    while checks <= max_checks:

        print(f"Monitoring cycle {checks}")

        checks += 1

    print("Monitoring completed.")


# =============================================================================
# SECTION 19 - Interface Monitoring
# =============================================================================


def interface_monitoring_demo() -> None:
    """
    Demonstrates interface monitoring.
    """

    print("\nInterface Monitoring")
    print("-" * 40)

    interfaces: list[str] = [
        "Gig0/0",
        "Gig0/1",
        "Gig0/2"
    ]

    index: int = 0

    while index < len(interfaces):

        print(f"Checking {interfaces[index]}")

        index += 1


# =============================================================================
# SECTION 20 - Service Availability Check
# =============================================================================


def service_availability_demo() -> None:
    """
    Demonstrates checking service availability.
    """

    print("\nService Availability Check")
    print("-" * 40)

    service_available: bool = False
    attempts: int = 0

    while not service_available:

        attempts += 1

        print(f"Checking service ({attempts})")

        if attempts == 4:
            service_available = True

    print("Service is available.")


# =============================================================================
# SECTION 21 - Log Monitoring
# =============================================================================


def log_monitoring_demo() -> None:
    """
    Demonstrates log monitoring.
    """

    print("\nLog Monitoring")
    print("-" * 40)

    logs: list[str] = [
        "INFO",
        "WARNING",
        "ERROR",
        "INFO"
    ]

    index: int = 0

    while index < len(logs):

        print(logs[index])

        index += 1


# =============================================================================
# SECTION 22 - Failed Login Monitoring
# =============================================================================


def failed_login_monitoring_demo() -> None:
    """
    Demonstrates failed login monitoring.
    """

    print("\nFailed Login Monitoring")
    print("-" * 40)

    failed_attempts: int = 0

    while failed_attempts < 3:

        failed_attempts += 1

        print(f"Failed login #{failed_attempts}")

    print("Account temporarily locked.")


# =============================================================================
# SECTION 23 - Brute Force Detection Simulation
# =============================================================================


def brute_force_demo() -> None:
    """
    Demonstrates brute-force detection.
    """

    print("\nBrute Force Detection")
    print("-" * 40)

    attempts: int = 0
    threshold: int = 5

    while attempts < threshold:

        attempts += 1

        print(f"Attempt {attempts}")

    print("Possible brute-force attack detected.")


# =============================================================================
# SECTION 24 - Task Queue Processing
# =============================================================================


def task_queue_demo() -> None:
    """
    Demonstrates processing a task queue.
    """

    print("\nTask Queue Processing")
    print("-" * 40)

    tasks: list[str] = [
        "Backup",
        "Collect Logs",
        "Restart Service",
        "Generate Report"
    ]

    index: int = 0

    while index < len(tasks):

        print(f"Executing: {tasks[index]}")

        index += 1


# =============================================================================
# SECTION 25 - API Polling Simulation
# =============================================================================


def api_polling_demo() -> None:
    """
    Demonstrates API polling.
    """

    print("\nAPI Polling Simulation")
    print("-" * 40)

    completed: bool = False
    attempts: int = 0

    while not completed:

        attempts += 1

        print(f"Polling API ({attempts})")

        if attempts == 3:
            completed = True

    print("Task completed.")


# =============================================================================
# SECTION 26 - Device Health Monitoring
# =============================================================================


def device_health_demo() -> None:
    """
    Demonstrates device health monitoring.
    """

    print("\nDevice Health Monitoring")
    print("-" * 40)

    devices: list[str] = [
        "R1",
        "R2",
        "SW1"
    ]

    index: int = 0

    while index < len(devices):

        print(f"Checking {devices[index]}")

        index += 1


# =============================================================================
# SECTION 27 - Automation Retry Queue
# =============================================================================


def automation_retry_demo() -> None:
    """
    Demonstrates retrying failed automation tasks.
    """

    print("\nAutomation Retry Queue")
    print("-" * 40)

    retries: int = 1
    max_retries: int = 3

    while retries <= max_retries:

        print(f"Retry attempt {retries}")

        retries += 1

    print("Automation finished.")


# =============================================================================
# SECTION 28 - Run Part Three
# =============================================================================


def run_part_three() -> None:
    """
    Runs all demonstrations
    from Part Three.
    """

    network_monitoring_demo()
    interface_monitoring_demo()
    service_availability_demo()
    log_monitoring_demo()
    failed_login_monitoring_demo()
    brute_force_demo()
    task_queue_demo()
    api_polling_demo()
    device_health_demo()
    automation_retry_demo()

# =============================================================================
# SECTION 29 - Professional Tips
# =============================================================================


def professional_tips_demo() -> None:
    """
    Demonstrates professional tips
    for writing while loops.
    """

    print("\nProfessional Tips")
    print("-" * 40)

    print("✔ Always update the loop condition.")
    print("✔ Keep while loops simple and readable.")
    print("✔ Use break only when appropriate.")
    print("✔ Avoid unnecessary infinite loops.")
    print("✔ Add timeout or retry limits whenever possible.")


# =============================================================================
# SECTION 30 - Best Practices
# =============================================================================


def best_practices_demo() -> None:
    """
    Demonstrates best practices.
    """

    print("\nBest Practices")
    print("-" * 40)

    print("✔ Initialize variables before the loop.")
    print("✔ Make exit conditions obvious.")
    print("✔ Keep loop bodies focused on one task.")
    print("✔ Prefer for loops when the iteration count is known.")
    print("✔ Use meaningful variable names.")


# =============================================================================
# SECTION 31 - Common Mistakes
# =============================================================================


def common_mistakes_demo() -> None:
    """
    Demonstrates common mistakes.
    """

    print("\nCommon Mistakes")
    print("-" * 40)

    print("✘ Forgetting to update the loop variable.")
    print("✘ Creating unintended infinite loops.")
    print("✘ Using while instead of for unnecessarily.")
    print("✘ Writing complex loop conditions.")
    print("✘ Missing retry or timeout limits.")


# =============================================================================
# SECTION 32 - Performance Tips
# =============================================================================


def performance_tips_demo() -> None:
    """
    Demonstrates performance tips.
    """

    print("\nPerformance Tips")
    print("-" * 40)

    print("✔ Keep expensive operations outside the loop.")
    print("✔ Stop early using break when possible.")
    print("✔ Avoid unnecessary polling.")
    print("✔ Minimize repeated calculations.")


# =============================================================================
# SECTION 33 - While Loop Cheat Sheet
# =============================================================================

"""
While Loop Cheat Sheet
======================

Basic

while condition:
    ...


Counter

counter = 1

while counter <= 5:
    counter += 1


Infinite Loop

while True:
    ...


Loop Control

break

continue

pass


while...else

while condition:
    ...

else:
    ...
"""


# =============================================================================
# SECTION 34 - Interview Questions
# =============================================================================

"""
Interview Questions
-------------------

1. What is a while loop?

2. When should while be used?

3. Difference between for and while?

4. What causes an infinite loop?

5. How can an infinite loop be avoided?

6. Explain break.

7. Explain continue.

8. What is while...else?

9. What is a sentinel value?

10. Give a networking example using while.
"""


# =============================================================================
# SECTION 35 - Coding Exercises
# =============================================================================

"""
Coding Exercises
----------------

Exercise 1

Print numbers from 10 down to 1.


Exercise 2

Retry a failed connection five times.


Exercise 3

Monitor a service until it becomes available.


Exercise 4

Count failed login attempts.


Exercise 5

Simulate a network timeout.
"""


# =============================================================================
# SECTION 36 - Challenge Exercises
# =============================================================================

"""
Challenge Exercises
-------------------

Challenge 1

Create a retry mechanism with a timeout.


Challenge 2

Monitor a device until it responds.


Challenge 3

Build a login attempt limiter.


Challenge 4

Process a task queue using while.


Challenge 5

Create a simple monitoring loop with a stop condition.
"""


# =============================================================================
# SECTION 37 - Mini Project
# =============================================================================


def mini_project_description() -> None:
    """
    Mini Project

    Network Device Monitoring Simulator

    Requirements

    - Monitor a device.
    - Retry connection attempts.
    - Stop when the device responds.
    - Display the total number of attempts.

    Skills

    ✔ while

    ✔ break

    ✔ Condition

    ✔ Counter
    """

    print("\nMini Project")
    print("-" * 40)

    attempts: int = 1
    device_online: bool = False

    while not device_online:

        print(f"Checking device... Attempt {attempts}")

        if attempts == 3:
            device_online = True

        attempts += 1

    print("Device is online.")
    print(f"Total attempts: {attempts - 1}")


# =============================================================================
# SECTION 38 - What's Next
# =============================================================================

"""
Next Lesson

15_functions.py

Topics

✔ Defining Functions

✔ Parameters

✔ Arguments

✔ Return Values

✔ Default Parameters

✔ *args

✔ **kwargs

✔ Lambda

✔ Recursion

✔ Practical Automation Examples
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
