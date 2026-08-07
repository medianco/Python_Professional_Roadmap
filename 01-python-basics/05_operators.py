"""
===============================================================================
File        : 05_operators.py
Author      : Mohammed AL-Dubai
Course      : Python Professional Roadmap
Lesson      : Operators

Description:
    This lesson explains Python operators used to perform arithmetic,
    comparison, assignment, logical, identity, membership,
    and bitwise operations.

Learning Objectives
-------------------
After completing this lesson, you will be able to:

✔ Understand Python operators.
✔ Perform arithmetic calculations.
✔ Use assignment operators.
✔ Compare values.
✔ Apply logical expressions.
✔ Understand identity operators.
✔ Use membership operators.
✔ Understand bitwise operators.
✔ Apply operators in network engineering and cybersecurity.

===============================================================================
"""

# =============================================================================
# SECTION 1 - Introduction to Operators
# =============================================================================

"""
Operators are special symbols used to perform operations on values.

Python provides several categories:

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
"""


def introduction_demo() -> None:
    """
    Demonstrates the concept of Python operators.
    """

    print("\nPython Operators")
    print("-" * 40)

    number1: int = 20
    number2: int = 5

    print(f"Number 1: {number1}")
    print(f"Number 2: {number2}")


# =============================================================================
# SECTION 2 - Arithmetic Operators
# =============================================================================


def arithmetic_demo() -> None:
    """
    Demonstrates arithmetic operators.
    """

    print("\nArithmetic Operators")
    print("-" * 40)

    x: int = 20
    y: int = 3

    print(f"{x} + {y} = {x + y}")
    print(f"{x} - {y} = {x - y}")
    print(f"{x} * {y} = {x * y}")
    print(f"{x} / {y} = {x / y}")
    print(f"{x} // {y} = {x // y}")
    print(f"{x} % {y} = {x % y}")
    print(f"{x} ** {y} = {x ** y}")


# =============================================================================
# SECTION 3 - Assignment Operators
# =============================================================================


def assignment_demo() -> None:
    """
    Demonstrates assignment operators.
    """

    print("\nAssignment Operators")
    print("-" * 40)

    value: int = 10

    print("Initial Value:", value)

    value += 5
    print("After += 5 :", value)

    value -= 2
    print("After -= 2 :", value)

    value *= 3
    print("After *= 3 :", value)

    value //= 2
    print("After //= 2:", value)


# =============================================================================
# SECTION 4 - Comparison Operators
# =============================================================================


def comparison_demo() -> None:
    """
    Demonstrates comparison operators.
    """

    print("\nComparison Operators")
    print("-" * 40)

    first_number: int = 100
    second_number: int = 50

    print(f"{first_number} == {second_number} : {first_number == second_number}")
    print(f"{first_number} != {second_number} : {first_number != second_number}")
    print(f"{first_number} > {second_number} : {first_number > second_number}")
    print(f"{first_number} < {second_number} : {first_number < second_number}")
    print(f"{first_number} >= {second_number} : {first_number >= second_number}")
    print(f"{first_number} <= {second_number} : {first_number <= second_number}")


# =============================================================================
# SECTION 5 - Arithmetic Operators in Networking
# =============================================================================


def network_arithmetic_demo() -> None:
    """
    Demonstrates arithmetic operators
    using networking examples.
    """

    print("\nNetwork Arithmetic Example")
    print("-" * 40)

    total_ports: int = 48
    used_ports: int = 31

    free_ports: int = total_ports - used_ports

    print(f"Total Ports : {total_ports}")
    print(f"Used Ports  : {used_ports}")
    print(f"Free Ports  : {free_ports}")


# =============================================================================
# SECTION 6 - Comparison Operators in Cybersecurity
# =============================================================================


def cybersecurity_comparison_demo() -> None:
    """
    Demonstrates comparison operators
    using cybersecurity examples.
    """

    print("\nCybersecurity Comparison Example")
    print("-" * 40)

    failed_attempts: int = 5
    maximum_attempts: int = 3

    account_locked: bool = failed_attempts >= maximum_attempts

    print(f"Failed Attempts : {failed_attempts}")
    print(f"Maximum Allowed : {maximum_attempts}")
    print(f"Account Locked  : {account_locked}")


# =============================================================================
# END OF PART 1
# =============================================================================

# =============================================================================
# SECTION 7 - Logical Operators
# =============================================================================


