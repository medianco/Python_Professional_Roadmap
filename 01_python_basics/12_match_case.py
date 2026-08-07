"""
===============================================================================
File        : 12_match_case.py
Author      : Mohammed AL-Dubai
Course      : Python Basics
Lesson      : Match Case (Pattern Matching)

Description:
    This lesson explains Python's match-case statement
    introduced in Python 3.10.

Learning Objectives
-------------------
After completing this lesson, you will be able to:

✔ Understand pattern matching.
✔ Replace long if-elif-else statements.
✔ Match numbers and strings.
✔ Use the wildcard pattern.
✔ Apply match-case in networking and cybersecurity.

===============================================================================
"""


# =============================================================================
# SECTION 1 - Introduction to Match Case
# =============================================================================


"""
The match statement compares one value
against multiple patterns.

General Syntax:

match value:

    case pattern:
        ...

    case pattern:
        ...

    case _:
        ...

The underscore (_) represents the default case.
"""


def introduction_demo() -> None:
    """
    Demonstrates the basic match-case syntax.
    """

    print("\nIntroduction to Match Case")
    print("-" * 40)

    port: int = 22

    match port:

        case 22:
            print("SSH")

        case _:
            print("Unknown")


# =============================================================================
# SECTION 2 - Matching Numbers
# =============================================================================


def matching_numbers_demo() -> None:
    """
    Demonstrates matching integer values.
    """

    print("\nMatching Numbers")
    print("-" * 40)

    status_code: int = 200

    match status_code:

        case 200:
            print("OK")

        case 404:
            print("Not Found")

        case 500:
            print("Internal Server Error")

        case _:
            print("Unknown Status Code")


# =============================================================================
# SECTION 3 - Matching Strings
# =============================================================================


def matching_strings_demo() -> None:
    """
    Demonstrates matching string values.
    """

    print("\nMatching Strings")
    print("-" * 40)

    protocol: str = "HTTPS"

    match protocol:

        case "HTTP":
            print("Web Traffic")

        case "HTTPS":
            print("Secure Web Traffic")

        case "SSH":
            print("Remote Management")

        case _:
            print("Unknown Protocol")


# =============================================================================
# SECTION 4 - Wildcard Pattern
# =============================================================================


def wildcard_demo() -> None:
    """
    Demonstrates the wildcard pattern.
    """

    print("\nWildcard Pattern")
    print("-" * 40)

    vlan: int = 99

    match vlan:

        case 10:
            print("Users")

        case 20:
            print("Servers")

        case 30:
            print("Management")

        case _:
            print("Unknown VLAN")


# =============================================================================
# SECTION 5 - Network Example
# =============================================================================


def network_service_demo() -> None:
    """
    Demonstrates identifying network services.
    """

    print("\nNetwork Service Detection")
    print("-" * 40)

    port: int = 443

    match port:

        case 22:
            print("SSH")

        case 53:
            print("DNS")

        case 80:
            print("HTTP")

        case 443:
            print("HTTPS")

        case _:
            print("Unknown Service")


# =============================================================================
# SECTION 6 - Cybersecurity Example
# =============================================================================


def cybersecurity_demo() -> None:
    """
    Demonstrates alert classification.
    """

    print("\nCybersecurity Alert")
    print("-" * 40)

    severity: str = "Critical"

    match severity:

        case "Critical":
            print("Immediate Incident Response")

        case "High":
            print("Notify SOC Team")

        case "Medium":
            print("Investigate")

        case "Low":
            print("Log Event")

        case _:
            print("Unknown Severity")


# =============================================================================
# SECTION 7 - Device Vendor Example
# =============================================================================


def vendor_demo() -> None:
    """
    Demonstrates matching device vendors.
    """

    print("\nNetwork Vendor Detection")
    print("-" * 40)

    vendor: str = "Cisco"

    match vendor:

        case "Cisco":
            print("Cisco IOS Device")

        case "Juniper":
            print("JunOS Device")

        case "Arista":
            print("EOS Device")

        case _:
            print("Unknown Vendor")


# =============================================================================
# SECTION 8 - Main Function (Part One)
# =============================================================================


def run_part_one() -> None:
    """
    Runs all demonstrations
    from Part One.
    """

    introduction_demo()
    matching_numbers_demo()
    matching_strings_demo()
    wildcard_demo()
    network_service_demo()
    cybersecurity_demo()
    vendor_demo()

# =============================================================================
# SECTION 9 - Multiple Patterns
# =============================================================================


def multiple_patterns_demo() -> None:
    """
    Demonstrates matching multiple patterns.
    """

    print("\nMultiple Patterns")
    print("-" * 40)

    protocol: str = "HTTP"

    match protocol:

        case "HTTP" | "HTTPS":
            print("Web Service")

        case "FTP" | "SFTP":
            print("File Transfer")

        case "SSH":
            print("Remote Access")

        case _:
            print("Unknown Protocol")


