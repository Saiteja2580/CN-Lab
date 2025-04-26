from cryptography.fernet import Fernet

# Function to generate a key (only once)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

# Function to load the secret key
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt the message
def encrypt_message(message):
    key = load_key()  # Load the key from the file
    f = Fernet(key)  # Create a Fernet instance
    encrypted_message = f.encrypt(message.encode())  # Encrypt the message
    return encrypted_message

# Sender Code
def send_encrypted_message():
    # Message to be sent
    message = "This is a secret message."
    print("Original Message:", message)

    # Encrypt the message
    encrypted_message = encrypt_message(message)
    print("Encrypted Message:", encrypted_message)

    # Simulate sending the encrypted message (in reality, this would be sent over a network)
    # For now, we'll just return the encrypted message for testing
    return encrypted_message

if __name__ == "__main__":
    generate_key()  # Run this once to generate and save the secret key
    send_encrypted_message()
