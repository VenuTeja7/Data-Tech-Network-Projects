import socket

HOST = "127.0.0.1"   # server IP (use server’s LAN IP if remote)
PORT = 8080

# Create TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    # Send simple HTTP GET request
    request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    client_socket.sendall(request.encode("utf-8"))

    # Receive response
    response = client_socket.recv(4096).decode("utf-8")
    print("----- HTTP RESPONSE -----")
    print(response)
