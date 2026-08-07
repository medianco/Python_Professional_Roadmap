"""
===============================================================================
File        : 11_if_else.py
Author      : Mohammed AL-Dubai
Course      : Python Professional Roadmap
Lesson      : Conditional Statements (if, elif, else)

Description:
    This lesson explains how Python makes decisions using
    conditional statements.

Learning Objectives
-------------------
After completing this lesson, you will be able to:

✔ Understand conditional statements.
✔ Use comparison operators.
✔ Write if, if-else, and if-elif-else statements.
✔ Build decision-making logic.
✔ Apply conditions in networking and cybersecurity scenarios.

===============================================================================
"""


# =============================================================================
# SECTION 1 - Introduction to Conditional Statements
# =============================================================================


"""
Conditional statements allow a program to make decisions.

General Syntax:

if condition:
    statement

elif another_condition:
    statement

else:
    statement

Conditions always evaluate to either:

True

or

False
"""


def introduction_demo() -> None:
    """
    Demonstrates the concept of conditional statements.
    """

    print("\nIntroduction to Conditional Statements")
    print("-" * 40)

    device_status: str = "UP"

    if device_status == "UP":
        print("Device is operational.")

    print("Condition evaluation completed.")


# =============================================================================
# SECTION 2 - Comparison Operators
# =============================================================================


def comparison_operators_demo() -> None:
    """
    Demonstrates comparison operators.
    """

    print("\nComparison Operators")
    print("-" * 40)

    x: int = 20
    y: int = 10

    print("x == y :", x == y)
    print("x != y :", x != y)
    print("x > y  :", x > y)
    print("x < y  :", x < y)
    print("x >= y :", x >= y)
    print("x <= y :", x <= y)


# =============================================================================
# SECTION 3 - Basic if Statement
# =============================================================================


def basic_if_demo() -> None:
    """
    Demonstrates a simple if statement.
    """

    print("\nBasic if Statement")
    print("-" * 40)

    port: int = 22

    if port == 22:
        print("SSH service detected.")

    print("Scan completed.")


# =============================================================================
# SECTION 4 - if...else Statement
# =============================================================================


def if_else_demo() -> None:
    """
    Demonstrates if...else statement.
    """

    print("\nif...else Statement")
    print("-" * 40)

    service_status: str = "DOWN"

    if service_status == "UP":
        print("Service is available.")
    else:
        print("Service is unavailable.")


# =============================================================================
# SECTION 5 - if...elif...else Statement
# =============================================================================


def if_elif_else_demo() -> None:
    """
    Demonstrates multiple conditions.
    """

    print("\nif...elif...else Statement")
    print("-" * 40)

    severity: str = "High"

    if severity == "Critical":
        print("Immediate response required.")
    elif severity == "High":
        print("Notify SOC team.")
    elif severity == "Medium":
        print("Monitor the event.")
    else:
        print("Informational event.")


# =============================================================================
# SECTION 6 - Boolean Values
# =============================================================================


def boolean_demo() -> None:
    """
    Demonstrates Boolean values.
    """

    print("\nBoolean Values")
    print("-" * 40)

    firewall_enabled: bool = True
    vpn_connected: bool = False

    print("Firewall Enabled :", firewall_enabled)
    print("VPN Connected    :", vpn_connected)

    if firewall_enabled:
        print("Firewall protection is active.")

    if not vpn_connected:
        print("VPN connection is not established.")


# =============================================================================
# SECTION 7 - Basic Nested if
# =============================================================================


def nested_if_demo() -> None:
    """
    Demonstrates a simple nested if statement.
    """

    print("\nNested if Statement")
    print("-" * 40)

    device_online: bool = True
    ssh_enabled: bool = True

    if device_online:

        print("Device is online.")

        if ssh_enabled:
            print("SSH access is available.")


# =============================================================================
# SECTION 8 - Network Example
# =============================================================================


def network_status_demo() -> None:
    """
    Demonstrates decision making
    in a networking scenario.
    """

    print("\nNetwork Status Example")
    print("-" * 40)

    interface_status: str = "UP"

    if interface_status == "UP":
        print("Interface is forwarding traffic.")
    else:
        print("Interface is down.")


# =============================================================================
# SECTION 9 - Cybersecurity Example
# =============================================================================


def security_alert_demo() -> None:
    """
    Demonstrates conditional logic
    in cybersecurity.
    """

    print("\nSecurity Alert Example")
    print("-" * 40)

    failed_logins: int = 7

    if failed_logins >= 5:
        print("Possible brute-force attack detected.")
    else:
        print("Login activity is normal.")


