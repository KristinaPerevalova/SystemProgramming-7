import socket


def handle_client_connection(client_socket):
    request = client_socket.recv(1024)
    print('Received {}'.format(request))
    client_socket.send('ACK!'.encode())
    client_socket.close()


def main():
    bind_ip = '0.0.0.0'
    bind_port = 9999

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(1)

    print('Listening on {}:{}'.format(bind_ip, bind_port))
    while True:
        client_sock, address = server.accept()
        print('Accepted connection from {}:{}'.format(address[0], address[1]))
        handle_client_connection(client_sock)


if __name__ == '__main__':
    main()
