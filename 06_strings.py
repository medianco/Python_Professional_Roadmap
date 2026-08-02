"""
===============================================================================
File        : 06_strings.py
Author      : Mohammed AL-Dubai
Course      : Python Basics
Lesson      : Strings

Description:
    This lesson explains Python strings, indexing, slicing,
    escape characters, and the most common string operations.

Learning Objectives
-------------------
After completing this lesson, you will be able to:

✔ Create string objects.
✔ Access characters using indexing.
✔ Use negative indexing.
✔ Extract substrings using slicing.
✔ Determine string length.
✔ Use escape characters.
✔ Apply string operations in networking and cybersecurity.

===============================================================================
"""

# =============================================================================
# SECTION 1 - Introduction to Strings
# =============================================================================

"""
A string is a sequence of Unicode characters.

Strings are:

✔ Immutable
✔ Ordered
✔ Iterable

Examples:

"Python"
'Network'
"Cyber Security"
"""


def introduction_demo() -> None:
    """
    Demonstrates the concept of Python strings.
    """

    print("\nIntroduction to Strings")
    print("-" * 40)

    text: str = "Python"

    print("Value:", text)
    print("Type :", type(text))


# =============================================================================
# SECTION 2 - Creating Strings
# =============================================================================


def creating_strings_demo() -> None:
    """
    Demonstrates different ways to create strings.
    """

    print("\nCreating Strings")
    print("-" * 40)

    first_name: str = "Mohammed"
    last_name: str = 'AL-Dubai'

    description: str = """
Network Engineering
Cybersecurity
Python Automation
"""

    print(first_name)
    print(last_name)
    print(description)


# =============================================================================
# SECTION 3 - String Indexing
# =============================================================================


def indexing_demo() -> None:
    """
    Demonstrates positive indexing.
    """

    print("\nString Indexing")
    print("-" * 40)

    text: str = "Python"

    print(f"text[0] = {text[0]}")
    print(f"text[1] = {text[1]}")
    print(f"text[2] = {text[2]}")
    print(f"text[5] = {text[5]}")


# =============================================================================
# SECTION 4 - Negative Indexing
# =============================================================================


def negative_indexing_demo() -> None:
    """
    Demonstrates negative indexing.
    """

    print("\nNegative Indexing")
    print("-" * 40)

    text: str = "Python"

    print(f"text[-1] = {text[-1]}")
    print(f"text[-2] = {text[-2]}")
    print(f"text[-3] = {text[-3]}")


# =============================================================================
# SECTION 5 - String Slicing
# =============================================================================


def slicing_demo() -> None:
    """
    Demonstrates string slicing.
    """

    print("\nString Slicing")
    print("-" * 40)

    text: str = "Cybersecurity"

    print(text[0:5])
    print(text[5:])
    print(text[:5])
    print(text[-4:])
    print(text[::2])
    print(text[::-1])


# =============================================================================
# SECTION 6 - String Length
# =============================================================================


def string_length_demo() -> None:
    """
    Demonstrates len().
    """

    print("\nString Length")
    print("-" * 40)

    hostname: str = "Core-Router"

    print("Hostname:", hostname)
    print("Length:", len(hostname))


# =============================================================================
# SECTION 7 - Escape Characters
# =============================================================================


def escape_characters_demo() -> None:
    """
    Demonstrates common escape characters.
    """

    print("\nEscape Characters")
    print("-" * 40)

    print("First Line\nSecond Line")

    print("Column1\tColumn2")

    print("Path: C:\\Users\\Admin")

    print("She said: \"Hello\"")

    print('It\'s Python')


# =============================================================================
# END OF PART 1
# =============================================================================

# =============================================================================
# SECTION 8 - Changing Letter Case
# =============================================================================


def letter_case_demo() -> None:
    """
    Demonstrates common letter case methods.
    """

    print("\nChanging Letter Case")
    print("-" * 40)

    text: str = "python for network automation"

    print("Original    :", text)
    print("upper()     :", text.upper())
    print("lower()     :", text.lower())
    print("title()     :", text.title())
    print("capitalize():", text.capitalize())
    print("swapcase()  :", text.swapcase())