# =============================================================================
# SECTION 10 - Main Function
# =============================================================================

def run_part_one() -> None:
    """
    Runs all demonstrations
    from Part One.
    """

    introduction_demo()
    comparison_operators_demo()
    basic_if_demo()
    if_else_demo()
    if_elif_else_demo()
    boolean_demo()
    nested_if_demo()
    network_status_demo()
    security_alert_demo()
  
# =============================================================================
# SECTION 11 - Logical Operator: and
# =============================================================================


def logical_and_demo() -> None:
    """
    Demonstrates the logical AND operator.
    """

    print("\nLogical Operator: and")
    print("-" * 40)

    device_online: bool = True
    ssh_enabled: bool = True

    if device_online and ssh_enabled:
        print("SSH connection is allowed.")
    else:
        print("SSH connection is unavailable.")


# =============================================================================
# SECTION 12 - Logical Operator: or
# =============================================================================


def logical_or_demo() -> None:
    """
    Demonstrates the logical OR operator.
    """

    print("\nLogical Operator: or")
    print("-" * 40)

    admin_user: bool = False
    operator_user: bool = True

    if admin_user or operator_user:
        print("Access granted.")
    else:
        print("Access denied.")


# =============================================================================
# SECTION 13 - Logical Operator: not
# =============================================================================


def logical_not_demo() -> None:
    """
    Demonstrates the logical NOT operator.
    """

    print("\nLogical Operator: not")
    print("-" * 40)

    maintenance_mode: bool = False

    if not maintenance_mode:
        print("System is available.")
    else:
        print("System is under maintenance.")


# =============================================================================
# SECTION 14 - Compound Conditions
# =============================================================================


def compound_conditions_demo() -> None:
    """
    Demonstrates compound conditions.
    """

    print("\nCompound Conditions")
    print("-" * 40)

    cpu_usage: int = 82
    memory_usage: int = 75

    if cpu_usage > 80 and memory_usage > 70:
        print("High system resource utilization.")
    else:
        print("System resources are within limits.")


# =============================================================================
# SECTION 15 - Range Checking
# =============================================================================


def range_check_demo() -> None:
    """
    Demonstrates checking numeric ranges.
    """

    print("\nRange Checking")
    print("-" * 40)

    signal_strength: int = 72

    if 70 <= signal_strength <= 100:
        print("Signal strength is excellent.")
    elif 50 <= signal_strength < 70:
        print("Signal strength is acceptable.")
    else:
        print("Weak signal.")


# =============================================================================
# SECTION 16 - Ternary Operator
# =============================================================================


def ternary_operator_demo() -> None:
    """
    Demonstrates the ternary operator.
    """

    print("\nTernary Operator")
    print("-" * 40)

    service_status: str = "UP"

    message = (
        "Service Available"
        if service_status == "UP"
        else "Service Unavailable"
    )

    print(message)


# =============================================================================
# SECTION 17 - User Authentication Example
# =============================================================================


def authentication_demo() -> None:
    """
    Demonstrates user authentication.
    """

    print("\nUser Authentication")
    print("-" * 40)

    username: str = "admin"
    password: str = "Cisco123"

    if username == "admin" and password == "Cisco123":
        print("Authentication successful.")
    else:
        print("Invalid username or password.")


# =============================================================================
# SECTION 18 - Network Access Control
# =============================================================================


def network_access_demo() -> None:
    """
    Demonstrates network access control.
    """

    print("\nNetwork Access Control")
    print("-" * 40)

    vlan: int = 10
    authenticated: bool = True

    if authenticated and vlan == 10:
        print("Access to VLAN 10 granted.")
    else:
        print("Network access denied.")


# =============================================================================
# SECTION 19 - Security Alert Classification
# =============================================================================


def alert_classification_demo() -> None:
    """
    Demonstrates alert classification.
    """

    print("\nSecurity Alert Classification")
    print("-" * 40)

    severity: str = "Critical"

    if severity == "Critical":
        print("Escalate immediately.")
    elif severity == "High":
        print("Notify SOC analyst.")
    elif severity == "Medium":
        print("Monitor the event.")
    else:
        print("Log the event.")


# =============================================================================
# SECTION 20 - Run Part Two
# =============================================================================


