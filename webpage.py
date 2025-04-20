import socket

def download_web_page(hostname, port, path, timeout=10):
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            # Set a timeout for the socket connection
            client_socket.settimeout(timeout)
            
            # Connect to the server
            client_socket.connect((hostname, port))
            
            # Prepare an HTTP GET request to fetch the page
            request = f"GET {path} HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n"
            
            # Send the HTTP GET request
            client_socket.send(request.encode())
            
            # Receive the response from the server
            response = b""
            while True:
                data = client_socket.recv(4096)  # Read data in chunks of 4096 bytes
                if not data:
                    break
                response += data
            
            # Decode and return the HTTP response
            return response.decode('utf-8', errors='ignore')
    
    except socket.timeout:
        return "Connection timed out"
    except socket.error as e:
        return f"Socket error: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
hostname = "www.google.co.in"
port = 80  # HTTP standard port
path = "/search?q=indiaq&sca_esv=2621f7b39c394d4e&sxsrf=AHTn8zomOEa2FOIuPOvVDtqESR-CoikH5w%3A1738567445346&source=hp&ei=FW-gZ_S9EYXn2roPxuToQQ&iflsig=ACkRmUkAAAAAZ6B9Ja5K9brHeQJnaxFK8uJMkIMZ7rse&sei=G2-gZ5epKdGYseMPh4zA0Qc"  # Path of the web page

# Download the web page
response = download_web_page(hostname, port, path)

# Print the HTTP response
print(response)
