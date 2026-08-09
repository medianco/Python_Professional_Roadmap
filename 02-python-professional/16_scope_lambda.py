"""
===============================================================================
File        : 16_scope_lambda.py
Author      : Mohammed AL-Dubai
Course      : Python Professional Roadmap
Stage       : Professional Python
Lesson      : Scope & Lambda Functions

Description:
    This lesson introduces variable scope in Python and explains
    how variables are accessed inside and outside functions.

Learning Objectives
-------------------
After completing this lesson, you will be able to:

✔ Understand variable scope.
✔ Understand local and global variables.
✔ Identify where a variable can be accessed.
✔ Understand function scope.
✔ Avoid common scope-related mistakes.

===============================================================================
"""


# =============================================================================
# SECTION 1 - What is Variable Scope?
# =============================================================================

"""
Variable Scope defines where a variable can be accessed
inside a Python program.

A variable may be available:

✔ Inside a function.
✔ Outside a function.
✔ Inside nested functions.
✔ Throughout a module.

Python determines variable access based on scope rules.
"""


# =============================================================================
# SECTION 2 - Global Variable
# =============================================================================

LAB_NAME: str = "Python Network Lab"


def show_global_variable() -> None:
    """
    Demonstrates accessing a global variable.
    """

    print(f"Lab Name: {LAB_NAME}")


def global_variable_demo() -> None:
    """
    Demonstrates a global variable.
    """

    print("\nGlobal Variable")
    print("-" * 40)

    print(f"Outside Function: {LAB_NAME}")

    show_global_variable()


# =============================================================================
# SECTION 3 - Local Variable
# =============================================================================


def show_hostname() -> None:
    """
    Demonstrates a local variable.
    """

    hostname: str = "R1"

    print(f"Hostname: {hostname}")


def local_variable_demo() -> None:
    """
    Demonstrates a local variable.
    """

    print("\nLocal Variable")
    print("-" * 40)

    show_hostname()


# =============================================================================
# SECTION 4 - Local Variable Cannot Be Accessed Outside
# =============================================================================


def create_device() -> None:
    """
    Creates a local device variable.
    """

    device: str = "Cisco Router"

    print(f"Inside Function: {device}")


def local_scope_demo() -> None:
    """
    Demonstrates local variable scope.
    """

    print("\nLocal Scope")
    print("-" * 40)

    create_device()

    print(
        "The variable 'device' exists only "
        "inside create_device()."
    )


# =============================================================================
# SECTION 5 - Same Variable Name in Different Scopes
# =============================================================================


device_name: str = "Global-Router"


def show_device_name() -> None:
    """
    Demonstrates the same variable name
    in different scopes.
    """

    device_name: str = "Local-Router"

    print(f"Inside Function : {device_name}")


def same_name_demo() -> None:
    """
    Demonstrates variable names in different scopes.
    """

    print("\nSame Variable Name")
    print("-" * 40)

    print(f"Outside Function: {device_name}")

    show_device_name()

    print(f"Outside Function: {device_name}")


# =============================================================================
# SECTION 6 - Function Parameters as Local Variables
# =============================================================================


def display_device(hostname: str) -> None:
    """
    Demonstrates that function parameters
    are local to the function.
    """

    print(f"Hostname: {hostname}")


def parameter_scope_demo() -> None:
    """
    Demonstrates parameter scope.
    """

    print("\nParameter Scope")
    print("-" * 40)

    display_device("R1")


# =============================================================================
# SECTION 7 - Practical Networking Example
# =============================================================================


def network_device() -> None:
    """
    Demonstrates local variables in a
    network automation scenario.
    """

    hostname: str = "R1"
    ip_address: str = "192.168.1.1"

    print(f"Hostname : {hostname}")
    print(f"IP Address: {ip_address}")


def networking_scope_demo() -> None:
    """
    Demonstrates variable scope in
    network automation.
    """

    print("\nNetworking Scope Example")
    print("-" * 40)

    network_device()


# =============================================================================
# SECTION 8 - Practical Cybersecurity Example
# =============================================================================


def security_event() -> None:
    """
    Demonstrates local variables in
    a cybersecurity scenario.
    """

    event_type: str = "Failed Login"
    severity: str = "HIGH"

    print(f"Event    : {event_type}")
    print(f"Severity : {severity}")