# =============================================================================
# SECTION 9 - Searching Strings
# =============================================================================


def searching_demo() -> None:
    """
    Demonstrates string searching methods.
    """

    print("\nSearching Strings")
    print("-" * 40)

    text: str = "Python Network Automation"

    print("find('Network')      :", text.find("Network"))
    print("find('Python')       :", text.find("Python"))
    print("startswith('Python') :", text.startswith("Python"))
    print("endswith('Automation'):", text.endswith("Automation"))


# =============================================================================
# SECTION 10 - Replacing Text
# =============================================================================


def replace_demo() -> None:
    """
    Demonstrates replace().
    """

    print("\nReplacing Text")
    print("-" * 40)

    text: str = "HTTP uses port 80"

    updated_text = text.replace("80", "443")

    print("Original :", text)
    print("Updated  :", updated_text)


# =============================================================================
# SECTION 11 - Removing Spaces
# =============================================================================


def strip_demo() -> None:
    """
    Demonstrates strip(), lstrip(), and rstrip().
    """

    print("\nRemoving Spaces")
    print("-" * 40)

    text: str = "   Python Basics   "

    print(f"Original : '{text}'")
    print(f"strip()  : '{text.strip()}'")
    print(f"lstrip() : '{text.lstrip()}'")
    print(f"rstrip() : '{text.rstrip()}'")


# =============================================================================
# SECTION 12 - Splitting Strings
# =============================================================================


def split_demo() -> None:
    """
    Demonstrates split().
    """

    print("\nSplitting Strings")
    print("-" * 40)

    protocols: str = "HTTP,HTTPS,SSH,DNS"

    protocol_list = protocols.split(",")

    print(protocol_list)

    for protocol in protocol_list:
        print(protocol)


# =============================================================================
# SECTION 13 - Joining Strings
# =============================================================================


def join_demo() -> None:
    """
    Demonstrates join().
    """

    print("\nJoining Strings")
    print("-" * 40)

    words = [
        "Python",
        "Network",
        "Automation"
    ]

    sentence = " ".join(words)

    print(sentence)


# =============================================================================
# SECTION 14 - String Validation
# =============================================================================


def validation_demo() -> None:
    """
    Demonstrates string validation methods.
    """

    print("\nString Validation")
    print("-" * 40)

    value1 = "Python"
    value2 = "2026"
    value3 = "Python2026"
    value4 = " "

    print(value1.isalpha())
    print(value2.isdigit())
    print(value3.isalnum())
    print(value4.isspace())
    print(value1.islower())
    print(value1.isupper())


# =============================================================================
# SECTION 15 - Network Engineering Example
# =============================================================================


def network_string_demo() -> None:
    """
    Demonstrates string processing
    in network engineering.
    """

    print("\nNetwork Engineering Example")
    print("-" * 40)

    ip_address: str = "192.168.10.1"

    octets = ip_address.split(".")

    print("IP Address :", ip_address)
    print("Octets     :", octets)

    print("First Octet :", octets[0])
    print("Last Octet  :", octets[-1])


# =============================================================================
# SECTION 16 - Cybersecurity Example
# =============================================================================


def cybersecurity_string_demo() -> None:
    """
    Demonstrates string processing
    in cybersecurity.
    """

    print("\nCybersecurity Example")
    print("-" * 40)

    log = "Failed login from 192.168.1.50"

    print("Log Entry:")
    print(log)

    print()

    print("Contains 'Failed':", "Failed" in log)
    print("Contains 'login' :", "login" in log)
    print("Contains 'SSH'   :", "SSH" in log)


# =============================================================================
# SECTION 17 - Log Analysis Example
# =============================================================================


def log_analysis_demo() -> None:
    """
    Demonstrates simple log analysis.
    """

    print("\nLog Analysis")
    print("-" * 40)

    log = "INFO: SSH connection established"

    parts = log.split(":")

    print("Level  :", parts[0])
    print("Message:", parts[1].strip())


# =============================================================================
# END OF PART 2
# =============================================================================

# =============================================================================
# SECTION 18 - find() vs index()
# =============================================================================