# =============================================================================
# SECTION 10 - Guard Conditions
# =============================================================================


def guard_conditions_demo() -> None:
    """
    Demonstrates guard conditions.
    """

    print("\nGuard Conditions")
    print("-" * 40)

    port: int = 443

    match port:

        case value if value < 1024:
            print("Well-Known Port")

        case value if value < 49152:
            print("Registered Port")

        case _:
            print("Dynamic Port")


# =============================================================================
# SECTION 11 - Matching Tuples
# =============================================================================


def tuple_matching_demo() -> None:
    """
    Demonstrates tuple pattern matching.
    """

    print("\nTuple Matching")
    print("-" * 40)

    packet: tuple[str, int] = (
        "TCP",
        443
    )

    match packet:

        case ("TCP", 443):
            print("HTTPS Traffic")

        case ("TCP", 22):
            print("SSH Traffic")

        case ("UDP", 53):
            print("DNS Query")

        case _:
            print("Unknown Packet")


# =============================================================================
# SECTION 12 - Matching Lists
# =============================================================================


def list_matching_demo() -> None:
    """
    Demonstrates list pattern matching.
    """

    print("\nList Matching")
    print("-" * 40)

    command: list[str] = [
        "show",
        "version"
    ]

    match command:

        case ["show", "version"]:
            print("Display device version")

        case ["show", "ip"]:
            print("Display IP information")

        case _:
            print("Unknown Command")


# =============================================================================
# SECTION 13 - Nested Patterns
# =============================================================================


def nested_patterns_demo() -> None:
    """
    Demonstrates nested pattern matching.
    """

    print("\nNested Patterns")
    print("-" * 40)

    device: tuple[str, tuple[str, str]] = (
        "Router",
        (
            "Cisco",
            "IOS-XE"
        )
    )

    match device:

        case ("Router", ("Cisco", os)):
            print(f"Cisco Router running {os}")

        case ("Switch", ("Cisco", os)):
            print(f"Cisco Switch running {os}")

        case _:
            print("Unknown Device")


# =============================================================================
# SECTION 14 - Network Command Recognition
# =============================================================================


def network_command_demo() -> None:
    """
    Demonstrates recognizing CLI commands.
    """

    print("\nNetwork Command Recognition")
    print("-" * 40)

    command: str = "show ip route"

    match command:

        case "show version":
            print("Display software version")

        case "show ip interface brief":
            print("Display interface summary")

        case "show ip route":
            print("Display routing table")

        case _:
            print("Unsupported Command")


# =============================================================================
# SECTION 15 - Interface Type Detection
# =============================================================================


def interface_type_demo() -> None:
    """
    Demonstrates interface type detection.
    """

    print("\nInterface Type Detection")
    print("-" * 40)

    interface: str = "GigabitEthernet"

    match interface:

        case "FastEthernet":
            print("100 Mbps")

        case "GigabitEthernet":
            print("1 Gbps")

        case "TenGigabitEthernet":
            print("10 Gbps")

        case _:
            print("Unknown Interface")


# =============================================================================
# SECTION 16 - Routing Protocol Detection
# =============================================================================


def routing_protocol_demo() -> None:
    """
    Demonstrates routing protocol detection.
    """

    print("\nRouting Protocol Detection")
    print("-" * 40)

    protocol: str = "OSPF"

    match protocol:

        case "OSPF":
            print("Link-State Routing")

        case "EIGRP":
            print("Advanced Distance Vector")

        case "RIP":
            print("Distance Vector")

        case "BGP":
            print("Path Vector")

        case _:
            print("Unknown Routing Protocol")


# =============================================================================
# SECTION 17 - Run Part Two
# =============================================================================


def run_part_two() -> None:
    """
    Runs all demonstrations
    from Part Two.
    """

    multiple_patterns_demo()
    guard_conditions_demo()
    tuple_matching_demo()
    list_matching_demo()
    nested_patterns_demo()
    network_command_demo()
    interface_type_demo()
    routing_protocol_demo()

# =============================================================================
# SECTION 18 - Pattern Capture
# =============================================================================


def pattern_capture_demo() -> None:
    """
    Demonstrates value capture
    with match-case.
    """

    print("\nPattern Capture")
    print("-" * 40)

    http_status: int = 404

    match http_status:

        case code if 200 <= code < 300:
            print(f"Success: {code}")

        case code if 300 <= code < 400:
            print(f"Redirection: {code}")

        case code if 400 <= code < 500:
            print(f"Client Error: {code}")

        case code if 500 <= code < 600:
            print(f"Server Error: {code}")

        case _:
            print("Unknown Status")


