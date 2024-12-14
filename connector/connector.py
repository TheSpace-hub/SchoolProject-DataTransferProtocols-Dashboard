from socket import socket, AF_INET, SOCK_STREAM
import json

from data.data import DataOut, DataIn


class Connector:
    def __init__(self, ip: str, port: int):
        self.ip: str = ip
        self.port: int = port
        self._s: socket = socket(AF_INET, SOCK_STREAM)

    def connect(self):
        self._s.connect((self.ip, self.port))
        print('Соединение успешно установленно')

    def send_data(self, data: DataOut):
        self._s.send((json.dumps(data, default=lambda o: o.__dict__) + '\n').encode())

    def get_data(self) -> DataIn:
        return json.loads(self._s.recv(1024), object_hook=lambda d: DataIn(**d))
