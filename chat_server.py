import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print(f"Client: {msg}")
        except:
            break
    conn.close()
    print(f"Connection with {addr} closed.")

def send_messages(conn):
    while True:
        msg = input("You: ")
        conn.sendall(msg.encode())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}...")

    conn, addr = server_socket.accept()

    recv_thread = threading.Thread(target=handle_client, args=(conn, addr))
    send_thread = threading.Thread(target=send_messages, args=(conn,))

    recv_thread.start()
    send_thread.start()