def cybersecurity_scope_demo() -> None:
    """
    Demonstrates variable scope in
    cybersecurity automation.
    """

    print("\nCybersecurity Scope Example")
    print("-" * 40)

    security_event()


# =============================================================================
# SECTION 9 - Part One Runner
# =============================================================================


def run_part_one() -> None:
    """
    Runs all demonstrations
    from Part One.
    """

    global_variable_demo()

    local_variable_demo()

    local_scope_demo()

    same_name_demo()

    parameter_scope_demo()

    networking_scope_demo()

    cybersecurity_scope_demo()

# =============================================================================
# SECTION 10 - LEGB Rule
# =============================================================================

"""
LEGB stands for:

L -> Local
E -> Enclosing
G -> Global
B -> Built-in

Python searches for a variable in this order:

1. Local
2. Enclosing
3. Global
4. Built-in
"""


# =============================================================================
# SECTION 11 - Local Scope in LEGB
# =============================================================================


device_name: str = "Global-R1"


def local_legb_demo() -> None:
    """
    Demonstrates the Local scope
    in the LEGB rule.
    """

    device_name: str = "Local-R1"

    print("\nLocal Scope - LEGB")
    print("-" * 40)

    print(f"Device: {device_name}")


# =============================================================================
# SECTION 12 - Enclosing Scope
# =============================================================================


def enclosing_legb_demo() -> None:
    """
    Demonstrates the Enclosing scope
    using a nested function.
    """

    device_name: str = "Enclosing-R1"

    def show_device() -> None:
        """
        Accesses a variable from
        the enclosing function.
        """

        print(f"Device: {device_name}")

    print("\nEnclosing Scope - LEGB")
    print("-" * 40)

    show_device()


# =============================================================================
# SECTION 13 - Global Scope in LEGB
# =============================================================================


network_name: str = "Enterprise Network"


def global_legb_demo() -> None:
    """
    Demonstrates the Global scope
    in the LEGB rule.
    """

    print("\nGlobal Scope - LEGB")
    print("-" * 40)

    print(f"Network: {network_name}")


# =============================================================================
# SECTION 14 - Built-in Scope
# =============================================================================


def builtin_legb_demo() -> None:
    """
    Demonstrates Built-in names
    in the LEGB rule.
    """

    print("\nBuilt-in Scope - LEGB")
    print("-" * 40)

    numbers: list[int] = [10, 20, 30, 40]

    print(f"Numbers: {numbers}")
    print(f"Length : {len(numbers)}")
    print(f"Maximum: {max(numbers)}")
    print(f"Minimum: {min(numbers)}")


# =============================================================================
# SECTION 15 - Complete LEGB Example
# =============================================================================


scope_name: str = "Global Scope"


def complete_legb_demo() -> None:
    """
    Demonstrates the complete LEGB search order.
    """

    scope_name: str = "Enclosing Scope"

    def show_scope() -> None:
        """
        Demonstrates Local and Enclosing lookup.
        """

        local_scope_name: str = "Local Scope"

        print(f"Local    : {local_scope_name}")
        print(f"Enclosing: {scope_name}")
        print(f"Global   : {globals()['scope_name']}")
        print(f"Built-in : {len([1, 2, 3])}")

    print("\nComplete LEGB Example")
    print("-" * 40)

    show_scope()


# =============================================================================
# SECTION 16 - LEGB Search Order
# =============================================================================


def legb_search_demo() -> None:
    """
    Demonstrates how Python searches
    for a variable name.
    """

    print("\nLEGB Search Order")
    print("-" * 40)

    print("1. Local")
    print("2. Enclosing")
    print("3. Global")
    print("4. Built-in")


# =============================================================================
# SECTION 17 - Practical Network Example
# =============================================================================


network_environment: str = "Production"


def network_scope_example() -> None:
    """
    Demonstrates LEGB in a network environment.
    """

    device_role: str = "Core Router"

    def display_network_info() -> None:
        """
        Accesses variables from different scopes.
        """

        device_status: str = "UP"

        print(f"Environment : {network_environment}")
        print(f"Device Role : {device_role}")
        print(f"Device Status: {device_status}")

    print("\nNetwork LEGB Example")
    print("-" * 40)

    display_network_info()


# =============================================================================
# SECTION 18 - Practical Cybersecurity Example
# =============================================================================


