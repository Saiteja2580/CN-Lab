import socket
import uuid

# Get the hostname and IP address
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# Get the MAC address
mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                        for elements in range(0, 2*6, 2)][::-1])

print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
print(f"MAC Address: {mac_address}")
