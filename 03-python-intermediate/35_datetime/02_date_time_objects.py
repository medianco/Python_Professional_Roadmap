
"""
Lesson 35.2 — Working with Date and Time Objects

Learn how to create date, time, and datetime objects
and access their individual components.
"""

# Import the classes required to represent dates and times.
from datetime import date, time, datetime


def main() -> None:
    """Create and display different date and time objects."""

    # Create a date object representing a specific calendar date.
    maintenance_date = date(2026, 10, 20)

    print("Date object:")
    print(maintenance_date)
    print(f"Year: {maintenance_date.year}")
    print(f"Month: {maintenance_date.month}")
    print(f"Day: {maintenance_date.day}")

    # Create a time object representing a scheduled maintenance time.
    maintenance_time = time(22, 30, 0)

    print("\nTime object:")
    print(maintenance_time)
    print(f"Hour: {maintenance_time.hour}")
    print(f"Minute: {maintenance_time.minute}")
    print(f"Second: {maintenance_time.second}")

    # Create a datetime object by combining a date and a time.
    maintenance_datetime = datetime(2026, 10, 20, 22, 30, 0)

    print("\nDatetime object:")
    print(maintenance_datetime)
    print(f"Date: {maintenance_datetime.date()}")
    print(f"Time: {maintenance_datetime.time()}")

    # Retrieve the current date and time from the system clock.
    current_datetime = datetime.now()

    print("\nCurrent datetime:")
    print(current_datetime)


# Execute main() only when this file is run directly.
if __name__ == "__main__":
    main()