security_environment: str = "SOC"


def security_scope_example() -> None:
    """
    Demonstrates LEGB in a cybersecurity environment.
    """

    alert_type: str = "Brute Force"

    def analyze_alert() -> None:
        """
        Accesses variables from multiple scopes.
        """

        severity: str = "HIGH"

        print(f"Environment: {security_environment}")
        print(f"Alert Type : {alert_type}")
        print(f"Severity   : {severity}")

    print("\nCybersecurity LEGB Example")
    print("-" * 40)

    analyze_alert()


# =============================================================================
# SECTION 19 - Part Two Runner
# =============================================================================


def run_part_two() -> None:
    """
    Runs all demonstrations
    from Part Two.
    """

    local_legb_demo()

    enclosing_legb_demo()

    global_legb_demo()

    builtin_legb_demo()

    complete_legb_demo()

    legb_search_demo()

    network_scope_example()

    security_scope_example()

# =============================================================================
# SECTION 20 - Reading a Global Variable
# =============================================================================


configuration_mode: str = "Production"


def read_global_variable() -> None:
    """
    Reads a global variable without modifying it.
    """

    print("\nReading a Global Variable")
    print("-" * 40)

    print(f"Configuration Mode: {configuration_mode}")


# =============================================================================
# SECTION 21 - Modifying a Global Variable
# =============================================================================


device_count: int = 0


def increment_device_count() -> None:
    """
    Modifies a global variable using the global keyword.
    """

    global device_count

    device_count += 1


def global_keyword_demo() -> None:
    """
    Demonstrates the global keyword.
    """

    print("\nGlobal Keyword")
    print("-" * 40)

    print(f"Initial Device Count: {device_count}")

    increment_device_count()
    increment_device_count()

    print(f"Updated Device Count: {device_count}")


# =============================================================================
# SECTION 22 - Why Avoid Excessive Global Variables?
# =============================================================================


def global_variable_best_practice_demo() -> None:
    """
    Demonstrates why excessive global variables
    should be avoided.
    """

    print("\nGlobal Variable Best Practice")
    print("-" * 40)

    print("Global variables can make code:")
    print("✘ Harder to test")
    print("✘ Harder to maintain")
    print("✘ Harder to understand")
    print("✔ Prefer parameters and return values")


# =============================================================================
# SECTION 23 - Nested Functions
# =============================================================================


def network_device_report() -> None:
    """
    Demonstrates a nested function.
    """

    hostname: str = "R1"
    ip_address: str = "192.168.1.1"

    def display_device() -> None:
        """
        Displays information from the enclosing function.
        """

        print(f"Hostname : {hostname}")
        print(f"IP Address: {ip_address}")

    print("\nNested Function")
    print("-" * 40)

    display_device()


# =============================================================================
# SECTION 24 - nonlocal Keyword
# =============================================================================


def create_counter() -> callable:
    """
    Creates a counter using a nested function
    and the nonlocal keyword.
    """

    count: int = 0

    def increment() -> int:
        """
        Updates the enclosing variable.
        """

        nonlocal count

        count += 1

        return count

    return increment


def nonlocal_demo() -> None:
    """
    Demonstrates the nonlocal keyword.
    """

    print("\nNonlocal Keyword")
    print("-" * 40)

    counter = create_counter()

    print(f"Counter: {counter()}")
    print(f"Counter: {counter()}")
    print(f"Counter: {counter()}")


# =============================================================================
# SECTION 25 - Multiple Independent Closures
# =============================================================================


def create_device_counter() -> callable:
    """
    Creates an independent device counter.
    """

    count: int = 0

    def increment() -> int:
        """
        Increments the local counter.
        """

        nonlocal count

        count += 1

        return count

    return increment


def independent_closures_demo() -> None:
    """
    Demonstrates independent closures.
    """

    print("\nIndependent Closures")
    print("-" * 40)

    router_counter = create_device_counter()
    switch_counter = create_device_counter()

    print(f"Router Counter: {router_counter()}")
    print(f"Router Counter: {router_counter()}")

    print(f"Switch Counter: {switch_counter()}")
    print(f"Switch Counter: {switch_counter()}")


# =============================================================================
# SECTION 26 - Practical Network Example
# =============================================================================


