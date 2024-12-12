class DataIn:
    def __init__(self, level: int):
        self.level: int = level


class DataOut:
    def __init__(self, k1: bool, k2: bool, k3: bool, k4: bool, k5: bool, k6: bool, k7: bool, red_key: bool):
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.k4 = k4
        self.k5 = k5
        self.k6 = k6
        self.k7 = k7
        self.red_key = red_key
