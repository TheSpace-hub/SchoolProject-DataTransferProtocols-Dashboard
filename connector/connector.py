import requests
import json

from data.data import DataOut, DataIn


class Connector:
    def __init__(self, host: str):
        self.host: str = host


    def send_data(self, data_out: DataOut):
        data_str = str(json.dumps(data_out, default=lambda o: o.__dict__))
        print(f'Data: {data_str}')
        response = requests.post(self.host, json={'data': data_str})