def create_monitor_counter() -> callable:
    """
    Creates a simple network monitoring counter.
    """

    checks: int = 0

    def perform_check() -> str:
        """
        Performs a monitoring check.
        """

        nonlocal checks

        checks += 1

        return f"Network check #{checks} completed"

    return perform_check


def network_closure_demo() -> None:
    """
    Demonstrates a closure in network monitoring.
    """

    print("\nNetwork Monitoring Closure")
    print("-" * 40)

    monitor = create_monitor_counter()

    print(monitor())
    print(monitor())
    print(monitor())


# =============================================================================
# SECTION 27 - Practical Cybersecurity Example
# =============================================================================


def create_alert_counter() -> callable:
    """
    Creates a security alert counter.
    """

    alerts: int = 0

    def register_alert() -> str:
        """
        Registers a security alert.
        """

        nonlocal alerts

        alerts += 1

        return f"Security Alert #{alerts} registered"

    return register_alert


def security_closure_demo() -> None:
    """
    Demonstrates a closure in cybersecurity.
    """

    print("\nSecurity Alert Closure")
    print("-" * 40)

    register_alert = create_alert_counter()

    print(register_alert())
    print(register_alert())
    print(register_alert())


# =============================================================================
# SECTION 28 - Global vs Nonlocal
# =============================================================================


global_counter: int = 0


def global_counter_demo() -> None:
    """
    Demonstrates the difference between
    global and nonlocal.
    """

    global global_counter

    global_counter += 1

    print(f"Global Counter: {global_counter}")


def global_vs_nonlocal_demo() -> None:
    """
    Compares global and nonlocal variables.
    """

    print("\nGlobal vs Nonlocal")
    print("-" * 40)

    global_counter_demo()

    def outer() -> callable:
        local_counter: int = 0

        def inner() -> int:
            nonlocal local_counter

            local_counter += 1

            return local_counter

        return inner

    counter = outer()

    print(f"Nonlocal Counter: {counter()}")
    print(f"Nonlocal Counter: {counter()}")


# =============================================================================
# SECTION 29 - Part Three Runner
# =============================================================================


def run_part_three() -> None:
    """
    Runs all demonstrations
    from Part Three.
    """

    read_global_variable()

    global_keyword_demo()

    global_variable_best_practice_demo()

    network_device_report()

    nonlocal_demo()

    independent_closures_demo()

    network_closure_demo()

    security_closure_demo()

    global_vs_nonlocal_demo()

# =============================================================================
# SECTION 30 - Lambda Functions
# =============================================================================

"""
A lambda function is a small anonymous function.

Syntax:

lambda arguments: expression

Example:

square = lambda number: number * number
"""


# =============================================================================
# SECTION 31 - Basic Lambda
# =============================================================================


def basic_lambda_demo() -> None:
    """
    Demonstrates a basic lambda function.
    """

    print("\nBasic Lambda Function")
    print("-" * 40)

    square = lambda number: number * number

    print(f"Square of 5: {square(5)}")
    print(f"Square of 10: {square(10)}")


# =============================================================================
# SECTION 32 - Lambda with Multiple Parameters
# =============================================================================


def multiple_parameter_lambda_demo() -> None:
    """
    Demonstrates a lambda function
    with multiple parameters.
    """

    print("\nLambda with Multiple Parameters")
    print("-" * 40)

    add = lambda first, second: first + second

    print(f"10 + 20 = {add(10, 20)}")
    print(f"30 + 40 = {add(30, 40)}")


# =============================================================================
# SECTION 33 - Lambda with Conditional Expression
# =============================================================================


def conditional_lambda_demo() -> None:
    """
    Demonstrates a lambda function
    with a conditional expression.
    """

    print("\nLambda with Conditional Expression")
    print("-" * 40)

    check_status = lambda status: (
        "UP" if status == "up" else "DOWN"
    )

    print(check_status("up"))
    print(check_status("down"))


# =============================================================================
# SECTION 34 - map()
# =============================================================================


def map_demo() -> None:
    """
    Demonstrates the map() function.
    """

    print("\nmap()")
    print("-" * 40)

    numbers: list[int] = [1, 2, 3, 4, 5]

    squared_numbers = list(
        map(
            lambda number: number * number,
            numbers
        )
    )

    print(f"Original: {numbers}")
    print(f"Squared : {squared_numbers}")


