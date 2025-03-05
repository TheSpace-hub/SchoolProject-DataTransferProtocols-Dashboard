from controller.button_viewer import ButtonViewer

viewer = ButtonViewer(False)

class DataIn:
    def __init__(self, level: int):
        self.level: int = level


class DataOut:
    def __init__(self, k1: bool, k2: bool, k3: bool, k4: bool, k5: bool, k6: bool, k7: bool):
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.k4 = k4
        self.k5 = k5
        self.k6 = k6
        self.k7 = k7
    
    def generate(self):
        self.k1 = viewer.get_key_status(0)
        self.k2 = viewer.get_key_status(1)
        self.k3 = viewer.get_key_status(2)
        self.k4 = viewer.get_key_status(3)
        self.k5 = viewer.get_key_status(4)
        self.k6 = viewer.get_key_status(5)
        self.k7 = viewer.get_key_status(6)




