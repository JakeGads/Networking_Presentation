import socket

alt = "404 Connection not found"
hostname = socket.gethostname()    
ip = socket.gethostbyname(hostname)