# =============================================================================
# SECTION 19 - HTTP Status Classification
# =============================================================================


def http_status_demo() -> None:
    """
    Demonstrates HTTP status processing.
    """

    print("\nHTTP Status Classification")
    print("-" * 40)

    status: int = 503

    match status:

        case 200:
            print("OK")

        case 301 | 302:
            print("Redirect")

        case 401:
            print("Unauthorized")

        case 403:
            print("Forbidden")

        case 404:
            print("Not Found")

        case 500 | 502 | 503:
            print("Server Error")

        case _:
            print("Unhandled Status")


# =============================================================================
# SECTION 20 - Security Event Classification
# =============================================================================


def security_event_demo() -> None:
    """
    Demonstrates security event classification.
    """

    print("\nSecurity Event Classification")
    print("-" * 40)

    event: str = "PORT_SCAN"

    match event:

        case "FAILED_LOGIN":
            print("Authentication Failure")

        case "PORT_SCAN":
            print("Reconnaissance Activity")

        case "MALWARE":
            print("Malware Detected")

        case "RANSOMWARE":
            print("Critical Threat")

        case _:
            print("Unknown Event")


# =============================================================================
# SECTION 21 - Login Monitoring
# =============================================================================


def login_monitoring_demo() -> None:
    """
    Demonstrates login event processing.
    """

    print("\nLogin Monitoring")
    print("-" * 40)

    login_result: str = "FAILED"

    match login_result:

        case "SUCCESS":
            print("User authenticated")

        case "FAILED":
            print("Authentication failed")

        case "LOCKED":
            print("Account locked")

        case _:
            print("Unknown Login State")


# =============================================================================
# SECTION 22 - Device Type Detection
# =============================================================================


def device_detection_demo() -> None:
    """
    Demonstrates device classification.
    """

    print("\nDevice Type Detection")
    print("-" * 40)

    device: str = "Firewall"

    match device:

        case "Router":
            print("Layer 3 Device")

        case "Switch":
            print("Layer 2 Device")

        case "Firewall":
            print("Security Appliance")

        case "Access Point":
            print("Wireless Device")

        case _:
            print("Unknown Device")


# =============================================================================
# SECTION 23 - API Response Processing
# =============================================================================


def api_response_demo() -> None:
    """
    Demonstrates API response handling.
    """

    print("\nAPI Response Processing")
    print("-" * 40)

    response: str = "SUCCESS"

    match response:

        case "SUCCESS":
            print("Configuration completed")

        case "TIMEOUT":
            print("Retry request")

        case "UNAUTHORIZED":
            print("Authentication required")

        case "NOT_FOUND":
            print("Requested object not found")

        case _:
            print("Unexpected API response")


# =============================================================================
# SECTION 24 - Network Automation Dispatcher
# =============================================================================


def automation_dispatcher_demo() -> None:
    """
    Demonstrates network automation commands.
    """

    print("\nNetwork Automation Dispatcher")
    print("-" * 40)

    command: str = "backup"

    match command:

        case "backup":
            print("Creating configuration backup")

        case "reload":
            print("Reloading device")

        case "save":
            print("Saving running configuration")

        case "interfaces":
            print("Collecting interface status")

        case _:
            print("Unknown Automation Command")


# =============================================================================
# SECTION 25 - SOC Alert Processing
# =============================================================================


def soc_alert_demo() -> None:
    """
    Demonstrates SOC alert handling.
    """

    print("\nSOC Alert Processing")
    print("-" * 40)

    severity: str = "HIGH"

    match severity:

        case "CRITICAL":
            print("Notify Incident Response")

        case "HIGH":
            print("Escalate to SOC")

        case "MEDIUM":
            print("Investigate")

        case "LOW":
            print("Log Event")

        case _:
            print("Unknown Severity")


# =============================================================================
# SECTION 26 - Threat Classification
# =============================================================================


def threat_classification_demo() -> None:
    """
    Demonstrates threat classification.
    """

    print("\nThreat Classification")
    print("-" * 40)

    threat: str = "Phishing"

    match threat:

        case "Phishing":
            print("Email Attack")

        case "DDoS":
            print("Availability Attack")

        case "SQL Injection":
            print("Web Application Attack")

        case "Ransomware":
            print("Encryption Malware")

        case _:
            print("Unknown Threat")


# =============================================================================
# SECTION 27 - Command Execution
# =============================================================================


def command_execution_demo() -> None:
    """
    Demonstrates command execution.
    """

    print("\nCommand Execution")
    print("-" * 40)

    operation: str = "start"

    match operation:

        case "start":
            print("Starting service")

        case "stop":
            print("Stopping service")

        case "restart":
            print("Restarting service")

        case _:
            print("Invalid Operation")


