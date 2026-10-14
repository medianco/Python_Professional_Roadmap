
"""
Lesson 35.3 — Datetime Formatting and Logging Integration

Learn how to format timestamps, generate log filenames,
and record network automation events.
"""

import logging
from datetime import datetime
from pathlib import Path


def configure_logger(log_file: Path) -> logging.Logger:
    """Configure a logger with console and file handlers."""

    # Create a named logger for this application.
    logger = logging.getLogger("network_report")
    logger.setLevel(logging.INFO)

    # Avoid adding duplicate handlers if configuration is repeated.
    if not logger.handlers:
        # Define a consistent format for log records.
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        # Display log messages in the terminal.
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        # Save log messages to the generated file.
        file_handler = logging.FileHandler(
            log_file,
            encoding="utf-8",
        )
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)

        # Attach both handlers to the logger.
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger


def main() -> None:
    """Demonstrate datetime formatting and logging."""

    # Create a fixed datetime value for formatting examples.
    event_datetime = datetime(2026, 10, 14, 11, 30, 45)

    print("Original datetime:")
    print(event_datetime)

    # Display common date and time formats.
    print("\nDate formats:")
    print(event_datetime.strftime("%Y-%m-%d"))
    print(event_datetime.strftime("%d/%m/%Y"))
    print(event_datetime.strftime("%B %d, %Y"))

    print("\nTime format:")
    print(event_datetime.strftime("%H:%M:%S"))

    # Format the timestamp for a compact report filename.
    example_filename = (
        f"network_report_{event_datetime.strftime('%Y%m%d_%H%M%S')}.log"
    )
    print("\nExample log filename:")
    print(example_filename)

    # Get the actual current time for this execution's log filename.
    run_datetime = datetime.now()
    filename_timestamp = run_datetime.strftime("%Y%m%d_%H%M%S")

    # Create the output directory next to this Python script.
    output_dir = Path(__file__).resolve().parent / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Build the full path for the generated log file.
    log_file = output_dir / f"network_report_{filename_timestamp}.log"

    # Configure logging to write to both the terminal and the file.
    logger = configure_logger(log_file)

    # Record sample network automation events.
    logger.info("Network report generation started.")
    logger.info("Device R1 interface status checked.")
    logger.info("Network report generation completed.")

    print(f"\nLog file saved to: {log_file}")


# Execute main() only when this file is run directly.
if __name__ == "__main__":
    main()
