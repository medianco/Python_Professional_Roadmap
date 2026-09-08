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

'''
# ABC vs Protocol
#
# ABC:
# - Relies on inheritance.
# - Enforces a contract for subclasses.
# - Can provide shared implementation.
# - Best when there is a strong relationship between classes.
# - Represents an "IS-A" relationship.
#
#      ABC
        │
        ├── Inheritance
        ├── Strong relationship
        ├── Contract
        └── Shared implementation
        
# Protocol:
# - Does not require inheritance.
# - Defines required behavior.
# - Focuses on structural typing.
# - Best when we care about what an object can do.
# - Represents "HAS-THE-REQUIRED-BEHAVIOR".
#

#    Protocol
        │
        ├── No inheritance required
        ├── Behavior
        ├── Structural typing
        └── Flexible design

# Key idea:
# ABC focuses on inheritance and a formal contract,
# while Protocol focuses on behavior and compatibility.

'''

from abc import ABC, abstractmethod
from typing import Protocol

class Connection(Protocol):

    def connect(self) -> str:
        ...

    def disconnect(self) -> str:
        ...

class SSHConnection:

    def connect(self) -> str:
        return "SSH connection established"

    def disconnect(self) -> str:
        return "SSH connection closed"
        
        
class TELNETConnection:

    def connect(self) -> str:
        return "TELNET connection established"

    def disconnect(self) -> str:
        return "TELNET connection closed"


class APIConnection:
    """Represent an API-based connection."""

    def connect(self) -> str:
        return "API connection established"

    def disconnect(self) -> str:
        return "API connection closed"
        

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
    


def establish_connection(connection: Connection) -> str:
    """Test a network connection."""
    return connection.connect()    
 
ssh = SSHConnection()
telnet = TELNETConnection()
api = APIConnection()


print(establish_connection(ssh))
print(establish_connection(telnet))
print(establish_connection(api))
print(ssh.disconnect())
print(api.disconnect())
print("=" * 45)


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
