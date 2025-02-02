import RPi.GPIO as gpio

class ButtonViewer:
    def __init__(self):
        gpio.setmode(gpio.BCM)
        self.pins = [1, 17, 27, 3, 26, 18, 12]
        for pin in self.pins:
            print(pin)
            gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_UP)

    def get_key_status(self, key: int):
        return not bool(gpio.input(self.pins[key]))

