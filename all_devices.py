import socket
import time

# Simulate the network with multiple devices
class Device:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
    
    def receive_message(self, message):
        print(f"{self.name} (IP: {self.ip}) received: {message}")

# Simulate the broadcast scenario
class Network:
    def __init__(self):
        self.devices = []
    
    def add_device(self, device):
        self.devices.append(device)
    
    def send_broadcast(self, message):
        print(f"Sending broadcast message: '{message}' to all devices in the network...\n")
        time.sleep(1)
        
        # All devices in the network receive the message
        for device in self.devices:
            device.receive_message(message)

# Create devices
device1 = Device("Device A", "192.168.1.1")
device2 = Device("Device B", "192.168.1.2")
device3 = Device("Device C", "192.168.1.3")
device4 = Device("Device D", "192.168.1.4")

# Create a network and add devices
network = Network()
network.add_device(device1)
network.add_device(device2)
network.add_device(device3)
network.add_device(device4)

# Simulate sending a broadcast message from Device A
device1.receive_message("Broadcast: Device A is online.")
network.send_broadcast("Broadcast: Hello, all devices in the network!")
