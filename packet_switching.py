import random
import time

# Simulate sending packets through different routes
routes = {
    'Packet 1': ['Router 1', 'Router 2', 'Building D'],
    'Packet 2': ['Router 3', 'Router 4', 'Building D'],
    'Packet 3': ['Router 2', 'Router 4', 'Building D']
}

# Original message
message = "Hello, Building D!"

# Splitting message into 3 packets
packet_data = {
    'Packet 1': message[:5],    # 'Hello'
    'Packet 2': message[5:12],  # ', Buil'
    'Packet 3': message[12:]    # 'ding D!'
}

# Simulate transmission
received_packets = {}

def send_packet(packet_name, data):
    print(f"Sending {packet_name} via {', '.join(routes[packet_name])}...")
    time.sleep(random.uniform(0.5, 1.5))  # Random delay to simulate network latency
    print(f"{packet_name} arrived at Building D.")
    received_packets[packet_name] = data

# Send all packets
for packet in packet_data:
    send_packet(packet, packet_data[packet])

# Reassemble the message
reassembled_message = (
    received_packets['Packet 1'] +
    received_packets['Packet 2'] +
    received_packets['Packet 3']
)

print("\nReassembled Message at Building D:")
print(reassembled_message)
