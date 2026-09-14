"""
Lesson 26.2 - Abstract Methods

This lesson introduces abstract methods.

Key concepts:
- @abstractmethod
- Abstract method
- Enforcing implementation in subclasses
"""

from abc import ABC, abstractmethod


# ============================================================
# Abstract Base Class
# ============================================================

class NetworkDevice(ABC):
    """
    Abstract Base Class for network devices.

    Every network device must provide its own implementation
    of the connect() method.
    """

    @abstractmethod
    def connect(self):
        """
        Abstract method.

        Subclasses MUST implement this method.
        """
        pass


# ============================================================
# Router
# ============================================================

class Router(NetworkDevice):
    """Represents a network router."""

    def connect(self):
        """Implement the required connect() method."""
        print("Router connected successfully.")


# ============================================================
# Switch
# ============================================================

class Switch(NetworkDevice):
    """Represents a network switch."""

    def connect(self):
        """Implement the required connect() method."""
        print("Switch connected successfully.")


# ============================================================
# Main Program
# ============================================================

if __name__ == "__main__":

    router = Router()
    switch = Switch()

    router.connect()
    switch.connect()

    # NetworkDevice() cannot be instantiated because it contains
    # an abstract method.
    #
    # device = NetworkDevice()
    #
    # This would raise:
    # TypeError: Can't instantiate abstract class NetworkDevice
