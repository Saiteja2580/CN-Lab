import socket
import os

HOST = '127.0.0.1'
PORT = 65432

file_path = input("Enter the path of the file to send: ")

if not os.path.exists(file_path):
    print("File does not exist.")
    exit()

filename = os.path.basename(file_path)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print(f"Connected to server {HOST}:{PORT}")

    client_socket.sendall(filename.encode())

    with open(file_path, 'rb') as f:
        data = f.read(1024)
        while data:
            client_socket.sendall(data)
            data = f.read(1024)

    print("File sent successfully.")