# =============================================================================
# SECTION 35 - map() with Network Data
# =============================================================================


def network_map_demo() -> None:
    """
    Demonstrates map() with network data.
    """

    print("\nmap() - Network Example")
    print("-" * 40)

    latencies: list[int] = [
        10,
        20,
        30,
        40
    ]

    increased_latency = list(
        map(
            lambda latency: latency + 5,
            latencies
        )
    )

    print(f"Original Latency: {latencies}")
    print(f"Updated Latency : {increased_latency}")


# =============================================================================
# SECTION 36 - filter()
# =============================================================================


def filter_demo() -> None:
    """
    Demonstrates the filter() function.
    """

    print("\nfilter()")
    print("-" * 40)

    numbers: list[int] = [
        10,
        15,
        20,
        25,
        30
    ]

    even_numbers = list(
        filter(
            lambda number: number % 2 == 0,
            numbers
        )
    )

    print(f"Numbers: {numbers}")
    print(f"Even   : {even_numbers}")


# =============================================================================
# SECTION 37 - filter() with Network Data
# =============================================================================


def active_devices_demo() -> None:
    """
    Filters active network devices.
    """

    print("\nfilter() - Network Example")
    print("-" * 40)

    devices: list[dict[str, str]] = [

        {
            "hostname": "R1",
            "status": "UP"
        },

        {
            "hostname": "R2",
            "status": "DOWN"
        },

        {
            "hostname": "SW1",
            "status": "UP"
        }
    ]

    active_devices = list(
        filter(
            lambda device: device["status"] == "UP",
            devices
        )
    )

    for device in active_devices:
        print(
            f"{device['hostname']} "
            f"-> {device['status']}"
        )


# =============================================================================
# SECTION 38 - sorted() with Lambda
# =============================================================================


def sorted_lambda_demo() -> None:
    """
    Demonstrates sorting with lambda.
    """

    print("\nsorted() with Lambda")
    print("-" * 40)

    devices: list[dict[str, object]] = [

        {
            "hostname": "R1",
            "latency": 30
        },

        {
            "hostname": "R2",
            "latency": 10
        },

        {
            "hostname": "R3",
            "latency": 20
        }
    ]

    sorted_devices = sorted(
        devices,
        key=lambda device: device["latency"]
    )

    for device in sorted_devices:
        print(
            f"{device['hostname']} "
            f"-> {device['latency']} ms"
        )


# =============================================================================
# SECTION 39 - sorted() in Reverse Order
# =============================================================================


def reverse_sort_demo() -> None:
    """
    Demonstrates reverse sorting with lambda.
    """

    print("\nReverse Sorting")
    print("-" * 40)

    ports: list[int] = [
        22,
        443,
        80,
        8080
    ]

    sorted_ports = sorted(
        ports,
        key=lambda port: port,
        reverse=True
    )

    print(f"Ports: {sorted_ports}")


# =============================================================================
# SECTION 40 - Cybersecurity Example
# =============================================================================


def security_alerts_demo() -> None:
    """
    Demonstrates lambda with security alerts.
    """

    print("\nLambda - Cybersecurity Example")
    print("-" * 40)

    alerts: list[dict[str, object]] = [

        {
            "event": "Failed Login",
            "severity": 3
        },

        {
            "event": "Port Scan",
            "severity": 5
        },

        {
            "event": "Malware Detection",
            "severity": 10
        }
    ]

    critical_alerts = list(
        filter(
            lambda alert: alert["severity"] >= 5,
            alerts
        )
    )

    critical_alerts = sorted(
        critical_alerts,
        key=lambda alert: alert["severity"],
        reverse=True
    )

    for alert in critical_alerts:

        print(
            f"{alert['event']} "
            f"-> Severity {alert['severity']}"
        )


# =============================================================================
# SECTION 41 - Combining map(), filter(), and sorted()
# =============================================================================


def combined_lambda_demo() -> None:
    """
    Demonstrates combining functional tools.
    """

    print("\nCombining Lambda Operations")
    print("-" * 40)

    latencies: list[int] = [
        15,
        50,
        10,
        80,
        25
    ]

    high_latency = list(
        filter(
            lambda latency: latency >= 25,
            latencies
        )
    )

    increased_latency = list(
        map(
            lambda latency: latency + 10,
            high_latency
        )
    )

    sorted_latency = sorted(
        increased_latency,
        reverse=True
    )

    print(f"Original : {latencies}")
    print(f"Filtered : {high_latency}")
    print(f"Updated  : {increased_latency}")
    print(f"Sorted   : {sorted_latency}")


