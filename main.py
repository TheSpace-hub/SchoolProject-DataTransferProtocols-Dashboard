import connector.connector
from data.data import DataOut


def main():
    c = connector.connector.Connector('127.0.0.1', 25570)
    c.connect()
    d = DataOut(False, False, False, False, False, False, False, False)
    while True:
        c.send_data(d)
        print(c.get_data().level)


if __name__ == '__main__':
    main()
