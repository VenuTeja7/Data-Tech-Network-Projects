import socket

# Server configuration
HOST = "127.0.0.1"   # localhost
PORT = 8080          # HTTP port (choose 80 if running as admin)

# HTML content to serve
html_page = """\
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

<!DOCTYPE html>
<html>
<head><title>Mini Web Server</title></head>
<body>
    <h1>Hello from Mini Web Server!</h1>
    <p>This page is served over TCP using Python sockets.</p>
</body>
</html>
"""

# Create TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"🚀 Web server running at http://{HOST}:{PORT}")

    while True:
        client_conn, client_addr = server_socket.accept()
        with client_conn:
            print(f"✅ Connected by {client_addr}")

            request = client_conn.recv(1024).decode("utf-8")
            print("----- HTTP REQUEST -----")
            print(request)

            # Always respond with the HTML page
            client_conn.sendall(html_page.encode("utf-8"))
