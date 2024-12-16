class ButtonHandler:
    def __init__(self):
        self.k1: int = 0
        self.k2: int = 0
        self.k3: int = 0
        self.k4: int = 0
        self.k5: int = 0
        self.k6: int = 0
        self.k7: int = 0
        self.red_key: int = 0
        self._last_k1 = False
        self._last_k2 = False
        self._last_k3 = False
        self._last_k4 = False
        self._last_k5 = False
        self._last_k6 = False
        self._last_k7 = False
        self._last_red_key = False

    def k1_status(self, status: bool) -> None:
        if status == False and self._last_k1 == True:
            self._last_k1 = False
            self.k1 += 1

    def k2_status(self, status: bool) -> None:
        if status == False and self._last_k2 == True:
            self._last_k2 = False
            self.k2 += 1

    def k3_status(self, status: bool) -> None:
        if status == False and self._last_k3 == True:
            self._last_k3 = False
            self.k3 += 1

    def k4_status(self, status: bool) -> None:
        if status == False and self._last_k4 == True:
            self._last_k4 = False
            self.k4 += 1

    def k5_status(self, status: bool) -> None:
        if status == False and self._last_k5 == True:
            self._last_k5 = False
            self.k5 += 1

    def k6_status(self, status: bool) -> None:
        if status == False and self._last_k6 == True:
            self._last_k6 = False
            self.k6 += 1

    def k7_status(self, status: bool) -> None:
        if status == False and self._last_k7 == True:
            self._last_k7 = False
            self.k7 += 1

    def red_key_status(self, status: bool) -> None:
        if status == False and self._last_red_key == True:
            self._last_red_key = False
            self.red_key += 1

    def get_active_keys(self) -> list:
        keys = []
        if self.k1 > 0:
            keys.append('k1')
            self.k1 -= 1
        if self.k2 > 0:
            keys.append('k2')
            self.k2 -= 1
        if self.k3 > 0:
            keys.append('k3')
            self.k3 -= 1
        if self.k4 > 0:
            keys.append('k4')
            self.k4 -= 1
        if self.k5 > 0:
            keys.append('k5')
            self.k5 -= 1
        if self.k6 > 0:
            keys.append('k6')
            self.k6 -= 1
        if self.k7 > 0:
            keys.append('k7')
            self.k7 -= 1
        if self.red_key > 0:
            keys.append('red_key')
            self.red_key -= 1
        return keys
