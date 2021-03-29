from socket import *


def main():
    host = 'localhost'
    port = 7777
    addr = (host, port)
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    data = 'hello world'
    udp_socket.sendto(data.encode(), addr)
    data, _ = udp_socket.recvfrom(1024)
    print(data.decode())
    udp_socket.close()


if __name__ == '__main__':
    main()

