import connector.connector
import controller.button_handler
from data.data import DataOut
import time

def main():
    c = connector.connector.Connector('185.220.37.105', 25570)
    c.connect()
    d = DataOut(False, False, False, False, False, False, False)
    while True:
        c.send_data(d)
        d.generate()
        c.get_data()


if __name__ == '__main__':
    main()