def logical_operators_demo() -> None:
    """
    Demonstrates logical operators.
    """

    print("\nLogical Operators")
    print("-" * 40)

    is_authenticated: bool = True
    has_permission: bool = False

    print(
        f"AND : {is_authenticated and has_permission}"
    )

    print(
        f"OR  : {is_authenticated or has_permission}"
    )

    print(
        f"NOT : {not has_permission}"
    )


# =============================================================================
# SECTION 8 - Identity Operators
# =============================================================================


def identity_operators_demo() -> None:
    """
    Demonstrates identity operators.
    """

    print("\nIdentity Operators")
    print("-" * 40)

    list1 = ["Router", "Switch"]
    list2 = ["Router", "Switch"]
    list3 = list1

    print(f"list1 is list2     : {list1 is list2}")
    print(f"list1 == list2     : {list1 == list2}")
    print(f"list1 is list3     : {list1 is list3}")
    print(f"list1 is not list2 : {list1 is not list2}")


# =============================================================================
# SECTION 9 - Membership Operators
# =============================================================================


def membership_operators_demo() -> None:
    """
    Demonstrates membership operators.
    """

    print("\nMembership Operators")
    print("-" * 40)

    protocols: list[str] = [
        "HTTP",
        "HTTPS",
        "SSH",
        "DNS"
    ]

    print(f"'SSH' in protocols      : {'SSH' in protocols}")
    print(f"'FTP' in protocols      : {'FTP' in protocols}")
    print(f"'FTP' not in protocols  : {'FTP' not in protocols}")


# =============================================================================
# SECTION 10 - Bitwise AND
# =============================================================================


def bitwise_and_demo() -> None:
    """
    Demonstrates the bitwise AND operator.
    """

    print("\nBitwise AND")
    print("-" * 40)

    first_value: int = 12
    second_value: int = 10

    result: int = first_value & second_value

    print(f"{first_value} & {second_value} = {result}")


# =============================================================================
# SECTION 11 - Bitwise OR
# =============================================================================


def bitwise_or_demo() -> None:
    """
    Demonstrates the bitwise OR operator.
    """

    print("\nBitwise OR")
    print("-" * 40)

    first_value: int = 12
    second_value: int = 10

    result: int = first_value | second_value

    print(f"{first_value} | {second_value} = {result}")


# =============================================================================
# SECTION 12 - Bitwise XOR
# =============================================================================


def bitwise_xor_demo() -> None:
    """
    Demonstrates the bitwise XOR operator.
    """

    print("\nBitwise XOR")
    print("-" * 40)

    first_value: int = 12
    second_value: int = 10

    result: int = first_value ^ second_value

    print(f"{first_value} ^ {second_value} = {result}")


# =============================================================================
# SECTION 13 - Bitwise Shift Operators
# =============================================================================


def bitwise_shift_demo() -> None:
    """
    Demonstrates bitwise shift operators.
    """

    print("\nBitwise Shift Operators")
    print("-" * 40)

    value: int = 8

    print(f"{value} << 1 = {value << 1}")
    print(f"{value} >> 1 = {value >> 1}")


# =============================================================================
# SECTION 14 - Network Engineering Example
# =============================================================================


def network_operator_demo() -> None:
    """
    Demonstrates operators in network engineering.
    """

    print("\nNetwork Engineering Example")
    print("-" * 40)

    vlan_id: int = 100
    native_vlan: int = 1

    print(f"VLAN ID       : {vlan_id}")
    print(f"Native VLAN   : {native_vlan}")
    print(f"Same VLAN     : {vlan_id == native_vlan}")

    active_ports: int = 22
    total_ports: int = 48

    print(f"Available Ports: {total_ports - active_ports}")


# =============================================================================
# SECTION 15 - Cybersecurity Example
# =============================================================================


def cybersecurity_operator_demo() -> None:
    """
    Demonstrates operators in cybersecurity.
    """

    print("\nCybersecurity Example")
    print("-" * 40)

    login_attempts: int = 4
    maximum_attempts: int = 5

    can_login: bool = login_attempts < maximum_attempts

    print(f"Attempts      : {login_attempts}")
    print(f"Maximum       : {maximum_attempts}")
    print(f"Access Allowed: {can_login}")

    port: int = 443

    print(f"HTTPS Port: {port == 443}")


# =============================================================================
# END OF PART 2
# =============================================================================

# =============================================================================
# SECTION 16 - Bitwise NOT Operator
# =============================================================================


def bitwise_not_demo() -> None:
    """
    Demonstrates the bitwise NOT operator.
    """

    print("\nBitwise NOT")
    print("-" * 40)

    value: int = 10

    result: int = ~value

    print(f"Original Value : {value}")
    print(f"Bitwise NOT    : {result}")


