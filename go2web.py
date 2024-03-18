import socket
import sys
import re

def make_http_request(host, path="/"):
    """Make a basic HTTP request using sockets."""
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, 80))
        ##s.connect((host, 1080))
        s.send(request.encode())
        response = b""
        while True:
            data = s.recv(1024)
            if not data:
                break
            response += data
    return response.decode()
