"""
===============================================================================
File        : 15_functions.py
Author      : Mohammed AL-Dubai
Course      : Python Basics
Lesson      : Functions

Description:
    This lesson introduces Python functions and demonstrates
    how to organize code into reusable, readable, and maintainable
    blocks.

Learning Objectives
-------------------
After completing this lesson, you will be able to:

✔ Understand what a function is.
✔ Define and call functions.
✔ Use parameters and return values.
✔ Write reusable code.
✔ Apply functions to networking and cybersecurity tasks.

===============================================================================
"""


# =============================================================================
# SECTION 1 - What is a Function?
# =============================================================================

"""
A function is a reusable block of code that performs
a specific task.

Benefits

✔ Reusability
✔ Readability
✔ Maintainability
✔ Modularity
"""


def introduction_demo() -> None:
    """
    Demonstrates a simple function.
    """

    print("\nIntroduction to Functions")
    print("-" * 40)
    print("Functions help organize and reuse code.")


# =============================================================================
# SECTION 2 - Defining a Function
# =============================================================================


def greet() -> None:
    """
    Prints a greeting message.
    """

    print("Hello, Python!")


def function_definition_demo() -> None:
    """
    Demonstrates defining and calling a function.
    """

    print("\nDefining a Function")
    print("-" * 40)

    greet()


# =============================================================================
# SECTION 3 - Calling Functions Multiple Times
# =============================================================================


def show_separator() -> None:
    """
    Prints a separator line.
    """

    print("=" * 40)


def calling_functions_demo() -> None:
    """
    Demonstrates calling functions multiple times.
    """

    print("\nCalling Functions")
    print("-" * 40)

    show_separator()

    print("First Call")

    show_separator()

    print("Second Call")

    show_separator()


# =============================================================================
# SECTION 4 - Type Hints
# =============================================================================


def display_hostname(hostname: str) -> None:
    """
    Displays a device hostname.
    """

    print(f"Hostname: {hostname}")


def type_hints_demo() -> None:
    """
    Demonstrates Type Hints.
    """

    print("\nType Hints")
    print("-" * 40)

    display_hostname("R1")
    display_hostname("SW1")


# =============================================================================
# SECTION 5 - Docstrings
# =============================================================================


def calculate_sum(first: int, second: int) -> int:
    """
    Returns the sum of two integers.
    """

    return first + second


def docstring_demo() -> None:
    """
    Demonstrates a documented function.
    """

    print("\nDocstrings")
    print("-" * 40)

    result: int = calculate_sum(10, 20)

    print(f"Result: {result}")


# =============================================================================
# SECTION 6 - Simple Networking Example
# =============================================================================


def connect_device() -> None:
    """
    Simulates connecting to a network device.
    """

    print("Connecting to device...")


def networking_demo() -> None:
    """
    Demonstrates a networking function.
    """

    print("\nNetworking Example")
    print("-" * 40)

    connect_device()


# =============================================================================
# SECTION 7 - Simple Cybersecurity Example
# =============================================================================


def scan_port() -> None:
    """
    Simulates scanning a network port.
    """

    print("Scanning TCP/22...")


def cybersecurity_demo() -> None:
    """
    Demonstrates a cybersecurity function.
    """

    print("\nCybersecurity Example")
    print("-" * 40)

    scan_port()


# =============================================================================
# SECTION 8 - Why Functions Matter
# =============================================================================


def why_functions_demo() -> None:
    """
    Demonstrates the importance of functions.
    """

    print("\nWhy Functions Matter")
    print("-" * 40)

    print("✔ Reduce code duplication.")
    print("✔ Improve readability.")
    print("✔ Simplify maintenance.")
    print("✔ Make testing easier.")
    print("✔ Support modular programming.")


# =============================================================================
# SECTION 9 - Run Part One
# =============================================================================


def run_part_one() -> None:
    """
    Runs all demonstrations
    from Part One.
    """

    introduction_demo()
    function_definition_demo()
    calling_functions_demo()
    type_hints_demo()
    docstring_demo()
    networking_demo()
    cybersecurity_demo()
    why_functions_demo()

# =============================================================================
# SECTION 10 - Parameters and Arguments
# =============================================================================


def greet_user(name: str) -> None:
    """
    Greets a user by name.
    """

    print(f"Hello, {name}!")


