import socket
import threading

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print("Client:", message)
        client_socket.sendall(message.encode())
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORT = 12345
    server_socket.bind(('localhost', PORT))
    server_socket.listen(5)
    print("Server is listening for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print("Connection established with", client_address)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()