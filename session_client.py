import time

class Server:
    def __init__(self):
        self.session_active = False

    def receive_request(self, message):
        print(f"Server received: {message}")
        if message == "SYN":
            print("Server sends: SYN-ACK")
            return "SYN-ACK"
        elif message == "ACK":
            self.session_active = True
            print("Session established!\n")
        elif message == "CLOSE":
            self.session_active = False
            print("Session closed by client.\n")

    def send_data(self, data):
        if self.session_active:
            print(f"Server sends data: {data}")
        else:
            print("No active session. Cannot send data.")

class Client:
    def __init__(self, server):
        self.server = server

    def establish_session(self):
        print("Client sends: SYN")
        response = self.server.receive_request("SYN")
        if response == "SYN-ACK":
            print("Client sends: ACK")
            self.server.receive_request("ACK")

    def send_data(self, data):
        if self.server.session_active:
            print(f"Client sends data: {data}")
            self.server.send_data(f"Acknowledged: {data}")
        else:
            print("Session not established. Cannot send data.")

    def close_session(self):
        print("Client sends: CLOSE")
        self.server.receive_request("CLOSE")

# Simulating the communication
server = Server()
client = Client(server)

# 1. Establish session
client.establish_session()
time.sleep(1)

# 2. Data exchange
client.send_data("Hello Server!")
time.sleep(1)
client.send_data("How are you?")
time.sleep(1)

# 3. Close session
client.close_session()
