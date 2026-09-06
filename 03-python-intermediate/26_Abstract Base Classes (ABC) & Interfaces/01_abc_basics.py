from abc import ABC, abstractmethod

class NetworkDevice(ABC):
    """Define the common interface for network devices."""

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

class CiscoRouter(NetworkDevice):
    """Represent a Cisco router."""

    def connect(self) -> str:
        """Connect to the Cisco router."""
        return "Connected to Cisco Router"
        
    def disconnect(self) -> str:
        return "Cisco Router disconnected"

    def show_status(self) -> str:
        return "Cisco Router status: UP"



router = CiscoRouter()

print(router.connect())
print(router.show_status())
print(router.disconnect())
