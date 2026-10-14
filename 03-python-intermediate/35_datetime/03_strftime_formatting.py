
"""
Lesson 35.3 — Formatting Dates with strftime()

Learn how to format datetime objects into readable strings.
"""

# Import datetime to create date and time objects.
from datetime import datetime


def main() -> None:
    """Demonstrate common datetime formatting patterns."""

    # Create a fixed datetime value for predictable examples.
    event_datetime = datetime(2026, 10, 14, 11, 30, 45)

    # Display the original datetime object.
    print("Original datetime:")
    print(event_datetime)

    # Format the date using a year-month-day pattern.
    print("\nDate formats:")
    print(event_datetime.strftime("%Y-%m-%d"))
    print(event_datetime.strftime("%d/%m/%Y"))
    print(event_datetime.strftime("%B %d, %Y"))

    # Format the time using a 24-hour clock.
    print("\nTime formats:")
    print(event_datetime.strftime("%H:%M:%S"))

    # Combine date and time into a readable timestamp.
    print("\nCombined datetime:")
    print(event_datetime.strftime("%Y-%m-%d %H:%M:%S"))

    # Create a timestamp format suitable for log records.
    log_timestamp = event_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print("\nNetwork event log:")
    print(f"[{log_timestamp}] R1 - Interface status checked")


# Execute main() only when this file is run directly.
if __name__ == "__main__":
    main()
