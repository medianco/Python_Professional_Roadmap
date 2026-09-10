"""
Lesson 25: Composition

This lesson demonstrates:
- Composition
- Composition vs. Inheritance
- Multiple Composition
- HAS-A relationship
- Object collaboration
- Delegation
- Loose Coupling
- Dependency Injection
- Protocol
- Flexible Components

Author: Mohammed AL-Dubai
"""

from typing import Protocol

# ==============================================================================
# 1. PROTOCOL
# ==============================================================================
# A Protocol acts as a "contract" or interface. It defines a set of behaviors 
# (methods) that matching classes must implement, without enforcing inheritance.
class Connection(Protocol):
    """Define the interface for a network connection."""

    def connect(self) -> str:
        """Establish a connection."""
        ...

class SSHConnection:
    """Represent an SSH connection."""
    
    # This class adheres to the Connection Protocol by implementing connect()
    def connect(self) -> str:
        """Establish an SSH connection."""
        return "SSH connection established"

class TelnetConnection:
    """Represent a Telnet connection."""

    # This class also adheres to the Connection Protocol implicitly (Duck Typing)
    def connect(self) -> str:
        """Establish a Telnet connection."""
        return "Telnet connection established"

class ConfigurationManager:
    """Manage network device configuration."""

    def backup_config(self) -> str:
        """Back up the device configuration."""
        return "Configuration backup completed"

class MonitoringManager:
    """Manage network device monitoring."""

    def check_status(self) -> str:
        """Return the device status."""
        return "Device status: OPTIMAL"


class NetworkDevice:
    """Represent a network device using composition and dependency injection."""

    # ==============================================================================
    # 2. DEPENDENCY INJECTION & LOOSE COUPLING
    # ==============================================================================
    # - DEPENDENCY INJECTION: Instead of instantiating the connections and managers 
    #   hardcoded inside the class, they are passed (injected) from the outside via __init__.
    #
    # - LOOSE COUPLING: NetworkDevice does not depend on concrete classes like SSHConnection.
    #   Instead, it depends on the abstract 'Connection' Protocol. This decouples the 
    #   device from specific connection types, making it easily extendable.
    def __init__(
        self, 
        name: str, 
        connection: Connection, 
        config_manager: ConfigurationManager, 
        monitoring_manager: MonitoringManager
    ):
        self.name = name
        # HAS-A Relationships (Composition)
        self.connection = connection
        self.config_manager = config_manager
        self.monitoring_manager = monitoring_manager

    # ==============================================================================
    # 3. DELEGATION
    # ==============================================================================
    # The NetworkDevice itself doesn't know how to perform the low-level connection.
    # It DELEGATES the connection work entirely to the injected connection object.
    def connect(self) -> str:
        """Connect to the device by delegating to the connection component."""
        return f"[{self.name}] {self.connection.connect()}"

    # ==============================================================================
    # 4. OBJECT COLLABORATION
    # ==============================================================================
    # Demonstrates multiple composed components working together to achieve a single task.
    def maintenance(self) -> list[str]:
        """Perform routine maintenance tasks using multiple composed managers."""
        return [
            f"[{self.name}] {self.config_manager.backup_config()}",
            f"[{self.name}] {self.monitoring_manager.check_status()}"
        ]


# --- Demonstration of how these patterns work together ---
if __name__ == "__main__":
    # Common manager components shared across multiple devices
    cfg_mgr = ConfigurationManager()
    mon_mgr = MonitoringManager()

    # 1. Device using SSH Connection 
    ssh_conn = SSHConnection()
    # Injecting SSH connection and managers into the device
    router = NetworkDevice("Core-Router-01", connection=ssh_conn, config_manager=cfg_mgr, monitoring_manager=mon_mgr)
    
    print("--- Testing Router with SSH ---")
    print(router.connect())
    print("\n".join(router.maintenance()))

    print("\n" + "="*40 + "\n")

    # 2. Seamlessly replacing connection types (Loose Coupling in action)
    # We switch to Telnet WITHOUT changing a single line of code in NetworkDevice.
    telnet_conn = TelnetConnection()
    switch = NetworkDevice("Edge-Switch-A", connection=telnet_conn, config_manager=cfg_mgr, monitoring_manager=mon_mgr)
    
    print("--- Testing Switch with Telnet ---")
    print(switch.connect())
    print("\n".join(switch.maintenance()))