def find_vs_index_demo() -> None:
    """
    Demonstrates the difference between find() and index().
    """

    print("\nfind() vs index()")
    print("-" * 40)

    text: str = "Python Network Automation"

    print("find('Network') :", text.find("Network"))
    print("find('Cisco')   :", text.find("Cisco"))

    print("index('Python') :", text.index("Python"))

    try:
        print(text.index("Cisco"))
    except ValueError:
        print("index() raised ValueError because the text was not found.")


# =============================================================================
# SECTION 19 - Counting Text
# =============================================================================


def count_demo() -> None:
    """
    Demonstrates count().
    """

    print("\ncount()")
    print("-" * 40)

    text: str = "SSH SSH HTTP SSH DNS"

    print("Original:", text)
    print("SSH Count :", text.count("SSH"))
    print("HTTP Count:", text.count("HTTP"))


# =============================================================================
# SECTION 20 - Text Alignment
# =============================================================================


def alignment_demo() -> None:
    """
    Demonstrates center(), ljust(), and rjust().
    """

    print("\nText Alignment")
    print("-" * 40)

    title: str = "Python"

    print(title.center(30, "-"))
    print(title.ljust(30, "."))
    print(title.rjust(30, "."))


# =============================================================================
# SECTION 21 - Zero Filling
# =============================================================================


def zfill_demo() -> None:
    """
    Demonstrates zfill().
    """

    print("\nzfill()")
    print("-" * 40)

    vlan_id: str = "25"

    print(vlan_id.zfill(5))
    print("7".zfill(3))


# =============================================================================
# SECTION 22 - partition() and rpartition()
# =============================================================================


def partition_demo() -> None:
    """
    Demonstrates partition() and rpartition().
    """

    print("\npartition() and rpartition()")
    print("-" * 40)

    email: str = "admin@example.com"

    print(email.partition("@"))
    print(email.rpartition("@"))


# =============================================================================
# SECTION 23 - Prefix and Suffix Removal
# =============================================================================


def prefix_suffix_demo() -> None:
    """
    Demonstrates removeprefix() and removesuffix().
    """

    print("\nPrefix and Suffix Removal")
    print("-" * 40)

    filename: str = "logfile.txt"

    print(filename.removesuffix(".txt"))

    command: str = "show ip route"

    print(command.removeprefix("show "))


# =============================================================================
# SECTION 24 - casefold()
# =============================================================================


def casefold_demo() -> None:
    """
    Demonstrates casefold().
    """

    print("\ncasefold()")
    print("-" * 40)

    first_text: str = "Python"
    second_text: str = "python"

    print(first_text.lower() == second_text.lower())
    print(first_text.casefold() == second_text.casefold())


# =============================================================================
# SECTION 25 - Encoding Strings
# =============================================================================


def encoding_demo() -> None:
    """
    Demonstrates encode().
    """

    print("\nencode()")
    print("-" * 40)

    text: str = "Cyber Security"

    encoded = text.encode("utf-8")

    print(encoded)
    print(type(encoded))


# =============================================================================
# SECTION 26 - Network Automation Example
# =============================================================================


def network_automation_string_demo() -> None:
    """
    Demonstrates string processing in network automation.
    """

    print("\nNetwork Automation Example")
    print("-" * 40)

    cli_output = "GigabitEthernet0/1 up up"

    parts = cli_output.split()

    interface = parts[0]
    status = parts[1]

    print("Interface:", interface)
    print("Status   :", status)


# =============================================================================
# SECTION 27 - Log Parsing Example
# =============================================================================


def log_parsing_demo() -> None:
    """
    Demonstrates parsing a simple log entry.
    """

    print("\nLog Parsing Example")
    print("-" * 40)

    log = "ERROR: Failed login from 192.168.1.50"

    level, _, message = log.partition(":")

    print("Level  :", level)
    print("Message:", message.strip())

    if "Failed" in message:
        print("Alert: Authentication failure detected.")


# =============================================================================
# END OF PART 3
# =============================================================================

# =============================================================================
# SECTION 28 - String Best Practices
# =============================================================================


