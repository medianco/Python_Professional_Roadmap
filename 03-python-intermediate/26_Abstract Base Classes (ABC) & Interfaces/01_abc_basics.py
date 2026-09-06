from abc import ABC, abstractmethod

class NetworkDevice(ABC):
    """Define the common interface for network devices."""

    @abstractmethod
    def connect(self) -> str:
        """Connect to the network device."""
        ...

class CiscoRouter(NetworkDevice):
    """Represent a Cisco router."""

    def connect(self) -> str:
        """Connect to the Cisco router."""
        return "Connected to Cisco Router"

router = CiscoRouter()

print(router.connect())
