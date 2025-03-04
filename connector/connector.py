import requests
import json

from data.data import DataOut, DataIn


class Connector:
    def __init__(self, host: str):
        self.host: str = host


    def send_data(self, data: DataOut):
        data = json.dumps(data, default=lambda o: o.__dict__).encode()
        response = requests.get(self.host, data=data)
        print(response.json())

