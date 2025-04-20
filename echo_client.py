import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The same port as used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("Connected to the echo server. Type messages (type 'exit' to quit).")

    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Echoed from server: {data.decode()}")
