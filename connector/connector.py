from socket import socket, AF_INET, SOCK_STREAM


class Connector:
    def __init__(self, ip: str, port: int):
        self.ip: str = ip
        self.port: int = port

    def connect(self):
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((self.ip, self.port))
        print('Соединение успешно установленно')
