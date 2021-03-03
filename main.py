# maybe i used those import pyautogui
from mouse.Mouse import Mouse
import time


class Main:

    def __init__(self):
        self.__mouse = Mouse()

    def run(self):
        self.__mouse.launch()
        while True:
            self.__mouse.listener_event_mouse()


if __name__ == '__main__':
    program = Main()
    program.run()