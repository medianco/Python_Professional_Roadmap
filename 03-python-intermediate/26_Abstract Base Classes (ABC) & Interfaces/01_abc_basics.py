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
   
 
                     NetworkDevice
                          ABC
                           │
                ┌──────────┴──────────┐
                │                     │
           Contract              Shared Logic
                │                     │
           connect()             show_hostname()
           disconnect()
           show_status()
                │
                ▼
         ┌──────────────┐
         │              │
       Router        Switch
         │              │
    Implementation  Implementation


   
                 NetworkDevice
                      ABC
                       │
              ┌────────┴────────┐
              │                 │
        CiscoRouter       CiscoSwitch
              │                 │
        connect()          connect()
        disconnect()       disconnect()
        show_status()      show_status()
   
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
    
    @abstractmethod
    def show_model(self) -> str:
        """Return the device model."""
        ...
        
        
    def show_hostname(self) -> str:
        """Return the device hostname."""
        return f"Hostname: {self.hostname}"
        
    def device_info(self) -> str:
        return f"Device: {self.hostname}\nType: {self.__class__.__name__}"
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

    def show_model(self) -> str:
        return "Cisco Router model: Cisco ASR 1000 Series"
        
 
class CiscoSwitch(NetworkDevice):
    """Represent a Cisco switch."""

    def connect(self) -> str:
        return "Cisco Switch connected"

    def disconnect(self) -> str:
        return "Cisco Switch disconnected"

    def show_status(self) -> str:
        return "Cisco Switch status: UP"
        
    def show_model(self) -> str:
        return "Cisco Switch model: Catalyst 2960 Series"    

'''
 ## ABC + Polymorphism
                     NetworkDevice (ABC)
                         │
              ┌──────────┴──────────┐
              │                     │
        CiscoRouter            CiscoSwitch
              │                     │
        show_status()          show_status()
              │                     │
              └──────────┬──────────┘
                         │
                    Polymorphism
'''

# Polymorphic function
def check_device(device: NetworkDevice) -> None:
    print(device.show_hostname())
    print(device.connect())
    print(device.show_status())
    print(device.disconnect())
   
# Create devices
devices = [
    CiscoRouter("R2"),
    CiscoSwitch("SW2"),
]


# Test polymorphism
for device in devices:
    check_device(device)
    print("=" * 30)
    
    
router = CiscoRouter("R1")

print(router.show_hostname())
print(router.show_model())
print(router.connect())
print(router.show_status())
print(router.disconnect())
print(router.device_info())
print('=' * 45)


switch = CiscoSwitch("SW1")

print(switch.show_hostname())
print(switch.show_model())
print(switch.connect())
print(switch.show_status())
print(switch.disconnect())
print(switch.device_info())
print('=' * 45)
