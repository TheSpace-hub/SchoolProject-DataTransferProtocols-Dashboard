import connector.connector
import controller.button_handler
from data.data import DataOut
import time

def main():
    c = connector.connector.Connector('http://dyachkov-project.ru/update')
    d = DataOut()
    while True:
        if d.update():
            print('Update')
            c.send_data(d)
            time.sleep(0.1)


if __name__ == '__main__':
    main()