def parameters_demo() -> None:
    """
    Demonstrates parameters and arguments.
    """

    print("\nParameters and Arguments")
    print("-" * 40)

    greet_user("Mohammed")
    greet_user("Python")


# =============================================================================
# SECTION 11 - Positional Arguments
# =============================================================================


def configure_device(hostname: str, ip_address: str) -> None:
    """
    Displays device information.
    """

    print(f"Hostname : {hostname}")
    print(f"IP Address: {ip_address}")


def positional_arguments_demo() -> None:
    """
    Demonstrates positional arguments.
    """

    print("\nPositional Arguments")
    print("-" * 40)

    configure_device("R1", "192.168.1.1")


# =============================================================================
# SECTION 12 - Keyword Arguments
# =============================================================================


def create_user(username: str, role: str) -> None:
    """
    Creates a user.
    """

    print(f"{username} -> {role}")


def keyword_arguments_demo() -> None:
    """
    Demonstrates keyword arguments.
    """

    print("\nKeyword Arguments")
    print("-" * 40)

    create_user(role="Administrator", username="admin")


# =============================================================================
# SECTION 13 - Default Parameters
# =============================================================================


def ping_host(host: str, count: int = 4) -> None:
    """
    Simulates a ping command.
    """

    print(f"Pinging {host} ({count} packets)")


def default_parameters_demo() -> None:
    """
    Demonstrates default parameters.
    """

    print("\nDefault Parameters")
    print("-" * 40)

    ping_host("8.8.8.8")
    ping_host("1.1.1.1", 10)


# =============================================================================
# SECTION 14 - Multiple Parameters
# =============================================================================


def create_vlan(vlan_id: int, name: str, status: str) -> None:
    """
    Displays VLAN information.
    """

    print(f"VLAN ID : {vlan_id}")
    print(f"Name    : {name}")
    print(f"Status  : {status}")


def multiple_parameters_demo() -> None:
    """
    Demonstrates multiple parameters.
    """

    print("\nMultiple Parameters")
    print("-" * 40)

    create_vlan(10, "Users", "Active")


# =============================================================================
# SECTION 15 - Returning Values
# =============================================================================


def calculate_total(first: int, second: int) -> int:
    """
    Returns the total of two numbers.
    """

    return first + second


def return_value_demo() -> None:
    """
    Demonstrates returning values.
    """

    print("\nReturning Values")
    print("-" * 40)

    result: int = calculate_total(15, 25)

    print(f"Result: {result}")


# =============================================================================
# SECTION 16 - Returning Multiple Values
# =============================================================================


def get_device_info() -> tuple[str, str]:
    """
    Returns device information.
    """

    return "R1", "192.168.1.1"


def multiple_return_demo() -> None:
    """
    Demonstrates returning multiple values.
    """

    print("\nReturning Multiple Values")
    print("-" * 40)

    hostname, ip_address = get_device_info()

    print(f"Hostname : {hostname}")
    print(f"IP Address: {ip_address}")


# =============================================================================
# SECTION 17 - Practical Example
# =============================================================================


def calculate_average(latencies: list[int]) -> float:
    """
    Calculates the average latency.
    """

    return sum(latencies) / len(latencies)


def practical_demo() -> None:
    """
    Demonstrates a practical example.
    """

    print("\nPractical Example")
    print("-" * 40)

    latency_values: list[int] = [10, 12, 15, 20, 18]

    average: float = calculate_average(latency_values)

    print(f"Average Latency: {average:.2f} ms")


# =============================================================================
# SECTION 18 - Run Part Two
# =============================================================================


def run_part_two() -> None:
    """
    Runs all demonstrations
    from Part Two.
    """

    parameters_demo()
    positional_arguments_demo()
    keyword_arguments_demo()
    default_parameters_demo()
    multiple_parameters_demo()
    return_value_demo()
    multiple_return_demo()
    practical_demo()

# =============================================================================
# SECTION 19 - Local Scope
# =============================================================================


def local_scope_demo() -> None:
    """
    Demonstrates local variables.
    """

    print("\nLocal Scope")
    print("-" * 40)

    def show_hostname() -> None:
        hostname: str = "R1"
        print(f"Hostname: {hostname}")

    show_hostname()


# =============================================================================
# SECTION 20 - Global Scope
# =============================================================================


LAB_NAME: str = "Python Network Lab"


