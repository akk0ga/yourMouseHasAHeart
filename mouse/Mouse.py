import pynput


class Mouse:
    def __init__(self):
        self.mouse = pynput.mouse
        self.listener = self.mouse.Listener
