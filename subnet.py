import ipaddress

def subnet_details(ip_with_subnet):
    # Create an IPv4Network object
    network = ipaddress.ip_network(ip_with_subnet, strict=False)
    
    print(f"IP Address: {ip_with_subnet.split('/')[0]}")
    print(f"Network Address: {network.network_address}")
    print(f"Broadcast Address: {network.broadcast_address}")
    print(f"Subnet Mask: {network.netmask}")
    print(f"Number of Usable Hosts: {network.num_addresses - 2}")

# Example usage
ip = "192.168.1.10/24"
subnet_details(ip)
