import socket

HOST = 'localhost'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Client 1: ")
        s.sendall(message.encode())
        data = s.recv(1024)
        print('Received from server:', data.decode())
