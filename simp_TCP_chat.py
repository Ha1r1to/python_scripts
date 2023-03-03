import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the other client
client_socket.connect(('localhost', 8000))

# send and receive messages between the clients
while True:
    message = input("Type your message: ")
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(f"Other client: {response}")
