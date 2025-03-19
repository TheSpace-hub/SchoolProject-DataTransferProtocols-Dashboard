from controller.button_viewer import ButtonViewer

viewer = ButtonViewer(False)

class DataIn:
    def __init__(self, level: int):
        self.level: int = level


class DataOut:
    def __init__(self):
        self.keys = [False] * 7

    def update(self):
        changes = False

        for i in range(len(self.keys)):
            changes = changes or self.keys[i] != viewer.get_key_status(i)
            self.keys[i] = viewer.get_key_status(i)
        
        return changes

