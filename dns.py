import socket

# Domain you want to resolve
domain_name = "aishasart.com"

# Use socket to get the IP address
ip_address = socket.gethostbyname(domain_name)

print(f"The IP address of {domain_name} is: {ip_address}")
