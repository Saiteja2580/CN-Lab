from cryptography.fernet import Fernet

# Function to load the secret key
def load_key():
    return open("secret.key", "rb").read()

# Function to decrypt the message
def decrypt_message(encrypted_message):
    key = load_key()  # Load the key from the file
    f = Fernet(key)  # Create a Fernet instance
    decrypted_message = f.decrypt(encrypted_message).decode()  # Decrypt the message
    return decrypted_message

# Receiver Code
def receive_decrypted_message(encrypted_message):
    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    # Example: Simulating receiving an encrypted message
    encrypted_message = b'...'  # The encrypted message sent from the sender
    receive_decrypted_message(encrypted_message)
