from socket import *


def main():
    host = 'localhost'
    port = 7777
    addr = (host, port)
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(addr)
    while True:
        print('wait data...')
        data, addr = sock.recvfrom(1024)
        print('client addr: ', addr, f'data={data}')
        sock.sendto(b'message received by the server: ' + data, addr)


if __name__ == '__main__':
    main()
