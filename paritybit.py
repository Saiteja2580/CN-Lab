def hamming_encode_4bit(data_bits):
    # Ensure the data is 4 bits
    if len(data_bits) != 4 or not all(bit in '01' for bit in data_bits):
        raise ValueError("Input must be a 4-bit binary string.")
    
    # Place data bits into their positions (1-indexed)
    d1 = int(data_bits[0])
    d2 = int(data_bits[1])
    d3 = int(data_bits[2])
    d4 = int(data_bits[3])
    
    # Calculate parity bits using even parity
    p1 = (d1 + d2 + d4) % 2
    p2 = (d1 + d3 + d4) % 2
    p4 = (d2 + d3 + d4) % 2
    
    # Build the encoded 7-bit message
    encoded = [p1, p2, d1, p4, d2, d3, d4]
    
    return ''.join(str(bit) for bit in encoded)

# Example usage
data = "1011"
encoded_message = hamming_encode_4bit(data)
print(f"Original 4-bit data: {data}")
print(f"Hamming encoded 7-bit message: {encoded_message}")