# =============================================================================
# SECTION 42 - Part Four Runner
# =============================================================================


def run_part_four() -> None:
    """
    Runs all demonstrations
    from Part Four.
    """

    basic_lambda_demo()

    multiple_parameter_lambda_demo()

    conditional_lambda_demo()

    map_demo()

    network_map_demo()

    filter_demo()

    active_devices_demo()

    sorted_lambda_demo()

    reverse_sort_demo()

    security_alerts_demo()

    combined_lambda_demo()

# =============================================================================
# SECTION 43 - Professional Tips
# =============================================================================


def professional_tips_demo() -> None:
    """
    Demonstrates professional tips for
    variable scope and lambda functions.
    """

    print("\nProfessional Tips")
    print("-" * 40)

    print("✔ Prefer local variables when possible.")
    print("✔ Pass data through function parameters.")
    print("✔ Return values instead of using global state.")
    print("✔ Keep lambda expressions simple.")
    print("✔ Use named functions for complex logic.")
    print("✔ Use closures when they provide a clear benefit.")


# =============================================================================
# SECTION 44 - Best Practices
# =============================================================================


def best_practices_demo() -> None:
    """
    Demonstrates best practices for
    scope and lambda functions.
    """

    print("\nBest Practices")
    print("-" * 40)

    print("✔ Follow the LEGB rule.")
    print("✔ Avoid unnecessary global variables.")
    print("✔ Keep functions focused.")
    print("✔ Use meaningful variable names.")
    print("✔ Prefer readable code over clever code.")
    print("✔ Add type hints to important functions.")


# =============================================================================
# SECTION 45 - Common Mistakes
# =============================================================================


def common_mistakes_demo() -> None:
    """
    Demonstrates common mistakes related
    to scope and lambda functions.
    """

    print("\nCommon Mistakes")
    print("-" * 40)

    print("✘ Modifying global variables unnecessarily.")
    print("✘ Confusing local and global scope.")
    print("✘ Using global for normal data passing.")
    print("✘ Writing complicated lambda expressions.")
    print("✘ Forgetting that closures preserve state.")


# =============================================================================
# SECTION 46 - Scope Cheat Sheet
# =============================================================================

"""
Scope Cheat Sheet
=================

Local
-----
Variables created inside a function.


Enclosing
---------
Variables from an outer function
used by an inner function.


Global
------
Variables defined at module level.


Built-in
--------
Names provided by Python itself.


LEGB
----
Local
Enclosing
Global
Built-in


global
------
Used when a function needs to modify
a global variable.


nonlocal
--------
Used when an inner function needs
to modify a variable from an enclosing function.


Lambda
------
Small anonymous function.

Example:

square = lambda number: number * number
"""


# =============================================================================
# SECTION 47 - Lambda Cheat Sheet
# =============================================================================

"""
Lambda Cheat Sheet
==================

Basic Lambda

square = lambda x: x * x


Multiple Parameters

add = lambda a, b: a + b


map()

map(
    lambda x: x * 2,
    numbers
)


filter()

filter(
    lambda x: x > 10,
    numbers
)


sorted()

sorted(
    devices,
    key=lambda device: device["latency"]
)
"""


# =============================================================================
# SECTION 48 - Interview Questions
# =============================================================================

"""
Interview Questions
-------------------

1. What is variable scope?

2. What does LEGB stand for?

3. What is the difference between local
   and global variables?

4. What is an enclosing scope?

5. What is the purpose of the global keyword?

6. What is the purpose of the nonlocal keyword?

7. What is a nested function?

8. What is a closure?

9. What is a lambda function?

10. What is the difference between map()
    and filter()?

11. How can lambda be used with sorted()?

12. When should you avoid using lambda?

"""


# =============================================================================
# SECTION 49 - Coding Exercises
# =============================================================================

"""
Coding Exercises
----------------

Exercise 1
Create a function that receives a list of
IP addresses and returns only private addresses.


Exercise 2
Create a function that filters network devices
whose status is "UP".


Exercise 3
Use sorted() and lambda to sort devices
according to CPU usage.


Exercise 4
Create a counter using nonlocal.


Exercise 5
Create a function that receives security alerts
and returns only HIGH severity alerts.
"""


