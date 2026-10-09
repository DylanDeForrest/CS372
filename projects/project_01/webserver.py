import socket
import sys

port = 28333

if len(sys.argv) > 1:
    port = int(sys.argv[1])
    
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", port))
s.listen()



while True:
    new_conn = s.accept()
    new_socket = new_conn[0]
    
    request = b""
    
    while b"\r\n\r\n" not in request:
        data = new_socket.recv(4096)
        if len(data) == 0:
            break
        request += data
        
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        "Content-Length: 6\r\n"
        "Connection: close\r\n"
        "\r\n"
        "Hello!"
    )
        
    new_socket.sendall(response.encode("ISO-8859-1"))
    new_socket.close()