def global_scope_demo() -> None:
    """
    Demonstrates global variables.
    """

    print("\nGlobal Scope")
    print("-" * 40)

    print(f"Lab Name: {LAB_NAME}")


# =============================================================================
# SECTION 21 - *args
# =============================================================================


def calculate_sum(*numbers: int) -> int:
    """
    Returns the sum of all numbers.
    """

    return sum(numbers)


def args_demo() -> None:
    """
    Demonstrates *args.
    """

    print("\n*args")
    print("-" * 40)

    result: int = calculate_sum(10, 20, 30, 40)

    print(f"Total: {result}")


# =============================================================================
# SECTION 22 - **kwargs
# =============================================================================


def display_device(**device: str) -> None:
    """
    Displays device information.
    """

    for key, value in device.items():
        print(f"{key}: {value}")


def kwargs_demo() -> None:
    """
    Demonstrates **kwargs.
    """

    print("\n**kwargs")
    print("-" * 40)

    display_device(
        hostname="R1",
        ip="192.168.1.1",
        vendor="Cisco"
    )


# =============================================================================
# SECTION 23 - Recursion
# =============================================================================


def countdown(number: int) -> None:
    """
    Demonstrates recursion.
    """

    if number == 0:
        print("Finished!")
        return

    print(number)

    countdown(number - 1)


def recursion_demo() -> None:
    """
    Demonstrates recursive functions.
    """

    print("\nRecursion")
    print("-" * 40)

    countdown(5)


# =============================================================================
# SECTION 24 - Lambda Functions
# =============================================================================


def lambda_demo() -> None:
    """
    Demonstrates lambda functions.
    """

    print("\nLambda Function")
    print("-" * 40)

    square = lambda number: number * number

    print(square(5))
    print(square(10))


# =============================================================================
# SECTION 25 - Practical Networking Example
# =============================================================================


def calculate_network_usage(*traffic: float) -> float:
    """
    Returns the total network usage.
    """

    return sum(traffic)


def networking_example_demo() -> None:
    """
    Demonstrates a networking example.
    """

    print("\nNetworking Example")
    print("-" * 40)

    usage: float = calculate_network_usage(
        120.5,
        85.3,
        150.2
    )

    print(f"Total Traffic: {usage:.1f} MB")


# =============================================================================
# SECTION 26 - Practical Cybersecurity Example
# =============================================================================


def analyze_event(event: str, severity: str) -> str:
    """
    Returns a formatted security event.
    """

    return f"{severity}: {event}"


def cybersecurity_example_demo() -> None:
    """
    Demonstrates a cybersecurity example.
    """

    print("\nCybersecurity Example")
    print("-" * 40)

    message: str = analyze_event(
        "Multiple failed login attempts",
        "HIGH"
    )

    print(message)


# =============================================================================
# SECTION 27 - Function Composition
# =============================================================================


def get_hostname() -> str:
    """
    Returns a hostname.
    """

    return "R1"


def print_hostname() -> None:
    """
    Demonstrates calling one function from another.
    """

    hostname: str = get_hostname()

    print(f"Hostname: {hostname}")


def function_composition_demo() -> None:
    """
    Demonstrates function composition.
    """

    print("\nFunction Composition")
    print("-" * 40)

    print_hostname()


# =============================================================================
# SECTION 28 - Run Part Three
# =============================================================================


def run_part_three() -> None:
    """
    Runs all demonstrations
    from Part Three.
    """

    local_scope_demo()
    global_scope_demo()
    args_demo()
    kwargs_demo()
    recursion_demo()
    lambda_demo()
    networking_example_demo()
    cybersecurity_example_demo()
    function_composition_demo()

# =============================================================================
# SECTION 29 - Network Device Connection Simulation
# =============================================================================


def connect_network_device(
    hostname: str,
    ip_address: str,
    username: str
) -> bool:
    """
    Simulates connecting to a network device.

    Returns:
        bool: Connection status.
    """

    print(f"Connecting to {hostname}")
    print(f"IP Address: {ip_address}")
    print(f"Username: {username}")

    return True


def connection_demo() -> None:
    """
    Demonstrates device connection.
    """

    print("\nNetwork Device Connection")
    print("-" * 40)

    status: bool = connect_network_device(
        "R1",
        "192.168.1.1",
        "admin"
    )

    print(f"Connection Status: {status}")


