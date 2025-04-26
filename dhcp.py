import time
import random

# Simulate the DHCP Server
class DHCPServer:
    def __init__(self):
        self.available_ips = ['192.168.1.10', '192.168.1.11', '192.168.1.12']
        self.boot_server = '192.168.1.100'
        self.dns_servers = ['8.8.8.8', '8.8.4.4']
    
    def offer_ip(self):
        if self.available_ips:
            # Offer an available IP
            ip = self.available_ips.pop(0)
            print(f"DHCP Server: Offering IP {ip}")
            return ip
        else:
            print("DHCP Server: No IP addresses available.")
            return None
    
    def acknowledge_ip(self, ip):
        print(f"DHCP Server: Acknowledging IP {ip} with boot server {self.boot_server} and DNS servers {self.dns_servers}")

# Simulate the DHCP Client (Device)
class DHCPClient:
    def __init__(self, server):
        self.server = server
    
    def send_dhcp_discover(self):
        print("Client: Sending DHCP Discover message to server...")
        time.sleep(random.uniform(0.5, 1))  # Simulating network delay
    
    def send_dhcp_request(self, ip):
        print(f"Client: Sending DHCP Request for IP {ip}...")
        time.sleep(random.uniform(0.5, 1))  # Simulating network delay
    
    def receive_dhcp_offer(self, ip):
        print(f"Client: Received DHCP Offer with IP {ip}")
    
    def receive_dhcp_acknowledgment(self, ip):
        print(f"Client: DHCP Acknowledgment received for IP {ip}")
        self.server.acknowledge_ip(ip)

# Main simulation function
def dhcp_simulation():
    server = DHCPServer()  # DHCP Server
    client = DHCPClient(server)  # DHCP Client
    
    # Simulate the DHCP process
    client.send_dhcp_discover()
    offered_ip = server.offer_ip()  # Server offers IP to client
    
    if offered_ip:
        client.receive_dhcp_offer(offered_ip)
        client.send_dhcp_request(offered_ip)  # Client requests the offered IP
        client.receive_dhcp_acknowledgment(offered_ip)

# Run the DHCP simulation
dhcp_simulation()