def run_part_two() -> None:
    """
    Runs all demonstrations
    from Part Two.
    """

    logical_and_demo()
    logical_or_demo()
    logical_not_demo()
    compound_conditions_demo()
    range_check_demo()
    ternary_operator_demo()
    authentication_demo()
    network_access_demo()
    alert_classification_demo()

# =============================================================================
# SECTION 21 - Advanced Nested if
# =============================================================================


def advanced_nested_if_demo() -> None:
    """
    Demonstrates advanced nested if statements.
    """

    print("\nAdvanced Nested if")
    print("-" * 40)

    device_online: bool = True
    ssh_enabled: bool = True
    authenticated: bool = True

    if device_online:

        print("Device is online.")

        if ssh_enabled:

            print("SSH service is enabled.")

            if authenticated:
                print("SSH session established.")
            else:
                print("Authentication failed.")

        else:
            print("SSH service is disabled.")

    else:
        print("Device is offline.")


# =============================================================================
# SECTION 22 - Port Classification
# =============================================================================


def port_classification_demo() -> None:
    """
    Demonstrates classifying network ports.
    """

    print("\nPort Classification")
    print("-" * 40)

    port: int = 443

    if port == 22:
        print("SSH")

    elif port == 23:
        print("Telnet")

    elif port == 53:
        print("DNS")

    elif port == 80:
        print("HTTP")

    elif port == 443:
        print("HTTPS")

    else:
        print("Unknown service.")


# =============================================================================
# SECTION 23 - Interface Health Check
# =============================================================================


def interface_health_demo() -> None:
    """
    Demonstrates interface monitoring.
    """

    print("\nInterface Health Check")
    print("-" * 40)

    interface_status: str = "UP"
    error_count: int = 2

    if interface_status == "UP" and error_count == 0:

        print("Interface is healthy.")

    elif interface_status == "UP":

        print("Interface is operational with errors.")

    else:

        print("Interface is down.")


# =============================================================================
# SECTION 24 - Firewall Decision
# =============================================================================


def firewall_decision_demo() -> None:
    """
    Demonstrates firewall access logic.
    """

    print("\nFirewall Decision")
    print("-" * 40)

    source_ip: str = "10.0.0.15"
    allowed_network: bool = True

    if allowed_network:
        print(f"Traffic from {source_ip} is allowed.")
    else:
        print(f"Traffic from {source_ip} is blocked.")


# =============================================================================
# SECTION 25 - User Authorization
# =============================================================================


def authorization_demo() -> None:
    """
    Demonstrates role-based access control.
    """

    print("\nRole-Based Authorization")
    print("-" * 40)

    role: str = "Network Engineer"

    if role == "Administrator":
        print("Full access granted.")

    elif role == "Network Engineer":
        print("Configuration access granted.")

    elif role == "SOC Analyst":
        print("Security monitoring access granted.")

    else:
        print("Read-only access.")


# =============================================================================
# SECTION 26 - Login Monitoring
# =============================================================================


def login_monitoring_demo() -> None:
    """
    Demonstrates login monitoring.
    """

    print("\nLogin Monitoring")
    print("-" * 40)

    failed_attempts: int = 6

    if failed_attempts >= 5:

        print("Potential brute-force attack detected.")

    else:

        print("Normal login activity.")


# =============================================================================
# SECTION 27 - Network Troubleshooting
# =============================================================================


def troubleshooting_demo() -> None:
    """
    Demonstrates troubleshooting logic.
    """

    print("\nNetwork Troubleshooting")
    print("-" * 40)

    cable_connected: bool = True
    interface_enabled: bool = False

    if not cable_connected:

        print("Connect the network cable.")

    elif not interface_enabled:

        print("Enable the interface.")

    else:

        print("Continue troubleshooting Layer 3.")


# =============================================================================
# SECTION 28 - Network Automation Example
# =============================================================================


def network_automation_demo() -> None:
    """
    Demonstrates decision making
    in network automation.
    """

    print("\nNetwork Automation Example")
    print("-" * 40)

    configuration_changed: bool = True

    if configuration_changed:

        print("Save configuration.")

    else:

        print("No changes detected.")


# =============================================================================
# SECTION 29 - SOC Alert Processing
# =============================================================================


def soc_processing_demo() -> None:
    """
    Demonstrates SOC alert processing.
    """

    print("\nSOC Alert Processing")
    print("-" * 40)

    severity: str = "Critical"

    if severity == "Critical":

        print("Notify Incident Response Team.")

    elif severity == "High":

        print("Notify SOC Team.")

    elif severity == "Medium":

        print("Create investigation ticket.")

    else:

        print("Archive event.")


