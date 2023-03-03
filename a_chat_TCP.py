import socket
import threading

def receive_messages(sock):
    while True:
        data = sock.recv(1024).decode()
        if not data:
            break
        print(data)

def main():
    host = 'localhost'
    port = 8000

    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)

    print(f'Listening on {host}:{port}')

    # Accept a connection
    conn, addr = sock.accept()
    print(f'Connected to {addr[0]}:{addr[1]}')

    # Start a thread to receive messages from the other side
    receive_thread = threading.Thread(target=receive_messages, args=(conn,))
    receive_thread.start()

    # Send messages to the other side
    while True:
        message = input()
        if message == 'quit':
            break
        conn.send(message.encode())

    # Close the connection
    conn.close()
    sock.close()

if __name__ == '__main__':
    main()
