import time
import random

class TokenBucket:
    def __init__(self, capacity, token_rate):
        self.capacity = capacity        # Maximum number of tokens in bucket
        self.token_rate = token_rate    # Tokens added per second
        self.tokens = 0                 # Current token count
        self.last_time = time.time()    # Last time tokens were added

    def add_tokens(self):
        current_time = time.time()
        elapsed = current_time - self.last_time
        # Add tokens based on elapsed time
        added_tokens = int(elapsed * self.token_rate)
        if added_tokens > 0:
            self.tokens = min(self.capacity, self.tokens + added_tokens)
            self.last_time = current_time

    def process_packet(self):
        self.add_tokens()  # Always add tokens before checking
        if self.tokens >= 1:
            self.tokens -= 1
            print(f"Packet accepted. Tokens left: {self.tokens}\n")
        else:
            print("Packet dropped! (No tokens available)\n")

# Create a token bucket with capacity 5 tokens and generation rate 1 token/sec
bucket = TokenBucket(capacity=5, token_rate=1)

# Simulate incoming packets
for _ in range(10):
    bucket.process_packet()
    time.sleep(random.uniform(0.2, 1.5))  # Random delay between packet arrivals