# =============================================================================
# SECTION 28 - Run Part Three
# =============================================================================


def run_part_three() -> None:
    """
    Runs all demonstrations
    from Part Three.
    """

    pattern_capture_demo()
    http_status_demo()
    security_event_demo()
    login_monitoring_demo()
    device_detection_demo()
    api_response_demo()
    automation_dispatcher_demo()
    soc_alert_demo()
    threat_classification_demo()
    command_execution_demo()

# =============================================================================
# SECTION 29 - Professional Tips
# =============================================================================


def professional_tips_demo() -> None:
    """
    Demonstrates professional tips
    for using match-case.
    """

    print("\nProfessional Tips")
    print("-" * 40)

    print("✔ Use match-case when comparing one value.")
    print("✔ Keep each case simple and readable.")
    print("✔ Group related patterns together.")
    print("✔ Always provide a default case.")
    print("✔ Prefer descriptive variable names.")


# =============================================================================
# SECTION 30 - Best Practices
# =============================================================================


def best_practices_demo() -> None:
    """
    Demonstrates best practices.
    """

    print("\nBest Practices")
    print("-" * 40)

    print("✔ Use match-case instead of long if-elif chains.")
    print("✔ Handle unexpected values with case _.")
    print("✔ Use guards only when necessary.")
    print("✔ Keep pattern matching easy to understand.")


# =============================================================================
# SECTION 31 - Common Mistakes
# =============================================================================


def common_mistakes_demo() -> None:
    """
    Demonstrates common mistakes.
    """

    print("\nCommon Mistakes")
    print("-" * 40)

    print("✘ Forgetting the wildcard case.")
    print("✘ Using match for complex Boolean logic.")
    print("✘ Creating too many nested patterns.")
    print("✘ Ignoring unsupported input values.")


# =============================================================================
# SECTION 32 - Performance Tips
# =============================================================================


def performance_tips_demo() -> None:
    """
    Demonstrates performance tips.
    """

    print("\nPerformance Tips")
    print("-" * 40)

    print("✔ Use match when many values share one variable.")
    print("✔ Avoid duplicate patterns.")
    print("✔ Keep each case focused on one task.")
    print("✔ Exit early after completing work.")


# =============================================================================
# SECTION 33 - if-elif vs match-case
# =============================================================================


def comparison_demo() -> None:
    """
    Compares if-elif with match-case.
    """

    print("\nif-elif vs match-case")
    print("-" * 40)

    print("if-elif:")
    print("- Better for complex Boolean conditions.")
    print("- Flexible for different variables.")

    print()

    print("match-case:")
    print("- Better for one variable with many values.")
    print("- Cleaner and easier to maintain.")


# =============================================================================
# SECTION 34 - Match-Case Cheat Sheet
# =============================================================================

"""
Match-Case Cheat Sheet
======================

Basic

match value:

    case pattern:
        ...

    case _:
        ...


Multiple Patterns

case "HTTP" | "HTTPS":


Guard Condition

case port if port < 1024:


Tuple Pattern

case ("TCP", 443):


List Pattern

case ["show", "version"]:


Wildcard

case _:
"""


# =============================================================================
# SECTION 35 - Interview Questions
# =============================================================================

"""
Interview Questions
-------------------

1. What is match-case?

2. When should match-case be used?

3. Difference between if and match?

4. What is case _?

5. What is a guard condition?

6. What are multiple patterns?

7. Can match-case replace every if statement?

8. What version of Python introduced match-case?

9. How can match-case simplify network automation?

10. Give a real-world use case for match-case.
"""


# =============================================================================
# SECTION 36 - Coding Exercises
# =============================================================================

"""
Coding Exercises
----------------

Exercise 1

Identify a network service from a port number.


Exercise 2

Classify HTTP status codes.


Exercise 3

Recognize routing protocols.


Exercise 4

Process security alerts.


Exercise 5

Create a CLI command dispatcher.
"""


# =============================================================================
# SECTION 37 - Mini Project
# =============================================================================


def mini_project_description() -> None:
    """
    Mini Project

    Network Command Dispatcher

    Requirements

    - Accept a command.
    - Match supported commands.
    - Display an appropriate action.
    - Handle unknown commands.

    Skills

    ✔ match

    ✔ case

    ✔ Wildcard

    ✔ Pattern Matching
    """

    print("\nMini Project")
    print("-" * 40)

    print("Network Command Dispatcher")


# =============================================================================
# SECTION 38 - What's Next
# =============================================================================

"""
Next Lesson

13_for_loops.py

Topics

✔ for Loop

✔ range()

✔ enumerate()

✔ break

✔ continue

✔ Nested Loops

✔ Network Automation

✔ Cybersecurity Examples
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
    comparison_demo()
    mini_project_description()


if __name__ == "__main__":
    main()
