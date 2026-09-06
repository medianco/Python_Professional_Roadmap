'''
                NetworkDevice (ABC)
                       │
          ┌────────────┴────────────┐
          │                         │
   Abstract Methods          Concrete Methods
          │                         │
   connect()                show_hostname()
   disconnect()                     │
   show_status()                    │
          │                         │
          ▼                         ▼
   Must Implement            Ready to Use
   
'''

from abc import ABC, abstractmethod

class NetworkDevice(ABC):
    """Define the common interface for network devices."""
    
    def __init__(self, hostname: str) -> None:
        self.hostname = hostname

    @abstractmethod
    def connect(self) -> str:
        """Connect to the network device."""
        ...
        
    @abstractmethod
    def disconnect(self) -> str:
        """Disconnect from the network device."""
        ...

    @abstractmethod
    def show_status(self) -> str:
        """Return the device status."""
        ...
        
    def show_hostname(self) -> str:
        """Return the device hostname."""
        return f"Hostname: {self.hostname}"   

class CiscoRouter(NetworkDevice):
    """Represent a Cisco router."""

    def connect(self) -> str:
        """Connect to the Cisco router."""
        return "Connected to Cisco Router"
        
    def disconnect(self) -> str:
        return "Cisco Router disconnected"

    def show_status(self) -> str:
        return "Cisco Router status: UP"



router = CiscoRouter("R1")

print(router.show_hostname())
print(router.connect())
print(router.show_status())
print(router.disconnect())
