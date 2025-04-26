import time
import random

# Function to simulate sending a packet
def send_packet(packet_num):
    print(f"Sender: Sending Packet {packet_num}")
    time.sleep(random.uniform(1, 3))  # Simulate packet transmission time

# Function to simulate receiver acknowledging the packet
def receive_ack(packet_num):
    print(f"Receiver: Acknowledging Packet {packet_num}")
    time.sleep(random.uniform(0.5, 1))  # Simulate acknowledgment time

# Stop-and-Wait Protocol Simulation
def stop_and_wait_protocol(total_packets):
    for packet_num in range(1, total_packets + 1):
        send_packet(packet_num)  # Sender sends packet
        receive_ack(packet_num)  # Receiver acknowledges the packet
        print(f"Sender: Received ACK for Packet {packet_num}\n")

# Simulate Stop-and-Wait for 3 packets
stop_and_wait_protocol(3)