# =============================================================================
# SECTION 17 - Operator Summary
# =============================================================================


def operator_summary_demo() -> None:
    """
    Displays a summary of Python operators.
    """

    print("\nOperator Summary")
    print("-" * 40)

    summary = {
        "Arithmetic": "+  -  *  /  //  %  **",
        "Assignment": "=  +=  -=  *=  /=  //=  %=",
        "Comparison": "==  !=  >  <  >=  <=",
        "Logical": "and  or  not",
        "Identity": "is  is not",
        "Membership": "in  not in",
        "Bitwise": "&  |  ^  ~  <<  >>"
    }

    for category, operators in summary.items():
        print(f"{category:<12}: {operators}")


# =============================================================================
# SECTION 18 - Best Practices
# =============================================================================


def best_practices_demo() -> None:
    """
    Demonstrates recommended practices when using operators.
    """

    print("\nBest Practices")
    print("-" * 40)

    """
    Best Practices:

    ✔ Use parentheses to improve readability.

    ✔ Avoid complex expressions.

    ✔ Use == for value comparison.

    ✔ Use is only for identity comparison.

    ✔ Choose meaningful variable names.

    ✔ Keep logical conditions simple.

    ✔ Comment complex bitwise operations.
    """

    print("Follow simple and readable expressions.")


# =============================================================================
# SECTION 19 - Common Mistakes
# =============================================================================


def common_mistakes_demo() -> None:
    """
    Explains common mistakes when using operators.
    """

    print("\nCommon Mistakes")
    print("-" * 40)

    """
    Mistake 1:

    Using = instead of ==


    Mistake 2:

    Using is to compare numbers or strings.


    Mistake 3:

    Forgetting operator precedence.


    Mistake 4:

    Writing complex logical expressions.


    Mistake 5:

    Using bitwise operators instead of logical operators.
    """

    print("Review comments for common mistakes.")


# =============================================================================
# SECTION 20 - Interview Questions
# =============================================================================


"""
Interview Questions
-------------------

1. What are Python operators?

2. What is the difference between:
   = and == ?

3. What is the difference between:
   == and is ?

4. What is operator precedence?

5. What are logical operators?

6. What are bitwise operators used for?

7. When should you use membership operators?

8. What is the difference between:
   and
   &
   ?

9. Why are bitwise operators important
   in networking?

10. Why should complex expressions
    be avoided?
"""


# =============================================================================
# SECTION 21 - Coding Exercises
# =============================================================================


"""
Exercise 1:

Calculate:

25 + 15
25 - 15
25 * 15
25 / 15


Exercise 2:

Compare two VLAN IDs.

Print whether they are equal.


Exercise 3:

Check if:

"SSH"

exists in a protocol list.


Exercise 4:

Use logical operators to determine
whether access should be granted.


Exercise 5:

Perform bitwise operations on:

12

and

10.
"""


# =============================================================================
# SECTION 22 - Mini Project
# =============================================================================


def mini_project_description() -> None:
    """
    Mini Project:

    Network Access Validator

    Scenario:

    A network administrator wants
    to verify device access.

    Requirements:

    Store:

    - Username
    - Password Status
    - Account Status
    - Failed Login Attempts

    Tasks:

    1. Compare login attempts.

    2. Check authentication status.

    3. Verify account availability.

    4. Generate an access report.

    5. Display the final decision.

    Skills Practiced:

    ✔ Arithmetic Operators

    ✔ Comparison Operators

    ✔ Logical Operators

    ✔ Membership Operators

    ✔ Identity Operators
    """

    print("\nMini Project: Network Access Validator")
    print("See project requirements above.")


# =============================================================================
# SECTION 23 - Final Main Function Update
# =============================================================================

def main() -> None:
    """
    Main function that runs all demonstrations.
    """

    # Part One
    introduction_demo()
    arithmetic_demo()
    assignment_demo()
    comparison_demo()
    network_arithmetic_demo()
    cybersecurity_comparison_demo()

    # Part Two
    logical_operators_demo()
    identity_operators_demo()
    membership_operators_demo()
    bitwise_and_demo()
    bitwise_or_demo()
    bitwise_xor_demo()
    bitwise_shift_demo()
    network_operator_demo()
    cybersecurity_operator_demo()

    # Part Three
    bitwise_not_demo()
    operator_summary_demo()
    best_practices_demo()
    common_mistakes_demo()
    mini_project_description()


if __name__ == "__main__":
    main()
