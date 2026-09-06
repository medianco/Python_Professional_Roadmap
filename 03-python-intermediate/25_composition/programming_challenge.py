from typing import Protocol

class Connection(Protocol):
    """Define the interface for a network connection."""

    def connect(self) -> str:
        """Establish a connection."""
        ...
        
    def disconnect(self) -> str:
        """Disconnect from the network device."""
        ...        

class SSHConnection:
    """Represent an SSH connection."""

    def connect(self) -> str:
        """Establish an SSH connection."""
        return "SSH connection established"

    def disconnect(self) -> str:
        """Disconnect from the network device."""
        return "SSH connection closed"

class TelnetConnection:
    """Represent a Telnet connection."""

    def connect(self) -> str:
        """Establish a Telnet connection."""
        return "Telnet connection established"
        
    def disconnect(self) -> str:
        """Disconnect from the network device."""
        return "Telnet connection closed"
  
class ConfigurationManager:
    """Manage network device configuration."""

    def backup_config(self) -> str:
        """Back up the device configuration."""
        return "Configuration backup completed"
   
    def restore_config(self) -> str:
        """Restore the device configuration."""
        return "Configuration restore completed"

  
class MonitoringManager:
    """Manage network device monitoring."""

    def check_status(self) -> str:
        """Return device monitoring status."""
        return "Device status: UP"        
'''
NetworkDevice
      │
      ├── connect()
      │      └── SSHConnection
      │
      ├── backup_config()
      │      └── ConfigurationManager
      │
      └── check_status()
             └── MonitoringManager
'''             
class NetworkDevice:
    """Represent a network device."""

    def __init__(
        self,
        hostname: str,
        connection: Connection,
        config: ConfigurationManager,
        monitoring: MonitoringManager,

        
    ) -> None:
        self.hostname = hostname
        self.connection = connection
        self.config = config
        self.monitoring = monitoring    
    
    def connect(self) -> str:
        """Connect to the network device using connection."""
        return self.connection.connect()
        
    def disconnect(self) -> str:
        """Disconnect from the network device."""
        return self.connection.disconnect()
        
    def backup_config(self) -> str:
        """Back up the device configuration."""
        return self.config.backup_config()

    def restore_config(self) -> str:
        """Restore the device configuration."""
        return self.config.restore_config()

    def check_status(self) -> str:
        """Check the device monitoring status."""
        return self.monitoring.check_status()



'''
 - CiscoRouter IS-A NetworkDevice
 - CiscoRouter HAS-A SSHConnection
 - CiscoRouter HAS-A ConfigurationManager
 - CiscoRouter HAS-A MonitoringManager

                 NetworkDevice
                /             \
               /               \
              ▼                 ▼
        Inheritance         Composition
              │                 │
              ▼                 ▼
        CiscoRouter       SSHConnection
                          ConfigurationManager
                          MonitoringManager
'''

class CiscoRouter(NetworkDevice):
    """Represent a Cisco router."""

    def show_platform(self) -> str:
        """Return the device platform."""
        return "Platform: Cisco IOS"

if __name__ == "__main__":
    

    connection = SSHConnection()
    config = ConfigurationManager()
    monitoring = MonitoringManager()
    
    device = NetworkDevice(
        "R1",
        connection,
        config,
        monitoring,
    )

    print(device.hostname)
    print(device.connect())
    print(device.check_status())
    print(device.backup_config())
    print(device.restore_config())
    print(device.disconnect())

    print('=' * 30)
    
    telnet = TelnetConnection()

    device_telnet = NetworkDevice(
        "R2",
        telnet,
        config,
        monitoring,
    )

    print(device_telnet.hostname)
    print(device_telnet.connect())
    print(device_telnet.check_status())
    print(device_telnet.backup_config())
    print(device_telnet.restore_config())
    print(device_telnet.disconnect())
    print('=' * 30)
    
    router = CiscoRouter(
        "R3",
        connection,
        config,
        monitoring,
    )
    
    print(router.hostname)
    print(router.show_platform())
    print(router.connect())
    print(router.check_status())
    print(router.backup_config())
    print(router.restore_config())
    print(router.disconnect())
    print('=' * 30)