# =============================================================================
# SECTION 30 - Configuration Backup
# =============================================================================


def backup_configuration(device: str) -> str:
    """
    Simulates configuration backup.
    """

    return f"Backup completed for {device}"


def backup_demo() -> None:
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

        result: str = backup_configuration(device)

        print(result)


# =============================================================================
# SECTION 31 - Ping Function
# =============================================================================


def ping_host(
    host: str,
    count: int = 4
) -> dict[str, object]:
    """
    Simulates ping operation.
    """

    return {
        "host": host,
        "packets": count,
        "status": "reachable"
    }


def ping_demo() -> None:
    """
    Demonstrates ping function.
    """

    print("\nPing Test")
    print("-" * 40)

    result: dict[str, object] = ping_host(
        "8.8.8.8"
    )

    print(result)


# =============================================================================
# SECTION 32 - Interface Status Check
# =============================================================================


def check_interface(
    interface: str,
    status: str
) -> str:
    """
    Checks interface status.
    """

    return f"{interface}: {status}"


def interface_demo() -> None:
    """
    Demonstrates interface checking.
    """

    print("\nInterface Status")
    print("-" * 40)

    interfaces: dict[str, str] = {
        "Gig0/0": "UP",
        "Gig0/1": "DOWN"
    }

    for interface, status in interfaces.items():

        print(
            check_interface(
                interface,
                status
            )
        )


# =============================================================================
# SECTION 33 - Port Scanner Simulation
# =============================================================================


def scan_port(
    host: str,
    port: int
) -> str:
    """
    Simulates port scanning.
    """

    return f"{host}:{port} is open"


def port_scan_demo() -> None:
    """
    Demonstrates port scanning.
    """

    print("\nPort Scanner")
    print("-" * 40)

    ports: list[int] = [
        22,
        80,
        443
    ]

    for port in ports:

        print(
            scan_port(
                "192.168.1.10",
                port
            )
        )


# =============================================================================
# SECTION 34 - Security Log Analyzer
# =============================================================================


def analyze_log(
    log: str
) -> str:
    """
    Analyzes a security log.
    """

    if "FAILED" in log:

        return "Security Alert"

    return "Normal Event"


def log_analysis_demo() -> None:
    """
    Demonstrates log analysis.
    """

    print("\nSecurity Log Analysis")
    print("-" * 40)

    logs: list[str] = [
        "SUCCESS LOGIN",
        "FAILED LOGIN",
        "SUCCESS LOGIN"
    ]

    for log in logs:

        print(
            analyze_log(log)
        )


# =============================================================================
# SECTION 35 - Automation Task Runner
# =============================================================================


def execute_task(
    task: str
) -> str:
    """
    Executes an automation task.
    """

    return f"Executing: {task}"


def automation_demo() -> None:
    """
    Demonstrates automation tasks.
    """

    print("\nAutomation Tasks")
    print("-" * 40)

    tasks: list[str] = [
        "Backup",
        "Collect Logs",
        "Generate Report"
    ]

    for task in tasks:

        print(
            execute_task(task)
        )


# =============================================================================
# SECTION 36 - Run Part Four
# =============================================================================


def run_part_four() -> None:
    """
    Runs all demonstrations
    from Part Four.
    """

    connection_demo()
    backup_demo()
    ping_demo()
    interface_demo()
    port_scan_demo()
    log_analysis_demo()
    automation_demo()

# =============================================================================
# SECTION 37 - Professional Tips
# =============================================================================


def professional_tips_demo() -> None:
    """
    Demonstrates professional tips
    for writing functions.
    """

    print("\nProfessional Tips")
    print("-" * 40)

    print("✔ Keep functions small and focused.")
    print("✔ Use meaningful function names.")
    print("✔ Write clear docstrings.")
    print("✔ Avoid repeating code.")
    print("✔ Return values instead of printing everything.")


# =============================================================================
# SECTION 38 - Best Practices
# =============================================================================


def best_practices_demo() -> None:
    """
    Demonstrates function best practices.
    """

    print("\nBest Practices")
    print("-" * 40)

    print("✔ One function should perform one task.")
    print("✔ Use type hints.")
    print("✔ Use descriptive parameters.")
    print("✔ Avoid unnecessary global variables.")
    print("✔ Keep functions reusable.")


