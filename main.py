# maybe i used those import pyautogui
from mouse.Mouse import Mouse
from mouse.Voice import Voice


class Main:

    def __init__(self):
        self.__mouse = Mouse()
        self.__voice = Voice()

    def run(self):
        self.__voice.start()
        self.__mouse.set_position()
        while True:
            self.__mouse.listener_event_mouse()


if __name__ == '__main__':
    program = Main()
    program.run()