# =============================================================================
# SECTION 30 - Run Part Three
# =============================================================================


def run_part_three() -> None:
    """
    Runs all demonstrations
    from Part Three.
    """

    advanced_nested_if_demo()
    port_classification_demo()
    interface_health_demo()
    firewall_decision_demo()
    authorization_demo()
    login_monitoring_demo()
    troubleshooting_demo()
    network_automation_demo()
    soc_processing_demo()


# =============================================================================
# SECTION 31 - Professional Tips
# =============================================================================


def professional_tips_demo() -> None:
    """
    Demonstrates professional tips
    for writing conditional statements.
    """

    print("\nProfessional Tips")
    print("-" * 40)

    print("✔ Keep conditions simple.")
    print("✔ Avoid deeply nested if statements.")
    print("✔ Use descriptive variable names.")
    print("✔ Group related conditions.")
    print("✔ Prefer readability over clever code.")


# =============================================================================
# SECTION 32 - Best Practices
# =============================================================================


def best_practices_demo() -> None:
    """
    Demonstrates best practices.
    """

    print("\nBest Practices")
    print("-" * 40)

    print("✔ Use elif instead of multiple if statements.")
    print("✔ Handle unexpected values.")
    print("✔ Use constants when appropriate.")
    print("✔ Keep decision logic organized.")


# =============================================================================
# SECTION 33 - Common Mistakes
# =============================================================================


def common_mistakes_demo() -> None:
    """
    Demonstrates common mistakes.
    """

    print("\nCommon Mistakes")
    print("-" * 40)

    print("✘ Forgetting indentation.")
    print("✘ Using = instead of ==.")
    print("✘ Writing unnecessary nested if statements.")
    print("✘ Ignoring else conditions.")
    print("✘ Creating overly complex conditions.")


# =============================================================================
# SECTION 34 - Performance Tips
# =============================================================================


def performance_tips_demo() -> None:
    """
    Demonstrates performance tips.
    """

    print("\nPerformance Tips")
    print("-" * 40)

    print("✔ Put the most common condition first.")
    print("✔ Avoid duplicate comparisons.")
    print("✔ Exit early when possible.")
    print("✔ Keep conditions efficient.")


# =============================================================================
# SECTION 35 - Decision Cheat Sheet
# =============================================================================

"""
Decision Cheat Sheet
====================

if

if condition:
    ...


if / else

if condition:
    ...
else:
    ...


if / elif / else

if condition:
    ...
elif condition:
    ...
else:
    ...


Logical Operators

and

or

not


Comparison Operators

==

!=

>

<

>=

<=


Ternary Operator

value = A if condition else B
"""


# =============================================================================
# SECTION 36 - Interview Questions
# =============================================================================

"""
Interview Questions
-------------------

1. What is a Boolean expression?

2. Difference between if and elif?

3. Difference between = and == ?

4. What does not do?

5. When should and be used?

6. When should or be used?

7. What is a ternary operator?

8. How does Python evaluate conditions?

9. Explain nested if statements.

10. How are conditional statements used in network automation?
"""


# =============================================================================
# SECTION 37 - Coding Exercises
# =============================================================================

"""
Coding Exercises
----------------

Exercise 1

Check if a port is SSH.


Exercise 2

Determine whether a service is UP or DOWN.


Exercise 3

Validate administrator login.


Exercise 4

Classify alert severity.


Exercise 5

Build a simple access control system.
"""


# =============================================================================
# SECTION 38 - Mini Project
# =============================================================================


def mini_project_description() -> None:
    """
    Mini Project

    Network Access Control Simulator

    Requirements

    - Authenticate users.
    - Check user role.
    - Verify VLAN membership.
    - Grant or deny access.
    - Display result.

    Skills

    ✔ if

    ✔ elif

    ✔ else

    ✔ Logical Operators

    ✔ Decision Making
    """

    print("\nMini Project")
    print("-" * 40)

    print("Network Access Control Simulator")


# =============================================================================
# SECTION 39 - What's Next
# =============================================================================

"""
Next Lesson

12_match_case.py

Topics

✔ match

✔ case

✔ Multiple Patterns

✔ Wildcards

✔ Pattern Matching

✔ Network Examples

✔ Cybersecurity Examples
"""


# =============================================================================
# SECTION 40 - Main Function
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