# =============================================================================
# SECTION 39 - Common Mistakes
# =============================================================================


def common_mistakes_demo() -> None:
    """
    Demonstrates common mistakes.
    """

    print("\nCommon Mistakes")
    print("-" * 40)

    print("✘ Creating very large functions.")
    print("✘ Using unclear names.")
    print("✘ Forgetting return values.")
    print("✘ Mixing multiple responsibilities.")
    print("✘ Overusing global variables.")


# =============================================================================
# SECTION 40 - Performance Tips
# =============================================================================


def performance_tips_demo() -> None:
    """
    Demonstrates performance tips.
    """

    print("\nPerformance Tips")
    print("-" * 40)

    print("✔ Avoid unnecessary function calls.")
    print("✔ Pass required data as parameters.")
    print("✔ Reuse existing functions.")
    print("✔ Keep calculations efficient.")


# =============================================================================
# SECTION 41 - Function Cheat Sheet
# =============================================================================

"""
Function Cheat Sheet
====================


Create Function

def function_name():
    pass


Function With Parameter

def function_name(value):
    pass


Function With Return

def function_name():
    return value


Default Parameter

def ping(host, count=4):
    pass


Multiple Arguments

def function(*args):
    pass


Keyword Arguments

def function(**kwargs):
    pass


Type Hints

def add(a: int, b: int) -> int:
    return a + b

"""


# =============================================================================
# SECTION 42 - Interview Questions
# =============================================================================

"""
Interview Questions
-------------------

1. What is a function?

2. Why do we use functions?

3. Difference between parameter and argument?

4. Difference between return and print?

5. What are default parameters?

6. Explain *args.

7. Explain **kwargs.

8. What is variable scope?

9. What is recursion?

10. Why are functions important in automation?


"""


# =============================================================================
# SECTION 43 - Coding Exercises
# =============================================================================

"""
Coding Exercises
----------------

Exercise 1

Create a function that calculates network latency average.


Exercise 2

Create a function that checks if a port is open.


Exercise 3

Create a function that validates an IP address.


Exercise 4

Create a function that counts failed login attempts.


Exercise 5

Create a function that generates a device report.

"""


# =============================================================================
# SECTION 44 - Challenge Exercises
# =============================================================================

"""
Challenge Exercises
-------------------

Challenge 1

Create a network device connection manager.


Requirements:

- Function for connection.
- Function for configuration backup.
- Function for status checking.


Challenge 2

Create a security log analyzer.


Requirements:

- Receive logs.
- Detect suspicious events.
- Return security alerts.


Challenge 3

Create an automation task scheduler.


Requirements:

- Store tasks.
- Execute tasks.
- Generate report.

"""


# =============================================================================
# SECTION 45 - Mini Project
# =============================================================================


def network_automation_manager() -> None:
    """
    Mini Project

    Network Automation Manager

    Features:

    - Device inventory.
    - Connection simulation.
    - Backup simulation.
    - Status report.

    """

    print("\nNetwork Automation Manager")
    print("-" * 40)

    devices: list[dict[str, str]] = [

        {
            "hostname": "R1",
            "ip": "192.168.1.1",
            "status": "UP"
        },

        {
            "hostname": "R2",
            "ip": "192.168.1.2",
            "status": "DOWN"
        },

        {
            "hostname": "SW1",
            "ip": "192.168.1.10",
            "status": "UP"
        }
    ]


    def show_device(device: dict[str, str]) -> None:
        """
        Displays device information.
        """

        print(
            f"{device['hostname']} | "
            f"{device['ip']} | "
            f"{device['status']}"
        )


    for device in devices:

        show_device(device)


# =============================================================================
# SECTION 46 - What's Next
# =============================================================================

"""
Next Lesson

16_scope_lambda.py

Topics

✔ Advanced Scope

✔ LEGB Rule

✔ Lambda Functions

✔ Functional Programming Basics

✔ Practical Examples
"""


# =============================================================================
# SECTION 47 - Main Function
# =============================================================================


def main() -> None:
    """
    Runs the complete lesson.
    """

    run_part_one()

    run_part_two()

    run_part_three()

    run_part_four()

    professional_tips_demo()

    best_practices_demo()

    common_mistakes_demo()

    performance_tips_demo()

    network_automation_manager()


if __name__ == "__main__":
    main()
