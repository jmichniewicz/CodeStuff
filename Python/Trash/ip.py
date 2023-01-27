## importing socket module
import socket
from contextlib import redirect_stdout
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")

with open('out.txt', 'w') as f:
    with redirect_stdout(f):
        print(hostname, ip_address)