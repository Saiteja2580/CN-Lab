import time
import random

class LeakyBucket:
    def __init__(self, capacity, drain_rate):
        self.capacity = capacity  # Maximum bucket size
        self.drain_rate = drain_rate  # How much the bucket drains each time
        self.current_load = 0  # Current amount of water/data

    def add_packet(self, packet_size):
        # Drain the bucket a little before adding a new packet
        self.current_load = max(0, self.current_load - self.drain_rate)
        
        print(f"Packet size: {packet_size}, Current load before adding: {self.current_load}")

        if self.current_load + packet_size <= self.capacity:
            self.current_load += packet_size
            print(f"Packet accepted. Current load: {self.current_load}\n")
        else:
            print("Packet dropped! (Bucket overflow)\n")

# Simulation
bucket = LeakyBucket(capacity=10, drain_rate=2)

# Simulate incoming packets
packet_sizes = [random.randint(1, 6) for _ in range(10)]  # Random packet sizes between 1 and 6

for packet in packet_sizes:
    bucket.add_packet(packet)
    time.sleep(0.5)  # Simulate time delay (optional)
