import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server is listening on {HOST}:{PORT}...")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")

        filename = conn.recv(1024).decode()
        print(f"Receiving file: {filename}")

        with open(f"received_{filename}", 'wb') as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)

        print(f"File received and saved as received_{filename}")