# =============================================================================
# SECTION 50 - Challenge Exercises
# =============================================================================

"""
Challenge Exercises
-------------------

Challenge 1
Create a network device monitor using:

- Nested functions
- nonlocal
- Closures


Challenge 2
Create a security alert processor using:

- filter()
- map()
- sorted()
- lambda


Challenge 3
Create an inventory processor that:

- Filters active devices.
- Sorts devices by IP.
- Extracts hostnames.
- Returns the final list.
"""


# =============================================================================
# SECTION 51 - Mini Project
# =============================================================================


def create_network_monitor() -> callable:
    """
    Creates a network monitoring system.

    The closure maintains the number of
    monitoring checks performed.
    """

    checks: int = 0

    def monitor(
        devices: list[dict[str, object]]
    ) -> dict[str, object]:
        """
        Processes network devices.
        """

        nonlocal checks

        checks += 1

        active_devices = list(
            filter(
                lambda device: device["status"] == "UP",
                devices
            )
        )

        sorted_devices = sorted(
            active_devices,
            key=lambda device: device["latency"]
        )

        hostnames = list(
            map(
                lambda device: device["hostname"],
                sorted_devices
            )
        )

        return {
            "check_number": checks,
            "active_devices": sorted_devices,
            "hostnames": hostnames
        }

    return monitor


# =============================================================================
# SECTION 52 - Mini Project Demo
# =============================================================================


def network_monitor_project() -> None:
    """
    Demonstrates the Network Monitor project.
    """

    print("\nNetwork Monitor Project")
    print("-" * 40)

    devices: list[dict[str, object]] = [

        {
            "hostname": "R1",
            "ip": "192.168.1.1",
            "status": "UP",
            "latency": 15
        },

        {
            "hostname": "R2",
            "ip": "192.168.1.2",
            "status": "DOWN",
            "latency": 80
        },

        {
            "hostname": "SW1",
            "ip": "192.168.1.10",
            "status": "UP",
            "latency": 10
        },

        {
            "hostname": "SW2",
            "ip": "192.168.1.11",
            "status": "UP",
            "latency": 25
        }
    ]

    monitor = create_network_monitor()

    report = monitor(devices)

    print(f"Monitoring Check: {report['check_number']}")

    print("\nActive Devices:")

    for device in report["active_devices"]:

        print(
            f"{device['hostname']} | "
            f"{device['ip']} | "
            f"{device['latency']} ms"
        )

    print("\nHostnames:")

    for hostname in report["hostnames"]:

        print(hostname)


# =============================================================================
# SECTION 53 - Final Lesson Summary
# =============================================================================


def lesson_summary() -> None:
    """
    Displays the main concepts covered
    in this lesson.
    """

    print("\nLesson Summary")
    print("-" * 40)

    topics: list[str] = [

        "Variable Scope",

        "Local Scope",

        "Enclosing Scope",

        "Global Scope",

        "Built-in Scope",

        "LEGB Rule",

        "global Keyword",

        "nonlocal Keyword",

        "Nested Functions",

        "Closures",

        "Lambda Functions",

        "map()",

        "filter()",

        "sorted()"
    ]

    for topic in topics:

        print(f"✔ {topic}")


# =============================================================================
# SECTION 54 - Next Lesson
# =============================================================================

"""
Next Lesson
-----------

17_modules_packages.py

Topics:

✔ Modules
✔ Import
✔ From Import
✔ Aliases
✔ __name__
✔ __main__
✔ Packages
✔ __init__.py
✔ Standard Library
✔ Creating Custom Modules
"""


# =============================================================================
# SECTION 55 - Main Function
# =============================================================================


def main() -> None:
    """
    Runs the complete lesson.
    """

    # Part 1
    run_part_one()

    # Part 2
    run_part_two()

    # Part 3
    run_part_three()

    # Part 4
    run_part_four()

    # Part 5
    professional_tips_demo()

    best_practices_demo()

    common_mistakes_demo()

    network_monitor_project()

    lesson_summary()


# =============================================================================
# PROGRAM ENTRY POINT
# =============================================================================


if __name__ == "__main__":
    main()
