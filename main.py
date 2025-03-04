import connector.connector
import controller.button_handler
from data.data import DataOut
import time

def main():
    c = connector.connector.Connector('http://dyachkov-project.ru/update')
    d = DataOut(False, False, False, False, False, False, False)
    while True:
        c.send_data(d)
        d.generate()

        print('Send some data')
        time.sleep(10)


if __name__ == '__main__':
    main()