def best_practices_demo() -> None:
    """
    Demonstrates recommended practices when working with strings.
    """

    print("\nString Best Practices")
    print("-" * 40)

    """
    Best Practices:

    ✔ Use f-strings for formatting.

    ✔ Use meaningful variable names.

    ✔ Strip user input before processing.

    ✔ Use split() instead of manual parsing.

    ✔ Use join() for string concatenation.

    ✔ Avoid repeated '+' inside loops.

    ✔ Validate user input.

    ✔ Use casefold() for case-insensitive comparisons.

    ✔ Keep strings immutable.
    """

    print("Follow clean and readable string operations.")


# =============================================================================
# SECTION 29 - Common Mistakes
# =============================================================================


def common_mistakes_demo() -> None:
    """
    Explains common mistakes when using strings.
    """

    print("\nCommon String Mistakes")
    print("-" * 40)

    """
    Mistake 1:

    Forgetting that strings are immutable.


    Mistake 2:

    Using index() without exception handling.


    Mistake 3:

    Using '+' repeatedly inside loops.


    Mistake 4:

    Forgetting strip() after user input.


    Mistake 5:

    Confusing find() with index().
    """

    print("Review the comments above.")


# =============================================================================
# SECTION 30 - Performance Tips
# =============================================================================


def performance_tips_demo() -> None:
    """
    Demonstrates performance recommendations.
    """

    print("\nPerformance Tips")
    print("-" * 40)

    print("Use join() instead of repeated '+' concatenation.")
    print("Reuse processed strings whenever possible.")
    print("Avoid unnecessary conversions.")


# =============================================================================
# SECTION 31 - Interview Questions
# =============================================================================


"""
Interview Questions
-------------------

1. What is a string?

2. Why are strings immutable?

3. What is the difference between:

   find()

   and

   index()?

4. What is slicing?

5. What does split() do?

6. What does join() do?

7. Why is strip() important?

8. What is the difference between:

   lower()

   and

   casefold()?

9. Why is encode() used?

10. How are strings used in
    network automation?
"""


# =============================================================================
# SECTION 32 - Coding Exercises
# =============================================================================


"""
Exercise 1

Convert a sentence to uppercase.


Exercise 2

Extract the username from:

admin@example.com


Exercise 3

Split:

192.168.1.1

into four octets.


Exercise 4

Count the number of:

SSH

inside a log message.


Exercise 5

Reverse a string using slicing.


Exercise 6

Replace every occurrence of:

HTTP

with

HTTPS.
"""


# =============================================================================
# SECTION 33 - Mini Project
# =============================================================================


def mini_project_description() -> None:
    """
    Mini Project:

    Network Log Analyzer

    Scenario:

    A security analyst receives
    network log entries.

    Tasks:

    1. Read a log entry.

    2. Detect log level.

    3. Extract IP address.

    4. Detect event type.

    5. Count failed logins.

    6. Generate a formatted report.

    Skills Practiced:

    ✔ split()

    ✔ replace()

    ✔ strip()

    ✔ find()

    ✔ count()

    ✔ f-string

    ✔ String Validation
    """

    print("\nMini Project: Network Log Analyzer")
    print("See project requirements above.")


# =============================================================================
# SECTION 34 - Final Main Function
# =============================================================================


def main() -> None:
    """
    Main function that runs all demonstrations.
    """

    # Part One
    introduction_demo()
    creating_strings_demo()
    indexing_demo()
    negative_indexing_demo()
    slicing_demo()
    string_length_demo()
    escape_characters_demo()

    # Part Two
    letter_case_demo()
    searching_demo()
    replace_demo()
    strip_demo()
    split_demo()
    join_demo()
    validation_demo()
    network_string_demo()
    cybersecurity_string_demo()
    log_analysis_demo()

    # Part Three
    find_vs_index_demo()
    count_demo()
    alignment_demo()
    zfill_demo()
    partition_demo()
    prefix_suffix_demo()
    casefold_demo()
    encoding_demo()
    network_automation_string_demo()
    log_parsing_demo()

    # Part Four
    best_practices_demo()
    common_mistakes_demo()
    performance_tips_demo()
    mini_project_description()


if __name__ == "__main__":
    main()

