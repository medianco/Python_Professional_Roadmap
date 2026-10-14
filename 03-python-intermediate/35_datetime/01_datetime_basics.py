
"""
Lesson 35.1 — Introduction to Datetime

Learn how to retrieve and display the current date and time.
"""

# Import the datetime class from Python's standard datetime module.
from datetime import datetime


def main() -> None:
    """Display the current date and time."""

    # Retrieve the current local date and time from the system clock.
    current_datetime = datetime.now()

    # Display the complete date and time.
    print("Current date and time:")
    print(current_datetime)

    # Extract and display the date components.
    print("\nDate components:")
    print(f"Year: {current_datetime.year}")
    print(f"Month: {current_datetime.month}")
    print(f"Day: {current_datetime.day}")

    # Extract and display the time components.
    print("\nTime components:")
    print(f"Hour: {current_datetime.hour}")
    print(f"Minute: {current_datetime.minute}")
    print(f"Second: {current_datetime.second}")


# Execute main() only when this file is run directly.
if __name__ == "__main__":
    main()
