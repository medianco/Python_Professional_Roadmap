"""
Lesson 25: Composition

This lesson demonstrates:
- Composition
- Multiple Composition
- HAS-A relationship
- Object collaboration
- Delegation
- Loose Coupling
- Dependency Injection
        
        NetworkDevice
              │
              └── ssh
                   │
                   └── SSHConnection
        NetworkDevice
             │
             └── HAS-A → SSHConnection
             
        ✅ NetworkDevice
              │
              ├── has-a SSHConnection
              ├── has-a ConfigurationManager
              ├── has-a MonitoringManager
              └── has-a BackupManager  
                     
        NetworkDevice
              │
              │ delegates SSH work
              ▼
        SSHConnection             

Author: Mohammed AL-Dubai

"""


class SSHConnection:
    """Represent an SSH connection."""

    def connect(self) -> str:
        """Establish an SSH connection."""
        return "SSH connection established"

class ConfigurationManager:
    """Manage network device configuration."""

    def backup_config(self) -> str:
        """Back up the device configuration."""
        return "Configuration backup completed"

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

    '''
    def __init__(self, hostname: str) -> None:
        self.hostname = hostname
        
        self.ssh = SSHConnection()
        self.config = ConfigurationManager()
        self.monitoring = MonitoringManager()
    '''
    
    def __init__(
        self,
        hostname: str,
        ssh: SSHConnection,
        config: ConfigurationManager,
        monitoring: MonitoringManager,
    ) -> None:
        self.hostname = hostname
        self.ssh = ssh
        self.config = config
        self.monitoring = monitoring    
    
    def connect(self) -> str:
        """Connect to the network device using SSH."""
    
        return self.ssh.connect()    
        
    def backup_config(self) -> str:
        """Back up the device configuration."""
    
        return self.config.backup_config()

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
        return "Cisco IOS"

if __name__ == "__main__":
    
    #device = NetworkDevice("R1")

    ssh = SSHConnection()
    config = ConfigurationManager()
    monitoring = MonitoringManager()
    
    device = NetworkDevice(
        "R1",
        ssh,
        config,
        monitoring,
    )

    print(device.hostname)
    print(device.connect())
    print(device.backup_config())
    print(device.check_status())
    print('=' * 30)
    
    router = CiscoRouter(
        "R1",
        ssh,
        config,
        monitoring,
    )
    
    print(router.hostname)
    print(router.show_platform())
    print(router.connect())
    print('=' * 30)
    
    print(device.ssh.connect()) 
 
