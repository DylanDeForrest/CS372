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
        
    first_line = request.split(b"\r\n")[0]
    
    first_line = first_line.decode("ISO-8859-1")
    
    parts = first_line.split()
    
    path = parts[1]
    
    file_name = path.split("/")[-1]
    
    try:
        with open(file_name, "rb") as fp:
            file_data = fp.read()
        
        if file_name.endswith(".html"):
            content_type = "text/htlm"
        else: 
            content_type = "text.plain"
            
        response = (
            "HTTP/1.1 200 OK\r\n"
            f"Content-Type: {content_type}\r\n"
            f"Content-Length: {len(file_data)}\r\n"
            "Connection: close\r\n"
            "\r\n"
        )
        
        new_socket.sendall(response.encode("ISO-8859-1"))
        
        new_socket.sendall(file_data)
    except:
        response = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/plain\r\n"
            "Content-Length: 13\r\n"
            "Connection: close\r\n"
            "\r\n"
            "404 not found"
        )
        new_socket.sendall(response.encode("ISO-8859-1"))
    
    new_socket.close()