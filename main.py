import connector.connector
import RPi.GPIO as gpio
from data.data import DataOut

def init_gpio():
    gpio.setmode(gpio.BCM)
    gpio.setup(12, gpio.IN)


def main():
    init_gpio()
    c = connector.connector.Connector('192.168.1.51', 25570)
    c.connect()
    d = DataOut(False, False, False, False, False, False, False, False)
    while True:
        d.k1 = bool(gpio.input(12))
        c.send_data(d)
        print(c.get_data().level)


if __name__ == '__main__':
    main()
