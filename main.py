# maybe i used those import pyautogui
from mouse.Mouse import Mouse
import time


class Main:

    def __init__(self):
        self.__mouse = Mouse(voice_mode='fr')

    def run(self):
        self.__mouse.start()
        while True:
            self.__mouse.listener_event_mouse()


if __name__ == '__main__':
    program = Main()
    program.run()